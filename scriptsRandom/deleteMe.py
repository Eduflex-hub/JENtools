import maya.cmds as mc

sel = mc.ls(sl=1)

for x in sel:    
    axis = 'rotateZ'
    source = x + '_' + axis
    mc.connectAttr(source + '.output', x + '.' + axis)

    if 'L_' in x:
        switch = 'L_lowerArm_01_endswitchCTRL'
    elif 'R_' in x:
        switch = 'R_lowerArm_01_endswitchCTRL'

    if 'thumb' in source:
        mc.connectAttr(switch + '.thumbBend', source + '.input')
    elif:
        mc.connectAttr(switch + '.handBend', source + '.input')
        