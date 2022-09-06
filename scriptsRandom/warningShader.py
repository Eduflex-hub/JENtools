# Warning Shader

import maya.cmds as cmds
import maya.mel as mel

def applyWarningToShader(geo, name, shader, driver, squashRange=[0.975, 0.95], stretchRange=[1.025, 1.05] ):
    rigPrefs = 'rig_preferences'
    warningShaderCacheModeMultDL = 'rig_warningShaderCacheMode_multDoubleLinear'
    if cmds.objExists( rigPrefs ):
        cmds.addAttr( rigPrefs + '.cacheMode', edit=True, defaultValue=0 )
        cmds.setAttr( rigPrefs + '.cacheMode', 0 )
        if not cmds.attributeQuery( 'separator4', node='rig_preferences', exists=True ):
            cmds.addAttr( 'rig_preferences', longName='separator4', niceName='---------------', attributeType='enum', enumName='--------' )
            cmds.setAttr( rigPrefs + '.separator4', channelBox=True )
        if not cmds.attributeQuery( 'warningShaders', node='rig_preferences', exists=True ):
            cmds.addAttr( 'rig_preferences', longName='warningShaders', attributeType='enum', enumName='Off:On', defaultValue=1 )
            cmds.setAttr( rigPrefs + '.warningShaders', channelBox=True )
        warningShaderCacheModeRev = 'rig_warningShaderCacheMode_reverse'
        if not cmds.objExists( warningShaderCacheModeRev ):
            warningShaderCacheModeRev = cmds.createNode( 'reverse', name=warningShaderCacheModeRev )
            cmds.connectAttr( rigPrefs + '.cacheMode', warningShaderCacheModeRev + '.inputX' )
        if not cmds.objExists( warningShaderCacheModeMultDL ):
            warningShaderCacheModeMultDL = cmds.createNode( 'multDoubleLinear', name=warningShaderCacheModeMultDL )
            cmds.connectAttr( warningShaderCacheModeRev + '.outputX', warningShaderCacheModeMultDL + '.input1' )
            cmds.connectAttr( rigPrefs + '.warningShaders', warningShaderCacheModeMultDL + '.input2' )

    # Creating the warning shader:
    tempShader = mel.eval( 'dnLibShader_makeStretchWarningShaderFromAttr ("' + driver + '", "' + name + '", "lambert", "")' )[0]
    if tempShader:
        # Getting the nodes that feed it:
        stretchUnitConv = cmds.listConnections( tempShader + '.incandescenceR', destination=False )[0]
        stretchRemapVal = cmds.listConnections( tempShader + '.incandescenceR', destination=False, skipConversionNodes=True )[0]
        squashUnitConv = cmds.listConnections( tempShader + '.incandescenceB', destination=False )[0]
        squashRemapVal = cmds.listConnections( tempShader + '.incandescenceB', destination=False, skipConversionNodes=True )[0]
        # Tweaking the ranges of the squash and stretch rempaValue nodes:
        cmds.setAttr( squashRemapVal + '.inputMin', squashRange[0] )
        cmds.setAttr( squashRemapVal + '.inputMax', squashRange[1] )
        cmds.setAttr( stretchRemapVal + '.inputMin', stretchRange[0] )
        cmds.setAttr( stretchRemapVal + '.inputMax', stretchRange[1] )
        # Setting up rig prefs control over the stretch shader visibility:

        if cmds.objExists( warningShaderCacheModeMultDL ):
            squashShaderCtrlRemapVal = cmds.createNode( 'remapValue', name=(name + '_squashWarningShaderControl_remapValue') )
            cmds.setAttr( squashShaderCtrlRemapVal + '.outputMin', cmds.getAttr( tempShader + '.incandescenceR' ) )
            cmds.connectAttr( warningShaderCacheModeMultDL + '.output', squashShaderCtrlRemapVal + '.inputValue' )
            cmds.connectAttr( squashShaderCtrlRemapVal + '.outValue', squashRemapVal + '.outputMax' )
            stretchShaderCtrlRemapVal = cmds.createNode( 'remapValue', name=(name + '_stretchWarningShaderControl_remapValue') )
            cmds.setAttr( stretchShaderCtrlRemapVal + '.outputMin', cmds.getAttr( tempShader + '.incandescenceR' ) )
            cmds.connectAttr( warningShaderCacheModeMultDL + '.output', stretchShaderCtrlRemapVal + '.inputValue' )
            cmds.connectAttr( stretchShaderCtrlRemapVal + '.outValue', stretchRemapVal + '.outputMax' )
        else:
            cmds.warning( 'Unable to find "' + driver + '" for ' + name + ' warning shader')
        
        cmds.select(geo, r=True)
        
        cmds.hyperShade(assign=tempShader)
       

'''
def warningShader():
    for side in ['L', 'R']:
        geo = '%s_antenna_01_geo' %side
        if cmds.objExists(geo):
            shader = '%s_stretchWarning_blinn' %side
            squashRange = [0.975, 0.95]
            stretchRange = [1.025, 1.05]
            
            curvInfo = cmds.createNode('curveInfo', n=('%s_antenna_01_curvInfo' %side))
            cmds.connectAttr('%s_frontAntenna_display_curveShape.worldSpace[0]'%side, curvInfo + '.inputCurve', force=True)
            
            cmds.addAttr('%s_frontAntenna_display_curve'%side, at='double', dv=0, ln='length')
            cmds.setAttr('%s_frontAntenna_display_curve.length'%side, edit=True, keyable=True)
            cmds.connectAttr(curvInfo + '.arcLength', '%s_frontAntenna_display_curve.length' %side, force=True)
            
            driver = '%s_frontAntenna_display_curve.length' %side
            
            applyWarningToShader(geo, '%s_stretch' %side, shader, driver, squashRange=squashRange, stretchRange=stretchRange )




def warningShader():
    nameMap = {'L':'01', 'R':'02', 'Front':'front', 'Back':'rear'}
    for side in ['L', 'R']:
        for face in ['Front', 'Back']:
            geo = '%s_wheelArm_%s_geo' % (nameMap[face], nameMap[side])
        if cmds.objExists(geo):
                shader = '%s_suspension%sWarning_blinn' % (side, face)
                squashRange = [0.975, 0.95]
                stretchRange = [1.025, 1.05]
                #geo = '%s_suspensionArm%s_geo' % (side, face)
                if face == 'Back':
                        face = 'rear'
'''