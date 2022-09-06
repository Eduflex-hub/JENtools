import maya.cmds as mc
import math

sel= mc.ls(sl=1, fl=1)
print sel

vtx1=sel[0]
vtx2=sel[1]


coord1=mc.xform(vtx1, q=1, t=1, ws=1)
coord2=mc.xform(vtx2, q=1, t=1, ws=1)

jointCoordX=(coord2[0]+coord1[0])/2
jointCoordY=(coord2[1]+coord1[1])/2
jointCoordZ=(coord2[2]+coord1[2])/2

allJoints = mc.ls('C_midJoint_0*_jnt')
amount = len(allJoints) + 01
name = 'C_midJoint_0' + str(amount) + '_JNT'

mc.select(cl=1)
jnt=mc.joint(n=name, rad=0.1)
mc.xform(jnt, t=(jointCoordX, jointCoordY, jointCoordZ), ws=1)

loc1=mc.spaceLocator()
mc.xform(loc1, t=coord1, ws=1)
loc2=mc.spaceLocator()
mc.xform(loc2, t=coord2, ws=1)

mc.aimConstraint(loc1[0], loc2[0], aim=(0,0,1),u=(-1,0,0))

orient=mc.xform(loc2, q=1, ro=1, ws=1)
print orient

mc.xform(jnt, ro=orient, ws=1)
mc.makeIdentity(jnt, a=1, r=1)
mc.delete(loc1)
mc.delete(loc2)
mc.select(jnt)

