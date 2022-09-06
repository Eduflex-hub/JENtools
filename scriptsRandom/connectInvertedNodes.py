import maya.cmds as mc



sel = mc.ls(sl=1)

attr=mc.listAttr(sel[0], k=1)

md = mc.createNode('multiplyDivide', n= sel[0].replace('CTRL', 'InverseMD'))
mc.setAttr(md+'.input2X', -1)
mc.setAttr(md+'.input2Y', -1)
mc.setAttr(md+'.input2Z', -1)

for x in attr:
    if x.startswith('translate') == True:
        if x == 'translateX':
            mc.connectAttr(sel[0]+'.' +x, md+'.input1X', f=1)
            mc.connectAttr(md+'.outputX', sel[1]+'.'+x, f=1)
        else: 
            mc.connectAttr(sel[0]+'.'+x, sel[1]+'.'+x)
    if x.startswith('rotate')==True:
        if x== 'rotateX':
            mc.connectAttr(sel[0]+'.'+x, sel[1]+'.'+x)
        elif  x== 'rotateY':
            mc.connectAttr(sel[0]+'.' +x, md+'.input1Y', f=1)
            mc.connectAttr(md+'.outputY', sel[1]+'.'+x, f=1)
        elif  x== 'rotateZ':
            mc.connectAttr(sel[0]+'.' +x, md+'.input1Z', f=1)
            mc.connectAttr(md+'.outputZ', sel[1]+'.'+x, f=1)

    if x.startswith('scale')==True:
        mc.connectAttr(sel[0]+'.s', sel[1]+'.s')









