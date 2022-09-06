import maya.cmds as mc

sel = mc.ls(sl=1)[0]

coord = mc.xform(sel, q=1, t=1, ws=1)

suffix = 'JNT'
function = 'wristBACK'

base = mc.spaceLocator(n=sel.replace(
    suffix, '_' + function + '_TriggerBaseLOC'))[0]
target = mc.spaceLocator(n=sel.replace(
    suffix, '_' + function + '_TriggerTargetLOC'))[0]
pose = mc.spaceLocator(n=sel.replace(
    suffix, '_' + function + '_TriggerPoseLOC'))[0]
grp = mc.group(base, target, pose, n=sel.replace(
    suffix, '_' + function + '_TriggerGRP'))
baseGRP = mc.group(pose, n=sel.replace(suffix, '_' + function + '_poseGRP'))

mc.xform(grp, t=coord, ws=1)
mc.xform(target, t=(0, 0, 1), os=1)
mc.xform(pose, t=(0, -1, 0), os=1)

mc.parentConstraint(sel, baseGRP, mo=1)

baseDeComp = mc.createNode('decomposeMatrix', n=sel.replace(
    suffix, '_' + function + '_deCompBase'))
targetDeComp = mc.createNode('decomposeMatrix', n=sel.replace(
    suffix, '_' + function + '_deCompTarget'))
poseDeComp = mc.createNode('decomposeMatrix', n=sel.replace(
    suffix, '_' + function + '_deCompPose'))

mc.connectAttr(base + '.worldMatrix[0]', baseDeComp + '.inputMatrix')
mc.connectAttr(target + '.worldMatrix[0]', targetDeComp + '.inputMatrix')
mc.connectAttr(pose + '.worldMatrix[0]', poseDeComp + '.inputMatrix')

pma1 = mc.createNode('plusMinusAverage', n=sel.replace(
    suffix, '_' + function + '_PMA1'))
pma2 = mc.createNode('plusMinusAverage', n=sel.replace(
    suffix, '_' + function + '_PMA2'))
mc.setAttr(pma1 + '.operation', 2)
mc.setAttr(pma2 + '.operation', 2)

mc.connectAttr(targetDeComp + '.outputTranslate', pma1 + '.input3D[0]')
mc.connectAttr(baseDeComp + '.outputTranslate', pma1 + '.input3D[1]')

mc.connectAttr(baseDeComp + '.outputTranslate', pma2 + '.input3D[1]')
mc.connectAttr(poseDeComp + '.outputTranslate', pma2 + '.input3D[0]')

angle = mc.createNode('angleBetween', n=sel.replace(
    suffix, '_' + function + '_AB'))

mc.connectAttr(pma1 + '.output3D', angle + '.vector1')
mc.connectAttr(pma2 + '.output3D', angle + '.vector2')

md = mc.createNode('multiplyDivide', n=sel.replace(
    suffix, '_' + function + '_MD'))
multDouble = mc.createNode('multDoubleLinear', n=sel.replace(
    suffix, '_' + function + '_MULTDOUBLE'))

mc.setAttr(multDouble + '.input1', 90)
mc.setAttr(multDouble + '.input2', 1)

mc.setAttr(md + '.operation', 2)

mc.connectAttr(angle + '.angle', md + '.input1.input1X')
mc.connectAttr(multDouble + '.output', md + '.input2.input2X')

cond = mc.createNode('condition', n=sel.replace(
    suffix, '_' + function + '_COND'))

mc.connectAttr(md + '.output.outputX', cond + '.colorIfFalse.colorIfFalseR')
mc.connectAttr(md + '.output.outputX', cond + '.firstTerm')

mc.setAttr(cond + '.colorIfTrue.colorIfTrueR', 1)
mc.setAttr(cond + '.operation', 2)
mc.setAttr(cond + '.secondTerm', 1)

result = mc.createNode('plusMinusAverage', n=sel.replace(
    suffix, '_' + function + '_RESULT'))
mc.setAttr(result + '.input1D[0]', 1)
mc.setAttr(result + '.operation', 2)
mc.connectAttr(cond + '.outColor.outColorR', result + '.input1D[1]')

condInv = mc.createNode('condition', n=sel.replace(
    suffix, '_' + function + '_CONDinv'))

mc.setAttr(condInv + '.secondTerm', 1)
mc.setAttr(condInv + '.operation', 4)
mc.setAttr(condInv + '.colorIfTrue.colorIfTrueR', 1)

mc.connectAttr(md + '.output.outputX', condInv + '.firstTerm')
mc.connectAttr(md + '.output.outputX', condInv + '.colorIfFalse.colorIfFalseR')

pmaInv = mc.createNode('plusMinusAverage', n=sel.replace(
    suffix, '_' + function + '_PMAinv'))

mc.setAttr(pmaInv + '.operation', 2)
mc.setAttr(pmaInv + '.input1D[0]', 1.125)

mc.connectAttr(condInv + '.outColor.outColorR', pmaInv + '.input1D[1]')

mdInv = mc.createNode('multiplyDivide', n=sel.replace(
    suffix, '_' + function + '_MDinv'))
mc.setAttr(mdInv + '.input2.input2X', -1)
mc.connectAttr(pmaInv + '.output1D', mdInv + '.input1.input1X')

clampInv = mc.createNode('clamp', n=sel.replace(
    suffix, '_' + function + '_CLAMPinv'))
mc.setAttr(clampInv + '.minR', 0)
mc.setAttr(clampInv + '.maxR', 1)

mc.connectAttr(mdInv + '.output.outputX', clampInv + '.input.inputR')
