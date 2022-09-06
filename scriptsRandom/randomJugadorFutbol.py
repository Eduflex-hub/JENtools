import maya.cmds as mc 
import random 

#Targets:

socket = mc.ls('L_socket_01_JNT','R_socket_01_JNT' )
ear = mc.ls('L_ear_01_localJNT', 'R_ear_01_localJNT')

nose = mc.ls('C_noseBase_01_localJNT')
head = mc.ls('C_head_01_JNT')
jaw = mc.ls('C_jaw_01_JNT')

randomNodes=[]
randomGroups=[]


#for Globals:
######################################
#position:

xPos = random.uniform(-0.2, 0.1)
yPos = random.uniform(-0.2, 0.155)
zPos = random.uniform(-0.1, 0.2)

#Rotate:

xRotate = random.uniform(-0.4, 0.5)
yRotate = random.uniform(-0.4, 0.5)
zRotate = random.uniform(-0.4, 0.5)

#Scale:

xScale = random.uniform(-0.1, 0.1)
yScale = random.uniform(-0.1, 0.1)
zScale = random.uniform(-0.1, 0.1)

#####################################
for x in socket:

	if mc.objExists(x.replace('_JNT', '_RandomPMA'))==False:
		CTRL=x.replace('_JNT', '_CTRL')
		randPMA=mc.createNode('plusMinusAverage', n=x.replace('_JNT', '_RandomPMA'))
		mc.connectAttr(CTRL+'.scale', randPMA+'.input3D[0]', f=1)
		mc.connectAttr(randPMA+'.output3D', x+'.scale', f=1)
	else:
		randPMA=x.replace('_JNT', '_RandomPMA')
		CTRL=x.replace('_JNT', '_CTRL')

	mc.setAttr(randPMA+'.input3D[1].input3Dx', xScale)
	mc.setAttr(randPMA+'.input3D[1].input3Dy', xScale)
	mc.setAttr(randPMA+'.input3D[1].input3Dz', xScale)

	if mc.objExists(x.replace('_JNT', '_randGRP'))==False:
		ztr=x.replace('_JNT', '_ZTR')
		randGRP=mc.createNode('transform', n=x.replace('_JNT', '_randGRP'))
		mc.delete(mc.parentConstraint(ztr, randGRP, mo=0))
		mc.parent(randGRP, ztr)
		mc.parent(CTRL, randGRP)
	else:
		randGRP=x.replace('_JNT', '_randGRP')
	if x.startswith('L_')==True:
		mc.setAttr(randGRP+'.tx', xPos)
		mc.setAttr(randGRP+'.ty', yPos)
		mc.setAttr(randGRP+'.tz', zPos)
	else:
		mc.setAttr(randGRP+'.tx', xPos)
		mc.setAttr(randGRP+'.ty', yPos*-1)
		mc.setAttr(randGRP+'.tz', zPos)

	randomNodes.append(randPMA)
	randomGroups.append(randGRP)

#Ears:
######################################
#position:

xPos = random.uniform(-0.2, 0.4)
yPos = random.uniform(-0.2, 0.35)
zPos = random.uniform(-0.1, 0.2)

#Rotate:

xRotate = random.uniform(-0.4, 1)
yRotate = random.uniform(-0.2, 1)
zRotate = random.uniform(-0.4, 1)

#Scale:

xScale = random.uniform(-0.1, 0.1)
yScale = random.uniform(-0.1, 0.1)
zScale = random.uniform(-0.1, 0.1)

#####################################
for x in ear:
	if mc.objExists(x.replace('JNT', 'RandomPosPMA'))==False:
		CTRL=x.replace('JNT', 'CTRL')
		randPosPMA=mc.createNode('plusMinusAverage', n=x.replace('JNT', 'RandomPosPMA'))
		mc.connectAttr(CTRL+'.translate', randPosPMA+'.input3D[0]', f=1)
		mc.connectAttr(randPosPMA+'.output3D', x+'.translate', f=1)

		randRotPMA=mc.createNode('plusMinusAverage', n=x.replace('JNT', 'RandomRotPMA'))
		mc.connectAttr(CTRL+'.rotate', randRotPMA+'.input3D[0]', f=1)
		mc.connectAttr(randRotPMA+'.output3D', x+'.rotate', f=1)

		randScalePMA=mc.createNode('plusMinusAverage', n=x.replace('JNT', 'RandomScalePMA'))
		mc.connectAttr(CTRL+'.scale', randScalePMA+'.input3D[0]', f=1)
		mc.connectAttr(randScalePMA+'.output3D', x+'.scale', f=1)
	else:
		randPosPMA=x.replace('JNT', 'RandomPosPMA')
		randRotPMA=x.replace('JNT', 'RandomRotPMA')
		randScalePMA=x.replace('JNT', 'RandomScalePMA')
		CTRL=x.replace('JNT', 'CTRL')

	if x.startswith('L_')==True:
		mc.setAttr(randPosPMA+'.input3D[1].input3Dx', xPos)
		mc.setAttr(randPosPMA+'.input3D[1].input3Dy', yPos)
		mc.setAttr(randPosPMA+'.input3D[1].input3Dz', zPos)

		mc.setAttr(randRotPMA+'.input3D[1].input3Dx', xRotate)
		mc.setAttr(randRotPMA+'.input3D[1].input3Dy', yRotate)
		mc.setAttr(randRotPMA+'.input3D[1].input3Dz', zRotate)

		mc.setAttr(randScalePMA+'.input3D[1].input3Dx', xScale)
		mc.setAttr(randScalePMA+'.input3D[1].input3Dy', xScale)
		mc.setAttr(randScalePMA+'.input3D[1].input3Dz', xScale)

	else:
		mc.setAttr(randPosPMA+'.input3D[1].input3Dx', xPos*-1)
		mc.setAttr(randPosPMA+'.input3D[1].input3Dy', yPos*-1)
		mc.setAttr(randPosPMA+'.input3D[1].input3Dz', zPos*-1)

		mc.setAttr(randRotPMA+'.input3D[1].input3Dx', xRotate)
		mc.setAttr(randRotPMA+'.input3D[1].input3Dy', yRotate)
		mc.setAttr(randRotPMA+'.input3D[1].input3Dz', zRotate)

		mc.setAttr(randScalePMA+'.input3D[1].input3Dx', xScale)
		mc.setAttr(randScalePMA+'.input3D[1].input3Dy', xScale)
		mc.setAttr(randScalePMA+'.input3D[1].input3Dz', xScale)

	randomNodes.append(randPosPMA)
	randomNodes.append(randRotPMA)
	randomNodes.append(randScalePMA)
	
#Nose:
######################################
#position:

xPos = random.uniform(-0.25, 0.4)
yPos = random.uniform(-0.1, 0.15)
zPos = random.uniform(-0.15, 0.2)

#Rotate:

xRotate = random.uniform(-8, 10)
yRotate = random.uniform(-1, 1)
zRotate = random.uniform(-0.5, 0.5)

#Scale:

xScale = random.uniform(-0.05, 0.05)
yScale = random.uniform(-0.05, 0.05)
zScale = random.uniform(-0.05, 0.05)

#####################################
for x in nose:
	if mc.objExists(x.replace('JNT', 'RandomPosPMA'))==False:
		CTRL=x.replace('JNT', 'CTRL')
		randPosPMA=mc.createNode('plusMinusAverage', n=x.replace('JNT', 'RandomPosPMA'))
		mc.connectAttr(CTRL+'.translate', randPosPMA+'.input3D[0]', f=1)
		mc.connectAttr(randPosPMA+'.output3D', x+'.translate', f=1)

		randRotPMA=mc.createNode('plusMinusAverage', n=x.replace('JNT', 'RandomRotPMA'))
		mc.connectAttr(CTRL+'.rotate', randRotPMA+'.input3D[0]', f=1)
		mc.connectAttr(randRotPMA+'.output3D', x+'.rotate', f=1)

		randScalePMA=mc.createNode('plusMinusAverage', n=x.replace('JNT', 'RandomScalePMA'))
		mc.connectAttr(CTRL+'.scale', randScalePMA+'.input3D[0]', f=1)
		mc.connectAttr(randScalePMA+'.output3D', x+'.scale', f=1)
	else:
		randPosPMA=x.replace('JNT', 'RandomPosPMA')
		randRotPMA=x.replace('JNT', 'RandomRotPMA')
		randScalePMA=x.replace('JNT', 'RandomScalePMA')
		CTRL=x.replace('JNT', 'CTRL')		
	

	mc.setAttr(randPosPMA+'.input3D[1].input3Dy', yPos)
	mc.setAttr(randPosPMA+'.input3D[1].input3Dz', zPos)

	mc.setAttr(randRotPMA+'.input3D[1].input3Dx', xRotate)
	mc.setAttr(randRotPMA+'.input3D[1].input3Dy', yRotate)
	mc.setAttr(randRotPMA+'.input3D[1].input3Dz', zRotate)

	mc.setAttr(randScalePMA+'.input3D[1].input3Dx', xScale)
	mc.setAttr(randScalePMA+'.input3D[1].input3Dy', xScale)
	mc.setAttr(randScalePMA+'.input3D[1].input3Dz', xScale)

	randomNodes.append(randPosPMA)
	randomNodes.append(randRotPMA)
	randomNodes.append(randScalePMA)
#jaw:
######################################

#Scale:

xScale = random.uniform(-0.01, 0.01)
yScale = random.uniform(-0.01, 0.01)
zScale = random.uniform(-0.01, 0.01)

#####################################
for x in jaw:

	if mc.objExists(x.replace('_JNT', '_RandomPMA'))==False:
		CTRL=x.replace('_JNT', '_CTRL')
		randPMA=mc.createNode('plusMinusAverage', n=x.replace('_JNT', '_RandomPMA'))
		mc.connectAttr(CTRL+'.scale', randPMA+'.input3D[0]', f=1)
		mc.connectAttr(randPMA+'.output3D', x+'.scale', f=1)
	else:
		randPMA=x.replace('_JNT', '_RandomPMA')
		CTRL=x.replace('_JNT', '_CTRL')

	mc.setAttr(randPMA+'.input3D[1].input3Dx', xScale)
	mc.setAttr(randPMA+'.input3D[1].input3Dy', yScale)
	mc.setAttr(randPMA+'.input3D[1].input3Dz', zScale)

	randomNodes.append(randPMA)
	
#head:
######################################



xScale = random.uniform(0, 0)
#####################################
for x in head:

	if mc.objExists(x.replace('_JNT', '_RandomPMA'))==False:
		CTRL=x.replace('_JNT', '_CTRL')
		randPMA=mc.createNode('plusMinusAverage', n=x.replace('_JNT', '_RandomPMA'))
		mc.connectAttr(CTRL+'.size', randPMA+'.input3D[0].input3Dx', f=1)
		mc.connectAttr(CTRL+'.size', randPMA+'.input3D[0].input3Dy', f=1)
		mc.connectAttr(CTRL+'.size', randPMA+'.input3D[0].input3Dz', f=1)
		mc.connectAttr(randPMA+'.output3D', CTRL+'.scale', f=1)
		mc.connectAttr(CTRL+'.scale', x+'.scale', f=1)
	else:
		randPMA=x.replace('_JNT', '_RandomPMA')
		CTRL=x.replace('_JNT', '_CTRL')

	mc.setAttr(randPMA+'.input3D[1].input3Dx', xScale)
	mc.setAttr(randPMA+'.input3D[1].input3Dy', xScale)
	mc.setAttr(randPMA+'.input3D[1].input3Dz', xScale)

	randomNodes.append(randPMA)
	
print randomNodes
print randomGroups


def connectVariant():

	for i in randomNodes:
		variantAttr='C_root_01_CTRL.Variant'
		print i	

		mc.setDrivenKeyframe(i + ".input3D[1].input3Dx", cd=variantAttr)
		mc.setDrivenKeyframe(i + ".input3D[1].input3Dy", cd=variantAttr)
		mc.setDrivenKeyframe(i + ".input3D[1].input3Dz", cd=variantAttr)

	for q in randomGroups:
		variantAttr='C_root_01_CTRL.Variant'
		print q


		mc.setDrivenKeyframe(q + ".translateX", cd=variantAttr)
		mc.setDrivenKeyframe(q + ".translateY", cd=variantAttr)
		mc.setDrivenKeyframe(q + ".translateZ", cd=variantAttr)


def resetToZero():

	for i in randomNodes:
		variantAttr='C_root_01_CTRL.Variant'
		print i	

		mc.setAttr(i + ".input3D[1].input3Dx", 0)
		mc.setAttr(i + ".input3D[1].input3Dy", 0)
		mc.setAttr(i + ".input3D[1].input3Dz", 0)		

	for q in randomGroups:
		variantAttr='C_root_01_CTRL.Variant'
		print q
		mc.setAttr(q + ".translateX", 0)
		mc.setAttr(q + ".translateY", 0)
		mc.setAttr(q + ".translateZ", 0)
		

#connectVariant()
#resetToZero()
		



	





