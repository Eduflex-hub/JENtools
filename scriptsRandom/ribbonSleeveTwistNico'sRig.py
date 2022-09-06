import maya.cmds as mc
from math import pow,sqrt
import pymel.core as pm

sel=mc.ls(sl=1)
def getDistance(_objA, _objB):
	gObjA = mc.xform(_objA, q=True, t=True, ws=True)
	gObjB = mc.xform(_objB, q=True, t=True, ws=True)
	
	return sqrt(pow(gObjA[0]-gObjB[0],2)+pow(gObjA[1]-gObjB[1],2)+pow(gObjA[2]-gObjB[2],2))

def ribbon (_objA, _objB, _divisions, _name):
	#NURBS GEO__________________________________________________________
	start=_objA
	end=_objB

	distance=getDistance(start, end)
	sleeveSuffix='_sleeve_'
	

	ribbonGRP=mc.createNode('transform', n=_name.replace('NURBS', 'ribbonGRP'))
	nurbs=mc.nurbsPlane(ax=(0,1,0), w=distance,lr=0.1, d=3, u=4, v=1, ch=0, n=_name)
	
	mc.rebuildSurface( nurbs, ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kc=0, su=4, du=3, sv=1, dv=1, tol=0.01, fr=0, dir=2)
	mc.parent(nurbs, ribbonGRP)
	folGRP=mc.createNode('transform', n=_name.replace('_NURBS', '_follicleGRP'), p=ribbonGRP)	

	for i in range(0, _divisions):
		#folicles_________________________________________________________
		index = range(0, _divisions).index(i)
		
		fol = mc.createNode('transform', n=_name.replace('NURBS', str(index)+'follicle'), ss=True)
		folShape = mc.createNode('follicle', n=_name.replace('NURBS', str(index)+'follicleShape'), p=fol, ss=True)
		
		mc.connectAttr(nurbs[0]+'Shape.local', folShape+'.inputSurface')
		mc.connectAttr(nurbs[0]+'Shape.worldMatrix[0]', folShape+'.inputWorldMatrix')
		mc.connectAttr(folShape+'.outRotate', fol+'.rotate')
		mc.connectAttr(folShape+'.outTranslate', fol+'.translate')
		mc.setAttr(fol+'.inheritsTransform', 0)
		
		form=1/(float(_divisions)*2)
		uValue= ((form+(form*index))*2)-form
		print uValue

		mc.setAttr(folShape+'.parameterU', uValue)
		mc.setAttr(folShape+'.parameterV', 0.5)
		mc.parent(fol, folGRP)
		
		minGRP=mc.createNode('transform', n=_name.replace('NURBS','JNT'+str(index)+'GRP'), p=fol)
		mc.scaleConstraint('c_main_00_ctl',minGRP, mo=0 )
		miniJoint=mc.joint(n=_name.replace('NURBS','rib'+str(index)+'JNT'), rad=0.8)
		mc.connectAttr(_objA+'.scale', miniJoint+'.scale' )


		mc.refresh()
	#driver system__________________________________________________________
	drvJoints=[]
	drvGrp=[]
	drvZTR=[]
	grpCTRL=[]
	ctrls=[]	
	aims=[]
	locsgroup=[]
	for x in range(0,3):
		index=range(0,3).index(x)
		drvJntGRP=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'drvJntGRP'), p=ribbonGRP)
		drvZTRGRP=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'drvJntZTR'), p=drvJntGRP)
		drvJNT=mc.joint(n=_name.replace('NURBS',str(index)+'drvJNT'), rad=1.5)		
		
		drvJoints.append(drvJNT)
		drvGrp.append(drvJntGRP)
		drvZTR.append(drvZTRGRP)

		grpCir=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'ribbonCtrlGRP'))
		cir=mc.circle(n=_name.replace('NURBS',str(index)+'ribbonCTRL'), r=5, nr=(1,0,0))[0]
		mc.parent(cir, grpCir)

		aimLoc=mc.spaceLocator(n=_name.replace('NURBS',str(index)+'aimLOC'))[0]
		

		locsGRP=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'locsGRP'), p=cir)
		mc.parent(aimLoc, locsGRP)		
		#mc.parent(locsGRP, ribbonGRP)
		
		
		locsgroup.append(locsGRP)

		ctrls.append(cir)
		
		aims.append(aimLoc)
		grpCTRL.append(grpCir)

		if index==0:			
			mc.xform(drvJntGRP, t= ((distance/2.0)*-1,0, 0), ws=1)
			mc.xform(grpCir, t= ((distance/2.0)*-1,0, 0), ws=1)
			#mc.parentConstraint(cir, drvJNT)
			mc.parent(grpCir, ribbonGRP)
			mc.parent(drvJntGRP, cir)
		
		if index==1:
			mc.xform(drvJntGRP, t= (0,0,0), ws=1)
			mc.xform(grpCir, t= (0,0,0), ws=1)
			#mc.parentConstraint(cir, drvJNT)
			mc.parent(grpCir, ribbonGRP)
			mc.parent(drvJntGRP, cir)
		if index==2:
			mc.xform(drvJntGRP, t= ((distance/2.0),0 ,0), ws=1)
			mc.xform(grpCir, t= ((distance/2.0), 0, 0), ws=1)
			#mc.parentConstraint(cir, drvJNT)
			mc.parent(grpCir, ribbonGRP)
			mc.parent(drvJntGRP, cir)
		mc.refresh()
		
	#twistHelpers___________________________________________________________________________________________

	mc.select(cl=1)
	jntAGRP=mc.createNode('transform',n=_name.replace('NURBS','twistHelperAGRP'), p='driverJoints_GRP')
	jntA=mc.joint(n=_name.replace('NURBS','twistHelperA'), rad=0.1)
	mc.parentConstraint(_objA,jntAGRP, mo=0 )
	mc.makeIdentity(jntA, a=1)
	jntAChild=mc.duplicate(jntA, n=_name.replace('NURBS','twistHelperA'))
	mc.parent(jntAChild, jntA)
	
	if _objA.startswith('L_')==True:
		mc.setAttr(jntAChild[0]+'.tx', 2)
		mc.makeIdentity(jntA, a=1)

	elif _objA.startswith('R_')==True:
		mc.setAttr(jntAChild[0]+'.tx', -2)
		mc.makeIdentity(jntA, a=1)

	else:		
		mc.setAttr(jntAChild[0]+'.tx', 2)
		mc.makeIdentity(jntA, a=1)
	
	ikATwistGRP=mc.createNode('transform',n=_name.replace('NURBS','ikATwistGRP'), p='dft_GRP' )
	mc.delete(mc.parentConstraint(_objA, ikATwistGRP, mo=0))
	handleA = mc.ikHandle(sj=jntA, ee=jntAChild[0], sol='ikRPsolver', n=_name.replace('NURBS','ikAHandle'))[0]
	mc.parent(handleA, ikATwistGRP )

	mc.parentConstraint(_objA, ikATwistGRP, mo=1)
	mc.select(cl=1)
	jntBGRP=mc.createNode('transform',n=_name.replace('NURBS','twistHelperBGRP'), p='driverJoints_GRP')
	jntB=mc.joint(n=_name.replace('NURBS','twistHelperB'), rad=0.1)
	mc.delete(mc.pointConstraint(_objB, jntBGRP,mo=0))
	mc.delete(mc.orientConstraint(_objA, jntBGRP,mo=0))

	mc.parentConstraint(_objB,jntBGRP, mo=1 )
	mc.makeIdentity(jntB, a=1)
	jntBChild=mc.duplicate(jntB, n=_name.replace('NURBS','twistHelperB'))
	mc.parent(jntBChild, jntB)	
	mc.setAttr(jntBChild[0]+'.tx', -2)

	if _objA.startswith('L_')==True:
		mc.setAttr(jntBChild[0]+'.tx', -2)
		mc.makeIdentity(jntB, a=1)

	elif _objA.startswith('R_')==True:
		mc.setAttr(jntBChild[0]+'.tx', 2)
		mc.makeIdentity(jntB, a=1)

	else:		
		mc.setAttr(jntAChild[0]+'.tx', -2)
		mc.makeIdentity(jntA, a=1)


	ikBTwistGRP=mc.createNode('transform',n=_name.replace('NURBS','ikBTwistGRP'), p='dft_GRP' )
	mc.delete(mc.pointConstraint(_objB, ikBTwistGRP,mo=0))
	mc.delete(mc.orientConstraint(_objA, ikBTwistGRP,mo=0))
	handleB = mc.ikHandle(sj=jntB, ee=jntBChild[0], sol='ikRPsolver', n=_name.replace('NURBS','ikBHandle'))[0]
	mc.parent(handleB, ikBTwistGRP )
	

	mc.parentConstraint(_objA, ikBTwistGRP, mo=1)
	#TwistLocators______________________________________________________________________________________________

	

	#orient to helpers__________________________________________________________________________________________
	

	mc.pointConstraint(ctrls[0], ctrls[2],grpCTRL[1], mo=1)

	aimFix=mc.createNode('transform', n=_name.replace('NURBS','aimForMid') )
	mc.delete(mc.parentConstraint(ctrls[0], aimFix, mo=0))
	mc.parent(aimFix,ctrls[0] )

	

	

	mc.parentConstraint(aims[0], drvZTR[0])
	mc.parentConstraint(aims[1], drvZTR[1])
	mc.parentConstraint(aims[2], drvZTR[2])

	#Skinning_________________________________________________________
	mc.select(drvJoints)
	mc.select(nurbs, add=1)
	mc.skinCluster(n=_name.replace('NURBS', 'NURBSskinCluster'),dr=2, par=0.5)

	mc.skinPercent(_name.replace('NURBS','NURBSskinCluster'), _name + '.cv[0][0:1]', transformValue=(drvJoints[0], 1.0))
	mc.skinPercent(_name.replace('NURBS','NURBSskinCluster'), _name + '.cv[1][0:1]', transformValue=(drvJoints[1], 0.002))
	mc.skinPercent(_name.replace('NURBS','NURBSskinCluster'), _name + '.cv[2][0:1]', transformValue=(drvJoints[1], 0.5))

	mc.skinPercent(_name.replace('NURBS','NURBSskinCluster'), _name + '.cv[3][0:1]', transformValue=(drvJoints[1], 1))

	mc.skinPercent(_name.replace('NURBS','NURBSskinCluster'), _name + '.cv[4][0:1]', transformValue=(drvJoints[1], 0.5))
	mc.skinPercent(_name.replace('NURBS','NURBSskinCluster'), _name + '.cv[5][0:1]', transformValue=(drvJoints[1], 0.002))
	mc.skinPercent(_name.replace('NURBS','NURBSskinCluster'), _name + '.cv[6][0:1]', transformValue=(drvJoints[2], 1.0))



	#positioning_and_binding twist_________________________________________________

	
	mc.parentConstraint(_objA, grpCTRL[0], mo=0)
	mc.parentConstraint(_objB, grpCTRL[2], mo=0)


	#mc.orientConstraint('L_twistHelper_01_JNT', locsgroup[0], mo=1)
	#mc.orientConstraint('L_twistHelper_02_JNT', locsgroup[2], mo=1)
	if _objA.startswith('L_')==True:
		mc.aimConstraint(ctrls[2], aimFix, aim=(1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)

	elif _objA.startswith('R_')==True:
		mc.aimConstraint(ctrls[2], aimFix, aim=(-1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)

	else:		
		mc.aimConstraint(ctrls[2], aimFix, aim=(1,0,0), u=(0,-1,0), wut='objectrotation', wuo=jntA)
	


	mc.orientConstraint(aimFix,grpCTRL[1], mo=0)

	mc.aimConstraint(aims[1], aims[0], aim=(1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)
	mc.aimConstraint(aims[1], aims[2], aim=(-1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)

	oriShort=mc.orientConstraint(drvJoints[0], drvJoints[2], drvJoints[1], mo=0)	
	mc.setAttr(oriShort[0]+'.interpType', 2)
	



	


#ribbon(sel[0], sel[1], 4, sel[0].replace('JNT', 'sleeve_NURBS'))
#ribbon(sel[1], sel[2], 6, sel[1].replace('JNT', 'NURBS'))
ribbon(sel[0], sel[1], 4, sel[0].replace('skn', 'sleeve_NURBS'))



	





