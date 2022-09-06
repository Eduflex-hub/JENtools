import maya.cmds as mc
from math import pow,sqrt
import pymel.core as pm

sel=mc.ls(sl=1)
def getDistance(_objA, _objB):
	gObjA = mc.xform(_objA, q=True, t=True, ws=True)
	gObjB = mc.xform(_objB, q=True, t=True, ws=True)
	
	return sqrt(pow(gObjA[0]-gObjB[0],2)+pow(gObjA[1]-gObjB[1],2)+pow(gObjA[2]-gObjB[2],2))

def simpleRibbon (_objA, _objB, _divisions, _drivers, _name):
	#NURBS GEO__________________________________________________________
	start=_objA
	end=_objB

	distance=getDistance(start, end)
	

	ribbonGRP=mc.createNode('transform', n=_name.replace('NURBS', 'ribbonGRP'))
	nurbs=mc.nurbsPlane(ax=(0,1,0), w=distance,lr=0.1, d=3, u=4, v=1, ch=0, n=_name)
	
	mc.rebuildSurface( nurbs, ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kc=0, su=_drivers, du=3, sv=1, dv=1, tol=0.01, fr=0, dir=2)
	mc.parent(nurbs, ribbonGRP)
	folGRP=mc.createNode('transform', n=_name.replace('_NURBS', '_follicleGRP'), p=ribbonGRP)
	cGRP=mc.createNode('transform', n=_name.replace('NURBS','ControlsGRP'), p=ribbonGRP)

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

		mc.setAttr(folShape+'.parameterU', uValue)
		mc.setAttr(folShape+'.parameterV', 0.5)
		mc.parent(fol, folGRP)
		
		minGRP=mc.createNode('transform', n=_name.replace('NURBS','JNT'+str(index)+'GRP'), p=fol)
		#mc.scaleConstraint('C_root_01_CTRL',minGRP, mo=0 )
		miniJoint=mc.joint(n=_name.replace('NURBS','rib'+str(index)+'JNT'), rad=0.1)
		mc.connectAttr(_objA+'.scale', miniJoint+'.scale')
		mc.refresh()
	#driver system__________________________________________________________
	drvJoints=[]
	drvGrp=[]
	drvZTR=[]
	grpCTRL=[]
	ctrls=[]	
	aims=[]
	locsgroup=[]
	for x in range(0,_drivers+1):
		index=range(0,_drivers+1).index(x)
		drvJntGRP=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'drvJntGRP'), p=ribbonGRP)
		drvZTRGRP=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'drvJntZTR'), p=drvJntGRP)
		drvJNT=mc.joint(n=_name.replace('NURBS',str(index)+'drvJNT'), rad=0.3)		
		
		drvJoints.append(drvJNT)	

		grpCir=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'ribbonCtrlGRP'))
		cir=mc.circle(n=_name.replace('NURBS',str(index)+'ribbonCTRL'), r=3, nr=(1,0,0))[0]
		mc.parent(cir, grpCir)	

		locsGRP=mc.createNode('transform', n=_name.replace('NURBS',str(index)+'locsGRP'), p=cir)		


		form=float(distance)/(float(_drivers))
		dValue= (form*index)
		print dValue
					
		mc.xform(drvJntGRP, t= (dValue-(distance/2.0),0, 0), ws=1)
		mc.xform(grpCir, t= (dValue-(distance/2.0),0, 0), ws=1)
		mc.parent(grpCir, cGRP)
		mc.parent(drvJntGRP, cir)	


	#Skinning_______________________________________________________________
	mc.select(drvJoints)
	mc.select(nurbs, add=1)
	mc.skinCluster(n=_name.replace('NURBS', 'NURBSskinCluster'),dr=2, par=0.5)

	

	mc.delete(mc.pointConstraint(_objA, _objB, cGRP, mo=0))
	


	


simpleRibbon(sel[0], sel[1], 8, 4, sel[0].replace('LOC', 'NURBS'))




	





