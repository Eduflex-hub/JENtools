import maya.cmds as mc

shoulderAngleZ = 12
upperArmAngleZ = 30
lowerArmAngleY = 14
handAngleX = 8
handAngleZ = 15

prefix = 'mocap_'

poleX = 7.285
poleY = 15.368
poleZ = -0.257

for i in range(0, 2):
    index = range(0, 2).index(i)
    if index == 0:
        side = 'L_'

    if index == 1:
        side = 'R_'
   
    mc.setAttr(prefix + side + 'clavicle_01_JNT.rz', shoulderAngleZ)
   
    mc.setAttr(prefix + side + 'upperArm_01_JNT.rz', upperArmAngleZ)
   
    mc.setAttr(prefix + side + 'lowerArm_01_JNT.ry', lowerArmAngleY)
   
    mc.setAttr(prefix + side + 'hand_01_JNT.rx', handAngleX)
   
    mc.setAttr(prefix + side + 'hand_01_JNT.rz', handAngleZ)

    handPos = mc.xform(prefix + side + 'hand_01_JNT', q=1, t=1, ws=1)
    handRot = mc.xform(prefix + side + 'hand_01_JNT', q=1, ro=1, ws=1)

    

    