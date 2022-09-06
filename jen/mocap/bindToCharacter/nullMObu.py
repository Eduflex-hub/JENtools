import maya.cmds as mc


def Constraints():
    # Creating Nulls-----------------------------------------------
    controls = mc.ls('*CTRL')
    excludeList = ['C_eyes_01_CTRL', 'R_eye_01_CTRL', 'L_eye_01_CTRL', 'C_spine_08_endikCTRL', 'L_socket_01_CTRL', 'R_socket_01_CTRL']
    root = 'C_root_01_CTRL'
    attrList = mc.listAttr(root, ud=1)
    print attrList
    if 'mocapAttach' in attrList:
        pass
    else:
        mc.addAttr(root, ln='mocapAttach', at='long', min=0, max=1, dv=0, k=1)

    for x in controls:
        parent = mc.listRelatives(x, p=1)[0]
        coords = mc.xform(x, q=1, t=1, ws=1)
        orient = mc.xform(x, q=1, ro=1, ws=1)
        if x not in excludeList:
            if x.startswith('C_root_') or x.startswith('C_main_') or x.endswith('maskCTRL'):
                continue
            null = mc.createNode('transform', n=x.replace('CTRL', 'NULL'))
            mc.xform(null, t=coords, ws=1)
            mc.xform(null, ro=orient, ws=1)
            mc.parent(null, parent)
            mc.makeIdentity(null, a=1)
            mc.parent(x, null)     
    print "Nulls creation Complete"
    # Rotating to T-Pose Variables:
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

        mc.setAttr(side + 'clavicle_01_NULL.rz', shoulderAngleZ)
        mc.setAttr(prefix + side + 'clavicle_01_JNT.rz', shoulderAngleZ)

        mc.setAttr(side + 'upperArm_01_fkNULL.rz', upperArmAngleZ)
        mc.setAttr(prefix + side + 'upperArm_01_JNT.rz', upperArmAngleZ)

        mc.setAttr(side + 'lowerArm_01_fkNULL.ry', lowerArmAngleY)
        mc.setAttr(prefix + side + 'lowerArm_01_JNT.ry', lowerArmAngleY)

        mc.setAttr(side + 'hand_01_fkNULL.rx', handAngleX)
        mc.setAttr(prefix + side + 'hand_01_JNT.rx', handAngleX)

        mc.setAttr(side + 'hand_01_fkNULL.rz', handAngleZ)
        mc.setAttr(prefix + side + 'hand_01_JNT.rz', handAngleZ)

        handPos = mc.xform(prefix + side + 'hand_01_JNT', q=1, t=1, ws=1)
        handRot = mc.xform(prefix + side + 'hand_01_JNT', q=1, ro=1, ws=1)

        mc.xform(side + 'hand_01_ikNULL', t=handPos, ws=1)
        mc.xform(side + 'hand_01_ikNULL', ro=handRot, ws=1)

        if side == 'L_':
            mc.setAttr(side + 'upperArm_01_PoleVector_ikNULL.tx', poleX)
        if side == 'R_':
            mc.setAttr(side + 'upperArm_01_PoleVector_ikNULL.tx', poleX * -1)
        mc.setAttr(side + 'upperArm_01_PoleVector_ikNULL.ty', poleY)
        mc.setAttr(side + 'upperArm_01_PoleVector_ikNULL.tz', poleZ)

    # CreatingConstraints-------------------------------------------
    print "Tpose_Complete"

    mocapJoints = mc.ls(prefix + '*JNT')
    excludeList = ['C_body_01_CTRL', 'L_foot_01_ikFootCTRL', 'R_foot_01_ikFootCTRL']

    for x in mocapJoints:
        name = x.replace(prefix, ' ')
        null = name.replace('JNT', 'NULL')
        fkNull = name.replace('JNT', 'fkNULL')
        ikNull = name.replace('JNT', 'ikNULL')
        poleVectorNull = name.replace('JNT', 'PoleVector_ikNULL')

        if null != 'C_spine_03_fkNULL':
            if mc.objExists(null) == True:
                mc.parentConstraint(x, null, mo=1)

            if mc.objExists(fkNull) == True:
                mc.parentConstraint(x, fkNull, mo=1)

            if mc.objExists(ikNull) == True:
                mc.parentConstraint(x, ikNull, mo=1)

            if mc.objExists(poleVectorNull) == True:
                mc.parentConstraint(x, poleVectorNull, mo=1)

        mc.parentConstraint('mocap_C_spine_06_JNT', 'C_spine_03_fkNULL', mo=1)
        mc.parentConstraint('mocap_C_hipBase_01_JNT', 'C_body_01_NULL', mo=1)
        mc.parentConstraint('mocap_L_foot_01_JNT', 'L_foot_01_ikFootNULL', mo=1)
        mc.parentConstraint('mocap_R_foot_01_JNT', 'R_foot_01_ikFootNULL', mo=1)

    print "Constraints_Complete"
    nulls = mc.ls('*NULL')


    for x in nulls:
        mc.setKeyframe(x, at='translate')
        mc.setKeyframe(x, at='rotate')
        attr = mc.listAttr(x, k=1, ud=1)
        if attr != None:
            for i in attr:
                if i == 'blendParent1':
                    mc.connectAttr('C_root_01_CTRL.mocapAttach', x + '.' + i, f=1)
    print "keyframe_Complete"


Constraints()
