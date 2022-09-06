import maya.cmds as mc
import maya.mel as mel

def win():
    if mc.window('win', exists = True):
        mc.deleteUI('win')
    mc.window('win', title="Sticky Creator", s=1, wh= (300, 180))   

    mc.columnLayout(columnAttach=('both', 10), rowSpacing=10, columnWidth=260)
    mc.text("'..._MSH'")
    mc.button(label='Create Geometries', c=createGeos )
    mc.text('Name it and paint... yes, you have to paint it....')
    mc.checkBox('check', l='is mirrored?', v=1)
    mc.textField('text')
    mc.button(label='Create Locator', c=createLocator)
    mc.text('Put the IntermMesh bottom')
    mc.textField('textMesh')
    mc.button(label='Create Stickys', c=create )
    mc.showWindow()
    

def createGeos(self):
    sel=mc.ls(sl=1)[0]      
    mc.duplicate(sel, n=sel.replace('_MSH', '_stickyIntermediate'))
    mc.duplicate(sel, n=sel.replace('_MSH', '_stickyMesh'))

def createLocator(self):
    sel = mc.ls(sl=1, fl=1)
    mirrorCheck = mc.checkBox('check', query=True, value = True)

    for x in sel:
        index = sel.index(x) + 1
        name = mc.textField('text',q=1, tx=1) + '_0' + str(index) 
        nameMirror = name.replace('L_', 'R_')
        vertexPos = mc.xform(x, q=1, t=1, ws=1)
        loc = mc.spaceLocator(n=name + '_stickyLocator')[0]
        mc.xform(loc, t=vertexPos, ws=1)    

        mc.setAttr(loc + '.localScaleX', 0.2)
        mc.setAttr(loc + '.localScaleY', 0.2)
        mc.setAttr(loc + '.localScaleZ', 0.2)
        

        if mirrorCheck == True:
            locMirror = mc.spaceLocator(n=nameMirror + '_stickyLocator')[0]
            mdPos = mc.createNode('multiplyDivide', n=name + '_PosMD')
            mc.connectAttr(loc+'.t', mdPos+'.input1')
            mc.connectAttr(mdPos+'.output', locMirror+'.t')
            mc.setAttr(mdPos+'.input2X', -1)

            mdRot = mc.createNode('multiplyDivide', n=name + '_RotMD')
            mc.connectAttr(loc+'.r', mdRot+'.input1')
            mc.connectAttr(mdRot+'.output', locMirror+'.r')
            mc.setAttr(mdRot+'.input2Y', -1)
            mc.setAttr(mdRot+'.input2Z', -1)

            mc.setAttr(locMirror + '.localScaleX', 0.2)
            mc.setAttr(locMirror + '.localScaleY', 0.2)
            mc.setAttr(locMirror + '.localScaleZ', 0.2)




def create(self):
    sel=mc.ls('*_stickyLocator')
    mesh = mc.textField('textMesh', q=1, tx=1)
    jointGroup= mc.createNode('transform', n='C_stickyJoints_GRP')
    controlsGroup= mc.createNode('transform', n='C_stickyControls_GRP')

    for x in sel:

        closestPointOnMesh = mc.createNode('closestPointOnMesh', n=x.replace('_stickyLocator' , '_closestPointOnMesh'))
        mc.connectAttr(mesh+'Shape.outMesh', closestPointOnMesh+'.inMesh')
        mc.connectAttr(x+'.translate', closestPointOnMesh+'.inPosition')
        closestVertex = mc.getAttr(closestPointOnMesh+'.closestVertexIndex')
        closestVertexPos = mc.xform(mesh+'.vtx['+str(closestVertex)+']', q=True, t=True)
        locatorOrient = mc.xform(x, q=1, ro=1, ws=1)

        mc.select(mesh + '.vtx[' + str(closestVertex) + ']')
        emitter=mc.emitter(n=x.replace('_stickyLocator', '_stickyEmitter'))
        mc.select(cl=1)
        grp = mc.createNode('transform', n=x.replace('_stickyLocator', '_stickyGrp'))
        joint = mc.joint(n=x.replace('_stickyLocator', '_stickyJoint'), rad=0.1)
        mc.parent(grp, jointGroup)
        mc.xform(grp, t=closestVertexPos, ws=1)
        mc.xform(grp, ro=locatorOrient, ws=1)

        ctrlGrp = mc.createNode('transform', n=x.replace('_stickyLocator', '_stickyCtrlGrp'))
        ctrl = mc.circle(n=x.replace('_stickyLocator', '_stickyCtrl'), r=0.1)
        mc.parent(ctrl, ctrlGrp)
        mc.parent(ctrlGrp, controlsGroup)
        mc.xform(ctrlGrp, t=closestVertexPos, ws=1)
        mc.xform(ctrlGrp, ro=locatorOrient, ws=1)

        mc.pointConstraint(emitter[1], ctrlGrp, mo=1)

        mc.connectAttr(ctrl[0]+'.t', joint+'.t')
        mc.connectAttr(ctrl[0]+'.r', joint+'.r')
        mc.connectAttr(ctrl[0]+'.s', joint+'.s')

    mc.select(cl=1)
    mc.joint(n='C_holder_01_stickyJoint', rad=0.1)
    mc.delete(sel)
    mc.delete(mc.ls('*_closestPointOnMesh'))

    sets = mc.ls('*stickyEmitterSet')
    for i in sets:
        inputNode = mc.listConnections(i + '.groupNodes')        
        mc.disconnectAttr(inputNode[0]+'.message', i + '.groupNodes[0]')
        mc.delete(i)    



win()
