import maya.cmds as mc
import maya.mel as mel

def dynChain():
	sel=mc.ls(sl=1)
	allJ=mc.select(sel[0], hi=1)
	allJ=mc.ls(sl=1)
	allDyn=[]
	allDrivers=[]
	allCTRLS=[]

	for i in allJ:
		index =allJ.index(i)
		jointOrient=mc.xform(i, q=1, ro=1, ws=1)
		jointPos=mc.xform(i, q=1, t=1, ws=1)
		parent=mc.listRelatives(i, p=1)
		child=mc.listRelatives(i, c=1)
		mc.select(cl=1)
		dynJoint=mc.joint(n=i.replace('_JNT', '_dynJoint'), rad=0.1)
		mc.select(cl=1)
		driverJoint=mc.joint(n=i.replace('_JNT', '_driverJoint'), rad=0.1)
		mc.xform(dynJoint, t=jointPos, ws=1)
		mc.xform(dynJoint, ro=jointOrient, ws=1)
		mc.xform(driverJoint, t=jointPos, ws=1)
		mc.xform(driverJoint, ro=jointOrient, ws=1)
		mc.makeIdentity(dynJoint, a=1)
		mc.makeIdentity(driverJoint, a=1)

		if child != None:
			ztr=mc.createNode('transform', n= i.replace('_JNT', '_dynZTR'))
			dynGrp=mc.createNode('transform', n= i.replace('_JNT', '_dynControlGRP'))
			CTRL=mc.circle(n= i.replace('_JNT', '_dynCTRL'), nr=(1,0,0), r=0.5)
			mc.parent(CTRL, dynGrp)
			mc.parent(dynGrp, ztr)
			mc.xform(ztr, t=jointPos, ws=1)
			mc.xform(ztr, ro=jointOrient, ws=1)
			allCTRLS.append(CTRL)

		if parent!=None:
			dynParent=parent[0].replace('_JNT', '_dynJoint')
			driverParent=parent[0].replace('_JNT', '_driverJoint')
			controlParent=parent[0].replace('_JNT', '_dynCTRL')


		if parent != None:
			if mc.objExists(dynParent)==True:
				mc.parent(dynJoint, dynParent)
				mc.parent(driverJoint, driverParent)
			if child != None:
				if mc.objExists(controlParent)==True:
					mc.parent(ztr, controlParent)

		allDyn.append(dynJoint)	
		allDrivers.append(driverJoint)
		
		if child !=None:
			mc.parentConstraint(CTRL[0], driverJoint, mo=1)
			'''
			tx=mc.getAttr(driverJoint+'.tx')
			ty=mc.getAttr(driverJoint+'.ty')
			tz=mc.getAttr(driverJoint+'.tz')

			rx=mc.getAttr(driverJoint+'.rx')
			ry=mc.getAttr(driverJoint+'.ry')
			rz=mc.getAttr(driverJoint+'.rz')

			sx=mc.getAttr(driverJoint+'.sx')
			sy=mc.getAttr(driverJoint+'.sy')
			sz=mc.getAttr(driverJoint+'.sz')

			nodeTx=mc.createNode('addDoubleLinear', n= driverJoint.replace('_driverJoint', '_ADL'))
			mc.setAttr(nodeTx+'.input2', tx)
			mc.connectAttr(CTRL[0]+'.tx', nodeTx+'.input1')
			mc.connectAttr(nodeTx+'.output', driverJoint+'.tx')

			nodeTy=mc.createNode('addDoubleLinear', n= driverJoint.replace('_driverJoint', '_ADL'))
			mc.setAttr(nodeTy+'.input2', ty)
			mc.connectAttr(CTRL[0]+'.ty', nodeTy+'.input1')
			mc.connectAttr(nodeTy+'.output', driverJoint+'.ty')

			nodeTz=mc.createNode('addDoubleLinear', n= driverJoint.replace('_driverJoint', '_ADL'))
			mc.setAttr(nodeTz+'.input2', tz)
			mc.connectAttr(CTRL[0]+'.tz', nodeTz+'.input1')
			mc.connectAttr(nodeTz+'.output', driverJoint+'.tz')

			nodeRx=mc.createNode('addDoubleLinear', n= driverJoint.replace('_driverJoint', '_ADL'))
			mc.setAttr(nodeRx+'.input2', rx)
			mc.connectAttr(CTRL[0]+'.rx', nodeRx+'.input1')
			mc.connectAttr(nodeRx+'.output', driverJoint+'.rx')

			nodeRy=mc.createNode('addDoubleLinear', n= driverJoint.replace('_driverJoint', '_ADL'))
			mc.setAttr(nodeRy+'.input2', ry)
			mc.connectAttr(CTRL[0]+'.ry', nodeRy+'.input1')
			mc.connectAttr(nodeRy+'.output', driverJoint+'.ry')

			nodeRz=mc.createNode('addDoubleLinear', n= driverJoint.replace('_driverJoint', '_ADL'))
			mc.setAttr(nodeRz+'.input2', rz)
			mc.connectAttr(CTRL[0]+'.rz', nodeRz+'.input1')
			mc.connectAttr(nodeRz+'.output', driverJoint+'.rz')
			'''
			


	first=allDyn[0]
	last=allDyn[-1]
	curveCoords=[]
	for x in allJ:
		jointCoord=mc.xform(x, q=1, t=1, ws=1)	
		curveCoords.append(jointCoord)

	curve=mc.curve(p=curveCoords, d=1)
	curve=mc.rename(curve, first.replace('_dynJoint','_setCurve'))
	
	curveAux=mc.curve(p=curveCoords, d=1)
	curveAux=mc.rename(curveAux, first.replace('_dynJoint','_auxSetCurve'))

	skinCurve=mc.curve(p=curveCoords, d=1)
	skinCurve=mc.rename(skinCurve, first.replace('_dynJoint','_skinCurve'))

	mc.select(curve)
	mel.eval('makeCurvesDynamic 2 { "0", "0", "1", "1", "0"};')

	mc.select(curveAux+'Shape')
	mc.select(curve, add=1)
	mel.eval('parent -r -s')
	mc.delete(curveAux)		

	dynCurve=mc.ls('curve1')[0]
	dynCurve=mc.rename(dynCurve, first.replace('_dynJoint','_dynCurve'))


	nucleus=mc.ls('nucleus1')[0]
	#mc.connectAttr('C_root_01_CTRL.dynamicsBlend', 'nucleus1.enable')

	follicleGRP=mc.ls('hairSystem1Follicles')[0]
	follicleGRP=mc.rename(follicleGRP, first.replace('_dynJoint','_follGRP'))

	follicle=mc.ls('follicle1')[0]
	follicle=mc.rename(follicle, first.replace('_dynJoint','_follicle'))
	mc.setAttr(follicle+'Shape.degree', 1)
	#mc.setAttr(follicle+'Shape.fixedSegmentLength', 1)

	mc.disconnectAttr(curve+'Shape.local',follicle+'Shape.startPosition' )
	mc.connectAttr(curveAux+'Shape.local',follicle+'Shape.startPosition' )
	mc.delete(curve+'Shape')
	

	hairSystem=mc.ls('hairSystem1')[0]
	hairSystem=mc.rename(hairSystem, first.replace('_dynJoint','_hairSystem'))

	condMethod = mc.createNode('condition', n=first.replace('dynJoint','_timeToMethodCondition'))
	mc.connectAttr('nucleus1.currentTime', condMethod+'.firstTerm')
	mc.connectAttr('nucleus1.startFrame', condMethod+'.secondTerm')
	mc.setAttr(condMethod+'.operation', 3)
	mc.setAttr(condMethod+'.colorIfTrueR', 3)
	mc.setAttr(condMethod+'.colorIfFalseR', 0)
	mc.connectAttr(condMethod+'.outColorR', hairSystem+'.simulationMethod')


	

	splineIK = mc.ikHandle(sj=first, ee=last, sol='ikSplineSolver', c=dynCurve,scv=0, fj=1, n=first.replace('_dynJoint','_dynSplineHandle'))[0]


	#mc.select(allDrivers)
	#mc.select(skinCurve, add=1)
	#mc.skinCluster(n=dynCurve.replace('_dynCurve', '_dynSkinCluster'), tsb=1)
	bs=mc.blendShape(skinCurve, curve )	
	mc.setAttr(bs[0]+'.'+skinCurve, 1)
	mc.select(skinCurve)
	mc.ClusterCurve()
	clus=mc.ls('cluster*Handle')
	for x in clus:		
		index=clus.index(x)		
		x=mc.rename(x,first.replace('_dynJoint','_'+str(index)+'clusCurve') )
		control=x.replace('01_'+str(index)+'clusCurve','0'+str(index+1)+'_dynCTRL' )

		print control
		if mc.objExists(control)==True:
			mc.parentConstraint(control, x, mo=1)
		else:
			control=x.replace('01_'+str(index)+'clusCurve','0'+str(index)+'_dynCTRL' )
			mc.parentConstraint(control, x, mo=1)
		mc.setAttr(x+'Cluster.relative',0)

	for x in allJ:
		y=x.replace('_JNT', '_dynJoint')
		z=x.replace('_JNT', '_driverJoint')
		cons=mc.parentConstraint(z,y,x, mo=0)
		mc.setAttr(cons[0]+'.interpType', 2)
		rev=mc.createNode('reverse', n= x.replace('_JNT', '_dynReverse'))
		mc.connectAttr('C_root_01_CTRL.dynamicsBlend', rev+'.inputX')
		mc.connectAttr(rev+'.outputX', cons[0]+'.'+z+'W0')

		mc.connectAttr('C_root_01_CTRL.dynamicsBlend', cons[0]+'.'+y+'W1')



		

		
		
		

	mc.delete('hairSystem1OutputCurves')

	mc.setAttr(hairSystem+'Shape.startCurveAttract', 0.001)
	mc.setAttr(hairSystem+'Shape.attractionDamp', 0)
	mc.setAttr(hairSystem+'Shape.motionDrag', 0)
	mc.setAttr(hairSystem+'Shape.mass', 0.05)
	mc.setAttr(hairSystem+'Shape.bendResistance', 0.1)
	mc.setAttr(hairSystem+'Shape.stretchResistance', 3)
	mc.setAttr(hairSystem+'Shape.turbulenceFrequency', 0.1)
	mc.setAttr(hairSystem+'Shape.turbulenceStrength', 0.1)
	mc.setAttr(hairSystem+'Shape.turbulenceSpeed', 0.1)
	mc.setAttr(hairSystem+'Shape.damp', 0)
	mc.setAttr('nucleus1.gravity', 0)

	mc.setAttr(follicle+'Shape.pointLock', 1)
	mc.setAttr(follicle+'Shape.restPose', 3)

	mc.setAttr(nucleus+'.spaceScale', 0.01)
	mc.setAttr(nucleus+'.gravity', 0.5)
	'''
	mc.setAttr(splineIK+'.dWorldUpVectorY', 1)
	mc.setAttr(splineIK+'.dWorldUpVectorZ', 0)
	mc.setAttr(splineIK+'.dWorldUpType', 3)
	mc.setAttr(splineIK+'.dTwistControlEnable', 1)	
	mc.connectAttr('C_Medusa_01_CTRL.worldMatrix[0]', splineIK+'.dWorldUpMatrix')
	'''
	





def applyDyn():
	sel=mc.ls(sl=1)
	for x in sel:
		mc.select(x)
		dynChain()

applyDyn()
