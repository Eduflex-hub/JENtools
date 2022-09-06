import maya.cmds as mc
import random 
import maya.mel as mel
sel=mc.ls(sl=1)

for x in sel:
	red = random.uniform(0, 0.5)
	green = random.uniform(0, 0.5)
	blue = random.uniform(0, 0.5)
	mc.polyColorPerVertex(x, rgb=(red,green,blue), a=1, cdo=1)
	mc.polyOptions(cs=1, cm='None')
'''
for x in sel:
	mc.polyOptions(cs=1, cm='ambientDiffuse')
'''