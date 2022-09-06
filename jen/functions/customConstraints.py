# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------
##
# Mocap Functions
##
# ------------------------------------------------------------------------------------------

import maya.cmds as mc


def nonLockCons(parentObj, obj):

    attrs = mc.listAttr(obj, l=1)
    translateSkip = []
    rotateSkip = []

    if attrs != None:
        for lockedAttr in attrs:
            if lockedAttr == 'visibility':
                attrs.remove(lockedAttr)        
        for attribute in attrs:
            if attribute.startswith('translate') == True:
                axis = attribute[-1]
                axis = axis.lower()
                translateSkip.append(axis)

            if attribute.startswith('rotate') == True:
                axis = attribute[-1]
                axis = axis.lower()
                rotateSkip.append(axis)


    mc.parentConstraint(parentObj, obj, mo=1, sr=rotateSkip, st=(translateSkip))


# def createSet