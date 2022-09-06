# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------
##
# TO DO:
##
# --------------------------------------------------------------------------------------------
import os
import sys

jtools = os.getenv("JENTOOLS")
sys.path.append(jtools)
import jenAutoRig.core.helperFunctions.setupFunctions as setFunc
reload(setFunc)


class upperChSetup(object):
    def __init__(self, name, module='', mirror=False, height=3):
        self.setF = setFunc.setupFunctionsClass()
        self.name = name
        self.module = module
        self.part = self.module.replace('_module', ' ')
        self.side = 'C'
        self.mirror = mirror
        self.suffix = '_ProxyLoc'
        self.groupSuffix = '_ProxyGrp'
        self.controlSuffix = '_ControlProxy'
        self.curveSuffix = '_CurveWireProxy'
        self.curveGroupSuffix = '_CurveWireGrp'
        self.upperCheekComponents = {
            'main': {
                'type': 'group',
                'nodeName': False,
                'parent': False,
                'translate': [0, 0, 0],
                'mirrorTranslate': [0, 0, 0],
                'proxyControlType': False

            },
            'inner': {
                'type': 'locator',
                'nodeName': False,
                'parent': False,
                'translate': [2, height, 0],
                'mirrorTranslate': [-2, height, 0],
                'proxyControlType': 'sphere'

            },
            'mid': {
                'type': 'locator',
                'nodeName': False,
                'parent': False,
                'translate': [4, height, 0],
                'mirrorTranslate': [-4, height, 0],
                'proxyControlType': 'sphere'

            },
            'outer': {
                'type': 'locator',
                'nodeName': False,
                'parent': False,
                'translate': [6, height, 0],
                'mirrorTranslate': [-6, height, 0],
                'proxyControlType': 'sphere'

            }
        }
        self.maingroup = False
        self.innerLoc = False
        self.midLoc = False
        self.outerLoc = False
        self.curveGroup = False

        if mirror:
            self.side = 'R'
        else:
            self.side = 'L'

        # Init Rig
        self.upperCheekProcess()

    def upperCheekProcess(self):
        ''' Construct the upperchek system in maya '''
        if self.upperCheekComponents['main']['type'] == 'group':
            self.upperCheekComponents['main']['nodeName'] = self.setF.createTransform(
                self.part + '_' + self.side + '_' + self.name + '_' + 'main' + self.groupSuffix)
            self.maingroup = self.upperCheekComponents['main']['nodeName']

        for key in self.upperCheekComponents.keys():
            if self.upperCheekComponents[key]['type'] == 'locator':
                self.upperCheekComponents[key]['nodeName'] = self.setF.addSpaceLoc(
                    self.part + '_' + self.side + '_' + self.name + '_' + key + self.suffix)

                grp = self.setF.group(
                    self.upperCheekComponents[key]['nodeName'], self.part + '_' + self.side + '_' + self.name + '_' + key + self.groupSuffix)

                self.setF.parentNodes(grp, self.upperCheekComponents['main']['nodeName'])

                controlType = self.upperCheekComponents[key]['proxyControlType']
                locator = self.upperCheekComponents[key]['nodeName']

                if controlType:
                    ctrl = self.setF.proxyControl(controlType, 0, self.part + '_' + self.side + '_' + self.name + '_' + key + self.controlSuffix)
                    self.setF.parentNodes(ctrl, locator)
                    self.setF.moveNode(ctrl, 0, 0, 0, t=True)

                if self.mirror:
                    tx = self.upperCheekComponents[key]['mirrorTranslate'][0]
                    ty = self.upperCheekComponents[key]['mirrorTranslate'][1]
                    tz = self.upperCheekComponents[key]['mirrorTranslate'][2]
                    self.setF.moveNode(grp, tx, ty, tz, t=True)

                else:
                    tx = self.upperCheekComponents[key]['translate'][0]
                    ty = self.upperCheekComponents[key]['translate'][1]
                    tz = self.upperCheekComponents[key]['translate'][2]
                    self.setF.moveNode(grp, tx, ty, tz, t=True)

        self.innerLoc = self.upperCheekComponents['inner']['nodeName'][0]
        self.midLoc = self.upperCheekComponents['mid']['nodeName'][0]
        self.outerLoc = self.upperCheekComponents['outer']['nodeName'][0]

        points = [self.innerLoc] + [self.midLoc] + [self.outerLoc]

        self.curveGroup = self.setF.curveOnPoints(self.part + '_' + self.side + '_' + self.name + self.curveSuffix,
                                 self.part + '_' + self.side + '_' + self.name + self.curveGroupSuffix, points, rigType='upperCheek')

