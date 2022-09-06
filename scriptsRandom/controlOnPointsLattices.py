import maya.cmds as mc

sel=mc.ls(sl=1, fl=1)
name=sel[0].split('.')
name=name[0]
print name

for x in sel:
	mc.select(x)
	index=sel.index(x)

	clu=mc.cluster(n=name.replace('lattice',str(index)+'CLU'))
	cir=mc.circle(n=name.replace('lattice',str(index)+'CTRL'), r=1, nr=(0,1,0))
	grp=mc.createNode('transform', n=name.replace('lattice',str(index)+'ZTR'))
	mc.parent(cir[0], grp)
	coord=mc.xform(x, q=1, t=1, ws=1)
	mc.xform(grp, t=coord, ws=1)

	mc.connectAttr(cir[0]+'.t', clu[0]+'Handle.t')
