import maya.cmds as mc
import random 
import maya.mel as mel

mats=mc.ls('MAT_*')
root = 'C_root_01_CTRL'
attrList = mc.listAttr(root, ud=1)

if 'colorChecker' in attrList:
    pass
else:
    mc.addAttr(root, ln='colorChecker', at='long', min=0, max=1, dv=0, k=1)

for x in mats:
    # color Values -----------------------------------------------------------------
    hue = random.uniform(0.0, 1.0)
    saturation = random.uniform(0.0, 1.0)
    value = random.uniform(0.0, 1.0)
    # ------------------------------------------------------------------------------
    # Creating Nodes----------------------------------------------------------------    
    if mc.objExists(x.replace('MAT','colorChecker'))==False:
        shadingGroup = mc.listConnections(x,type='shadingEngine')[0]
        colorBlender = mc.createNode('blendColors', n=x.replace('MAT', 'blender'))
        print colorBlender
        colorChecker = mc.createNode('blinn', n=x.replace('MAT', 'colorChecker'))    
        print colorChecker
        mc.setAttr(colorChecker+'.color', hue, saturation, value, type = 'double3')
        # --------------------------------------------------------------------------
        # Connecting Nodes----------------------------------------------------------
        mc.connectAttr(x + '.outColor', colorBlender + '.color2', f=1)
        mc.connectAttr(colorChecker + '.outColor', colorBlender + '.color1', f=1)
        mc.connectAttr(colorBlender + '.output', shadingGroup + '.surfaceShader', f=1)
        mc.connectAttr(root + '.colorChecker', colorBlender + '.blender', f=1)

    else:
        colorChecker = x.replace('MAT', 'colorChecker')
        mc.setAttr(colorChecker+'.color', hue, saturation, value, type = 'double3')







    
    






        