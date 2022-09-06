import maya.cmds as mc
import maya.mel as mel

def localGrp(_obj):
	for x in _obj:
	    coord = mc.xform(x, q=1, t=1, ws=1)
	    orient= mc.xform(x, q=1, ro=1, ws=1)
	    grp=mc.createNode('transform',n= x+'_GRP')
	    mc.xform(grp, t=coord, ws=1)
	    mc.xform(grp, ro=orient, ws=1)
	    mc.parent(x, grp)

sel=mc.ls(sl=1)

base=sel[0]
tip=sel[1]

handleGRP=mc.createNode('transform', n=base.replace('JNT','ikHandleGRP'))
handle = mc.ikHandle(sj=base, ee=tip, sol='ikRPsolver', n=base.replace('JNT','ikHandle'))[0]
mc.delete(mc.pointConstraint(handle, handleGRP, mo=0))
mc.parent(handle, handleGRP)

baseCoord=mc.xform(base, q=1, t=1, ws=1)
tipCoord=mc.xform(tip, q=1, t=1, ws=1)

mc.distanceDimension(sp=baseCoord ,ep=tipCoord)

loc1=mc.rename('locator1', base.replace('JNT', 'distLoc'))
loc2=mc.rename('locator2', tip.replace('JNT', 'distLoc'))
dist=mc.rename('distanceDimension1', tip.replace('JNT', 'distDimension'))

distGrp=mc.createNode('transform', n=base.replace('JNT', 'distGRP'))

mc.parent(handleGRP, distGrp)
	
_obj=[loc1, loc2, dist]

localGrp(_obj)

mc.select(_obj)

mel.eval('pickWalk -d up;')
groups=mc.ls(sl=1)
mc.parent(groups, distGrp)

mdFixStretch=mc.createNode('multiplyDivide', n=base.replace('JNT', 'StretchFix_MD'))
mdStretch=mc.createNode('multiplyDivide', n=base.replace('JNT', 'Stretch_MD'))
condStretch=mc.createNode('condition', n=base.replace('JNT', 'Stretch_COND'))

mc.connectAttr(dist+'Shape.distance', mdFixStretch+'.input1X')
mc.connectAttr('C_root_01_CTRL.scaleX', mdFixStretch+'.input2X')
mc.setAttr(mdFixStretch+'.operation', 2)


mc.connectAttr(mdFixStretch+'.outputX', mdStretch +'.input1X')
distNum=mc.getAttr(mdStretch+'.input1X')
mc.setAttr(mdStretch+'.input2X', distNum)
mc.setAttr(mdStretch+'.operation', 2)


mc.connectAttr(mdStretch+'.outputX', condStretch+'.firstTerm')
mc.connectAttr(mdStretch+'.outputX', condStretch+'.colorIfTrueR')
mc.connectAttr(mdStretch+'.outputX', condStretch+'.colorIfFalseR')
mc.setAttr(condStretch+'.secondTerm', 1)
#mc.setAttr(condStretch+'.colorIfFalse', 1,1,1)
mc.setAttr(condStretch+'.operation', 3)

mc.connectAttr(condStretch+'.outColorR', base+'.scaleY')

mdSquash=mc.createNode('multiplyDivide', n=base.replace('JNT', 'Squash_MD'))
mc.setAttr(mdSquash+'.operation', 3)	
mc.connectAttr(mdStretch+'.outputX', mdSquash+'.input1X')
mc.setAttr(mdSquash+'.input2X', -1)

squashCond=mc.createNode('condition', n=base.replace('JNT', 'Squash_COND'))
mc.setAttr(squashCond+'.operation', 4)
mc.setAttr(squashCond+'.secondTerm', 1)
mc.connectAttr(mdSquash+'.outputX', squashCond+'.firstTerm')
mc.connectAttr(mdSquash+'.outputX', squashCond+'.colorIfTrueR')
mc.connectAttr(mdSquash+'.outputX', squashCond+'.colorIfFalseR')

mc.connectAttr(squashCond+'.outColorR', base+'.scaleX')
mc.connectAttr(squashCond+'.outColorR', base+'.scaleZ')
