import maya.cmds as mc

meshes=mc.ls('C_tiras*LOW')
for x in meshes:
    vertexList = [x + '.vtx[54]', x + '.vtx[60]', x + '.vtx[64]', x + '.vtx[69]', x + '.vtx[75]', x + '.vtx[78]', x + '.vtx[80]']
    joints=[]
    for i in vertexList:
        index = vertexList.index(i)
        pos = mc.xform(i, q=1, t=1, ws=1)
        mc.select(cl=1)
        jnt = mc.joint(n= x.replace('LOW', str(index) + 'JNT'), p=pos)
        joints.append(jnt)
        mc.select(cl=1)
        if index > 0:
        	mc.delete(mc.aimConstraint(jnt, joints[index-1], aimVector=(1,0,0), u=(0,1,0)))       	
        	mc.makeIdentity(jnt, a=1)
        	mc.parent(jnt, joints[index-1])
        mc.refresh()

