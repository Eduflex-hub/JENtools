import maya.cmds as mc

def separateMesh():
	sel = mc.ls(sl=1)
	mc.ConvertSelectionToVertices()
	selObj = sel[0].split('.')[0]
	mc.polySplitEdge(sel, operation=1)
	objs = mc.polySeparate(selObj)

	for o in objs[0:-1]:
		mc.polyCloseBorder(o)
		mc.xform(o, cp=1)
		mc.polyColorPerVertex(o, cdo=1)

	for o in objs:
		try:
			mc.parent(o, 'loMesh_group')
		except: 0

	mc.select(mc.listRelatives('loMesh_group', c=1), r=1)
	mc.delete(ch=1)

	mc.select(d=1)

def mirrorSelected():
	sel = mc.ls(sl=1)
	tNode = mc.createNode('transform')
	dups = []
	for e in sel:
		if e[0] == 'L':
			mirName = 'R'+e[1:]
		elif e[0] == 'R':
			mirName = 'L'+e[1:]
		else:
			mirName = e+'Mirror'

		dup = mc.duplicate(e, n=mirName)[0]
		mc.select(dup)
		dups.append(dup)
		mc.parent(dup, tNode)
		#joint = mc.getAttr(dup+'.joint')
		#if joint[0] == 'L':
			#joint = joint.replace('L_', 'R_')
		#elif joint[0] == 'R':
			#joint = joint.replace('R_', 'L_')

		#mc.setAttr(dup+'.joint', joint, type='string')

	mc.setAttr(tNode+'.sx', -1)

	for e in dups:
		mc.parent(e, 'loMesh_group')
		mc.makeIdentity(e, apply=1)
		mc.select(e, r=1)
		mc.polySetToFaceNormal()
		mc.polyAverageNormal()

		mc.delete(tNode)

#separateMesh()
mirrorSelected()