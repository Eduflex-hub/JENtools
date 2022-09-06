import maya.cmds as mc

pupilJoints = mc.ls('*pupil_01_JNT')
eyeControl = 'C_eyes_01_CTRL'

for x in pupilJoints:
	#Creating Joints
	index = pupilJoints.index(x)
	irisJoint = mc.duplicate(x)
	irisJoint = mc.rename(irisJoint, x.replace('pupil', 'iris'))
	irisParent = mc.listRelatives(irisJoint, p=1)[0]
	print irisParent

	ztr = mc.createNode('transform', n=irisJoint.replace('JNT', 'JNT_ZTR'), p=irisParent)

	mc.delete(mc.parentConstraint(irisJoint, ztr, mo=0))	
	mc.parent(irisJoint, ztr)

	#Creating system
	if index == 0:
		mc.addAttr(eyeControl, ln='____', at='enum', en='iris', k=1)
		
	if x.startswith('C_head_01_L_'):
		attr = 'lIris'
		mc.addAttr(eyeControl, ln=attr, at='float', dv=1,  k=1)

	elif x.startswith('C_head_01_R_'):
		attr = 'rIris'
		mc.addAttr(eyeControl, ln=attr, at='float', dv=1,  k=1)	

	pma = mc.createNode('plusMinusAverage', n=irisJoint.replace('JNT', 'transPMA'))
	mc.setAttr(pma + '.input1D[1]', -1)
	mc.connectAttr(eyeControl + '.' + attr, pma + '.input1D[0]')

	remapTrans = mc.createNode('remapValue', n=irisJoint.replace('JNT', 'transREMAP'))
	mc.setAttr(remapTrans + '.inputMin', -1)
	mc.setAttr(remapTrans + '.inputMax', 1)
	mc.setAttr(remapTrans + '.outputMin', 1)
	mc.setAttr(remapTrans + '.outputMax', -1)

	mc.setAttr(remapTrans + '.value[0].value_FloatValue', 0.5)
	mc.setAttr(remapTrans + '.value[0].value_Position', 0)
	mc.setAttr(remapTrans + '.value[2].value_FloatValue', 0.5)
	mc.setAttr(remapTrans + '.value[2].value_Position', 0.5)
	mc.setAttr(remapTrans + '.value[1].value_FloatValue', 0.72)
	mc.setAttr(remapTrans + '.value[1].value_Position', 1)
	mc.setAttr(remapTrans + '.value[2].value_Interp', 1)

	mc.connectAttr(pma + '.output1D', remapTrans + '.inputValue')
	mc.connectAttr(remapTrans + '.outValue', irisJoint + '.tz')


	remapScale = mc.createNode('remapValue', n=irisJoint.replace('JNT', 'scaleREMAP'))
	mc.setAttr(remapScale + '.inputMin', 0)
	mc.setAttr(remapScale + '.inputMax', 2)
	mc.setAttr(remapScale + '.outputMin', 0.5)
	mc.setAttr(remapScale + '.outputMax', 1.5)

	mc.setAttr(remapScale + '.value[0].value_FloatValue', 0)
	mc.setAttr(remapScale + '.value[0].value_Position', 0)
	mc.setAttr(remapScale + '.value[2].value_FloatValue', 0.5)
	mc.setAttr(remapScale + '.value[2].value_Position', 0.5)
	mc.setAttr(remapScale + '.value[1].value_FloatValue', 1)
	mc.setAttr(remapScale + '.value[1].value_Position', 1)
	mc.setAttr(remapScale + '.value[2].value_Interp', 1)

	mc.connectAttr(eyeControl + '.' + attr, remapScale + '.inputValue')
	mc.connectAttr(remapScale + '.outValue', irisJoint + '.sx' )
	mc.connectAttr(remapScale + '.outValue', irisJoint + '.sy' )

	

	


