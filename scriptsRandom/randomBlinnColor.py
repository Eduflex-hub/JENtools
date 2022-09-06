import maya.cmds as mc
import random 
import maya.mel as mel

#sel=mc.ls('ASSET*:*MSH')
sel=mc.ls('*MSH')
print sel

for x in sel:
	print x 
	#mel.eval('polyNormalPerVertex -ufn true;')
	#mc.polyNormalPerVertex(x, ufn=1)
	hue = random.uniform(0.0, 1.0)
	saturation = random.uniform(0.0, 1.0)
	value = random.uniform(0.0, 1.0)
	if mc.objExists(x.replace('MSH','FIXCOLOR'))==False:
		blin=mc.createNode('blinn', n=x.replace('MSH', '_FIXCOLOR'))
		mc.setAttr(blin+'.color', hue, saturation, value, type = 'double3')
		mc.select(x)
		mc.hyperShade( assign=blin)
		mc.polyOptions(cs=0)
		
	else:
		mc.setAttr(x.replace('MSH', 'FIXCOLOR')+'.color', hue, saturation,value, type = 'double3')
		mc.select(x)
		mc.hyperShade(assign=x.replace('MSH', 'FIXCOLOR'))
		mc.polyOptions(cs=0)




		