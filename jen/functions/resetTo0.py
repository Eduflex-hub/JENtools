import maya.cmds as mc

controls = mc.ls("*CTRL")
stickys = mc.ls("*stickyCtrl")

for c in controls:
    allAttributes = mc.listAttr(c, se=1)
    keyAttributes = mc.listAttr(c, k=1)

    for attr in allAttributes:
        if attr in keyAttributes:
            if attr.startswith("translate") is True:
                mc.setAttr(c + "." + attr, 0)
            if attr.startswith("scale") is True:
                mc.setAttr(c + "." + attr, 1)
            if attr.startswith("rotate") is True:
                mc.setAttr(c + "." + attr, 0)
