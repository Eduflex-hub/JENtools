import maya.cmds as mc


def faceLocator():
    # leftSide Locs------------------------------------------------
    L_eyeSocketLOC = mc.spaceLocator(n='L_eyeSocket_01_tempLOC')
    L_eyeCenterLOC = mc.spaceLocator(n='L_eyeCenter_01_tempLOC')
    L_eyePupilLOC = mc.spaceLocator(n='L_pupil_01_tempLOC')

    L_upperLidParentLOC = mc.spaceLocator(n='L_upperLid_01_tempLOC')
    L_lowerLidParentLOC = mc.spaceLocator(n='L_lowerLid_01_tempLOC')

    L_upperLidLOC = mc.spaceLocator(n='L_upperLid_02_tempLOC')
    L_lowerLidLOC = mc.spaceLocator(n='L_lowerLid_02_tempLOC')

    mc.parent(L_eyePupilLOC, L_eyeCenterLOC)
    mc.parent(L_eyeCenterLOC, L_eyeSocketLOC)

    mc.parent(L_upperLidLOC, L_upperLidParentLOC)
    mc.parent(L_lowerLidLOC, L_lowerLidParentLOC)

    mc.xform(L_eyePupilLOC, t=(0, 0, 2))
    mc.xform(L_upperLidLOC, t=(0, 0, 2))
    mc.xform(L_lowerLidLOC, t=(0, 0, 2))

    mc.xform(L_upperLidParentLOC, ro=(-30, 0, 0))
    mc.xform(L_lowerLidParentLOC, ro=(30, 0, 0))

    leftGrp = mc.createNode('transform', n='L_eyeLocators_GRP')
    mc.parent(L_eyeSocketLOC, L_upperLidParentLOC, L_lowerLidParentLOC, leftGrp)
    mc.xform(leftGrp, t=(5, 0, 0))

    # rigthSide Locs-----------------------------------------------
    R_eyeSocketLOC = mc.spaceLocator(n='R_eyeSocket_01_tempLOC')
    R_eyeCenterLOC = mc.spaceLocator(n='R_eyeCenter_01_tempLOC')
    R_eyePupilLOC = mc.spaceLocator(n='R_pupil_01_tempLOC')

    R_upperLidParentLOC = mc.spaceLocator(n='R_upperLid_01_tempLOC')
    R_lowerLidParentLOC = mc.spaceLocator(n='R_lowerLid_01_tempLOC')

    R_upperLidLOC = mc.spaceLocator(n='R_upperLid_02_tempLOC')
    R_lowerLidLOC = mc.spaceLocator(n='R_lowerLid_02_tempLOC')

    mc.parent(R_eyePupilLOC, R_eyeCenterLOC)
    mc.parent(R_eyeCenterLOC, R_eyeSocketLOC)

    mc.parent(R_upperLidLOC, R_upperLidParentLOC)
    mc.parent(R_lowerLidLOC, R_lowerLidParentLOC)

    mc.xform(R_eyePupilLOC, t=(0, 0, 2))
    mc.xform(R_upperLidLOC, t=(0, 0, 2))
    mc.xform(R_lowerLidLOC, t=(0, 0, 2))

    mc.xform(R_upperLidParentLOC, ro=(-30, 0, 0))
    mc.xform(R_lowerLidParentLOC, ro=(30, 0, 0))

    rigthGrp = mc.createNode('transform', n='R_eyeLocators_GRP')
    mc.parent(R_eyeSocketLOC, R_upperLidParentLOC, R_lowerLidParentLOC, rigthGrp)
    mc.xform(rigthGrp, t=(-5, 0, 0))

    # Angle Query--------------------------------------------------------------------

    suffix = '_tempLOC'

    for i in range(0, 2):
        index = range(0, 2).index(i)
        if index == 0:
            i = 'L_eyeAngleExtractor' + suffix
            base = L_eyeCenterLOC[0]
            target = L_lowerLidLOC[0]
            pose = L_upperLidLOC[0]
            grp = leftGrp

        elif index == 1:
            i = 'R_eyeAngleExtractor' + suffix
            base = R_eyeCenterLOC[0]
            target = R_lowerLidLOC[0]
            pose = R_upperLidLOC[0]
            grp = rigthGrp

        baseDeComp = mc.createNode('decomposeMatrix', n=i.replace(suffix, '_deCompBase'))
        targetDeComp = mc.createNode('decomposeMatrix', n=i.replace(suffix, '_deCompTarget'))
        poseDeComp = mc.createNode('decomposeMatrix', n=i.replace(suffix, '_deCompPose'))

        mc.connectAttr(base + '.worldMatrix[0]', baseDeComp + '.inputMatrix')
        mc.connectAttr(target + '.worldMatrix[0]', targetDeComp + '.inputMatrix')
        mc.connectAttr(pose + '.worldMatrix[0]', poseDeComp + '.inputMatrix')

        pma1 = mc.createNode('plusMinusAverage', n=i.replace(suffix, '_PMA1'))
        pma2 = mc.createNode('plusMinusAverage', n=i.replace(suffix, '_PMA2'))
        mc.setAttr(pma1 + '.operation', 2)
        mc.setAttr(pma2 + '.operation', 2)

        mc.connectAttr(targetDeComp + '.outputTranslate', pma1 + '.input3D[0]')
        mc.connectAttr(baseDeComp + '.outputTranslate', pma1 + '.input3D[1]')

        mc.connectAttr(baseDeComp + '.outputTranslate', pma2 + '.input3D[1]')
        mc.connectAttr(poseDeComp + '.outputTranslate', pma2 + '.input3D[0]')

        angle = mc.createNode('angleBetween', n=i.replace(suffix, '_AB'))

        mc.connectAttr(pma1 + '.output3D', angle + '.vector1')
        mc.connectAttr(pma2 + '.output3D', angle + '.vector2')

        pmaResult = mc.createNode('plusMinusAverage', n=i.replace(suffix, '_RESULT'))
        mc.connectAttr(angle + '.angle', pmaResult + '.input1D[0]')
        mc.addAttr(grp, ln='lidsAngle', at='float', k=1)
        mc.connectAttr(pmaResult + '.output1D', grp + '.lidsAngle')


def createSystem():
    eyesMainControlZTR = mc.createNode('transform', n='C_eyes_01_ZTR')
    eyesMainControl = mc.circle(n='C_eyes_01_CTRL', nr=(0, 0, 1), r=5, c=(0, 0, 0))[0]
    mc.parent(eyesMainControl, eyesMainControlZTR)

    mc.addAttr(eyesMainControl, ln='__', at='enum', en='pupils', k=1)
    mc.addAttr(eyesMainControl, ln='lPupil', at='float', min=0.01, dv=1,  k=1)
    mc.addAttr(eyesMainControl, ln='rPupil', at='float', min=0.01, dv=1,  k=1)
    mc.addAttr(eyesMainControl, ln='___', at='enum', en='eyelids', max=1, min=0, k=1)
    mc.addAttr(eyesMainControl, ln='fleshyEyelids', at='float', max=1, min=0, k=1)
    mc.addAttr(eyesMainControl, ln='lBlink', at='float', max=1, min=0, k=1)
    mc.addAttr(eyesMainControl, ln='lBlinkPose', at='float', max=1, min=0, k=1)
    mc.addAttr(eyesMainControl, ln='rBlink', at='float', max=1, min=0, k=1)
    mc.addAttr(eyesMainControl, ln='rBlinkPose', at='float', max=1, min=0, k=1)

    # Variables------------------------------------------------
    for x in range(0, 2):
        index = range(0, 2).index(x)
        if index == 0:
            eyeGrpProxy = 'L_eyeLocators_GRP'
            eyeSocketProxy = 'L_eyeSocket_01_tempLOC'
            eyeCenterProxy = 'L_eyeCenter_01_tempLOC'
            eyePupilProxy = 'L_pupil_01_tempLOC'

            eyeUpperLidParentProxy = 'L_upperLid_01_tempLOC'
            eyeLowerLidParentProxy = 'L_lowerLid_01_tempLOC'

            eyeUpperLidProxy = 'L_upperLid_02_tempLOC'
            eyeLowerLidProxy = 'L_lowerLid_02_tempLOC'

            pupilAttr = 'lPupil'
            blinkAttr = 'lBlink'
            blinkPoseAttr = 'lBlinkPose'

            side = 'L_'

        elif index == 1:
            eyeGrpProxy = 'R_eyeLocators_GRP'
            eyeSocketProxy = 'R_eyeSocket_01_tempLOC'
            eyeCenterProxy = 'R_eyeCenter_01_tempLOC'
            eyePupilProxy = 'R_pupil_01_tempLOC'

            eyeUpperLidParentProxy = 'R_upperLid_01_tempLOC'
            eyeLowerLidParentProxy = 'R_lowerLid_01_tempLOC'

            eyeUpperLidProxy = 'R_upperLid_02_tempLOC'
            eyeLowerLidProxy = 'R_lowerLid_02_tempLOC'

            pupilAttr = 'rPupil'
            blinkAttr = 'rBlink'
            blinkPoseAttr = 'rBlinkPose'

            side = 'R_'

        angle = mc.getAttr(eyeGrpProxy + '.lidsAngle')
        moveValue = 1

        eyeSocketProxyPos = mc.xform(eyeSocketProxy, q=1, t=1, ws=1)
        eyeSocketProxyRot = mc.xform(eyeSocketProxy, q=1, ro=1, ws=1)

        eyeCenterProxyPos = mc.xform(eyeCenterProxy, q=1, t=1, ws=1)
        eyeCenterProxyRot = mc.xform(eyeCenterProxy, q=1, ro=1, ws=1)

        eyePupilProxyPos = mc.xform(eyePupilProxy, q=1, t=1, ws=1)
        eyePupilProxyRot = mc.xform(eyePupilProxy, q=1, ro=1, ws=1)

        eyeUpperLidParentProxyPos = mc.xform(eyeUpperLidParentProxy, q=1, t=1, ws=1)
        eyeUpperLidParentProxyRot = mc.xform(eyeUpperLidParentProxy, q=1, ro=1, ws=1)

        eyeLowerLidParentProxyPos = mc.xform(eyeLowerLidParentProxy, q=1, t=1, ws=1)
        eyeLowerLidParentProxyRot = mc.xform(eyeLowerLidParentProxy, q=1, ro=1, ws=1)

        eyeUpperLidProxyPos = mc.xform(eyeUpperLidProxy, q=1, t=1, ws=1)
        eyeUpperLidProxyRot = mc.xform(eyeUpperLidProxy, q=1, ro=1, ws=1)

        eyeLowerLidProxyPos = mc.xform(eyeLowerLidProxy, q=1, t=1, ws=1)
        eyeLowerLidProxyRot = mc.xform(eyeLowerLidProxy, q=1, ro=1, ws=1)

        # Creating Joints------------------------------------------------

        mc.select(cl=1)
        socketJoint = mc.joint(n=side + 'socket_01_JNT', rad=1.5)
        mc.xform(socketJoint, t=eyeSocketProxyPos, ws=1)
        mc.xform(socketJoint, ro=eyeSocketProxyRot, ws=1)
        mc.makeIdentity(socketJoint, a=1)
        mc.select(cl=1)

        eyeJoint = mc.joint(n=side + 'eye_01_JNT', rad=0.8)
        mc.xform(eyeJoint, t=eyeCenterProxyPos, ws=1)
        mc.xform(eyeJoint, ro=eyeCenterProxyRot, ws=1)
        mc.makeIdentity(eyeJoint, a=1)
        mc.parent(eyeJoint, socketJoint)
        mc.select(cl=1)

        pupilJoint = mc.joint(n=side + 'pupil_01_JNT', rad=0.8)
        mc.xform(pupilJoint, t=eyePupilProxyPos, ws=1)
        mc.xform(pupilJoint, ro=eyePupilProxyRot, ws=1)
        mc.makeIdentity(pupilJoint, a=1)
        mc.parent(pupilJoint, eyeJoint)
        mc.select(cl=1)

        upperLidParentJoint = mc.joint(n=side + 'upperLid_01_JNT', rad=0.8)
        mc.xform(upperLidParentJoint, t=eyeUpperLidParentProxyPos, ws=1)
        mc.xform(upperLidParentJoint, ro=eyeUpperLidParentProxyRot, ws=1)
        mc.makeIdentity(upperLidParentJoint, a=1)
        mc.select(cl=1)

        upperLidJoint = mc.joint(n=side + 'upperLid_02_JNT', rad=0.8)
        mc.xform(upperLidJoint, t=eyeUpperLidProxyPos, ws=1)
        mc.xform(upperLidJoint, ro=eyeUpperLidProxyRot, ws=1)
        mc.makeIdentity(upperLidJoint, a=1)
        mc.parent(upperLidJoint, upperLidParentJoint)
        mc.select(cl=1)

        lowerLidParentJoint = mc.joint(n=side + 'lowerLid_01_JNT', rad=0.8)
        mc.xform(lowerLidParentJoint, t=eyeLowerLidParentProxyPos, ws=1)
        mc.xform(lowerLidParentJoint, ro=eyeLowerLidParentProxyRot, ws=1)
        mc.makeIdentity(lowerLidParentJoint, a=1)
        mc.select(cl=1)

        lowerLidJoint = mc.joint(n=side + 'lowerLid_02_JNT', rad=0.8)
        mc.xform(lowerLidJoint, t=eyeLowerLidProxyPos, ws=1)
        mc.xform(lowerLidJoint, ro=eyeLowerLidProxyRot, ws=1)
        mc.makeIdentity(lowerLidJoint, a=1)
        mc.parent(lowerLidJoint, lowerLidParentJoint)
        mc.select(cl=1)

        mc.joint(n='C_lidsHolder_01_JNT', rad=0.8)
        mc.select(cl=1)

        # Creating Global Controls and system:
        eyeSocketControlZTR = mc.createNode('transform', n=side + 'socket_01_ZTR')
        eyeSocketControl = mc.circle(n=side + 'socket_01_CTRL', nr=(0, 0, 1), r=5, c=(0, 0, 5))[0]
        mc.parent(eyeSocketControl, eyeSocketControlZTR)
        mc.xform(eyeSocketControlZTR, t=eyeSocketProxyPos, ws=1)
        mc.xform(eyeSocketControlZTR, ro=eyeSocketProxyRot, ws=1)
        mc.parentConstraint(eyeSocketControl, socketJoint, mo=1)
        mc.connectAttr(eyeSocketControl + '.s', socketJoint + '.s')

        eyeControlGRP = mc.createNode('transform', n=side + 'eye_01_GRP')
        eyeControlZTR = mc.createNode('transform', n=side + 'eye_01_ZTR', p=eyeControlGRP)
        eyeControl = mc.circle(n=side + 'eye_01_CTRL', nr=(0, 0, 1), r=5, c=(0, 0, 0))[0]
        mc.parent(eyeControl, eyeControlZTR)
        mc.xform(eyeControlGRP, t=eyeCenterProxyPos, ws=1)
        mc.xform(eyeControlGRP, ro=eyeCenterProxyRot, ws=1)
        mc.setAttr(eyeControlZTR + '.tz', 30)
        mc.aimConstraint(eyeControl, eyeJoint, wuo=eyeSocketControl,
                         wut='objectrotation', wu=(0, 1, 0), u=(0, 1, 0), aim=(0, 0, 1))
        mc.disconnectAttr(socketJoint + '.scale', eyeJoint + '.inverseScale')

        # Creating local Controls and system:
        upperLidZTR = mc.createNode('transform', n=side + 'upperLid_01_ZTR')
        upperLid = mc.circle(n=side + 'upperLid_01_CTRL', nr=(0, 0, 1), r=2, c=(0, 0, 0))[0]
        mc.parent(upperLid, upperLidZTR)
        mc.xform(upperLidZTR, t=eyeUpperLidProxyPos, ws=1)

        lowerLidZTR = mc.createNode('transform', n=side + 'lowerLid_01_ZTR')
        lowerLid = mc.circle(n=side + 'lowerLid_01_CTRL', nr=(0, 0, 1), r=2, c=(0, 0, 0))[0]
        mc.parent(lowerLid, lowerLidZTR)
        mc.xform(lowerLidZTR, t=eyeLowerLidProxyPos, ws=1)

        followHelperGRP = mc.createNode('transform', n=side + 'eyeLidFinalRot_01_GRP')
        followHelper = mc.createNode('transform', n=side + 'eyeLidFinalRot_01_CONS', p=followHelperGRP)
        mc.xform(followHelperGRP, t=eyeCenterProxyPos, ws=1)
        mc.xform(followHelperGRP, ro=eyeCenterProxyRot, ws=1)
        mc.parent(followHelperGRP, socketJoint)
        mc.parentConstraint(eyeJoint, followHelper, mo=1)

        # Creating NOdes----------------------------------------------------------------------
        # Remaping translations:------------------------------------------------------------
        lowLidVertRMP = mc.createNode('remapValue', n=side + 'lowerLid_vertical_01_REMAP')
        mc.connectAttr(lowerLid + '.ty', lowLidVertRMP + '.inputValue')
        mc.setAttr(lowLidVertRMP + '.inputMin', moveValue * -1)
        mc.setAttr(lowLidVertRMP + '.inputMax', moveValue)
        mc.setAttr(lowLidVertRMP + '.outputMin', angle)
        mc.setAttr(lowLidVertRMP + '.outputMax', angle * -1)

        lowLidSideRMP = mc.createNode('remapValue', n=side + 'lowerLid_side_01_REMAP')
        mc.connectAttr(lowerLid + '.tx', lowLidSideRMP + '.inputValue')
        mc.setAttr(lowLidSideRMP + '.inputMin', moveValue * -1)
        mc.setAttr(lowLidSideRMP + '.inputMax', moveValue)
        mc.setAttr(lowLidSideRMP + '.outputMin', -10)
        mc.setAttr(lowLidSideRMP + '.outputMax', 10)

        lowLidPMA = mc.createNode('plusMinusAverage', n=side + 'lowerLid_01_PMA')
        mc.connectAttr(lowLidVertRMP + '.outValue', lowLidPMA + '.input3D[0].input3Dx')
        mc.connectAttr(lowLidSideRMP + '.outValue', lowLidPMA + '.input3D[0].input3Dy')
        # Connecting Side Move and Rotation:
        mc.connectAttr(lowLidPMA + '.output3Dy', lowerLidParentJoint + '.ry')
        mc.connectAttr(lowerLid + '.rz', lowerLidParentJoint + '.rz')

        upLidVertRMP = mc.createNode('remapValue', n=side + 'upperLid_vertical_01_REMAP')
        mc.connectAttr(upperLid + '.ty', upLidVertRMP + '.inputValue')
        mc.setAttr(upLidVertRMP + '.inputMin', moveValue * -1)
        mc.setAttr(upLidVertRMP + '.inputMax', moveValue)
        mc.setAttr(upLidVertRMP + '.outputMin', angle)
        mc.setAttr(upLidVertRMP + '.outputMax', angle * -1)

        upLidSideRMP = mc.createNode('remapValue', n=side + 'upperLid_side_01_REMAP')
        mc.connectAttr(upperLid + '.tx', upLidSideRMP + '.inputValue')
        mc.setAttr(upLidSideRMP + '.inputMin', moveValue * -1)
        mc.setAttr(upLidSideRMP + '.inputMax', moveValue)
        mc.setAttr(upLidSideRMP + '.outputMin', -10)
        mc.setAttr(upLidSideRMP + '.outputMax', 10)

        upLidPMA = mc.createNode('plusMinusAverage', n=side + 'upperLid_01_PMA')
        mc.connectAttr(upLidVertRMP + '.outValue', upLidPMA + '.input3D[0].input3Dx')
        mc.connectAttr(upLidSideRMP + '.outValue', upLidPMA + '.input3D[0].input3Dy')
        # Connecting Side Move and Rotation:
        mc.connectAttr(upLidPMA + '.output3Dy', upperLidParentJoint + '.ry')
        mc.connectAttr(upperLid + '.rz', upperLidParentJoint + '.rz')

        # Starting fleshyEleyelids------------------------------------------------------
        fleshyMD = mc.createNode('multiplyDivide', n=side + 'fleshyEyelid_01_MD')
        mc.connectAttr(followHelper + '.rx', fleshyMD + '.input1X')
        mc.connectAttr(followHelper + '.ry', fleshyMD + '.input1Y')
        mc.connectAttr(followHelper + '.rz', fleshyMD + '.input1Z')
        mc.connectAttr(eyesMainControl + '.fleshyEyelids', fleshyMD + '.input2X')
        mc.connectAttr(eyesMainControl + '.fleshyEyelids', fleshyMD + '.input2Y')

        # FleshyRemaps:
        lowLidFollow = mc.createNode('remapValue', n=side + 'lowerLid_01_followREMAP')
        mc.connectAttr(fleshyMD + '.outputX', lowLidFollow + '.inputValue')
        mc.setAttr(lowLidFollow + '.inputMin', angle * -1)
        mc.setAttr(lowLidFollow + '.inputMax', angle)
        mc.setAttr(lowLidFollow + '.outputMin', angle * -1)
        mc.setAttr(lowLidFollow + '.outputMax', angle)
        mc.setAttr(lowLidFollow + '.value[0].value_FloatValue', 0.42)
        mc.setAttr(lowLidFollow + '.value[0].value_Position', 0)
        mc.setAttr(lowLidFollow + '.value[2].value_FloatValue', 0.5)
        mc.setAttr(lowLidFollow + '.value[2].value_Position', 0.5)
        mc.setAttr(lowLidFollow + '.value[1].value_FloatValue', 0.72)
        mc.setAttr(lowLidFollow + '.value[1].value_Position', 1)
        mc.setAttr(lowLidFollow + '.value[2].value_Interp', 1)

        upLidFollow = mc.createNode('remapValue', n=side + 'upperLid_01_followREMAP')
        mc.connectAttr(fleshyMD + '.outputX', upLidFollow + '.inputValue')
        mc.setAttr(upLidFollow + '.inputMin', angle * -1)
        mc.setAttr(upLidFollow + '.inputMax', angle)
        mc.setAttr(upLidFollow + '.outputMin', angle * -1)
        mc.setAttr(upLidFollow + '.outputMax', angle)
        mc.setAttr(upLidFollow + '.value[0].value_FloatValue', 0.16)
        mc.setAttr(upLidFollow + '.value[0].value_Position', 0)
        mc.setAttr(upLidFollow + '.value[2].value_FloatValue', 0.5)
        mc.setAttr(upLidFollow + '.value[2].value_Position', 0.5)
        mc.setAttr(upLidFollow + '.value[1].value_FloatValue', 1)
        mc.setAttr(upLidFollow + '.value[1].value_Position', 1)
        mc.setAttr(upLidFollow + '.value[2].value_Interp', 1)

        sideFollowRmp = mc.createNode('remapValue', n=side + 'eyeSide_01_followREMAP')
        mc.connectAttr(fleshyMD + '.outputY', sideFollowRmp + '.inputValue')
        mc.setAttr(sideFollowRmp + '.inputMin', angle * -1)
        mc.setAttr(sideFollowRmp + '.inputMax', angle)
        mc.setAttr(sideFollowRmp + '.outputMin', -10)
        mc.setAttr(sideFollowRmp + '.outputMax', 10)

        # Connecting with mains PMAs-------------------------------------------------------------

        mc.connectAttr(lowLidFollow + '.outValue', lowLidPMA + '.input3D[1].input3Dx')
        mc.connectAttr(sideFollowRmp + '.outValue', lowLidPMA + '.input3D[1].input3Dy')

        mc.connectAttr(upLidFollow + '.outValue', upLidPMA + '.input3D[1].input3Dx')
        mc.connectAttr(sideFollowRmp + '.outValue', upLidPMA + '.input3D[1].input3Dy')

        # Blink----------------------------------------------------------------------------------
        blinkPMA = mc.createNode('plusMinusAverage', n=side + 'eyeLidBlink_01_PMA')
        mc.setAttr(blinkPMA + '.operation', 2)
        mc.connectAttr(lowLidPMA + '.output3Dx', blinkPMA + '.input3D[0].input3Dx')
        mc.connectAttr(upLidPMA + '.output3Dx', blinkPMA + '.input3D[1].input3Dx')
        mc.setAttr(blinkPMA + '.input3D[2].input3Dx', angle * -1)

        eyeLidBLinkMD = mc.createNode('multiplyDivide', n=side + 'eyelidBlink_01_MD')
        mc.connectAttr(blinkPMA + '.output3Dx', eyeLidBLinkMD + '.input1X')
        mc.connectAttr(eyesMainControl + '.' + blinkAttr, eyeLidBLinkMD + '.input2X')

        # Blending blink with mains PMAs------------------------------------------------------------

        lowerLidBlend = mc.createNode('blendColors', n=side + 'lowerLidBlend_01_BC')
        mc.connectAttr(eyesMainControl + '.' + blinkPoseAttr, lowerLidBlend + '.blender')
        mc.connectAttr(eyeLidBLinkMD + '.outputX', lowerLidBlend + '.color2R')
        mc.setAttr(lowerLidBlend + '.color1R', 0)
        mc.setAttr(lowerLidBlend + '.color1G', 0)
        mc.setAttr(lowerLidBlend + '.color1B', 0)

        upperLidBlend = mc.createNode('blendColors', n=side + 'upperLidBlend_01_BC')
        mc.connectAttr(eyesMainControl + '.' + blinkPoseAttr, upperLidBlend + '.blender')
        mc.connectAttr(eyeLidBLinkMD + '.outputX', upperLidBlend + '.color1R')
        mc.setAttr(upperLidBlend + '.color2R', 0)
        mc.setAttr(upperLidBlend + '.color2G', 0)
        mc.setAttr(upperLidBlend + '.color2B', 0)

        lowerBlinkPMA = mc.createNode('plusMinusAverage', n=side + 'lowerLidBlink_01_PMA')
        mc.setAttr(lowerBlinkPMA + '.operation', 2)
        mc.connectAttr(lowLidPMA + '.output3Dx', lowerBlinkPMA + '.input3D[0].input3Dx')
        mc.connectAttr(lowerLidBlend + '.outputR', lowerBlinkPMA + '.input3D[1].input3Dx')

        upperBlinkPMA = mc.createNode('plusMinusAverage', n=side + 'lowerLidBlink_01_PMA')
        mc.connectAttr(upLidPMA + '.output3Dx', upperBlinkPMA + '.input3D[0].input3Dx')
        mc.connectAttr(upperLidBlend + '.outputR', upperBlinkPMA + '.input3D[1].input3Dx')

        # Connecting with lowerLidJoint-------------------------------------------------------------

        mc.connectAttr(lowerBlinkPMA + '.output3Dx', lowerLidParentJoint + '.rx')

        # Addtional Push Nodes for upperJoint-----------------------------------------------------------

        upperPushPMA = mc.createNode('plusMinusAverage', n=side + 'upperPush_01_PMA')
        mc.connectAttr(lowerLidParentJoint + '.rx', upperPushPMA + '.input3D[1].input3Dx')
        mc.setAttr(upperPushPMA + '.input3D[0].input3Dx', angle)

        upperPushClamp = mc.createNode('clamp', n=side + 'upperPush_01_CLAMP')
        mc.setAttr(upperPushClamp + '.minR', angle * -1)
        mc.connectAttr(upperBlinkPMA + '.output3Dx', upperPushClamp + '.inputR')
        mc.connectAttr(upperPushPMA + '.output3Dx', upperPushClamp + '.maxR')

        mc.connectAttr(upperPushClamp + '.outputR', upperLidParentJoint + '.rx')

        # Connecting Pupils------------------------------------------------------------

        mc.connectAttr(eyesMainControl + '.' + pupilAttr, pupilJoint + '.sx')
        mc.connectAttr(eyesMainControl + '.' + pupilAttr, pupilJoint + '.sy')





faceLocator()
#createSystem()
