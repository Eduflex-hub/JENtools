import maya.cmds as mc
from math import pow, sqrt
import pymel.core as pm

sel = mc.ls(sl=1)


def getDistance(_objA, _objB):
    gObjA = mc.xform(_objA, q=True, t=True, ws=True)
    gObjB = mc.xform(_objB, q=True, t=True, ws=True)

    return sqrt(pow(gObjA[0] - gObjB[0], 2) + pow(gObjA[1] - gObjB[1], 2) + pow(gObjA[2] - gObjB[2], 2))


def simpleRibbon(_objA, _objB, _divisions, _drivers, _name):
    # NURBS GEO__________________________________________________________
    start = _objA
    end = _objB

    distance = getDistance(start, end)

    ribbonGRP = mc.createNode(
        'transform', n=_name.replace('NURBS', 'ribbonGRP'))
    nurbs = mc.nurbsPlane(ax=(0, 0, 1), w=distance,
                          lr=0.1, d=3, u=4, v=1, ch=0, n=_name)
    mc.xform(nurbs, ro=(0, 0, 90), ws=1)
    mc.makeIdentity(nurbs, a=1)

    mc.rebuildSurface(nurbs, ch=0, rpo=1, rt=0, end=1, kr=0,
                      kcp=0, kc=0, su=8, du=3, sv=1, dv=1, tol=0.01, fr=0, dir=2)
    mc.parent(nurbs, ribbonGRP)
    folGRP = mc.createNode('transform', n=_name.replace(
        '_NURBS', '_follicleGRP'), p=ribbonGRP)
    cGRP = mc.createNode('transform', n=_name.replace(
        'NURBS', 'ControlsGRP'), p=ribbonGRP)
    miniJoints = []
    for i in range(0, _divisions):
        # folicles_________________________________________________________
        index = range(0, _divisions).index(i)

        fol = mc.createNode('transform', n=_name.replace(
            'NURBS', str(index) + 'follicle'), ss=True)
        folShape = mc.createNode('follicle', n=_name.replace(
            'NURBS', str(index) + 'follicleShape'), p=fol, ss=True)

        mc.connectAttr(nurbs[0] + 'Shape.local', folShape + '.inputSurface')
        mc.connectAttr(nurbs[0] + 'Shape.worldMatrix[0]',
                       folShape + '.inputWorldMatrix')
        mc.connectAttr(folShape + '.outRotate', fol + '.rotate')
        mc.connectAttr(folShape + '.outTranslate', fol + '.translate')
        mc.setAttr(fol + '.inheritsTransform', 0)

        form = 1 / (float(_divisions) * 2)
        uValue = ((form + (form * index)) * 2) - form

        mc.setAttr(folShape + '.parameterU', uValue)
        mc.setAttr(folShape + '.parameterV', 0.5)
        mc.parent(fol, folGRP)

        minGRP = mc.createNode('transform', n=_name.replace(
            'NURBS', 'JNT' + str(index) + 'GRP'), p=fol)
        #mc.scaleConstraint('C_root_01_CTRL',minGRP, mo=0 )
        miniJoint = mc.joint(n=_name.replace(
            'NURBS', 'rib' + str(index) + 'JNT'), rad=1)
        miniJoints.append(miniJoint)
        mc.connectAttr(_objA + '.scale', miniJoint + '.scale')
        mc.refresh()
    # driver system__________________________________________________________
    drvJoints = []
    drvGrp = []
    drvZTR = []
    grpCTRL = []
    ctrls = []
    aims = []
    locsgroup = []
    for x in range(0, _drivers + 1):
        index = range(0, _drivers + 1).index(x)
        drvJntGRP = mc.createNode('transform', n=_name.replace(
            'NURBS', str(index) + 'drvJntGRP'), p=ribbonGRP)
        drvZTRGRP = mc.createNode('transform', n=_name.replace(
            'NURBS', str(index) + 'drvJntZTR'), p=drvJntGRP)
        drvJNT = mc.joint(n=_name.replace(
            'NURBS', str(index) + 'drvJNT'), rad=0.3)

        drvJoints.append(drvJNT)

        grpCir = mc.createNode('transform', n=_name.replace(
            'NURBS', str(index) + 'ribbonCtrlGRP'))
        cir = mc.circle(n=_name.replace('NURBS', str(
            index) + 'ribbonCTRL'), r=5, nr=(0, 1, 0))[0]
        mc.parent(cir, grpCir)

        locsGRP = mc.createNode('transform', n=_name.replace(
            'NURBS', str(index) + 'locsGRP'), p=cir)

        form = float(distance) / (float(_drivers))
        dValue = (form * index)

        mc.xform(drvJntGRP, t=(0, dValue - (distance / 2.0), 0), ws=1)
        mc.xform(grpCir, t=(0, dValue - (distance / 2.0), 0), ws=1)
        mc.parent(grpCir, cGRP)
        mc.parent(drvJntGRP, cir)

    # Skinning_______________________________________________________________
    mc.select(drvJoints)
    mc.select(nurbs, add=1)
    skinCluster = mc.skinCluster(n=_name.replace(
        'NURBS', 'NURBSskinCluster'), dr=2, par=0.5)[0]

    mc.skinPercent(skinCluster, nurbs[0] + '.cv[10] [0:10]',
                   tv=[(drvJoints[0], 0), (drvJoints[1], 0), (drvJoints[2], 1)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[9] [0:1]', tv=[
                   (drvJoints[0], 0), (drvJoints[1], 0.08), (drvJoints[2], 0.92)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[8] [0:1]', tv=[
                   (drvJoints[0], 0), (drvJoints[1], 0.25), (drvJoints[2], 0.75)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[7] [0:1]', tv=[
                   (drvJoints[0], 0), (drvJoints[1], 0.5), (drvJoints[2], 0.5)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[6] [0:1]', tv=[
                   (drvJoints[0], 0), (drvJoints[1], 0.75), (drvJoints[2], 0.25)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[5] [0:1]', tv=[
                   (drvJoints[0], 0.05), (drvJoints[1], 0.9), (drvJoints[2], 0.05)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[4] [0:1]', tv=[
                   (drvJoints[0], 0.25), (drvJoints[1], 0.75), (drvJoints[2], 0)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[3] [0:1]', tv=[
                   (drvJoints[0], 0.5), (drvJoints[1], 0.5), (drvJoints[2], 0)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[2] [0:1]', tv=[
                   (drvJoints[0], 0.75), (drvJoints[1], 0.25), (drvJoints[2], 0)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[1] [0:1]', tv=[
                   (drvJoints[0], 0.92), (drvJoints[1], 0.08), (drvJoints[2], 0)])
    mc.skinPercent(skinCluster, nurbs[0] + '.cv[0] [0:1]',
                   tv=[(drvJoints[0], 1), (drvJoints[1], 0), (drvJoints[2], 0)])

    mc.delete(mc.pointConstraint(_objA, _objB, cGRP, mo=0))

    curveCoords = []
    for j in drvJoints:
        index = drvJoints.index(j)
        jointCoord = mc.xform(j, q=1, t=1, ws=1)
        curveCoords.append(jointCoord)

    curve = mc.curve(ep=curveCoords, d=1)
    curve = mc.rename(curve, _name.replace('NURBS', 'lengthCRV'))
    curveVertex = mc.ls(curve + '.cv[*]', fl=1)
    curveVertexCount = float(len(curveVertex))

    for x in curveVertex:
        index = curveVertex.index(x)
        mc.select(x)
        clu = mc.cluster(n=_name.replace(
            'NURBS', '_' + str(index) + 'lengthCLU'))
        print clu
        control = _name.replace('NURBS', str(index) + 'ribbonCTRL')
        mc.setAttr(clu[0] + '.relative', 0)
        mc.parent(clu[1], control)

    ci = mc.createNode('curveInfo', n=_name.replace('NURBS', 'CInfo'))
    mc.connectAttr(curve + 'Shape.worldSpace[0]', ci + '.inputCurve', f=1)

    mdStretch = mc.createNode(
        'multiplyDivide', n=curve.replace('lengthCRV', '_stretchMD'))
    mc.connectAttr(ci + '.arcLength', mdStretch + '.input1X')
    mc.setAttr(mdStretch + '.operation', 2)
    attr = mc.getAttr(mdStretch + '.input1X')
    mc.setAttr(mdStretch + '.input2X', attr)

    cond = mc.createNode('condition', n=curve.replace(
        'lengthCRV', '_stretchCOND'))
    mc.setAttr(cond + '.operation', 2)
    mc.setAttr(cond + '.secondTerm', 1)
    mc.connectAttr(mdStretch + '.outputX', cond + '.firstTerm')
    mc.connectAttr(mdStretch + '.outputX', cond + '.colorIfTrueR')

    mdSquash = mc.createNode(
        'multiplyDivide', n=curve.replace('lengthCRV', '_squashMD'))
    mc.setAttr(mdSquash + '.operation', 3)
    mc.connectAttr(mdStretch + '.outputX', mdSquash + '.input1X')
    mc.setAttr(mdSquash + '.input2X', -1)

    squashCond = mc.createNode(
        'condition', n=curve.replace('lengthCRV', '_squashCOND'))
    mc.setAttr(squashCond + '.operation', 1)
    mc.setAttr(squashCond + '.secondTerm', 1)
    mc.connectAttr(mdSquash + '.outputX', squashCond + '.firstTerm')
    mc.connectAttr(mdSquash + '.outputX', squashCond + '.colorIfTrueR')

    for x in miniJoints:
        #mc.connectAttr(cond+'.outColorR', x+'.scaleX')
        mc.connectAttr(squashCond + '.outColorR', x + '.scaleY')
        mc.connectAttr(squashCond + '.outColorR', x + '.scaleZ')


simpleRibbon(sel[0], sel[1], 3, 2, sel[0].replace('LOC', 'NURBS'))
