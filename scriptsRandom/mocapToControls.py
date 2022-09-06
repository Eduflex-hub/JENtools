# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------
##
# mocap to controls
##
# --------------------------------------------------------------------------------------------

# IMPORTS
import maya.cmds as mc
import os
import sys

jtools = os.getenv("JENTOOLS")
print jtools
sys.path.append(jtools)
print '*'*50

from functions.mocapFunctions import mocapConvertHelper as mch



def Constraints():
    # Creating Nulls-----------------------------------------------
    #excludeList = ['C_eyes_01_CTRL', 'R_eye_01_CTRL', 'L_eye_01_CTRL', 'C_spine_08_endikCTRL', 'L_socket_01_CTRL', 'R_socket_01_CTRL']
    root = 'C_root_01_CTRL'
    attrList = mc.listAttr(root, ud=1)
    print attrList
    if 'mocapAttach' in attrList:
        pass
    else:
        mc.addAttr(root, ln='mocapAttach', at='long', min=0, max=1, dv=0, k=1)

    # Rotating to T-Pose Variables:
    #shoulderAngleZ = 12
    shoulderAngleZ = 5
    upperArmAngleZ = 42
    lowerArmAngleY = 0
    handAngleX = 0
    handAngleZ = 0

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

        mc.setAttr(side + 'clavicle_01_CTRL.rz', shoulderAngleZ)
        mc.setAttr(prefix + side + 'clavicle_01_JNT.rz', shoulderAngleZ)

        mc.setAttr(side + 'upperArm_01_fkCTRL.rz', upperArmAngleZ)
        mc.setAttr(prefix + side + 'upperArm_01_JNT.rz', upperArmAngleZ)

        mc.setAttr(side + 'lowerArm_01_fkCTRL.ry', lowerArmAngleY)
        mc.setAttr(prefix + side + 'lowerArm_01_JNT.ry', lowerArmAngleY)

        mc.setAttr(side + 'hand_01_fkCTRL.rx', handAngleX)
        mc.setAttr(prefix + side + 'hand_01_JNT.rx', handAngleX)

        mc.setAttr(side + 'hand_01_fkCTRL.rz', handAngleZ)
        mc.setAttr(prefix + side + 'hand_01_JNT.rz', handAngleZ)

        handPos = mc.xform(prefix + side + 'hand_01_JNT', q=1, t=1, ws=1)
        handRot = mc.xform(prefix + side + 'hand_01_JNT', q=1, ro=1, ws=1)

        mc.xform(side + 'hand_01_ikCTRL', t=handPos, ws=1)
        mc.xform(side + 'hand_01_ikCTRL', ro=handRot, ws=1)

        if side == 'L_':
            mc.setAttr(side + 'upperArm_01_PoleVector_ikCTRL.tx', poleX)
        if side == 'R_':
            mc.setAttr(side + 'upperArm_01_PoleVector_ikCTRL.tx', poleX * -1)
        mc.setAttr(side + 'upperArm_01_PoleVector_ikCTRL.ty', poleY)
        mc.setAttr(side + 'upperArm_01_PoleVector_ikCTRL.tz', poleZ)

    print "Tpose_Complete"

    # CreatingConstraints-------------------------------------------

    mocapJoints = mc.ls(prefix + '*JNT')
    #excludeList = ['C_body_01_CTRL', 'L_foot_01_ikFootCTRL', 'R_foot_01_ikFootCTRL']

    constrainedControls = []

    for x in mocapJoints:
        name = x.replace(prefix, ' ')
        Control = name.replace('JNT', 'CTRL')
        fkControl = name.replace('JNT', 'fkCTRL')
        ikControl = name.replace('JNT', 'ikCTRL')
        poleVectorControl = name.replace('JNT', 'PoleVector_ikCTRL')

        if Control == 'C_hip_01_CTRL':
            pass

        else:
            if Control != 'C_spine_03_fkCTRL':
                if mc.objExists(Control) == True:
                    #mc.parentConstraint(x, Control, mo=1)
                    mch.nonLockCons(x, Control)
                    constrainedControls.append(Control)

                if mc.objExists(fkControl) == True:
                    #mc.parentConstraint(x, fkControl, mo=1)
                    mch.nonLockCons(x, fkControl)
                    constrainedControls.append(fkControl)

                if mc.objExists(ikControl) == True:
                    #mc.parentConstraint(x, ikControl, mo=1)
                    mch.nonLockCons(x, ikControl)
                    constrainedControls.append(ikControl)

                if mc.objExists(poleVectorControl) == True:
                    #mc.parentConstraint(x, poleVectorControl, mo=1)
                    mch.nonLockCons(x, poleVectorControl)
                    constrainedControls.append(poleVectorControl)

        #mc.parentConstraint('mocap_C_spine_06_JNT', 'C_spine_03_fkCTRL', mo=1)
        mch.nonLockCons('mocap_C_spine_06_JNT', 'C_spine_03_fkCTRL')
        #mc.parentConstraint('mocap_C_hip_01_JNT', 'C_body_01_CTRL', mo=1)
        mch.nonLockCons('mocap_C_hip_01_JNT', 'C_body_01_CTRL')
        #mc.parentConstraint('mocap_L_foot_01_JNT', 'L_foot_01_ikFootCTRL', mo=1)
        mch.nonLockCons('mocap_L_foot_01_JNT', 'L_foot_01_ikFootCTRL')
        #mc.parentConstraint('mocap_R_foot_01_JNT', 'R_foot_01_ikFootCTRL', mo=1)
        mch.nonLockCons('mocap_R_foot_01_JNT', 'R_foot_01_ikFootCTRL')

        constrainedControls.append('C_spine_03_fkCTRL')
        constrainedControls.append('C_body_01_CTRL')
        constrainedControls.append('L_foot_01_ikFootCTRL')
        constrainedControls.append('R_foot_01_ikFootCTRL')

    print "Constraints_Complete"

    mc.sets(constrainedControls, n='bakeableControls')

    for x in constrainedControls:

        mc.setKeyframe(x, at='translate')
        mc.setKeyframe(x, at='rotate')
        attr = mc.listAttr(x, k=1, ud=1)
        if attr != None:
            for i in attr:
                if i == 'blendParent1':
                    mc.connectAttr('C_root_01_CTRL.mocapAttach', x + '.' + i, f=1)
    print "keyframe_Complete"


Constraints()
