import maya.cmds as mc

sel = mc.ls('*page*G*CTRL')

for x in sel:
	y=x.replace('CTRL', 'CLU')
	mc.connectAttr(x+'.s', y+'.s')
	mc.connectAttr(x+'.t', y+'.t')
	mc.connectAttr(x+'.r', y+'.r')
