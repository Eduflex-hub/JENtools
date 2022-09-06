import maya.mel as mel
import maya.api.OpenMaya as OpenMayaApi

def convert_joints_to_shapes(skinnedMesh):

    skinCluster = mel.eval('findRelatedSkinCluster("%s")' % skinnedMesh)
    
    infs = {id:str(inf) for id,inf in enumerate(cmds.skinCluster(skinCluster, q=True, inf=True)) }
        
    for jid, jname in infs.items():            
            cmds.duplicate(skinnedMesh, name=jname + '_geo')

def convert_skn_to_shapes(skinnedMesh, blend_shape, root_env = 'main_env'):
    """ base mesh should be at rest, skinned mesh is the combined shape"""
       
    skinCluster = mel.eval('findRelatedSkinCluster("%s")' % skinnedMesh)
    
    infs = {id:str(inf) for id,inf in enumerate(cmds.skinCluster(skinCluster, q=True, inf=True)) }
    
    nverts = len(cmds.ls(skinnedMesh + '.vtx[*]', fl=True))
    
    for vid in range(nverts):
        
        # get the inf data
        
        blends = cmds.skinPercent(skinCluster,skinnedMesh + ".vtx[%s]" % vid, q=True, v=True)
        
        for jid, blend in enumerate(blends):
            cmds.setAttr('%s.inputTarget[0].inputTargetGroup[%s].targetWeights[%s]' % (blend_shape, jid, vid), blend)       
             
                
#convert_joints_to_shapes('ta_face_softDef_100_bs')    
#convert_skn_to_shapes('ta_face_softDef_100_bs', 'blendShape1', root_env = 'main_env')

##


import maya.mel as mel
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim

def split_blendshape_by_skin(skinnedMesh, neutralMesh):
    def getMesh(geo):
        shape = cmds.listRelatives(geo, s=True)[0]
        sel = OpenMaya.MSelectionList()
        sel.add(shape)
        MObj = OpenMaya.MObject()
        
        sel.getDependNode(0, MObj)
        
        return MObj, OpenMaya.MFnMesh(MObj)

    skinCluster = mel.eval('findRelatedSkinCluster("%s")' % skinnedMesh)
    
    # load geos as api
    skinMObj, skinMFn  = getMesh(skinnedMesh)
    neutralMObj, neutralMFn  = getMesh(neutralMesh)
    
    nverts = skinMFn.numVertices()
    
    # get points of meshes
    skinPoints = OpenMaya.MPointArray()
    neutralPoints = OpenMaya.MPointArray()
    
    skinMFn.getPoints(skinPoints)
    neutralMFn.getPoints(neutralPoints)
    
    # load in the skin cluster as api
    
    selList = OpenMaya.MSelectionList()
    selList.add(skinCluster)
    clusterNode = OpenMaya.MObject()
    selList.getDependNode(0, clusterNode)
    skinFn = OpenMayaAnim.MFnSkinCluster(clusterNode)
    
    wlPlug = skinFn.findPlug('weightList')
    wPlug = skinFn.findPlug('weights')
    wlAttr = wlPlug.attribute()
    wAttr = wPlug.attribute()
    wInfIds = OpenMaya.MIntArray()
    
    # get the MDagPath for all influence
    infDags = OpenMaya.MDagPathArray()
    skinFn.influenceObjects(infDags)
    
    # create a dictionary whose key is the MPlug indice id and 
    # whose value is the influence list id
    infIds = {}
    infs = []
    for x in xrange(infDags.length()):
       infPath = infDags[x].fullPathName()
       infId = int(skinFn.indexForInfluenceObject(infDags[x]))
       infIds[infId] = x
       infs.append(infPath)   
    
    bsMFns = []
    
    bsPoints = []
    
    for inf in infs:
        bsName = cmds.ls(inf)[0].replace('_env', '')
        bs = cmds.duplicate(neutralMesh, name=bsName)[0]
        bsMobj, bsMfn = getMesh(bs)
        bsMFns.append(bsMfn)
        
        points = OpenMaya.MPointArray()
        bsMfn.getPoints(points)
        
        bsPoints.append(points)
    
    weights = {}
    for vId in xrange(wlPlug.numElements()):
       vWeights = {}
       # tell the weights attribute which vertex id it represents
       wPlug.selectAncestorLogicalIndex(vId, wlAttr)
       
       # get the indice of all non-zero weights for this vert
        wPlug.getExistingArrayAttributeIndices(wInfIds)
        
       # create a copy of the current wPlug
       infPlug = OpenMaya.MPlug(wPlug)
       for infId in wInfIds:
       # tell the infPlug it represents the current influence id
       infPlug.selectAncestorLogicalIndex(infId, wAttr)
       
       vWeights[infIds[infId]] = infPlug.asDouble()
        
        # store weights in dict
        weights[vId] = vWeights
    
    print 'Finished storing weights'
    
    # loop the weights
    
    for vid in range(nverts):
        
        weightList = weights[vid]    
        
        for infId, value in weightList.items():
                       
            nPoint = bsPoints[infId][vid]
            tPoint = skinPoints[vid]
                                   
            outPoint = ( OpenMaya.MVector(nPoint[0], nPoint[1], nPoint[2]) * (1.0 -value) ) +  ( OpenMaya.MVector(tPoint[0], tPoint[1], tPoint[2]) * value )
            
            bsPoints[infId].set(vid, outPoint[0], outPoint[1], outPoint[2])
            
    for mfn, points in zip(bsMFns, bsPoints):
        mfn.setPoints(points) 

'''
# names of meshes and skin cluster 
skinnedMesh = 'tmp_Shapes_02_ta_face_mesh'
neutralMesh = 'tmp_Shapes_ta_face_geo'        
split_blendshape_by_skin(skinnedMesh, neutralMesh)