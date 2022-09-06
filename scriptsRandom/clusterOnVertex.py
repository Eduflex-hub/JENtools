import maya.cmds as mc


def clusters(_controls=0):
    sel = mc.ls(sl=1, fl=1)
    name = sel[0].split('.')
    name = name[0]

    for x in sel:
        mc.select(x)
        index = sel.index(x)
        clu = mc.cluster(n=name.replace('CRV', str(index) + 'CLU'))
        if _controls == 1:
            cir = mc.circle(n=name.replace('CRV', str(index) + 'CTRL'), r=10, nr=(0, 0, 1))
            grp = mc.createNode('transform', n=name.replace('CRV', str(index) + 'ZTR'))
            mc.parent(cir[0], grp)
            coord = mc.xform(x, q=1, t=1, ws=1)
            mc.xform(grp, t=coord, ws=1)
            mc.connectAttr(cir[0] + '.t', clu[0] + 'Handle.t')


clusters(_controls=1)
