import maya.cmds as mc

def flor(_name, _base):
    pua = mc.ls('*' + _name + '*MSH')
    base = mc.ls('*' + _base + '*MSH')
    for b in base:
        jnt = mc.joint(n=b.replace('MSH', 'JNT'))
        mc.delete(mc.parentConstraint(b, jnt, mo=0))
        mc.makeIdentity(jnt, a=1)
        ZTR = mc.createNode('transform', n=b.replace('MSH', 'ZTR'))
        mainCTRL = mc.circle(n=b.replace('MSH', 'CTRL'), r=15, nr=(0, 1, 0), c=(0, 0, 0))[0]
        mc.parent(mainCTRL, ZTR)
        mc.delete(mc.parentConstraint(b, ZTR, mo=0))
        mc.parent(jnt, mainCTRL)

    for i in pua:
        mc.select(cl=1)
        jnt = mc.joint(n=i.replace('MSH', 'JNT'))
        mc.delete(mc.parentConstraint(i, jnt, mo=0))
        mc.makeIdentity(jnt, a=1)
        ZTR = mc.createNode('transform', n=i.replace('MSH', 'ZTR'))
        CTRL = mc.circle(n=i.replace('MSH', 'CTRL'), r=2, nr=(0, 0, 1), c=(0, 0, -5))[0]
        mc.parent(CTRL, ZTR)
        mc.delete(mc.parentConstraint(i, ZTR, mo=0))
        mc.parent(jnt, CTRL)


#flor('auriculares', 'cania')
#flor('Petalo', 'MicInterior')


def arbusto(_name):
    arbusto = mc.ls('*' + _name + '*MSH')
    for i in arbusto:
        # vertexList = [i + '.vtx[345]', i + '.vtx[218]', i + '.vtx[278]', i + '.vtx[297]']
        # vertexList = [i + '.vtx[18]', i + '.vtx[22]']
        # vertexList = [i + '.vtx[1436]', i + '.vtx[1244]', i + '.vtx[1063]']
        # vertexList = [i + '.vtx[1434]']
        vertexList = [i + '.vtx[1436]', i + '.vtx[79]', i + '.vtx[774]', i + '.vtx[1056]']
        controls = []
        ztrs = []
        for x in vertexList:
            index = vertexList.index(x)
            pos = mc.xform(x, q=1, t=1, ws=1)
            print i
            ori = mc.xform(i, q=1, ro=1, ws=1)
            ZTR = mc.createNode('transform', n=i.replace('MSH', str(index) + 'ZTR'))
            CTRL = mc.circle(n=i.replace('MSH', str(index) + 'CTRL'), r=2, nr=(0, 0, 1), c=(0, 0, 0))[0]
            #CTRL = mc.circle(n=i.replace('MSH', str(index) + 'CTRL'), r=4, nr=(0, 1, 0), c=(0, 0, 0))[0]
            jnt = mc.joint(n=i.replace('MSH', str(index) + 'JNT'))
            mc.parent(CTRL, ZTR)
            mc.xform(ZTR, t=pos, ws=1)
            mc.xform(ZTR, ro=ori, ws=1)
            mc.makeIdentity(jnt, a=1)
            #mc.parent(jnt, CTRL)
            controls.append(CTRL)
            ztrs.append(ZTR)
        mc.parent(ztrs[1], controls[0])
        mc.parent(ztrs[2], controls[1])
        mc.parent(ztrs[3], controls[2])


# arbusto('ColganteHojas')

def monsteras(_name):
    monsteras = mc.ls('*' + _name + '*MSH')

    for i in monsteras:
       
        tempVertex1 = i + '.vtx[1154]'
        tempVertex2 = i + '.vtx[1010]'
        tempVertex3 = i + '.vtx[389]'
        pos1 = mc.xform(tempVertex1, q=1, t=1, ws=1)
        pos2 = mc.xform(tempVertex2, q=1, t=1, ws=1)
        pos3 = mc.xform(tempVertex3, q=1, t=1, ws=1)
        loc1 = mc.spaceLocator(n= 'loc1')
        loc2 = mc.spaceLocator(n= 'loc2')
        loc3 = mc.spaceLocator(n= 'loc3')
        mc.xform(loc1, t=pos1, ws=1)
        mc.xform(loc2, t=pos2, ws=1)
        mc.xform(loc3, t=pos3, ws=1)
        mc.aimConstraint(loc2[0], loc1[0], wuo=loc3[0], wut='object', u=(0,-1,0))

        ori=mc.xform(loc1, q=1, ro=1, ws=1)
        mc.delete(loc1, loc2, loc3)
        vertexList = [i + '.vtx[1154]', i + '.vtx[1010]', i + '.vtx[816]' ]
        controls = []
        ztrs = []
        for x in vertexList:
            index = vertexList.index(x)
            pos = mc.xform(x, q=1, t=1, ws=1)                      
            ZTR = mc.createNode('transform', n=i.replace('MSH', str(index) + 'ZTR'))
            CTRL = mc.circle(n=i.replace('MSH', str(index) + 'CTRL'), r=2, nr=(1, 0, 0), c=(0, 0, 0))[0]            
            jnt = mc.joint(n=i.replace('MSH', str(index) + 'JNT'))
            mc.parent(CTRL, ZTR)
            mc.xform(ZTR, t=pos, ws=1)
            mc.xform(ZTR, ro=ori, ws=1)
            mc.makeIdentity(jnt, a=1)            
            controls.append(CTRL)
            ztrs.append(ZTR)
        mc.parent(ztrs[1], controls[0])
        mc.parent(ztrs[2], controls[1])
        #mc.parent(ztrs[3], controls[2])


#monsteras('_Hoja')





def skin():
    joints = mc.ls('*Petalo*JNT')
    for x in joints:
        y = x.replace('JNT', 'MSH')
        if mc.objExists(y) is True:
            mc.select(x)
            mc.select(y, add=1)
            mc.skinCluster()


#skin()


def skin2():
    meshes = mc.ls('*_Hoja_*MSH')
    for x in meshes:
        part = x.split('__')[0]
        joints = mc.ls(part + '*JNT')
        parent = []

        for j in joints:
            par = mc.listRelatives(j, p=1)[0]
            parent.append(par)
        print x
        print joints
        #mc.parent(joints[3], joints[2])
        mc.parent(joints[2], joints[1])
        mc.parent(joints[1], joints[0])

        mc.select(x)
        mc.select(joints, add=1)
        mc.skinCluster()
        #mc.parent(joints[3], parent[3])
        mc.parent(joints[2], parent[2])
        mc.parent(joints[1], parent[1])


skin2()
