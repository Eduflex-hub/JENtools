import maya.cmds as mc

sel = mc.ls('*Key*MSH')

for x in sel:
	vertex=x+'.vtx[19]'
	pos=mc.xform(vertex, q=1, t=1, ws=1)
	ztr=mc.createNode('transform', n=x.replace('_MSH', 'ZTR'))
	cir=mc.circle(n=x.replace('_MSH', 'CTRL'), nr=(0,1,0), c=(0,1,0), r=0.5)
	mc.transformLimits(ty=(-0.14,0), ety=(True, True))
	mc.parent(cir, ztr)
	mc.xform(ztr, t=pos, ws=1)
	mc.select(cir)
	jnt=mc.joint(n=x.replace('_MSH', 'JNT'))
	mc.xform(jnt, t=(0,0,0), os=1)
	mc.select(x)
	mc.select(jnt, add=1)
	mc.skinCluster()
	
	
