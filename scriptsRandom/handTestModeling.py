import maya.cmds as mc
import maya.mel as mel

sel = mc.ls(sl=1)
if sel[0].startswith('L_') == True:
    switchCtrl = 'L_handSwitch_01_CTRL'
    side = 'L_'

elif sel[0].startswith('R_') == True:
    switchCtrl = 'R_handSwitch_01_CTRL'
    side = 'R_'


if mc.objExists('L_handSwitch_01_CTRL.____') is True:
    pass
else:
    mc.addAttr(switchCtrl, ln='____', at='enum', en='handPoses:', k=1)
    mc.addAttr(switchCtrl, ln='spread', at='float', min=0, max=1, k=1)
    mc.addAttr(switchCtrl, ln='fist', at='float', min=0, max=1, k=1)
    mc.addAttr(switchCtrl, ln='metaArc', at='float', min=0, max=1, k=1)

maingrp = mc.createNode('transform', n=x.replace('JNT', 'maingrp'))

for x in sel:
    if x.endswith('endJNT') == False:        
        index = sel.index(x)
        group = mc.createNode('transform', n=x.replace('JNT', 'GRP'))
        CONS = mc.createNode('transform', n=x.replace('JNT', 'CONS'), p=group)
        ZTR = mc.createNode('transform', n=x.replace('JNT', 'ZTR'), p=CONS)
        CTRL = mel.eval('curve -d 1 -p -0.8 0.8 0.8 -p 0.8 0.8 0.8 -p 0.8 -0.8 0.8 -p -0.8 -0.8 0.8 -p -0.8 0.8 0.8 -p -0.8 0.8 -0.8 -p 0.8 0.8 -0.8 -p 0.8 0.8 0.8 -p 0.8 -0.8 0.8 -p 0.8 -0.8 -0.8 -p -0.8 -0.8 -0.8 -p -0.8 -0.8 0.8 -p -0.8 -0.8 -0.8 -p -0.8 0.8 -0.8 -p 0.8 0.8 -0.8 -p 0.8 -0.8 -0.8 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')
        CTRL = mc.rename(CTRL, x.replace('JNT', 'CTRL'))
        mc.parent(CTRL, ZTR)

        parentJoint = mc.listRelatives(x, p=1, typ='joint')
        childJoint = mc.listRelatives(x, c=1, typ='joint')

        mc.delete(mc.parentConstraint(x, group, mo=0))

        mc.select(CTRL + '.cv[3:5]')
        mc.select(CTRL + '.cv[10:13]', add=1)
        mc.select(CTRL + '.cv[0]', add=1)
        clu1 = mc.cluster()

        mc.select(CTRL + '.cv[1:2]')
        mc.select(CTRL + '.cv[6:9]', add=1)
        mc.select(CTRL + '.cv[14:15]', add=1)
        clu2 = mc.cluster()
        mc.pointConstraint(x, clu1)
        mc.pointConstraint(childJoint, clu2)
        mc.delete(CTRL, ch=1)
        mc.delete(clu1[1], clu2[1])

        mc.parentConstraint(CTRL, x, mo=1)
        mc.connectAttr(CTRL + '.s', x + '.s')
        mc.parent(group, maingrp)
        if index > 0:
            mc.parentConstraint(parentJoint[0].replace('JNT', 'CTRL'), group, mo=1)


mc.setDrivenKeyframe(side + "fingerIndex_01_ZTR.rotateX", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerIndex_01_ZTR.rotateY", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerIndex_01_ZTR.rotateZ", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerIndex_01_ZTR.rotateX", cd=switchCtrl + ".metaArc", dv=1, v=5.654)
mc.setDrivenKeyframe(side + "fingerIndex_01_ZTR.rotateY", cd=switchCtrl + ".metaArc", dv=1, v=2.88)
mc.setDrivenKeyframe(side + "fingerIndex_01_ZTR.rotateZ", cd=switchCtrl + ".metaArc", dv=1, v=-2.453)

mc.setDrivenKeyframe(side + "fingerMiddle_01_ZTR.rotateX", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerMiddle_01_ZTR.rotateY", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerMiddle_01_ZTR.rotateZ", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerMiddle_01_ZTR.rotateX", cd=switchCtrl + ".metaArc", dv=1, v=4.154)
mc.setDrivenKeyframe(side + "fingerMiddle_01_ZTR.rotateY", cd=switchCtrl + ".metaArc", dv=1, v=-0.331)
mc.setDrivenKeyframe(side + "fingerMiddle_01_ZTR.rotateZ", cd=switchCtrl + ".metaArc", dv=1, v=-1.671)

mc.setDrivenKeyframe(side + "fingerRing_01_ZTR.rotateX", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerRing_01_ZTR.rotateY", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerRing_01_ZTR.rotateZ", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerRing_01_ZTR.rotateX", cd=switchCtrl + ".metaArc", dv=1, v=-13.139)
mc.setDrivenKeyframe(side + "fingerRing_01_ZTR.rotateY", cd=switchCtrl + ".metaArc", dv=1, v=1.252)
mc.setDrivenKeyframe(side + "fingerRing_01_ZTR.rotateZ", cd=switchCtrl + ".metaArc", dv=1, v=-2.023)

mc.setDrivenKeyframe(side + "fingerPinky_01_ZTR.rotateX", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerPinky_01_ZTR.rotateY", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerPinky_01_ZTR.rotateZ", cd=switchCtrl + ".metaArc")
mc.setDrivenKeyframe(side + "fingerPinky_01_ZTR.rotateX", cd=switchCtrl + ".metaArc", dv=1, v=-19.459)
mc.setDrivenKeyframe(side + "fingerPinky_01_ZTR.rotateY", cd=switchCtrl + ".metaArc", dv=1, v=0.346)
mc.setDrivenKeyframe(side + "fingerPinky_01_ZTR.rotateZ", cd=switchCtrl + ".metaArc", dv=1, v=-7.265)


mc.setDrivenKeyframe(side + "fingerThumb_01_ZTR.rotateX", cd=switchCtrl + ".spread")
mc.setDrivenKeyframe(side + "fingerThumb_01_ZTR.rotateY", cd=switchCtrl + ".spread")
mc.setDrivenKeyframe(side + "fingerThumb_01_ZTR.rotateZ", cd=switchCtrl + ".spread")
mc.setDrivenKeyframe(side + "fingerThumb_01_ZTR.rotateX", cd=switchCtrl + ".spread", dv=1, v=-6.838)
mc.setDrivenKeyframe(side + "fingerThumb_01_ZTR.rotateY", cd=switchCtrl + ".spread", dv=1, v=-13.131)
mc.setDrivenKeyframe(side + "fingerThumb_01_ZTR.rotateZ", cd=switchCtrl + ".spread", dv=1, v=33.075)

mc.setDrivenKeyframe(side + "fingerIndex_02_ZTR.rotateY", cd=switchCtrl + ".spread")
mc.setDrivenKeyframe(side + "fingerIndex_02_ZTR.rotateY", cd=switchCtrl + ".spread", dv=1, v=-33.221)

mc.setDrivenKeyframe(side + "fingerMiddle_02_ZTR.rotateY", cd=switchCtrl + ".spread")
mc.setDrivenKeyframe(side + "fingerMiddle_02_ZTR.rotateY", cd=switchCtrl + ".spread", dv=1, v=-11.571)

#mc.setDrivenKeyframe(side + "fingerRing_02_ZTR.rotateY", cd=switchCtrl+".spread")
#mc.setDrivenKeyframe(side + "fingerRing_02_ZTR.rotateY", cd=switchCtrl+".spread", dv=1, v=5.183)

mc.setDrivenKeyframe(side + "fingerPinky_02_ZTR.rotateY", cd=switchCtrl + ".spread")
mc.setDrivenKeyframe(side + "fingerPinky_02_ZTR.rotateY", cd=switchCtrl + ".spread", dv=1, v=25.048)


mc.setDrivenKeyframe(side + "fingerThumb_01_CONS.rotateY", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerThumb_01_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerThumb_01_CONS.rotateY", cd=switchCtrl + ".fist", dv=1, v=-10.602)
mc.setDrivenKeyframe(side + "fingerThumb_01_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-2.467)


mc.setDrivenKeyframe(side + "fingerThumb_02_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerThumb_02_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-13.773)

mc.setDrivenKeyframe(side + "fingerThumb_03_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerThumb_03_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-50.082)


mc.setDrivenKeyframe(side + "fingerIndex_02_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerIndex_02_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-57.436)

mc.setDrivenKeyframe(side + "fingerIndex_03_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerIndex_03_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-65.823)

mc.setDrivenKeyframe(side + "fingerIndex_04_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerIndex_04_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-76.496)


mc.setDrivenKeyframe(side + "fingerMiddle_02_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerMiddle_02_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-57.436)

mc.setDrivenKeyframe(side + "fingerMiddle_03_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerMiddle_03_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-59.406)

mc.setDrivenKeyframe(side + "fingerMiddle_04_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerMiddle_04_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-68.035)


mc.setDrivenKeyframe(side + "fingerRing_02_CONS.rotateX", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerRing_02_CONS.rotateY", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerRing_02_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerRing_02_CONS.rotateX", cd=switchCtrl + ".fist", dv=1, v=-2.502)
mc.setDrivenKeyframe(side + "fingerRing_02_CONS.rotateY", cd=switchCtrl + ".fist", dv=1, v=-5.638)
mc.setDrivenKeyframe(side + "fingerRing_02_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-57.436)

mc.setDrivenKeyframe(side + "fingerRing_03_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerRing_03_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-57.436)

mc.setDrivenKeyframe(side + "fingerRing_04_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerRing_04_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-57.436)


mc.setDrivenKeyframe(side + "fingerPinky_02_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerPinky_02_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-57.436)

mc.setDrivenKeyframe(side + "fingerPinky_03_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerPinky_03_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-57.436)

mc.setDrivenKeyframe(side + "fingerPinky_04_CONS.rotateZ", cd=switchCtrl + ".fist")
mc.setDrivenKeyframe(side + "fingerPinky_04_CONS.rotateZ", cd=switchCtrl + ".fist", dv=1, v=-57.436)
