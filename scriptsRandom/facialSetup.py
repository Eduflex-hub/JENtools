import maya.cmds as mc



def pointLocators():

	localRigGRP=mc.createNode('transform', n='C_localJoints_01_GRP' )
	localLidsGRP=mc.createNode('transform', n='C_localEyeLids_GRP' )
	localLipsGRP=mc.createNode('transform', n='C_headLips_GRP' )


	###################################
	#local rig Locators
	###################################
	#NOSE#
	noseBase=mc.spaceLocator(n='C_noseBase_01_localTarget')
	leftNoseFosa=mc.spaceLocator(n='L_noseFosa_01_localTarget')
	rigthNoseFosa=mc.spaceLocator(n='R_noseFosa_01_localTarget')
	mc.parent(leftNoseFosa, rigthNoseFosa, noseBase)
	nosePosMD=mc.createNode('multiplyDivide', n='C_noseMirrorPosNode_MD')
	mc.connectAttr(leftNoseFosa[0]+'.translate', nosePosMD+'.input1')
	mc.setAttr(nosePosMD+'.input2X', -1)
	mc.connectAttr(nosePosMD+'.output', rigthNoseFosa[0]+'.translate')

	noseRotMD=mc.createNode('multiplyDivide', n='C_noseMirrorRotNode_MD')
	mc.connectAttr(leftNoseFosa[0]+'.rotate', noseRotMD+'.input1')
	mc.setAttr(noseRotMD+'.input2Y', -1)
	mc.setAttr(noseRotMD+'.input2Z', -1)
	mc.connectAttr(noseRotMD+'.output', rigthNoseFosa[0]+'.rotate')
	mc.move(noseBase, (0.6.0))

	#LIP#
	lip=mc.spaceLocator(n='C_lip_01_localTarget')

	#EAR#
	leftEar=mc.spaceLocator(n='L_ear_01_localTarget')
	leftEarTop=mc.spaceLocator(n='L_earTop_01_localTarget')
	mc.parent(leftEarTop, leftEar)

	rigthEar=mc.spaceLocator(n='R_ear_01_localTarget')
	rigthEarTop=mc.spaceLocator(n='R_earTop_01_localTarget')
	mc.parent(rigthEarTop, rigthEar)

	earPosMD=mc.createNode('multiplyDivide', n='C_earMirrorPosNode_MD')
	mc.connectAttr(leftEar[0]+'.translate', earPosMD+'.input1')
	mc.setAttr(earPosMD+'.input2X', -1)
	mc.connectAttr(earPosMD+'.output', rigthEar[0]+'.translate')

	earRotMD=mc.createNode('multiplyDivide', n='C_earMirrorRotNode_MD')
	mc.connectAttr(leftEar[0]+'.rotate', earRotMD+'.input1')
	mc.setAttr(earRotMD+'.input2Y', -1)
	mc.setAttr(earRotMD+'.input2Z', -1)
	mc.connectAttr(earRotMD+'.output', rigthEar[0]+'.rotate')

	earTopPosMD=mc.createNode('multiplyDivide', n='C_earTopMirrorPosNode_MD')
	mc.connectAttr(leftEarTop[0]+'.translate', earTopPosMD+'.input1')
	mc.setAttr(earTopPosMD+'.input2X', -1)
	mc.connectAttr(earTopPosMD+'.output', rigthEarTop[0]+'.translate')

	earTopRotMD=mc.createNode('multiplyDivide', n='C_earTopMirrorRotNode_MD')
	mc.connectAttr(leftEarTop[0]+'.rotate', earTopRotMD+'.input1')
	mc.setAttr(earTopRotMD+'.input2Y', -1)
	mc.setAttr(earTopRotMD+'.input2Z', -1)
	mc.connectAttr(earTopRotMD+'.output', rigthEarTop[0]+'.rotate')


	leftCheek=mc.spaceLocator(n='L_cheek_01_localTarget')
	rigthCheek=mc.spaceLocator(n='R_cheek_01_localTarget')

	cheekPosMD=mc.createNode('multiplyDivide', n='C_cheekMirrorPosNode_MD')
	mc.connectAttr(leftCheek[0]+'.translate', cheekPosMD+'.input1')
	mc.setAttr(cheekPosMD+'.input2X', -1)
	mc.connectAttr(cheekPosMD+'.output', rigthCheek[0]+'.translate')

	chin=mc.spaceLocator(n='C_chin_01_localTarget')

	mc.parent(noseBase, lip, leftEar, rigthEar, leftCheek, rigthCheek, chin, localRigGRP)

	###################################
	#lids rig Locators
	###################################
	'''
	leftCenterEye=mc.spaceLocator(n='L_eyeCenter_01_localTarget')
	rigthCenterEye=mc.spaceLocator(n='R_eyeCenter_01_localTarget')

	for i in range(0,4):
		index= range(0,4).index(x)
		upperLid=mc.spaceLocator(n='R_eyeCenter_0'+str(index)+'_localTarget')
		upperCrease=mc.spaceLocator(n='R_eyeCenter_0'+str(index)+'_localTarget')

		lowerCrease=mc.spaceLocator(n='R_eyeCenter_0'+str(index)+'_localTarget')
	'''
pointLocators()

	