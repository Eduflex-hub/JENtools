import maya.cmds as mc

def nonLockCons(parentObj, obj, mo, consType):

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
    
    if consType == 'orient':
        cons=mc.orientConstraint(parentObj, obj, mo=mo)

    elif consType == 'parent':
        cons=mc.parentConstraint(parentObj, obj, mo=mo, sr=rotateSkip, st=translateSkip)
    

    return cons


def ikToFkMatch():

    sel = mc.ls(sl=1)
    leftFkFollowers = mc.ls('*:L_*fkFollowMatch')
    leftIkFollowers = mc.ls('*:L_*ikFollowMatch')

    rigthFkFollowers = mc.ls('*:R_*fkFollowMatch')
    rigthIkFollowers = mc.ls('*:R_*ikFollowMatch')
   

    constraints = []
    if sel[0].startswith('L_') == True:
        if sel[0].endswith('ikCTRL')==True:
            for i in leftFkFollowers:
                control = i.replace('_fkFollowMatch', ' ')
                cons = nonLockCons(i, control, 0, 'parent')
                constraints.append(cons[0])

        if sel[0].endswith('fkCTRL')==True:
            for i in leftIkFollowers:
                print i
                control = i.replace('_ikFollowMatch', ' ')
                print control
                cons = nonLockCons(i, control, 0, 'orient')
                constraints.append(cons[0])

    if sel[0].startswith('R_') == True:
        if sel[0].endswith('ikCTRL')==True:
            for i in rigthFkFollowers:
                control = i.replace('_fkFollowMatch', ' ')
                cons = nonLockCons(i, control, 0, 'parent')
                constraints.append(cons[0])

        if sel[0].endswith('fkCTRL')==True:
            for i in rigthIkFollowers:
                control = i.replace('_ikFollowMatch', ' ')
                cons = nonLockCons(i, control, 0, 'orient')
                constraints.append(cons[0])
    mc.delete(constraints)

ikToFkMatch()
