import maya.cmds as mc

sel = mc.ls(sl=1)

bsNode='C_headMouthExpresions_BSNODE'



for x in sel:
	if x.startswith('L_') == True:
		side='L_'

	if x.startswith('R_') == True:
		side='R_'

	inRmp = mc.createNode('remapValue', n=x.replace('CTRL', 'IN_REMAP'))
	outRmp = mc.createNode('remapValue', n=x.replace('CTRL', 'OUT_REMAP'))
	upRmp = mc.createNode('remapValue', n=x.replace('CTRL', 'UP_REMAP'))
	downRmp = mc.createNode('remapValue', n=x.replace('CTRL', 'DOWN_REMAP'))

	mc.setAttr(inRmp+'.inputMax', -1)
	mc.setAttr(downRmp+'.inputMax', -1)

	mc.connectAttr(x+'.tx', inRmp+'.inputValue')
	mc.connectAttr(x+'.tx', outRmp+'.inputValue')
	mc.connectAttr(x+'.ty', upRmp+'.inputValue')
	mc.connectAttr(x+'.ty', downRmp+'.inputValue')

	mc.connectAttr(inRmp+'.outValue', bsNode+ '.'+ side +'mouthCornerIn_TGT')
	mc.connectAttr(outRmp+'.outValue', bsNode+ '.'+ side +'mouthCornerOut_TGT')
	mc.connectAttr(upRmp+'.outValue', bsNode+ '.'+ side +'mouthCornerUp_TGT')
	mc.connectAttr(downRmp+'.outValue', bsNode+ '.'+ side +'mouthCornerDown_TGT')


	
