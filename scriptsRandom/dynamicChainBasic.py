import maya.cmds as mc
import maya.mel as mel

def dynChain():
	sel=mc.ls(sl=1)	
	allJ=mc.select(sel[0], hi=1)
	allJ=mc.ls(sl=1)	
	allDyn=[]
	allDrivers=[]

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


	first=allDyn[0]
	last=allDyn[-1]
	curveCoords=[]	
	for x in allJ:
		jointCoord=mc.xform(x, q=1, t=1, ws=1)	
		curveCoords.append(jointCoord)

	curve=mc.curve(ep=curveCoords, d=2)
	curve=mc.rename(curve, first.replace('_dynJoint','_setCurve'))
	mc.select(curve)
	mel.eval('makeCurvesDynamic 2 { "1", "0", "1", "1", "0"};')
	dynCurve=mc.ls('curve1')[0]
	dynCurve=mc.rename(dynCurve, first.replace('_dynJoint','_dynCurve'))
	splineIK = mc.ikHandle(sj=first, ee=last, sol='ikSplineSolver', c=dynCurve,scv=0, fj=1, n=first.replace('_dynJoint','_dynSplineHandle'))[0]

	nucleus=mc.ls('nucleus1')[0]	

	follicleGRP=mc.ls('hairSystem1Follicles')[0]
	follicleGRP=mc.rename(follicleGRP, first.replace('_dynJoint','_follGRP'))

	follicle=mc.ls('follicle1')[0]
	follicle=mc.rename(follicle, first.replace('_dynJoint','_follicle'))

	hairSystem=mc.ls('hairSystem1')[0]
	hairSystem=mc.rename(hairSystem, first.replace('_dynJoint','_hairSystem'))

	mc.select(allDrivers)
	mc.select(curve, add=1)
	mc.skinCluster(n=dynCurve.replace('_dynCurve', '_dynSkinCluster'), tsb=1)

	for x in allJ:
		y=x.replace('_JNT', '_dynJoint')
		mc.parentConstraint(y,x, mo=0)

	mc.delete('hairSystem1OutputCurves')

	mc.setAttr(hairSystem+'Shape.startCurveAttract', 3)
	mc.setAttr(hairSystem+'Shape.attractionDamp', 1)
	mc.setAttr(hairSystem+'Shape.motionDrag', 0.1)
	mc.setAttr(hairSystem+'Shape.mass', 0.5)
	mc.setAttr(hairSystem+'Shape.bendResistance', 100)
	mc.setAttr(hairSystem+'Shape.stretchResistance', 3)
	mc.setAttr(hairSystem+'Shape.turbulenceFrequency', 0.5)
	mc.setAttr(hairSystem+'Shape.turbulenceStrength', 5)
	mc.setAttr(hairSystem+'Shape.turbulenceSpeed', 0.5)
	mc.setAttr(hairSystem+'Shape.damp', 1)

	mc.setAttr(follicle+'Shape.pointLock', 1)
	mc.setAttr(follicle+'Shape.restPose', 3)

	mc.setAttr(nucleus+'.spaceScale', 0.01)
	mc.setAttr(nucleus+'.gravity', 0.5)






def applyDyn():
	sel=mc.ls(sl=1)
	for x in sel:
		mc.select(x)
		dynChain()

applyDyn()
