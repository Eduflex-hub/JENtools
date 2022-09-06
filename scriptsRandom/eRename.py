import maya.cmds as mc

def win():
	if mc.window('win', exists = True):
		mc.deleteUI('win')

	wind = mc.window('win', t="eRename", wh=(200, 55))	
	mc.columnLayout( adj=True )
	text=mc.textField('text')
	mc.button( label='Rename', c= rename )
	mc.showWindow(wind)

def rename(self):
	sel = mc.ls(sl=1)
	name=mc.textField('text', q=1, text=True)
	for x in sel:		
		index = sel.index(x)+01			
		meshType = 	mc.objectType( x)		
		shape=mc.listRelatives(x, shapes=1)
		print shape

		
		if meshType.startswith('transform') == True:
			mc.rename(x, name+'_0'+str(index)+'_MSH', ignoreShape=1)
			mc.rename(shape, name+'_0'+str(index)+'_MSHShape')

		if meshType.startswith('joint') == True:		
			mc.rename(x, name+'_0'+str(index)+'_JNT')

win()



