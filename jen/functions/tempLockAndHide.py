import maya.cmds as mc
import os
import sys

jtools = os.getenv("JENTOOLS")
sys.path.append(jtools)

from jen.functions import abstractFunctions as absFunc
reload(absFunc)


root = ['C_root_01_CTRL']
main = ['C_main_01_CTRL']

bendys = mc.ls('*bendyCTRL')
stickys = mc.ls('*stickyCtrl')

spine = ['C_body_01_CTRL', 'C_spine_02_fkCTRL',
         'C_spine_03_fkCTRL', 'C_chest_01_ikCTRL', 'C_hip_01_CTRL', 'C_spine_08_endikCTRL']

ikFoot = mc.ls('*_foot_01_ikFootCTRL')

ikHand = mc.ls('*hand*CTRL')

fingers = mc.ls('*finger*CTRL')

poles = mc.ls('*PoleVector*ikCTRL')

switch = mc.ls('*switchCTRL')

FKs = mc.ls('*fkCTRL')

clavicles = mc.ls('*clavicle*CTRL')

head = ['C_neck_01_CTRL', 'C_head_01_CTRL']

sleeves = mc.ls('*sleeveCTRL')
eyes = mc.ls('*eyes_*CTRL')
eye = mc.ls('*eye_*CTRL')

visHide = root + bendys + stickys + spine + ikFoot + ikHand + \
    poles + switch + FKs + clavicles + head + sleeves + eyes + eye + fingers

transHide = switch + FKs

rotHide = bendys + poles + switch + eye

scaleHide = main + bendys + spine + ikFoot + \
    ikHand + fingers + poles + switch + FKs + clavicles + eyes + eye

for x in visHide:
    absFunc.lockHide(x, 'visibility')

for x in transHide:
    absFunc.lockHide(x, 'translate')

for x in rotHide:
    absFunc.lockHide(x, 'rotate')

for x in scaleHide:
    absFunc.lockHide(x, 'scale')
