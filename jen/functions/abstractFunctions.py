import maya.cmds as mc
import maya.mel as mel
from math import pow,sqrt
import pymel.core as pm
import sys
import json
import os
def lockHide(obj, transform, freeze = 0):
	attr = mc.listAttr(obj, k=1)
	if transform == 'all':
		for i in attr:
			if i.startswith('translate')==True or i.startswith('rotate')==True or i.startswith('scale')==True or i.startswith('visibility')==True:				
				mc.setAttr(obj + '.' + i, l=1, cb= 0, k=0)

	if transform == 'translate':
		for i in attr:
			if i.startswith('translate') ==True:
				mc.setAttr(obj + '.' + i, l=1, cb= 0, k=0)
		

	if transform == 'rotate':
		for i in attr:
			if i.startswith('rotate') ==True:
				mc.setAttr(obj + '.' + i, l=1, cb= 0, k=0)

	if transform == 'scale':
		for i in attr:
			if i.startswith('scale') ==True:
				mc.setAttr(obj + '.' + i, l=1, cb= 0, k=0)

	if transform == 'visibility':
		for i in attr:
			if i.startswith('visibility') ==True:
				mc.setAttr(obj + '.' + i, l=1, cb= 0, k=0)

	if freeze == 1:
		mc.setAttr(obj + '.overrideEnabled', 1)
		mc.setAttr(obj + '.overrideDisplayType', 2)

	


def storeNodeAttrAsJson(rigPath, node):
	currentDict={
					'savedIn' : rigPath,
					'name': node,

				}

	attributes=mc.listAttr(node, ud=1, hd=1)
	for x in attributes:
		info=mc.getAttr(node+'.'+x)
		
		currentDict[x]=info
	

	jsonPath= rigPath
	with open(jsonPath + r'/' + node+ '.json', 'w') as outfile:
		json.dump(currentDict, outfile, sort_keys=1, indent=4)

	sys.stdout.write("Data Saved.")

def getSimpleJson(nodePath,query_value):
	   '''
	   #Reads a variable from json file
	   '''
	   
	   if os.path.exists(nodePath):
		   fIn = open(nodePath, 'r')
		   jsonContainer = json.load(fIn)
			  
		   
		   value = jsonContainer.get(query_value)
		   
		   return value
		   fIn.close()
	   else:
		   print "Config Simple Json File not found", module
		   return False

def getDoubleDictJson(nodePath,module,attr):
		'''
		#Reads a variable from json file
		'''
	   
		if os.path.exists(nodePath):
			fIn = open(nodePath, 'r')
			jsonContainer = json.load(fIn)
			  
			tempValue=jsonContainer.get(module)
			#print tempValue
			if tempValue != None:
				value=jsonContainer.get(module).get(attr)
				return value
				#print value
				fIn.close()
				   
			
		else:
			print "Config Double Json File not found", module
			return False

def loadJenNode(_jsonPath):
	node=mc.createNode('transform', n='jenAutorig_projectPathNode', ss=1)
	mc.setAttr('jenAutorig_projectPathNode.hiddenInOutliner', 1)

	mc.addAttr(node,longName='dirInChar', dt="string")
	mc.addAttr(node,longName='assetInChar', dt="string")
	mc.addAttr(node,longName='dirInProp', dt="string")
	mc.addAttr(node,longName='assetInProp', dt="string")
	mc.addAttr(node,longName='finalPath', dt="string")
	mc.addAttr(node,longName='publishedPath', dt="string")
	
	dirInChar=getSimpleJson(_jsonPath, 'dirInChar')
	assetInChar=getSimpleJson(_jsonPath, 'assetInChar')
	dirInProp=getSimpleJson(_jsonPath, 'dirInProp')
	assetInProp=getSimpleJson(_jsonPath, 'assetInProp')
	finalPath=getSimpleJson(_jsonPath, 'finalPath')
	publishedPath=getSimpleJson(_jsonPath, 'publishedPath')

	mc.setAttr(node+'.dirInChar', dirInChar, type='string')
	mc.setAttr(node+'.assetInChar', assetInChar, type='string')
	mc.setAttr(node+'.dirInProp', dirInProp, type='string')
	mc.setAttr(node+'.assetInProp', assetInProp, type='string')
	mc.setAttr(node+'.finalPath', finalPath, type='string')
	mc.setAttr(node+'.publishedPath', publishedPath, type='string')

def getDistance(_objA, _objB):
	gObjA = mc.xform(_objA, q=True, t=True, ws=True)
	gObjB = mc.xform(_objB, q=True, t=True, ws=True)
	
	return sqrt(pow(gObjA[0]-gObjB[0],2)+pow(gObjA[1]-gObjB[1],2)+pow(gObjA[2]-gObjB[2],2))

def extractControl(_transform,_shape):	
	dup = mc.duplicate(_shape, returnRootsOnly=1, rc=1)[0]
	mc.parent(dup, w=1)
	mc.setAttr(dup + '.tx', k=1, lock=0)
	mc.setAttr(dup + '.ty', k=1, lock=0)
	mc.setAttr(dup + '.tz', k=1, lock=0)

	mc.setAttr(dup + '.rx', k=1, lock=0)
	mc.setAttr(dup + '.ry', k=1, lock=0)
	mc.setAttr(dup + '.rz', k=1, lock=0)

	mc.setAttr(dup + '.sx', k=1, lock=0)
	mc.setAttr(dup + '.sy', k=1, lock=0)
	mc.setAttr(dup + '.sz', k=1, lock=0)


	mc.makeIdentity(dup, a=1, s=1)
	dupShape = mc.listRelatives(dup, c=1)[0] 	

	mc.parent(dup, _transform)
	mc.makeIdentity(dup, a=1)
	mc.parent(dupShape, _transform, r=1, shape=1)
	mc.delete(dup)
	mc.rename(dupShape, _transform+'Shape')
	return _transform

def localGrp(_node):
	lista=mc.ls(_node)
	parents=[]
	for x in lista:
		coord = mc.xform(x, q=1, t=1, ws=1)
		orient= mc.xform(x, q=1, ro=1, ws=1)
		grp=mc.createNode('transform',n= x+'_GRP')
		ztr=mc.createNode('transform',n= x+'_ZTR')
		mc.parent(ztr, grp)
		mc.xform(grp, t=coord, ws=1)
		mc.xform(grp, ro=orient, ws=1)
		mc.parent(x, ztr)
		parents.append(grp)
	return parents

def getPointer(_pointerText, _leftList, _centerList, _rigthList):

	listData=_pointerText
	listData=listData.split(',')
	for x in listData:
		mesh=x
		if x.startswith('L_'):
			if _leftList !=False:
				_leftList.append(mesh)
		elif x.startswith('R_'):
			if _rigthList !=False:
				_rigthList.append(mesh)
		elif x.startswith('C_'):
			if _centerList !=False:
				_centerList.append(mesh)
		else:
			return False

def removeMesh():
	namespaceToDelete = 'tempModel'
	mc.namespace(set=namespaceToDelete)
	mc.delete(mc.namespaceInfo(listOnlyDependencyNodes=True))
	mc.namespace(set=':')
	mc.namespace(rm=namespaceToDelete)

def forwardAxis(_joint):	
	_child=mc.listRelatives(_joint, c=1)[0]	
	posX=mc.getAttr(_child+'.tx')
	posY=mc.getAttr(_child+'.ty')
	posZ=mc.getAttr(_child+'.tz')
	childCoord=[abs(posX)], [abs(posY)], [abs(posZ)]		
	maximum=max(childCoord)	
	
	if maximum == childCoord[0]:
		axis='X'
	if maximum == childCoord[1]:
		axis='Y'
	if maximum == childCoord[2]:
		axis='Z'

	return axis

def setCurveColor(_curve,_color):
	if _color == 'red':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 13)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 13)

	if _color == 'green':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 14)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 14)

	if _color == 'yellow':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 17)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 17)

	if _color == 'blue':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 15)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 15)

	if _color == 'orange':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 12)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 12)

	if _color == 'black':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 1)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 1)

	if _color == 'gray':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 2)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 2)

	if _color == 'pink':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 9)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 9)

	if _color == 'blueLight':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 18)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 18)

	if _color == 'greenDark':
		if mc.getAttr(_curve+'Shape.overrideEnabled')==0:
			mc.setAttr(_curve + 'Shape.overrideEnabled', 1)
			mc.setAttr(_curve + 'Shape.overrideColor', 7)
		else:
			mc.setAttr(_curve + 'Shape.overrideColor', 7)

def applyLimbRibbon(_objA, _objB, _divisions, _name, _sleeve=0):
	start=_objA
	end=_objB

	distance=getDistance(start, end)	

	ribbonGRP=mc.createNode('transform', n=_name.replace('NURBS', 'ribbonGRP'), p='dft_GRP')
	nurbs=mc.nurbsPlane(ax=(0,1,0), w=distance,lr=0.1, d=3, u=4, v=1, ch=0, n=_name)
	
	mc.rebuildSurface( nurbs, ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kc=0, su=4, du=3, sv=1, dv=1, tol=0.01, fr=0, dir=2)
	mc.parent(nurbs, ribbonGRP)
	folGRP=mc.createNode('transform', n=_name.replace('_NURBS', '_follicleGRP'), p='joints_group')	
	miniJoints=[]
	for i in range(0, _divisions):
		#folicles_________________________________________________________
		index = range(0, _divisions).index(i)
		
		fol = mc.createNode('transform', n=_name.replace('NURBS', str(index)+'follicle'), ss=True,p=folGRP)
		folShape = mc.createNode('follicle', n=_name.replace('NURBS', str(index)+'follicleShape'), p=fol, ss=True)
		
		mc.connectAttr(nurbs[0]+'Shape.local', folShape+'.inputSurface')
		mc.connectAttr(nurbs[0]+'Shape.worldMatrix[0]', folShape+'.inputWorldMatrix')
		mc.connectAttr(folShape+'.outRotate', fol+'.rotate')
		mc.connectAttr(folShape+'.outTranslate', fol+'.translate')
		mc.setAttr(fol+'.inheritsTransform', 0)
		
		form=1/(float(_divisions)*2)
		uValue= ((form+(form*index))*2)-form		

		mc.setAttr(folShape+'.parameterU', uValue)
		mc.setAttr(folShape+'.parameterV', 0.5)		
		
		minGRP=mc.createNode('transform', n=_name.replace('NURBS','JNT'+str(index)+'GRP'), p=fol)
		mc.scaleConstraint('C_root_01_CTRL',minGRP, mo=0 )
		miniJoint=mc.joint(n=_name.replace('NURBS','rib'+str(index)+'JNT'), rad=0.8)
		miniJoints.append(miniJoint)
		if _objA.startswith('C_') is True:
			mc.connectAttr(_objA+'.scaleY', miniJoint+'.scaleX' )
			mc.connectAttr(_objA+'.scaleZ', miniJoint+'.scaleY' )
			mc.connectAttr(_objA+'.scaleX', miniJoint+'.scaleZ' )
		else:
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
		grpCir=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'bendyCtrlGRP'), p='C_main_01_CTRL')
		if forwardAxis(start)=='X':
			cir=mc.circle(n=_name.replace('NURBS',str(index)+'bendyCTRL'), r=5, nr=(1,0,0))[0]
		if forwardAxis(start)=='Y':
			cir=mc.circle(n=_name.replace('NURBS',str(index)+'bendyCTRL'), r=5, nr=(0,1,0))[0]
		if _sleeve==1:			
			mc.circle(cir, e=1, r=4)
			mc.setAttr(cir+'.v', 0)


		mc.parent(cir, grpCir)

		drvJntGRP=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'drvJointGRP'), p=cir)
		drvZTRGRP=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'drvJointZTR'), p=drvJntGRP)
		drvJNT=mc.joint(n=_name.replace('NURBS',str(index)+'drvJoint'), rad=1.5)
		mc.setAttr(drvJNT+'.v', 0)
		
		drvJoints.append(drvJNT)
		drvGrp.append(drvJntGRP)
		drvZTR.append(drvZTRGRP)		

		aimLoc=mc.spaceLocator(n=_name.replace('NURBS',str(index)+'aimLOC'))[0]
		locsGRP=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'locsGRP'), p=cir)
		mc.setAttr(aimLoc+'.v', 0)
		mc.parent(aimLoc, locsGRP)
		
		locsgroup.append(locsGRP)

		ctrls.append(cir)
		
		aims.append(aimLoc)
		grpCTRL.append(grpCir)

		if index==0:
			mc.xform(drvJntGRP, t= ((distance/2.0)*-1,0, 0), ws=1)
			mc.xform(grpCir, t= ((distance/2.0)*-1,0, 0), ws=1)
			tempDad=mc.listRelatives(_objA, p=1)
			setCurveColor(cir, 'red')
			if tempDad != 'None':
				if mc.objExists(tempDad[0].replace('JNT', '2bendyCTRL'))==True:
					mc.parent(grpCir, tempDad[0].replace('JNT', '2bendyCTRL'))
					mc.setAttr(cir+'.v', 0)	
		
		if index==1:
			mc.xform(drvJntGRP, t= (0,0,0), ws=1)
			mc.xform(grpCir, t= (0,0,0), ws=1)
			setCurveColor(cir, 'yellow')
			

		if index==2:
			mc.xform(drvJntGRP, t= ((distance/2.0),0 ,0), ws=1)
			mc.xform(grpCir, t= ((distance/2.0), 0, 0), ws=1)
			setCurveColor(cir, 'red')
		
			

		mc.refresh()
		
	#twistHelpers___________________________________________________________________________________________

	mc.select(cl=1)
	twistGRP=mc.createNode('transform', n=_name.replace('NURBS','twistHelpersGRP'), p='driverJoints_GRP')

	jntAGRP=mc.createNode('transform',n=_name.replace('NURBS','twistHelperAGRP'), p=twistGRP)
	jntA=mc.joint(n=_name.replace('NURBS','twistHelperA'), rad=0.1)
	twistTempCONSA=mc.parentConstraint(_objA,jntAGRP, mo=0 )
	mc.makeIdentity(jntA, a=1)
	jntAChild=mc.duplicate(jntA, n=_name.replace('NURBS','twistHelperA'))
	mc.parent(jntAChild, jntA)
	
	if _objA.startswith('L_')==True:
		if forwardAxis(start)=='X':
			mc.setAttr(jntAChild[0]+'.tx', 2)
		if forwardAxis(start)=='Y':
			mc.setAttr(jntAChild[0]+'.ty', 2)
		mc.makeIdentity(jntA, a=1)

	elif _objA.startswith('R_')==True:
		if forwardAxis(start)=='X':
			mc.setAttr(jntAChild[0]+'.tx', -2)
		if forwardAxis(start)=='Y':
			mc.setAttr(jntAChild[0]+'.ty', -2)
		mc.makeIdentity(jntA, a=1)

	else:	
		if forwardAxis(start)=='X':
			mc.setAttr(jntAChild[0]+'.tx', 2)
		if forwardAxis(start)=='Y':
			mc.setAttr(jntAChild[0]+'.ty', 2)
		mc.makeIdentity(jntA, a=1)
	
	ikATwistGRP=mc.createNode('transform',n=_name.replace('NURBS','ikATwistGRP'), p='dft_GRP' )
	mc.delete(mc.parentConstraint(_objA, ikATwistGRP, mo=0))
	handleA = mc.ikHandle(sj=jntA, ee=jntAChild[0], sol='ikRPsolver', n=_name.replace('NURBS','ikAHandle'))[0]
	mc.parent(handleA, ikATwistGRP )

	mc.parentConstraint(_objA, ikATwistGRP, mo=1)
	mc.select(cl=1)
	jntBGRP=mc.createNode('transform',n=_name.replace('NURBS','twistHelperBGRP'), p=twistGRP)
	jntB=mc.joint(n=_name.replace('NURBS','twistHelperB'), rad=0.1)
	twistTempCONSB=mc.parentConstraint(_objB,jntBGRP, mo=0 )
	mc.makeIdentity(jntB, a=1)
	jntBChild=mc.duplicate(jntB, n=_name.replace('NURBS','twistHelperB'))
	mc.parent(jntBChild, jntB)
	if forwardAxis(start)=='X':
		mc.setAttr(jntBChild[0]+'.tx', -30)
	if forwardAxis(start)=='Y':
		mc.setAttr(jntBChild[0]+'.ty', -30)

	if _objA.startswith('L_')==True:
		if forwardAxis(start)=='X':
			mc.setAttr(jntBChild[0]+'.tx', -30)
		if forwardAxis(start)=='Y':
			mc.setAttr(jntBChild[0]+'.ty', -30)
		
		mc.makeIdentity(jntB, a=1)

	elif _objA.startswith('R_')==True:
		if forwardAxis(start)=='X':
			mc.setAttr(jntBChild[0]+'.tx', 30)
		if forwardAxis(start)=='Y':
			mc.setAttr(jntBChild[0]+'.ty', 30)		
		mc.makeIdentity(jntB, a=1)

	else:
		if forwardAxis(start)=='X':
			mc.setAttr(jntBChild[0]+'.tx', -30)
		if forwardAxis(start)=='Y':
			mc.setAttr(jntBChild[0]+'.ty', -30)		
		mc.makeIdentity(jntB, a=1)


	ikBTwistGRP=mc.createNode('transform',n=_name.replace('NURBS','ikBTwistGRP'), p='dft_GRP' )
	mc.delete(mc.parentConstraint(_objB, ikBTwistGRP,mo=0))
	handleB = mc.ikHandle(sj=jntB, ee=jntBChild[0], sol='ikRPsolver', n=_name.replace('NURBS','ikBHandle'))[0]
	mc.parent(handleB, ikBTwistGRP )
	

	mc.parentConstraint(_objA, ikBTwistGRP, mo=1)

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
	
	isDadC=mc.listRelatives(grpCTRL[0], p=1)[0]
	if isDadC.endswith('bendyCTRL')==False:
		mc.parentConstraint(_objA, grpCTRL[0], mo=0)
		mc.parentConstraint(_objB, grpCTRL[2], mo=0)

	else:	
		mc.parentConstraint(_objB, grpCTRL[2], mo=0)
		mc.setAttr(grpCTRL[0]+'.tx',0)
		mc.setAttr(grpCTRL[0]+'.ty',0)
		mc.setAttr(grpCTRL[0]+'.tz',0)
		mc.setAttr(grpCTRL[0]+'.rx',0)
		mc.setAttr(grpCTRL[0]+'.rx',0)
		mc.setAttr(grpCTRL[0]+'.rz',0)

	if _objA.startswith('L_')==True:
		if forwardAxis(start)=='X':
			mc.aimConstraint(ctrls[2], aimFix, aim=(1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)
		if forwardAxis(start)=='Y':
			mc.aimConstraint(ctrls[2], aimFix, aim=(1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)

	elif _objA.startswith('R_')==True:
		if forwardAxis(start)=='X':
			mc.aimConstraint(ctrls[2], aimFix, aim=(-1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)
		if forwardAxis(start)=='Y':
			mc.aimConstraint(ctrls[2], aimFix, aim=(-1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)

	else:
		if forwardAxis(start)=='X':
			mc.aimConstraint(ctrls[2], aimFix, aim=(1,0,0), u=(0,-1,0), wut='objectrotation', wuo=jntA)
		if forwardAxis(start)=='Y':
			mc.aimConstraint(ctrls[2], aimFix, aim=(0,1,0), u=(0,1,0), wut='objectrotation', wuo=jntA)
	


	mc.orientConstraint(aimFix,grpCTRL[1], mo=0)

	if forwardAxis(start)=='X':
		mc.aimConstraint(aims[1], aims[0], aim=(1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)
	if forwardAxis(start)=='Y':
		mc.aimConstraint(aims[1], aims[0], aim=(1,0,0), u=(0,0,1), wut='objectrotation',wu=(0,0,1), wuo=jntA)

	if forwardAxis(start)=='X':	
		if _sleeve==1:
			mc.aimConstraint(aims[1], aims[2], aim=(-1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntA)
		else:
			mc.aimConstraint(aims[1], aims[2], aim=(-1,0,0), u=(0,1,0), wut='objectrotation', wuo=jntB)
	if forwardAxis(start)=='Y':
		if _sleeve==1:
			mc.aimConstraint(aims[1], aims[2], aim=(-1,0,0), u=(0,0,1), wut='objectrotation',wu=(0,0,1), wuo=jntA)
		else:
			mc.aimConstraint(aims[1], aims[2], aim=(-1,0,0), u=(0,0,1), wut='objectrotation',wu=(0,0,1), wuo=jntB)

	oriShort=mc.orientConstraint(drvJoints[0], drvJoints[2], drvJoints[1], mo=0)	
	mc.setAttr(oriShort[0]+'.interpType', 2)

	#twistLocators-------------------------------------------------------------------------	
	parent=mc.listRelatives(_objA, p=1)[0]	
	child=mc.listRelatives(_objA, c=1)[0]	
	if mc.objExists(parent.replace('JNT', '0bendyCTRL'))==False:
		mc.delete(twistTempCONSA)		
		mc.orientConstraint(parent, jntAGRP, mo=1)
		mc.pointConstraint(_objA, jntAGRP, mo=1)

		if _sleeve==0:
			twistLocA = mc.spaceLocator(n= _objA.replace('JNT', 'twistLOC'))
			twistLOCGRPA=mc.createNode('transform', n=_objA.replace('JNT', 'twistLOCGRP'))
		else:
			twistLocA = mc.spaceLocator(n= _objA.replace('JNT', 'sleeveTwistLOC'))
			twistLOCGRPA=mc.createNode('transform', n=_objA.replace('JNT', 'sleeveTwistLOCGRP'))
		mc.parent(twistLocA, twistLOCGRPA)
		mc.delete(mc.parentConstraint(_objA, twistLOCGRPA))
		mc.parent(twistLOCGRPA, _objA)
		mc.setAttr(twistLOCGRPA+'.v', 0)
		mc.poleVectorConstraint(twistLocA, handleA)		


		if child.endswith('endJNT') ==True:
			if _sleeve==0:
				secondChild=mc.listRelatives(child, c=1)[0]			
				if mc.objExists(secondChild.replace('JNT', 'module'))==True:
					attr=mc.getAttr(secondChild.replace('JNT', 'module')+'.ribbon')				
					if attr==0:
						mc.delete(twistTempCONSB)
						mc.parentConstraint(secondChild, jntBGRP, mo=1)						
						twistLocB = mc.spaceLocator(n= _objB.replace('JNT', 'twistLOC'))
						twistLOCGRPB=mc.createNode('transform', n=_objB.replace('JNT', 'tTwistLOCGRP') )						
						mc.parent(twistLocB, twistLOCGRPB)
						mc.delete(mc.parentConstraint(_objB, twistLOCGRPB))
						mc.parent(twistLOCGRPB, secondChild)
						mc.setAttr(twistLOCGRPB+'.v', 0)
						mc.poleVectorConstraint(twistLocB, handleB)

	else:
		if _sleeve==0:
			mc.delete(twistTempCONSB)
			mc.parentConstraint(mc.listRelatives(child, c=1)[0], jntBGRP, mo=1)

			twistLocB = mc.spaceLocator(n= _objA.replace('JNT', 'twistLOC'))
			twistLOCGRPB=mc.createNode('transform', n=_objA.replace('JNT', 'twistLOCGRP') )
			mc.parent(twistLocB, twistLOCGRPB)
			mc.delete(mc.parentConstraint(_objB, twistLOCGRPB))
			mc.parent(twistLOCGRPB, child)
			mc.setAttr(twistLOCGRPB+'.v', 0)
			mc.poleVectorConstraint(twistLocB, handleB)

	if _sleeve==1:		
		for i in ctrls:
			grp=mc.listRelatives(i, p=1)[0]
			mc.parent(i, i.replace('_01_sleeve_', '_01_'))
			mc.delete(grp)
		return miniJoints




if __name__ == '__main__':
	pass



