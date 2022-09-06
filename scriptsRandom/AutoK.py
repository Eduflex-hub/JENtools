import maya.cmds as mc
import maya.mel as mel

sel=mc.ls(sl=1)

if mc.objExists('driverJoints_GRP')==False:
	drvGrp=mc.createNode('transform',n='driverJoints_GRP')
	mc.parent(drvGrp, 'Rig')
else:
	drvGrp='driverJoints_GRP'
mc.select(sel)

def localGrp(_obj):
	lista=mc.ls(_obj)
	for x in lista:
		coord = mc.xform(x, q=1, t=1, ws=1)
		orient= mc.xform(x, q=1, ro=1, ws=1)
		grp=mc.createNode('transform',n= x+'_GRP')
		mc.xform(grp, t=coord, ws=1)
		mc.xform(grp, ro=orient, ws=1)
		mc.parent(x, grp)


def arm():

	#ik Joints_______________________________________________________________
	ikA=[]
	ikB=[]
	ikC=[]
	for x in sel:
		index=sel.index(x)

		coord=mc.xform(x, q=1, t=1, ws=1)
		orient=mc.xform(x, q=1, ro=1, ws=1)
		if index == 0:
			legGrp=mc.createNode('transform', n=x.replace('JNT','ikJNT_GRP'))
			mc.parent(legGrp, drvGrp)
			mc.select(cl=1)

		joint=mc.joint(n=x.replace('JNT', 'ikJNT'))
		mc.xform(joint, t=coord, ws=1)
		mc.xform(joint, ro=orient, ws=1)

		
		
		if index == 0:
			mc.parent(joint, legGrp)
			ikA.append(joint)
		if index ==2:
			ikC.append(joint)
			child=mc.listRelatives(x, c=1)
			ikZTR=mc.createNode('transform', n=child[0].replace('JNT','ikZTR'))
			ikCONS=mc.createNode('transform', n=child[0].replace('JNT','ikCONS'))
			ikCTRL=mel.eval('curve -d 1 -p 3 3 3 -p 3 3 -3 -p -3 3 -3 -p -3 -3 -3 -p 3 -3 -3 -p 3 -3 3 -p -3 -3 3 -p -3 3 3 -p 3 3 3 -p 3 -3 3 -p 3 -3 -3 -p 3 3 -3 -p -3 3 -3 -p -3 3 3 -p -3 -3 3 -p -3 -3 -3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')
			ikCTRL=mc.rename(ikCTRL, ikZTR.replace('ikZTR', 'ikCTRL'))
			mc.parent(ikCTRL, ikCONS)
			mc.parent(ikCONS, ikZTR)
			mc.parent(ikZTR, 'C_main_01_CTRL')			
			mc.connectAttr(ikCTRL+'.s', ikC[0]+'.s')

			coord=mc.xform(child, q=1, t=1, ws=1)
			orient=mc.xform(child, q=1, ro=1, ws=1)

			mc.xform(ikZTR, t=coord, ws=1)
			mc.xform(ikZTR, ro=orient, ws=1)



		if index==1:
			ikB.append(joint)

		mc.makeIdentity(joint, a=1)

	#fk Joints____________________________________________________________________
	fkA=[]
	fkB=[]
	fkC=[]
	for x in sel:
		index=sel.index(x)

		coord=mc.xform(x, q=1, t=1, ws=1)
		orient=mc.xform(x, q=1, ro=1, ws=1)
		if index == 0:
			legGrp=mc.createNode('transform', n=x.replace('JNT','fkJNT_GRP'))
			mc.parent(legGrp, drvGrp)
			mc.select(cl=1)

		joint=mc.joint(n=x.replace('JNT', 'fkJNT'))
		mc.xform(joint, t=coord, ws=1)
		mc.xform(joint, ro=orient, ws=1)
		if index == 0:			
			mc.parent(joint, legGrp)
			fkA.append(joint)
		if index ==2:
			fkC.append(joint)
		if index==1:
			fkB.append(joint)

		mc.makeIdentity(joint, a=1)

	shoulderJoint=mc.ls(mc.listRelatives(sel[0], p=1))
	allFK=shoulderJoint+fkA+fkB+fkC	

	for x in allFK:
		index=allFK.index(x)
		child=mc.listRelatives(x, c=1)
		child2=mc.listRelatives(sel[2], c=1)
		child3=mc.listRelatives(child2, c=1)				
		fkCTRL=mel.eval('curve -d 1 -p -3 3 3 -p 3 3 3 -p 3 -3 3 -p -3 -3 3 -p -3 3 3 -p -3 3 -3 -p 3 3 -3 -p 3 3 3 -p 3 -3 3 -p 3 -3 -3 -p -3 -3 -3 -p -3 -3 3 -p -3 -3 -3 -p -3 3 -3 -p 3 3 -3 -p 3 -3 -3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')
		if index ==0:
			fkCTRL=mc.rename(fkCTRL, x.replace('JNT','fkCTRL'))
			fkZTR=mc.createNode('transform', n=x.replace('JNT','ZTR'))
			fkCONS=mc.createNode('transform', n=x.replace('JNT','CONS'))

		else:
			if x.endswith('endfkJNT')==True:
				fkCTRL=mc.rename(fkCTRL, child2[0].replace('JNT','fkCTRL'))
				fkZTR=mc.createNode('transform', n=child2[0].replace('JNT','fkZTR'))
				fkCONS=mc.createNode('transform', n=child2[0].replace('JNT','fkCONS'))

			else:
				fkCTRL=mc.rename(fkCTRL, x.replace('JNT','CTRL'))
				fkZTR=mc.createNode('transform', n=x.replace('JNT','ZTR'))
				fkCONS=mc.createNode('transform', n=x.replace('JNT','CONS'))

		
		mc.parent(fkCTRL, fkCONS)
		mc.parent(fkCONS, fkZTR)

		if child !=None:
			mc.delete(mc.parentConstraint(x, fkZTR, mo=0))
		else:
			mc.delete(mc.parentConstraint(child2, fkZTR, mo=0))

		mc.select(fkCTRL+'.cv[3:5]')
		mc.select(fkCTRL+'.cv[10:13]', add=1)
		mc.select(fkCTRL+'.cv[0]', add=1)
		clu1=mc.cluster()

		mc.select(fkCTRL+'.cv[1:2]')
		mc.select(fkCTRL+'.cv[6:9]', add=1)
		mc.select(fkCTRL+'.cv[14:15]', add=1)
		clu2=mc.cluster()

		mc.pointConstraint(x, clu1)
		if child != None:
			mc.pointConstraint(child, clu2)
		else:
			for i in child3:
				if i.endswith('endJNT')==True:
					mc.pointConstraint(i, clu2)
		mc.delete(fkCTRL, ch=1)
		mc.delete(clu1[1], clu2[1])
		
		mc.parentConstraint(fkCTRL, x, mo=1)
		if index==3:
			mc.connectAttr(fkCTRL+'.s', fkC[0]+'.s')
		
		if index==0:
			mc.parent(fkZTR, 'C_main_01_CTRL')
		elif index ==1:
			mc.parent(fkZTR, 'C_main_01_CTRL')
		else:			
			fkTempParent=mc.listRelatives(x, p=1)[0]				
			ctrlTempPar=fkTempParent.replace('JNT','CTRL')
			CONSTemp= fkA[0].replace('fkJNT', 'fkCONS')

			mc.parent(fkZTR, CONSTemp)
			mc.parentConstraint(ctrlTempPar, fkCONS, mo=1)


				
		

	
	#Constraints and switch kinematics_______________________________________
	switchCtrl=mel.eval("curve -d 1 -p -0.5 0 -1.5 -p -1 0 -1.5 -p 0 0 -2.5 -p 1 0 -1.5 -p 0.5 0 -1.5 -p 0.5 0 -0.5 -p 1.5 0 -0.5 -p 1.5 0 -1 -p 2.5 0 0 -p 1.5 0 1 -p 1.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 1.5 -p 1 0 1.5 -p 0 0 2.5 -p -1 0 1.5 -p -0.5 0 1.5 -p -0.5 0 0.5 -p -1.5 0 0.5 -p -1.5 0 1 -p -2.5 0 0 -p -1.5 0 -1 -p -1.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 -1.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;")
	switchCtrl=mc.rename(switchCtrl, ikC[0].replace('ikJNT', 'switchCTRL'))
	switchGrp=mc.createNode('transform', n=ikC[0].replace('ikJNT', 'switchGRP'))
	mc.parent(switchCtrl, switchGrp)
	pos1=mc.xform(ikC[0], q=1, t=1, ws=1)
	orient1=mc.xform(ikC[0], q=1, ro=1, ws=1)

	pos2=mc.xform(ikB[0], q=1, t=1, ws=1)
	orient2=mc.xform(ikB[0], q=1, ro=1, ws=1)

	locSwitch=mc.spaceLocator(n='switchLoc')
	locSwitchGrp=mc.createNode('transform', n='switchLocGrp')
	mc.parent(locSwitch,locSwitchGrp)

	mc.xform(locSwitchGrp, t=pos1, ws=1)
	mc.xform(locSwitchGrp, ro=orient1, ws=1)

	mc.xform(switchGrp, t=pos2, ws=1)
	mc.xform(switchGrp, ro=orient2, ws=1)

	mc.parentConstraint(locSwitch, switchGrp, mo=1)
	mc.xform(locSwitch, ro=(0,0,90), os=1)
	mc.delete(switchGrp+'_parentConstraint1')
	mc.delete(locSwitchGrp)
	mc.xform(switchCtrl, ro=(0,0,-90), os=1)	
	mc.makeIdentity(switchCtrl, a=1)

	mc.addAttr(switchCtrl, ln='IK_FK', at='float', min=0, max=1, k=1)
	mc.addAttr(switchCtrl, ln='ikSpace', at='enum', en='world:hip:chest:shoulders:head', k=1)
	mc.addAttr(switchCtrl, ln='fkSpace', at='enum', en='shoulders:chest:hip:world', k=1)

	rev=mc.createNode('reverse', n=switchCtrl.replace('switchCTRL', 'reverse'))
	mc.connectAttr(switchCtrl+'.IK_FK', rev+'.inputX')

	blend=mc.createNode('blendColors', n=switchCtrl.replace('switchCTRL', 'BC'))
	mc.connectAttr(switchCtrl+'.IK_FK', blend+'.blender')

	blend2=mc.createNode('blendColors', n=switchCtrl.replace('switchCTRL', 'BC'))
	mc.connectAttr(switchCtrl+'.IK_FK', blend2+'.blender')

	mc.connectAttr(fkA[0]+'.scaleX', blend+'.color1R')
	mc.connectAttr(ikA[0]+'.scaleX', blend+'.color2R')

	mc.connectAttr(fkB[0]+'.scaleX', blend2+'.color1R')
	mc.connectAttr(ikB[0]+'.scaleX', blend2+'.color2R')

	mc.connectAttr(blend+'.outputR', sel[0]+'.scaleX')	
	mc.connectAttr(blend2+'.outputR', sel[1]+'.scaleX')
	mc.parent(switchGrp, 'C_main_01_CTRL')
	mc.parentConstraint(sel[2], switchGrp, mo=1)

	blendScale=mc.createNode('blendColors', n=switchCtrl.replace('switchCTRL', 'scaleBC'))
	mc.connectAttr(switchCtrl+'.IK_FK', blendScale+'.blender')

	mc.connectAttr(fkC[0]+'.scale', blendScale+'.color1')
	mc.connectAttr(ikC[0]+'.scale', blendScale+'.color2')
	mc.connectAttr(blendScale+'.output', sel[2]+'.scale')

	mani=mc.listRelatives(sel[2], c=1)
	mc.disconnectAttr(sel[2]+'.scale',mani[0]+'.inverseScale')


	for sj in sel:
		ikj=sj.replace('JNT','ikJNT')
		fkj=sj.replace('JNT','fkJNT')
		oriCons=mc.orientConstraint(ikj, fkj, sj, mo=1)
		#pointCons=mc.pointConstraint(ikj, fkj, sj, mo=1)
		mc.setAttr(oriCons[0]+'.interpType', 2)

		mc.connectAttr(switchCtrl+'.IK_FK', oriCons[0]+'.'+fkj+'W1')
		mc.connectAttr(rev+'.outputX', oriCons[0]+'.'+ikj+'W0')

		#mc.connectAttr(switchCtrl+'.IK_FK', pointCons[0]+'.'+fkj+'W1')
		#mc.connectAttr(rev+'.outputX', pointCons[0]+'.'+ikj+'W0')

	#ikHandle________________________________________________________________

	handle = mc.ikHandle(sj=ikA[0], ee=ikC[0], sol='ikRPsolver', n=ikA[0].replace('ikJNT','ikHandle'))[0]
	handleGrp=mc.createNode('transform', n= handle.replace('Handle', 'HandleGrp'))
	handleCoord=mc.xform(handle, q=1, t=1, ws=1)
	mc.xform(handleGrp, t=handleCoord, ws=1)
	mc.parent(handle, handleGrp)
	mc.parent(handleGrp, 'dft_GRP')
	
	poleLoc = mc.spaceLocator(n=ikA[0].replace('ikJNT','ikPoleLoc'))[0]
	poleGrp = mc.createNode('transform', n=ikA[0].replace('ikJNT','ikPoleLocGrp'))
	mc.connectAttr(handle+'.poleVector', poleLoc+'.translate')
	mc.disconnectAttr(handle+'.poleVector', poleLoc+'.translate')
	mc.parent(poleLoc, poleGrp)
	ikAPos=mc.xform(ikA, q=1,t=1,ws=1)
	mc.xform(poleGrp, t=ikAPos, ws=1)

	mc.delete(mc.aimConstraint(ikA, ikC, poleLoc, aim=(0,0,-1), u=(0,1,0), wut='object', wuo=handle))

	rotPoleLoc=mc.spaceLocator(n=ikA[0].replace('ikJNT','ikRotPoleLoc'))[0]
	rotPoleLocGrp=mc.createNode('transform', n=ikA[0].replace('ikJNT','ikRotPoleLocGrp'))
	mc.parent(rotPoleLoc, rotPoleLocGrp)
	mc.delete(mc.pointConstraint(ikA, ikC, rotPoleLocGrp, mo=0))
	mc.delete(mc.orientConstraint(poleLoc, rotPoleLocGrp, mo=0))
	mc.parent(poleGrp, rotPoleLoc)
	mc.xform(rotPoleLoc, ro=(-90,0,0), os=1, r=1)

	poleLocPos=mc.xform(poleLoc, q=1,t=1,ws=1)
	poleControl=mel.eval('curve -d 1 -p 0 1 0 -p 0 0.707107 0.707107 -p 0 0 1 -p 0 -0.707107 0.707107 -p 0 -1 0 -p 0 -0.707107 -0.707107 -p 0 0 -1 -p 0 0.707107 -0.707107 -p 0 1 0 -p -0.707107 0.707107 0 -p -1 0 0 -p -0.707107 -0.707107 0 -p 0 -1 0 -p 0.707107 -0.707107 0 -p 1 0 0 -p 0.707107 0.707107 0 -p 0 1 0 -p 0 0.707107 -0.707107 -p 0 0 -1 -p 0.707107 0 -0.707107 -p 1 0 0 -p 0.707107 0 0.707107 -p 0 0 1 -p -0.707107 0 0.707107 -p -1 0 0 -p -0.707107 0 -0.707107 -p 0 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 ;')
	poleControl=mc.rename(poleControl, ikA[0].replace('ikJNT','PoleVector_ikCTRL'))			
	mc.xform(poleControl, t=poleLocPos, ws=1  )
	mc.poleVectorConstraint(poleControl, handle)
	mc.delete(rotPoleLocGrp)
	localGrp(poleControl)
	papi=mc.listRelatives(poleControl, p=1)
	mc.parent(papi, 'C_main_01_CTRL')

	#Squash/Stretch___________________________________________________________
	aCoord=mc.xform(ikA, q=1, t=1, ws=1)
	bCoord=mc.xform(ikC, q=1, t=1, ws=1)


	mc.distanceDimension(sp=aCoord ,ep=bCoord)

	loc1=mc.rename('locator1', ikA[0].replace('ikJNT', 'distLoc'))
	loc2=mc.rename('locator2', ikC[0].replace('endikJNT', 'distLoc'))
	dist=mc.rename('distanceDimension1', ikC[0].replace('endikJNT', 'distDimension'))
		
	distGrp=mc.createNode('transform', n=ikA[0].replace('ikJNT', 'distGRP'))
	
	_obj=[loc1, loc2, dist]
	localGrp(_obj)
	mc.select(_obj)
	mel.eval('pickWalk -d up;')
	groups=mc.ls(sl=1)
	mc.parent(groups, distGrp)
	mc.parent(distGrp, 'dft_GRP')

	mdFixStretch=mc.createNode('multiplyDivide', n=ikA[0].replace('ikJNT', 'StretchFix_MD'))
	mdStretch=mc.createNode('multiplyDivide', n=ikA[0].replace('ikJNT', 'Stretch_MD'))
	condStretch=mc.createNode('condition', n=ikA[0].replace('ikJNT', 'Stretch_COND'))

	mc.connectAttr(dist+'Shape.distance', mdFixStretch+'.input1X')
	mc.connectAttr('C_root_01_CTRL.scaleX', mdFixStretch+'.input2X')
	mc.setAttr(mdFixStretch+'.operation', 2)

	mc.connectAttr(mdFixStretch+'.outputX', mdStretch +'.input1X')
	distNum=mc.getAttr(mdStretch+'.input1X')
	mc.setAttr(mdStretch+'.input2X', distNum)
	mc.setAttr(mdStretch+'.operation', 2)	

	mc.connectAttr(mdStretch+'.outputX', condStretch+'.firstTerm')
	mc.connectAttr(mdStretch+'.outputX', condStretch+'.colorIfTrueR')
	mc.setAttr(condStretch+'.secondTerm', 1)
	mc.setAttr(condStretch+'.colorIfFalse', 1,1,1)
	mc.setAttr(condStretch+'.operation', 3)

	mc.connectAttr(condStretch+'.outColorR', ikA[0]+'.scaleX')
	mc.connectAttr(condStretch+'.outColorR', ikB[0]+'.scaleX')

	#Binding ikControls to Joints___________________________________________________________
	mc.select(loc2)
	mc.pickWalk(d='up')
	newGrp=mc.ls(sl=1)
	
	mc.parentConstraint(ikCTRL, newGrp, mo=1)
	mc.parentConstraint(ikCTRL, handleGrp, mo=1)
	mc.orientConstraint(ikCTRL, ikC[0], mo=1)

	mc.select(loc1)
	mc.pickWalk(d='up')
	newGrp=mc.ls(sl=1)

	tempClav=mc.listRelatives(sel[0], p=1)
	tempClav=tempClav[0].replace('JNT', 'fkCTRL')

	mc.parentConstraint(tempClav, newGrp, mo=1)
	mc.parentConstraint(tempClav, ikA[0], mo=1)



def spineXUp():

	#ikSpline####################################################################################################
	select=mc.ls(sl=1)	
	print select

	curveCoords=[]			
	for x in select:
		jointCoord=mc.xform(x, q=1, t=1, ws=1)
		curveCoords.append(jointCoord)
		print x
		print jointCoord

	print curveCoords
	curve=mc.curve( ep=curveCoords, d=3)
	curve=mc.rename(curve, sel[0].replace('_JNT','_ikCurve' ))
	

	#ik lower and upper Joints###########################################################
	hipJnt =mc.listRelatives(sel[0], p=1)
	mc.select(cl=1)
	upperName =sel[-1].replace('_JNT','_ikSplineDrvJNT')
	lowerName =sel[0].replace('_JNT','_ikSplineDrvJNT')


	upperIkJoint=mc.joint(n=upperName)

	mc.select(cl=1)
	lowerIkJoint=mc.joint(n=lowerName)	
	mc.select(cl=1)

	midIkJoint=mc.joint(n=sel[1].replace('_JNT', '_ikSplineDrvJNT'))

	ikSplineJoints=mc.ls('*ikSplineDrvJNT')

	for x in ikSplineJoints:
		mc.select(cl=1)
		motionNode=mc.pathAnimation( x, n='C_motionNode_Temp' ,c=curve, fa='x' ,wu=(0,0,1), fm=1, bank=True )
		mc.cutKey(motionNode, at='uValue', time = (0, 1000), clear = True)
		if x == upperName:
			mc.setAttr(motionNode+'.uValue', 1)
		if x == lowerName:
			mc.setAttr(motionNode+'.uValue', 0)
		if x == midIkJoint:
			mc.setAttr(motionNode+'.uValue', 0.5)
		mc.delete(x, mp=1)

		mc.parent(x, 'driverJoints_GRP')
		ori=mc.xform(sel[0], q=1,ro=1, ws=1)
		mc.xform(x,ro=ori, ws=1)
		mc.makeIdentity(x, a=1)


	ikSplineJoints=mc.ls('*_ikSplineDrvJNT')
	

	hipZTR=mc.createNode('transform', n='C_hip_01_ZTR')
	hipCTRL=mel.eval('curve -d 1 -p 0 10 10 -p 0 -10 10 -p 0 -10 -10 -p 0 10 -10 -p 0 10 10 -k 0 -k 1 -k 2 -k 3 -k 4 ;' )
	hipCTRL=mc.rename(hipCTRL, hipZTR.replace('_ZTR', '_CTRL'))
	mc.parent(hipCTRL, hipZTR)
	mc.delete(mc.parentConstraint(sel[0], hipZTR, mo=0))


	mc.skinCluster(ikSplineJoints, curve, n=curve.replace('_ikCurve', '_skinCluster'), dr=4.0)	
	mc.parent(curve, 'dft_GRP')	

	upperGRP=mc.createNode('transform', n=upperName.replace('_ikSplineDrvJNT','_ikSplineDrvZTR'))
	upperControl=mc.circle(n=upperName.replace('_ikSplineDrvJNT','_ikSplineDrvCTRL'), r=16, nr=(1,0,0))
	mc.parent(upperControl, upperGRP)
	mc.delete(mc.parentConstraint(upperIkJoint, upperGRP, mo=0))
	mc.parentConstraint(upperControl, upperIkJoint, mo=0)
	mc.orientConstraint(upperControl, sel[-1])

	lowerGRP=mc.createNode('transform', n=lowerName.replace('_ikSplineDrvJNT','_ikSplineDrvZTR'))
	lowerControl=mc.circle(n=lowerName.replace('_ikSplineDrvJNT','_ikSplineDrvCTRL'), r=16, nr=(1,0,0))
	mc.parent(lowerControl, lowerGRP)
	mc.delete(mc.parentConstraint(lowerIkJoint, lowerGRP, mo=0))
	mc.parentConstraint(lowerControl, lowerIkJoint, mo=0)
	mc.parentConstraint(lowerControl, hipJnt, mo=0)


	midGRP=mc.createNode('transform', n=midIkJoint.replace('_ikSplineDrvJNT','_ikSplineDrvZTR'))
	midControl=mc.circle(n=midIkJoint.replace('_ikSplineDrvJNT','_ikSplineDrvCTRL'), r=16, nr=(1,0,0))
	mc.parent(midControl, midGRP)
	mc.delete(mc.parentConstraint(midIkJoint, midGRP, mo=0))
	mc.parentConstraint(midControl, midIkJoint, mo=0)

	mc.parent(upperGRP, hipCTRL)
	mc.parent(lowerGRP, hipCTRL)
	mc.parent(midGRP, hipCTRL)

	fkSpineControl1=mel.eval('curve -d 1 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 1.431811 -15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p -5.991438 -1.431811 15.7761 -p -5.991438 1.431811 15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p 5.991438 -1.431811 -15.7761 -p 5.991438 1.431811 -15.7761 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;')
	fkSpineControl1=mc.rename(fkSpineControl1, lowerControl[0].replace('_ikSplineDrvCTRL','_fkSplineCTRL') )
	fkSpineZTR1=mc.createNode('transform', n=fkSpineControl1.replace('_fkSplineCTRL','_fkSplineZTR'))
	mc.delete(mc.orientConstraint(lowerControl[0], fkSpineZTR1, mo=0))
	mc.parent(fkSpineControl1, fkSpineZTR1)
	mc.makeIdentity(fkSpineControl1, a=1)
	mc.delete(mc.pointConstraint(midControl, lowerControl, fkSpineZTR1, mo=0))
	mc.parent(fkSpineZTR1, hipCTRL)

	fkSpineControl2=mel.eval('curve -d 1 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 1.431811 -15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p -5.991438 -1.431811 15.7761 -p -5.991438 1.431811 15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p 5.991438 -1.431811 -15.7761 -p 5.991438 1.431811 -15.7761 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;')
	fkSpineControl2=mc.rename(fkSpineControl2, midControl[0].replace('_ikSplineDrvCTRL','_fkSplineCTRL') )
	fkSpineZTR2=mc.createNode('transform', n=fkSpineControl2.replace('_fkSplineCTRL','_fkSplineZTR'))
	mc.delete(mc.orientConstraint(lowerControl[0], fkSpineZTR2, mo=0))
	mc.parent(fkSpineControl2, fkSpineZTR2)
	mc.makeIdentity(fkSpineControl2, a=1)
	mc.delete(mc.pointConstraint(upperControl, midControl, fkSpineZTR2, mo=0))
	mc.parent(fkSpineZTR2, fkSpineControl1)

	mc.parentConstraint(fkSpineControl1, midGRP, mo=1)
	mc.parentConstraint(fkSpineControl2, upperGRP, mo=1)
	mc.parent(hipZTR,'C_main_01_CTRL')

	splineIK = mc.ikHandle(sj=sel[0], ee=sel[-1], sol='ikSplineSolver', c=curve,scv=0, fj=1,pcv=0, n=curve.replace('_ikCurve','_ikSplineHandle'))[0]	
	mc.parent(splineIK, 'dft_GRP')

	mc.setAttr(splineIK+'.dTwistControlEnable',1)
	mc.setAttr(splineIK+'.dWorldUpType',4)
	mc.setAttr(splineIK+'.dWorldUpVectorY',1)
	mc.setAttr(splineIK+'.dWorldUpVectorX',0)
	mc.connectAttr(lowerControl[0]+'.worldMatrix[0]', splineIK+'.dWorldUpMatrix')
	mc.connectAttr(upperControl[0]+'.worldMatrix[0]', splineIK+'.dWorldUpMatrixEnd')

	#Squash/Stretch___________________________________________________________________
	
	ci=mc.createNode('curveInfo', n=curve.replace('_ikCurve', '_CI'))

	mc.connectAttr(curve+'Shape.worldSpace[0]', ci+'.inputCurve')

	mdFix=mc.createNode('multiplyDivide', n=curve.replace('_ikCurve', '_scaleFixMD'))
	mc.connectAttr('C_root_01_CTRL.scaleX', mdFix+'.input2X')
	mc.connectAttr(ci+'.arcLength', mdFix+'.input1X')
	mc.setAttr(mdFix+'.operation', 2)

	mdStretch=mc.createNode('multiplyDivide', n=curve.replace('_ikCurve', '_stretchMD'))
	mc.connectAttr(mdFix+'.outputX', mdStretch+'.input1X')
	mc.setAttr(mdStretch+'.operation', 2)
	attr=mc.getAttr(mdStretch+'.input1X')
	mc.setAttr(mdStretch+'.input2X', attr)

	cond=mc.createNode('condition', n=curve.replace('_ikCurve', '_stretchCOND'))
	mc.setAttr(cond+'.operation', 2)
	mc.setAttr(cond+'.secondTerm', 1)
	mc.connectAttr(mdStretch+'.outputX', cond+'.firstTerm')
	mc.connectAttr(mdStretch+'.outputX', cond+'.colorIfTrueR')

	mdSquash=mc.createNode('multiplyDivide', n=curve.replace('_ikCurve', '_squashMD'))
	mc.setAttr(mdSquash+'.operation', 3)	
	mc.connectAttr(mdStretch+'.outputX', mdSquash+'.input1X')
	mc.setAttr(mdSquash+'.input2X', -1)

	squashCond=mc.createNode('condition', n=curve.replace('_ikCurve', '_squashCOND'))
	mc.setAttr(squashCond+'.operation', 4)
	mc.setAttr(squashCond+'.secondTerm', 1)
	mc.connectAttr(mdSquash+'.outputX', squashCond+'.firstTerm')
	mc.connectAttr(mdSquash+'.outputX', squashCond+'.colorIfTrueR')

	for x in sel:
		if x != sel[-1]:
			mc.connectAttr(cond+'.outColorR', x+'.scaleX')
			mc.connectAttr(squashCond+'.outColorR', x+'.scaleY')
			mc.connectAttr(squashCond+'.outColorR', x+'.scaleZ')
	
	
def spineYUP():

	#ikSpline####################################################################################################
	select=mc.ls(sl=1)	
	print select

	curveCoords=[]			
	for x in select:
		jointCoord=mc.xform(x, q=1, t=1, ws=1)
		curveCoords.append(jointCoord)
		print x
		print jointCoord

	print curveCoords
	curve=mc.curve( ep=curveCoords, d=3)
	curve=mc.rename(curve, sel[0].replace('_JNT','_ikCurve' ))
	

	#ik lower and upper Joints###########################################################
	hipJnt =mc.listRelatives(sel[0], p=1)
	mc.select(cl=1)
	upperName =sel[-1].replace('_JNT','_ikSplineDrvJNT')
	lowerName =sel[0].replace('_JNT','_ikSplineDrvJNT')


	upperIkJoint=mc.joint(n=upperName)

	mc.select(cl=1)
	lowerIkJoint=mc.joint(n=lowerName)	
	mc.select(cl=1)

	midIkJoint=mc.joint(n=sel[1].replace('_JNT', '_ikSplineDrvJNT'))

	ikSplineJoints=mc.ls('*ikSplineDrvJNT')

	for x in ikSplineJoints:
		mc.select(cl=1)
		motionNode=mc.pathAnimation( x, n='C_motionNode_Temp' ,c=curve, fa='x' ,wu=(0,0,1), fm=1, bank=True )
		mc.cutKey(motionNode, at='uValue', time = (0, 1000), clear = True)
		if x == upperName:
			mc.setAttr(motionNode+'.uValue', 1)
		if x == lowerName:
			mc.setAttr(motionNode+'.uValue', 0)
		if x == midIkJoint:
			mc.setAttr(motionNode+'.uValue', 0.5)
		mc.delete(x, mp=1)

		mc.parent(x, 'driverJoints_GRP')
		ori=mc.xform(sel[0], q=1,ro=1, ws=1)
		#mc.xform(x,ro=ori, ws=1)
		mc.makeIdentity(x, a=1)


	ikSplineJoints=mc.ls('*_ikSplineDrvJNT')
	

	hipZTR=mc.createNode('transform', n='C_hip_01_ZTR')
	hipCTRL=mel.eval('curve -d 1 -p 0 10 10 -p 0 -10 10 -p 0 -10 -10 -p 0 10 -10 -p 0 10 10 -k 0 -k 1 -k 2 -k 3 -k 4 ;' )
	mc.xform(hipCTRL, ro=(0,0,90))
	mc.makeIdentity(hipCTRL, a=1)
	hipCTRL=mc.rename(hipCTRL, hipZTR.replace('_ZTR', '_CTRL'))
	mc.parent(hipCTRL, hipZTR)
	#mc.delete(mc.parentConstraint(sel[0], hipZTR, mo=0))
	mc.delete(mc.pointConstraint(sel[0], hipZTR, mo=0))


	mc.skinCluster(ikSplineJoints, curve, n=curve.replace('_ikCurve', '_skinCluster'), dr=4.0)	
	mc.parent(curve, 'dft_GRP')	

	upperGRP=mc.createNode('transform', n=upperName.replace('_ikSplineDrvJNT','_ikSplineDrvZTR'))
	upperControl=mc.circle(n=upperName.replace('_ikSplineDrvJNT','_ikSplineDrvCTRL'), r=16, nr=(0,1,0))
	mc.parent(upperControl, upperGRP)
	mc.delete(mc.pointConstraint(upperIkJoint, upperGRP, mo=0))
	mc.parentConstraint(upperControl, upperIkJoint, mo=1)
	mc.orientConstraint(upperControl, sel[-1], mo=1)

	lowerGRP=mc.createNode('transform', n=lowerName.replace('_ikSplineDrvJNT','_ikSplineDrvZTR'))
	lowerControl=mc.circle(n=lowerName.replace('_ikSplineDrvJNT','_ikSplineDrvCTRL'), r=16, nr=(0,1,0))
	mc.parent(lowerControl, lowerGRP)
	mc.delete(mc.pointConstraint(lowerIkJoint, lowerGRP, mo=0))
	mc.parentConstraint(lowerControl, lowerIkJoint, mo=1)
	mc.parentConstraint(lowerControl, hipJnt, mo=1)


	midGRP=mc.createNode('transform', n=midIkJoint.replace('_ikSplineDrvJNT','_ikSplineDrvZTR'))
	midControl=mc.circle(n=midIkJoint.replace('_ikSplineDrvJNT','_ikSplineDrvCTRL'), r=16, nr=(0,1,0))
	mc.parent(midControl, midGRP)
	mc.delete(mc.pointConstraint(midIkJoint, midGRP, mo=0))
	mc.parentConstraint(midControl, midIkJoint, mo=1)

	mc.parent(upperGRP, hipCTRL)
	mc.parent(lowerGRP, hipCTRL)
	mc.parent(midGRP, hipCTRL)

	fkSpineControl1=mel.eval('curve -d 1 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 1.431811 -15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p -5.991438 -1.431811 15.7761 -p -5.991438 1.431811 15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p 5.991438 -1.431811 -15.7761 -p 5.991438 1.431811 -15.7761 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;')
	fkSpineControl1=mc.rename(fkSpineControl1, lowerControl[0].replace('_ikSplineDrvCTRL','_fkSplineCTRL') )
	fkSpineZTR1=mc.createNode('transform', n=fkSpineControl1.replace('_fkSplineCTRL','_fkSplineZTR'))
	#mc.delete(mc.orientConstraint(lowerControl[0], fkSpineZTR1, mo=0))
	mc.parent(fkSpineControl1, fkSpineZTR1)
	mc.makeIdentity(fkSpineControl1, a=1)
	mc.delete(mc.pointConstraint(midControl, lowerControl, fkSpineZTR1, mo=0))
	mc.parent(fkSpineZTR1, hipCTRL)

	fkSpineControl2=mel.eval('curve -d 1 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 1.431811 -15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p -5.991438 -1.431811 15.7761 -p -5.991438 1.431811 15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p 5.991438 -1.431811 -15.7761 -p 5.991438 1.431811 -15.7761 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;')
	fkSpineControl2=mc.rename(fkSpineControl2, midControl[0].replace('_ikSplineDrvCTRL','_fkSplineCTRL') )
	fkSpineZTR2=mc.createNode('transform', n=fkSpineControl2.replace('_fkSplineCTRL','_fkSplineZTR'))
	#mc.delete(mc.orientConstraint(lowerControl[0], fkSpineZTR2, mo=0))
	mc.parent(fkSpineControl2, fkSpineZTR2)
	mc.makeIdentity(fkSpineControl2, a=1)
	mc.delete(mc.pointConstraint(upperControl, midControl, fkSpineZTR2, mo=0))
	mc.parent(fkSpineZTR2, fkSpineControl1)

	mc.parentConstraint(fkSpineControl1, midGRP, mo=1)
	mc.parentConstraint(fkSpineControl2, upperGRP, mo=1)
	mc.parent(hipZTR,'C_main_01_CTRL')

	splineIK = mc.ikHandle(sj=sel[0], ee=sel[-1], sol='ikSplineSolver', c=curve,scv=0, fj=1,pcv=0, n=curve.replace('_ikCurve','_ikSplineHandle'))[0]	
	mc.parent(splineIK, 'dft_GRP')

	mc.setAttr(splineIK+'.dTwistControlEnable',1)
	mc.setAttr(splineIK+'.dWorldUpType',4)
	mc.setAttr(splineIK+'.dWorldUpVectorY',0)
	mc.setAttr(splineIK+'.dWorldUpVectorX',0)
	mc.setAttr(splineIK+'.dWorldUpVectorZ',1)
	mc.setAttr(splineIK+'.dWorldUpVectorEndX',0)
	mc.setAttr(splineIK+'.dWorldUpVectorEndY',0)
	mc.setAttr(splineIK+'.dWorldUpVectorEndZ',1)
	mc.connectAttr(lowerControl[0]+'.worldMatrix[0]', splineIK+'.dWorldUpMatrix')
	mc.connectAttr(upperControl[0]+'.worldMatrix[0]', splineIK+'.dWorldUpMatrixEnd')

	#Squash/Stretch___________________________________________________________________
	
	ci=mc.createNode('curveInfo', n=curve.replace('_ikCurve', '_CI'))

	mc.connectAttr(curve+'Shape.worldSpace[0]', ci+'.inputCurve')

	mdFix=mc.createNode('multiplyDivide', n=curve.replace('_ikCurve', '_scaleFixMD'))
	mc.connectAttr('C_root_01_CTRL.scaleX', mdFix+'.input2X')
	mc.connectAttr(ci+'.arcLength', mdFix+'.input1X')
	mc.setAttr(mdFix+'.operation', 2)

	mdStretch=mc.createNode('multiplyDivide', n=curve.replace('_ikCurve', '_stretchMD'))
	mc.connectAttr(mdFix+'.outputX', mdStretch+'.input1X')
	mc.setAttr(mdStretch+'.operation', 2)
	attr=mc.getAttr(mdStretch+'.input1X')
	mc.setAttr(mdStretch+'.input2X', attr)

	cond=mc.createNode('condition', n=curve.replace('_ikCurve', '_stretchCOND'))
	mc.setAttr(cond+'.operation', 2)
	mc.setAttr(cond+'.secondTerm', 1)
	mc.connectAttr(mdStretch+'.outputX', cond+'.firstTerm')
	mc.connectAttr(mdStretch+'.outputX', cond+'.colorIfTrueR')

	mdSquash=mc.createNode('multiplyDivide', n=curve.replace('_ikCurve', '_squashMD'))
	mc.setAttr(mdSquash+'.operation', 3)	
	mc.connectAttr(mdStretch+'.outputX', mdSquash+'.input1X')
	mc.setAttr(mdSquash+'.input2X', -1)

	squashCond=mc.createNode('condition', n=curve.replace('_ikCurve', '_squashCOND'))
	mc.setAttr(squashCond+'.operation', 4)
	mc.setAttr(squashCond+'.secondTerm', 1)
	mc.connectAttr(mdSquash+'.outputX', squashCond+'.firstTerm')
	mc.connectAttr(mdSquash+'.outputX', squashCond+'.colorIfTrueR')

	for x in sel:
		if x != sel[-1]:
			mc.connectAttr(cond+'.outColorR', x+'.scaleX')
			mc.connectAttr(squashCond+'.outColorR', x+'.scaleY')
			mc.connectAttr(squashCond+'.outColorR', x+'.scaleZ')
	


def leg():

	#ik Joints_______________________________________________________________
	ikA=[]
	ikB=[]
	ikC=[]
	for x in sel:
		index=sel.index(x)

		coord=mc.xform(x, q=1, t=1, ws=1)
		orient=mc.xform(x, q=1, ro=1, ws=1)
		if index == 0:
			legGrp=mc.createNode('transform', n=x.replace('JNT','ikJNT_GRP'))
			mc.parent(legGrp, drvGrp)
			mc.select(cl=1)

		joint=mc.joint(n=x.replace('JNT', 'ikJNT'))
		mc.xform(joint, t=coord, ws=1)
		mc.xform(joint, ro=orient, ws=1)		
		
		if index == 0:
			mc.parent(joint, legGrp)
			ikA.append(joint)
		if index ==2:
			ikC.append(joint)
		if index==1:
			ikB.append(joint)

		mc.makeIdentity(joint, a=1)


	footJoint=mc.listRelatives(ikC[0], c=1)[0]
	footPos=mc.xform(footJoint, q=1, t=1, ws=1)

	ikCTRL=mel.eval('curve -d 1 -p -6 0 13 -p 6 0 13 -p 6 0 -15 -p -6 0 -15 -p -6 0 13 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
	ikCTRL=mc.rename(footJoint.replace('JNT', 'CTRL'))
	ikZTR=mc.createNode('transform', n=footJoint.replace('JNT','ZTR'))
	ikCONS=mc.createNode('transform', n=footJoint.replace('JNT','CONS'))
	mc.parent(ikCTRL, ikCONS)
	mc.parent(ikCONS, ikZTR)
	mc.parent(ikZTR, 'C_main_01_CTRL')

	mc.xform(ikZTR, t=footPos, ws=1)
	mc.select(ikCTRL +'.cv[*]')
	mc.move(0,y=1)

	mc.addAttr(ikCTRL, ln='footRoll', at='float', dv=0,  k=1)
	mc.addAttr(ikCTRL, ln='rollAngle', at='float', dv=20,  k=1)
	mc.addAttr(ikCTRL, ln='footBank', at='float', dv=0,  k=1)

	############################
	#Create ikFoot Nodes_________________________________________________________________________
	############################

	#BankNodes
	bankIn=mc.createNode('condition',n= footJoint.replace('JNT', 'bankInCOND'))
	bankExt=mc.createNode('condition',n= footJoint.replace('JNT', 'bankExtCOND'))

	mc.connectAttr(ikCTRL+'.footBank',bankIn+'.colorIfTrueR' )
	mc.connectAttr(ikCTRL+'.footBank',bankIn+'.firstTerm' )
	if ikA[0].startswith('R_')==True:
		mc.setAttr(bankIn+'.operation', 5)
	else:
		mc.setAttr(bankIn+'.operation', 3)

	mc.setAttr(bankIn+'.colorIfFalseR', 0)
	mc.setAttr(bankIn+'.colorIfFalseG', 0)
	mc.setAttr(bankIn+'.colorIfFalseB', 0)

	mc.connectAttr(ikCTRL+'.footBank',bankExt+'.colorIfTrueR' )
	mc.connectAttr(ikCTRL+'.footBank',bankExt+'.firstTerm' )
	if ikA[0].startswith('R_')==True:
		mc.setAttr(bankExt+'.operation', 3)
	else:
		mc.setAttr(bankExt+'.operation', 5)

	mc.setAttr(bankExt+'.colorIfFalseR', 0)
	mc.setAttr(bankExt+'.colorIfFalseG', 0)
	mc.setAttr(bankExt+'.colorIfFalseB', 0)

	#footRoll and Angle Nodes__________________________________________________________

	footFixDir=mc.createNode('multiplyDivide',n= footJoint.replace('JNT', 'fixDirectionMD'))
	mc.connectAttr(ikCTRL+'.rollAngle', footFixDir+'.input1X')
	mc.setAttr(footFixDir+'.input2X', -1)

	footPMA=mc.createNode('plusMinusAverage',n= footJoint.replace('JNT', 'PMA'))
	mc.connectAttr(ikCTRL+'.footRoll', footPMA+'.input2D[0].input2Dx')
	mc.connectAttr(footFixDir+'.outputX', footPMA+'.input2D[1].input2Dx')

	footA=mc.createNode('condition',n= footJoint.replace('JNT', 'ACOND'))
	mc.connectAttr(ikCTRL+'.footRoll',footA+'.colorIfTrueR' )
	mc.connectAttr(ikCTRL+'.footRoll',footA+'.firstTerm' )
	mc.connectAttr(ikCTRL+'.rollAngle',footA+'.secondTerm' )
	mc.connectAttr(ikCTRL+'.rollAngle',footA+'.colorIfFalseR' )
	mc.setAttr(footA+'.operation', 5)

	footB=mc.createNode('condition',n= footJoint.replace('JNT', 'BCOND'))
	mc.connectAttr(footPMA+'.output2Dx',footB+'.colorIfTrueR' )
	mc.connectAttr(ikCTRL+'.footRoll',footB+'.firstTerm' )
	mc.connectAttr(ikCTRL+'.rollAngle',footB+'.secondTerm' )
	mc.setAttr(footB+'.colorIfFalseR', 0 )
	mc.setAttr(footB+'.operation', 3)

	footC=mc.createNode('condition',n= footJoint.replace('JNT', 'CCOND'))	
	mc.connectAttr(ikCTRL+'.footRoll',footC+'.firstTerm')	
	mc.connectAttr(ikCTRL+'.footRoll', footC+'.colorIfFalseR' )
	mc.setAttr(footC+'.operation', 3)

	outputMD=mc.createNode('multiplyDivide',n= footJoint.replace('JNT', 'outputMD'))
	mc.connectAttr(footA+'.outColorR', outputMD+'.input1X')
	mc.connectAttr(footB+'.outColorR', outputMD+'.input1Y')
	mc.connectAttr(footC+'.outColorR', outputMD+'.input1Z')	

	footAOutput=mc.createNode('condition',n= footJoint.replace('JNT', 'AOutputCOND'))
	mc.connectAttr(outputMD+'.outputX',footAOutput+'.firstTerm' )
	mc.connectAttr(outputMD+'.outputX',footAOutput+'.colorIfFalseR' )
	mc.setAttr(footAOutput+'.operation', 5)
	
	#######################
	#ikFoot Inverse Drivers
	#######################
	if ikA[0].startswith('L_')==True:
		locators=mc.ls('L_footHelpers*LOC')		

	if ikA[0].startswith('R_')==True:
		locators=mc.ls('R_footHelpers*LOC')
	
	tempChild=mc.listRelatives(sel[2], c=1)
	tempLoc=mc.spaceLocator(n='loca1')
	mc.xform(tempLoc, t=footPos, ws=1)
	tempList=mc.ls(tempLoc)
	allPoints=tempChild +locators+tempList
	lastInverse=[]
	mc.select(cl=1)
	for i in allPoints:
		index=allPoints.index(i)
		pos=mc.xform(i, q=1, t=1, ws=1)
		rot=mc.xform(i, q=1, ro=1, ws=1)
		inverseJoint=mc.joint(n=tempChild[0].replace('01_JNT', str(index)+'_ikInverseJoint'))
		
		if index ==0:
			mc.xform(inverseJoint, t=footPos, ws=1)
			mc.parent(inverseJoint, 'driverJoints_GRP')
		elif index==-1:
			mc.xform(inverseJoint, t=footPos, ws=1)
		else:
			mc.xform(inverseJoint, t=pos, ws=1)
			mc.xform(inverseJoint, ro=rot, ws=1)
			mc.makeIdentity(inverseJoint, a=1)

		if index==0:			
				mc.parentConstraint(ikCTRL, inverseJoint, mo=1)
		if index==1:
			mc.connectAttr(bankIn+'.outColorR', inverseJoint+'.rz')
		if index==2:
			mc.connectAttr(bankExt+'.outColorR', inverseJoint+'.rz')
		if index==3:
			mc.connectAttr(outputMD+'.outputZ', inverseJoint+'.rx')
		if index==4:
			mc.connectAttr(outputMD+'.outputY', inverseJoint+'.rx')
			ikJoint=inverseJoint.replace('4_ikInverseJoint','02_ikJNT')
			mc.orientConstraint(inverseJoint, ikJoint, mo=1)
		if index==5:
			mc.connectAttr(footAOutput+'.outColorR', inverseJoint+'.rx')
			ikJoint=inverseJoint.replace('5_ikInverseJoint','01_ikJNT')
			mc.orientConstraint(inverseJoint, ikJoint, mo=1)
		if index==6:
			lastInverse.append(inverseJoint)
			
	

	mc.delete(tempLoc)


		



	#fk Joints____________________________________________________________________
	fkA=[]
	fkB=[]
	fkC=[]
	for x in sel:
		index=sel.index(x)

		coord=mc.xform(x, q=1, t=1, ws=1)
		orient=mc.xform(x, q=1, ro=1, ws=1)
		if index == 0:
			legGrp=mc.createNode('transform', n=x.replace('JNT','fkJNT_GRP'))
			mc.parent(legGrp, drvGrp)
			mc.select(cl=1)

		joint=mc.joint(n=x.replace('JNT', 'fkJNT'))
		mc.xform(joint, t=coord, ws=1)
		mc.xform(joint, ro=orient, ws=1)
		if index == 0:			
			mc.parent(joint, legGrp)
			fkA.append(joint)
		if index ==2:
			fkC.append(joint)
		if index==1:
			fkB.append(joint)

		mc.makeIdentity(joint, a=1)	
		
		if x.endswith('endJNT')	==False:		
			fkCTRL=mel.eval('curve -d 1 -p -3 3 3 -p 3 3 3 -p 3 -3 3 -p -3 -3 3 -p -3 3 3 -p -3 3 -3 -p 3 3 -3 -p 3 3 3 -p 3 -3 3 -p 3 -3 -3 -p -3 -3 -3 -p -3 -3 3 -p -3 -3 -3 -p -3 3 -3 -p 3 3 -3 -p 3 -3 -3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')
			fkCTRL=mc.rename(fkCTRL, x.replace('JNT','fkCTRL'))
			fkZTR=mc.createNode('transform', n=x.replace('JNT','fkZTR'))
			fkCONS=mc.createNode('transform', n=x.replace('JNT','fkCONS'))
			mc.parent(fkCTRL, fkCONS)
			mc.parent(fkCONS, fkZTR)
			mc.delete(mc.parentConstraint(x, fkZTR, mo=0))

			child=mc.listRelatives(x, c=1)

			mc.select(fkCTRL+'.cv[3:5]')
			mc.select(fkCTRL+'.cv[10:13]', add=1)
			mc.select(fkCTRL+'.cv[0]', add=1)
			clu1=mc.cluster()

			mc.select(fkCTRL+'.cv[1:2]')
			mc.select(fkCTRL+'.cv[6:9]', add=1)
			mc.select(fkCTRL+'.cv[14:15]', add=1)
			clu2=mc.cluster()

			mc.pointConstraint(x, clu1)
			mc.pointConstraint(child, clu2)
		
			mc.delete(fkCTRL, ch=1)
			mc.delete(clu1[1], clu2[1])
		
			mc.parentConstraint(fkCTRL, joint, mo=1)
		
		
			if index==0:
				mc.parent(fkZTR, 'C_main_01_CTRL')
			else:
				fkTempParent=mc.listRelatives(x, p=1)[0]
				fkTempExtraParent=mc.listRelatives(fkTempParent, p=1)[0]

				if fkTempParent.endswith('endJNT')==True:
					ctrlTempPar=fkTempExtraParent.replace('JNT','fkCTRL')
					CONSTemp= sel[0].replace('JNT', 'fkCONS')
					mc.parent(fkZTR, CONSTemp)
					mc.parentConstraint(ctrlTempPar, fkCONS, mo=1)

				else:
					ctrlTempPar=fkTempParent.replace('JNT','fkCTRL')
					CONSTemp= sel[0].replace('JNT', 'fkCONS')
					mc.parent(fkZTR, CONSTemp)
					mc.parentConstraint(ctrlTempPar, fkCONS, mo=1)	

		mc.select(joint)
	#Constraints and switch kinematics_______________________________________
	switchCtrl=mel.eval("curve -d 1 -p -0.5 0 -1.5 -p -1 0 -1.5 -p 0 0 -2.5 -p 1 0 -1.5 -p 0.5 0 -1.5 -p 0.5 0 -0.5 -p 1.5 0 -0.5 -p 1.5 0 -1 -p 2.5 0 0 -p 1.5 0 1 -p 1.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 1.5 -p 1 0 1.5 -p 0 0 2.5 -p -1 0 1.5 -p -0.5 0 1.5 -p -0.5 0 0.5 -p -1.5 0 0.5 -p -1.5 0 1 -p -2.5 0 0 -p -1.5 0 -1 -p -1.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 -1.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;")
	switchCtrl=mc.rename(switchCtrl, ikC[0].replace('ikJNT', 'switchCTRL'))
	switchGrp=mc.createNode('transform', n=ikC[0].replace('ikJNT', 'switchGRP'))
	mc.parent(switchCtrl, switchGrp)
	pos1=mc.xform(ikC[0], q=1, t=1, ws=1)
	orient1=mc.xform(ikC[0], q=1, ro=1, ws=1)

	pos2=mc.xform(ikB[0], q=1, t=1, ws=1)
	orient2=mc.xform(ikB[0], q=1, ro=1, ws=1)

	locSwitch=mc.spaceLocator(n='switchLoc')
	locSwitchGrp=mc.createNode('transform', n='switchLocGrp')
	mc.parent(locSwitch,locSwitchGrp)

	mc.xform(locSwitchGrp, t=pos1, ws=1)
	mc.xform(locSwitchGrp, ro=orient1, ws=1)

	mc.xform(switchGrp, t=pos2, ws=1)
	mc.xform(switchGrp, ro=orient2, ws=1)

	mc.parentConstraint(locSwitch, switchGrp, mo=1)
	mc.xform(locSwitch, ro=(0,0,90), os=1)
	mc.delete(switchGrp+'_parentConstraint1')
	mc.delete(locSwitchGrp)
	mc.xform(switchCtrl, ro=(0,0,-90), os=1)	
	mc.makeIdentity(switchCtrl, a=1)

	mc.addAttr(switchCtrl, ln='IK_FK', at='float', min=0, max=1, k=1)
	mc.addAttr(switchCtrl, ln='ikSpace', at='enum', en='world:hip', k=1)
	mc.addAttr(switchCtrl, ln='fkSpace', at='enum', en='hip:world', k=1)

	rev=mc.createNode('reverse', n=switchCtrl.replace('switchCTRL', 'reverse'))
	mc.connectAttr(switchCtrl+'.IK_FK', rev+'.inputX')

	blend=mc.createNode('blendColors', n=switchCtrl.replace('switchCTRL', 'BC'))
	mc.connectAttr(switchCtrl+'.IK_FK', blend+'.blender')

	blend2=mc.createNode('blendColors', n=switchCtrl.replace('switchCTRL', 'BC'))
	mc.connectAttr(switchCtrl+'.IK_FK', blend2+'.blender')

	mc.connectAttr(fkA[0]+'.scaleX', blend+'.color1R')
	mc.connectAttr(ikA[0]+'.scaleX', blend+'.color2R')

	mc.connectAttr(fkB[0]+'.scaleX', blend2+'.color1R')
	mc.connectAttr(ikB[0]+'.scaleX', blend2+'.color2R')

	mc.connectAttr(blend+'.outputR', sel[0]+'.scaleX')	
	mc.connectAttr(blend2+'.outputR', sel[1]+'.scaleX')
	mc.parent(switchGrp, 'C_main_01_CTRL')
	mc.parentConstraint(sel[2], switchGrp, mo=1)

	blendScale=mc.createNode('blendColors', n=switchCtrl.replace('switchCTRL', 'scaleBC'))
	mc.connectAttr(switchCtrl+'.IK_FK', blendScale+'.blender')

	mc.connectAttr(fkC[0]+'.scale', blendScale+'.color1')
	mc.connectAttr(ikC[0]+'.scale', blendScale+'.color2')
	mc.connectAttr(blendScale+'.output', sel[2]+'.scale')

	mani=mc.listRelatives(sel[2], c=1)
	mc.disconnectAttr(sel[2]+'.scale',mani[0]+'.inverseScale')


	for sj in sel:
		ikj=sj.replace('JNT','ikJNT')
		fkj=sj.replace('JNT','fkJNT')
		oriCons=mc.orientConstraint(ikj, fkj, sj, mo=1)		
		mc.setAttr(oriCons[0]+'.interpType', 2)
		mc.connectAttr(switchCtrl+'.IK_FK', oriCons[0]+'.'+fkj+'W1')
		mc.connectAttr(rev+'.outputX', oriCons[0]+'.'+ikj+'W0')		

	#ikHandle________________________________________________________________

	handle = mc.ikHandle(sj=ikA[0], ee=ikC[0], sol='ikRPsolver', n=ikA[0].replace('ikJNT','ikHandle'))[0]
	handleGrp=mc.createNode('transform', n= handle.replace('Handle', 'HandleGrp'))
	handleCoord=mc.xform(handle, q=1, t=1, ws=1)
	mc.xform(handleGrp, t=handleCoord, ws=1)
	mc.parent(handle, handleGrp)
	mc.parent(handleGrp, 'dft_GRP')
	
	poleLoc = mc.spaceLocator(n=ikA[0].replace('ikJNT','ikPoleLoc'))[0]
	poleGrp = mc.createNode('transform', n=ikA[0].replace('ikJNT','ikPoleLocGrp'))
	mc.connectAttr(handle+'.poleVector', poleLoc+'.translate')
	mc.disconnectAttr(handle+'.poleVector', poleLoc+'.translate')
	mc.parent(poleLoc, poleGrp)
	ikAPos=mc.xform(ikA, q=1,t=1,ws=1)
	mc.xform(poleGrp, t=ikAPos, ws=1)

	mc.delete(mc.aimConstraint(ikA, ikC, poleLoc, aim=(0,0,-1), u=(0,1,0), wut='object', wuo=handle))

	rotPoleLoc=mc.spaceLocator(n=ikA[0].replace('ikJNT','ikRotPoleLoc'))[0]
	rotPoleLocGrp=mc.createNode('transform', n=ikA[0].replace('ikJNT','ikRotPoleLocGrp'))
	mc.parent(rotPoleLoc, rotPoleLocGrp)
	mc.delete(mc.pointConstraint(ikA, ikC, rotPoleLocGrp, mo=0))
	mc.delete(mc.orientConstraint(poleLoc, rotPoleLocGrp, mo=0))
	mc.parent(poleGrp, rotPoleLoc)
	mc.xform(rotPoleLoc, ro=(-90,0,0), os=1, r=1)

	poleLocPos=mc.xform(poleLoc, q=1,t=1,ws=1)
	poleControl=mel.eval('curve -d 1 -p 0 1 0 -p 0 0.707107 0.707107 -p 0 0 1 -p 0 -0.707107 0.707107 -p 0 -1 0 -p 0 -0.707107 -0.707107 -p 0 0 -1 -p 0 0.707107 -0.707107 -p 0 1 0 -p -0.707107 0.707107 0 -p -1 0 0 -p -0.707107 -0.707107 0 -p 0 -1 0 -p 0.707107 -0.707107 0 -p 1 0 0 -p 0.707107 0.707107 0 -p 0 1 0 -p 0 0.707107 -0.707107 -p 0 0 -1 -p 0.707107 0 -0.707107 -p 1 0 0 -p 0.707107 0 0.707107 -p 0 0 1 -p -0.707107 0 0.707107 -p -1 0 0 -p -0.707107 0 -0.707107 -p 0 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 ;')
	poleControl=mc.rename(poleControl, ikA[0].replace('ikJNT','PoleVector_ikCTRL'))			
	mc.xform(poleControl, t=poleLocPos, ws=1  )
	mc.poleVectorConstraint(poleControl, handle)
	mc.delete(rotPoleLocGrp)
	localGrp(poleControl)
	papi=mc.listRelatives(poleControl, p=1)
	mc.parent(papi, 'C_main_01_CTRL')

	#Squash/Stretch___________________________________________________________
	aCoord=mc.xform(ikA, q=1, t=1, ws=1)
	bCoord=mc.xform(ikC, q=1, t=1, ws=1)


	mc.distanceDimension(sp=aCoord ,ep=bCoord)

	loc1=mc.rename('locator1', ikA[0].replace('ikJNT', 'distLoc'))
	loc2=mc.rename('locator2', ikC[0].replace('endikJNT', 'distLoc'))
	dist=mc.rename('distanceDimension1', ikC[0].replace('endikJNT', 'distDimension'))
		
	distGrp=mc.createNode('transform', n=ikA[0].replace('ikJNT', 'distGRP'))
	
	_obj=[loc1, loc2, dist]
	localGrp(_obj)
	mc.select(_obj)
	mel.eval('pickWalk -d up;')
	groups=mc.ls(sl=1)
	mc.parent(groups, distGrp)
	mc.parent(distGrp, 'dft_GRP')

	mdFixStretch=mc.createNode('multiplyDivide', n=ikA[0].replace('ikJNT', 'StretchFix_MD'))
	mdStretch=mc.createNode('multiplyDivide', n=ikA[0].replace('ikJNT', 'Stretch_MD'))
	condStretch=mc.createNode('condition', n=ikA[0].replace('ikJNT', 'Stretch_COND'))

	mc.connectAttr(dist+'Shape.distance', mdFixStretch+'.input1X')
	mc.connectAttr('C_root_01_CTRL.scaleX', mdFixStretch+'.input2X')
	mc.setAttr(mdFixStretch+'.operation', 2)

	mc.connectAttr(mdFixStretch+'.outputX', mdStretch +'.input1X')
	distNum=mc.getAttr(mdStretch+'.input1X')
	mc.setAttr(mdStretch+'.input2X', distNum)
	mc.setAttr(mdStretch+'.operation', 2)

	mc.connectAttr(mdStretch+'.outputX', condStretch+'.firstTerm')
	mc.connectAttr(mdStretch+'.outputX', condStretch+'.colorIfTrueR')
	mc.setAttr(condStretch+'.secondTerm', 1)
	mc.setAttr(condStretch+'.colorIfFalse', 1,1,1)
	mc.setAttr(condStretch+'.operation', 3)

	mc.connectAttr(condStretch+'.outColorR', ikA[0]+'.scaleX')
	mc.connectAttr(condStretch+'.outColorR', ikB[0]+'.scaleX')

	
	
	########################
	#Bind footControl to rig
	########################
	TempStretchLoc=mc.select(loc2)
	mc.pickWalk(d='up')
	tempStretchGRP=mc.ls(sl=1)
	mc.parentConstraint(lastInverse, tempStretchGRP, mo=1)
	mc.parentConstraint(lastInverse, handleGrp, mo=1)




#spineYUP()
arm()
#leg()
