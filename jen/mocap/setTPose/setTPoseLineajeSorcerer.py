import maya.cmds as mc

shoulderAngleZ = 5
upperArmAngleZ = 42
lowerArmAngleY = 0
handAngleX = 0
handAngleZ = 0

prefix = 'mocap_'

poleX = 9.267
poleY = 22.325
poleZ = -0.576

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
   
    #mc.setAttr(prefix + side + 'hand_01_JNT.rz', handAngleZ)

    handPos = mc.xform(prefix + side + 'hand_01_JNT', q=1, t=1, ws=1)
    handRot = mc.xform(prefix + side + 'hand_01_JNT', q=1, ro=1, ws=1)

    

    