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


class eyebrowSetup(object):
    def __init__(self, name, module='', height=3):
        self.setF = setFunc.setupFunctionsClass()
        self.name = name
        self.module = module
        self.part = self.module.replace('_module', ' ')
        self.side = 'C'
        self.suffix = '_ProxyLoc'
        self.groupSuffix = '_ProxyGrp'
        self.controlSuffix = '_ControlProxy'
        self.curveSuffix = '_CurveWireProxy'
        self.curveGroupSuffix = '_CurveWireGrp'
        self.eyebrowComponents = {
            'main': {
                'key': 'main',
                'type': 'group',
                'side': 'C',
                'nodeName': False,
                'parent': False,
                'translate': [0, 0, 0],
                'proxyControlType': False

            },
            'L_inner': {
                'key': 'inner',
                'type': 'locator',
                'side': 'L',
                'nodeName': False,
                'parent': False,
                'translate': [1.714, height, 0],
                'proxyControlType': 'sphere'

            },
            'L_mid': {
                'key': 'mid',
                'type': 'locator',
                'side': 'L',
                'nodeName': False,
                'parent': False,
                'translate': [3.714, height, 0],
                'proxyControlType': 'sphere'

            },
            'L_outer': {
                'key': 'outer',
                'type': 'locator',
                'side': 'L',
                'nodeName': False,
                'parent': False,
                'translate': [6, height, 0],
                'proxyControlType': 'sphere'
            },
            'C_center': {
                'key': 'center',
                'type': 'locator',
                'side': 'C',
                'nodeName': False,
                'parent': False,
                'translate': [0, height, 0],
                'proxyControlType': 'sphere'

            },
            'R_inner': {
                'key': 'inner',
                'type': 'locator',
                'side': 'R',
                'nodeName': False,
                'parent': False,
                'translate': [-1.714, height, 0],
                'proxyControlType': 'sphere'

            },
            'R_mid': {
                'key': 'mid',
                'type': 'locator',
                'side': 'R',
                'nodeName': False,
                'parent': False,
                'translate': [-3.714, height, 0],
                'proxyControlType': 'sphere'

            },
            'R_outer': {
                'key': 'outer',
                'type': 'locator',
                'side': 'R',
                'nodeName': False,
                'parent': False,
                'translate': [-6, height, 0],
                'proxyControlType': 'sphere'
            },
            'L_master': {
                'key': 'master',
                'type': 'locator',
                'side': 'L',
                'nodeName': False,
                'parent': False,
                'translate': [3.714, height, 0],
                'proxyControlType': 'circle'
            },
            'R_master': {
                'key': 'master',
                'type': 'locator',
                'side': 'R',
                'nodeName': False,
                'parent': False,
                'translate': [-3.714, height, 0],
                'proxyControlType': 'circle'
            }

        }
        self.maingroup = False
        self.innerLoc = False
        self.midLoc = False
        self.outerLoc = False
        self.curveGroup = False

        # Init Rig
        self.eyebrowProcess()

    def eyebrowProcess(self):
        ''' Construct the eyebrow system in maya '''
        if self.eyebrowComponents['main']['type'] == 'group':
            self.eyebrowComponents['main']['nodeName'] = self.setF.createTransform(
                self.part + '_' + self.side + '_' + self.name + '_' + 'main' + self.groupSuffix)
            self.maingroup = self.eyebrowComponents['main']['nodeName']

        for key in self.eyebrowComponents.keys():
            self.side = self.eyebrowComponents[key]['side']
            partName = self.eyebrowComponents[key]['key']

            if self.eyebrowComponents[key]['type'] == 'locator':
                self.eyebrowComponents[key]['nodeName'] = self.setF.addSpaceLoc(
                    self.part + '_' + self.side + '_' + self.name + '_' + partName + self.suffix)

                grp = self.setF.group(
                    self.eyebrowComponents[key]['nodeName'], self.part + '_' + self.side + '_' + self.name + '_' + partName + self.groupSuffix)

                self.setF.parentNodes(
                    grp, self.eyebrowComponents['main']['nodeName'])

                controlType = self.eyebrowComponents[key]['proxyControlType']
                locator = self.eyebrowComponents[key]['nodeName']

                if controlType:
                    ctrl = self.setF.proxyControl(
                        controlType, 0, self.part + '_' + self.side + '_' + self.name + '_' + partName + self.controlSuffix)
                    self.setF.parentNodes(ctrl, locator)
                    self.setF.moveNode(ctrl, 0, 0, 0, t=True)

                    tx = self.eyebrowComponents[key]['translate'][0]
                    ty = self.eyebrowComponents[key]['translate'][1]
                    tz = self.eyebrowComponents[key]['translate'][2]
                    self.setF.moveNode(grp, tx, ty, tz, t=True)

        self.L_innerLoc = self.eyebrowComponents['L_inner']['nodeName'][0]
        self.L_midLoc = self.eyebrowComponents['L_mid']['nodeName'][0]
        self.L_outerLoc = self.eyebrowComponents['L_outer']['nodeName'][0]
        self.C_center = self.eyebrowComponents['C_center']['nodeName'][0]
        self.R_innerLoc = self.eyebrowComponents['R_inner']['nodeName'][0]
        self.R_midLoc = self.eyebrowComponents['R_mid']['nodeName'][0]
        self.R_outerLoc = self.eyebrowComponents['R_outer']['nodeName'][0]

        points = [self.L_outerLoc] + [self.L_midLoc] + [self.L_innerLoc] + \
            [self.C_center] + [self.R_innerLoc] + \
            [self.R_midLoc] + [self.R_outerLoc]

        self.curveGroup = self.setF.curveOnPoints(self.part + '_' + self.name + self.curveSuffix,
                                                  self.part + '_' + self.side + '_' + self.name + self.curveGroupSuffix,
                                                  points, rigType='eyebrow')
