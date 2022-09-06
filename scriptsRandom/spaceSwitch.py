import maya.cmds as mc


class SpaceSwitch:
	def __init__(self):
		self.spaceControl = mc.ls(sl=1)[-1]
		self.selection = mc.ls(sl=1)
		self.parentControls = mc.ls(sl=1)
		del(self.parentControls[-1])

		self.doIt()

	def doIt(self):		
		qty = len(self.selection)
		mergedList = [''.join(self.selection[0 : qty-1])]
		
		simplifyList = mergedList[0].replace('_01_CTRL', ':')	
		simplifyList = simplifyList.replace('_01_ikCTRL', ':')		
		simplifyList = simplifyList.replace('_01_ikFootCTRL', ':')

		l = list(simplifyList)
		del(l[-1])
		attrName = ''.join(l)
		print attrName
		mc.addAttr(self.spaceControl, ln='parentSpace', at='enum', en=attrName, dv=0, k=1)

		parentGroups = self.createConstraintGroup(self.spaceControl)

		spaceConstraint = mc.parentConstraint(self.parentControls, parentGroups[1], mo=1)
		for s in self.parentControls:
			if s is not self.spaceControl:
					index = self.parentControls.index(s)
					remap=mc.createNode('remapValue', n=s + 'remapSpace')
					mc.setAttr(remap+'.value[2].value_FloatValue', 1)
					mc.setAttr(remap+'.value[2].value_Position', 0.5)
					mc.setAttr(remap+'.value[1].value_FloatValue', 0)
					mc.setAttr(remap+'.value[1].value_Position', 1)
					mc.setAttr(remap+'.value[2].value_Interp', 1)
					mc.connectAttr(self.spaceControl+'.parentSpace',remap+'.inputValue')
					mc.connectAttr(remap+'.outValue', spaceConstraint[0]+'.'+s+'W'+str(index))
					mc.setAttr(remap+'.inputMin',index-1)
					mc.setAttr(remap+'.inputMax',index+1)
				

				
				

		
				

	def createConstraintGroup(self, control):
		parent = mc.listRelatives(control, p=1)[0]
		ztr = mc.createNode('transform', n='{}_spaceZtr'.format(control), p=parent)
		offset = mc.createNode('transform', n='{}_spaceOffset'.format(control), p=ztr)
		mc.xform(ztr, t=(0, 0, 0), ro=(0, 0, 0), os=1)
		mc.parent(control, offset)

		return ztr, offset


SpaceSwitch()
