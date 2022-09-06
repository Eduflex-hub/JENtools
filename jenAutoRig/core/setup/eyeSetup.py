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


class eyeRigSetup(object):
    def __init__(self, name, module='', offset=0):
        self.setF = setFunc.setupFunctionsClass()
        self.name = name
        self.module = module
        self.offset = offset
        self.side = 'C'
        self.group = None
        self.eyeComponents = {
            'socket': {
                'locator': False,
                'parent': False,
                'translate': [0, 0, 0],
                'rotate': [0, 0, 0],
                'angleQuery': False,
                'proxyControl': True,
                'proxyControlType': 'circle',
                'proxyControlOffset': 3
            },
            'pupil': {
                'locator': False,
                'parent': False,
                'translate': [0, 0, 2],
                'rotate': [0, 0, 0],
                'angleQuery': False,
                'proxyControl': False,
                'proxyControlType': False,
                'proxyControlOffset': False
            },
            'center': {
                'locator': False,
                'parent': False,
                'translate': [0, 0, 0],
                'rotate': [0, 0, 0],
                'angleQuery': 'center',
                'proxyControl': True,
                'proxyControlType': 'circle',
                'proxyControlOffset': 0
            },
            'upperLid_01': {
                'locator': False,
                'parent': False,
                'translate': [0, 0, 0],
                'rotate': [-30, 0, 0],
                'angleQuery': False,
                'proxyControl': False,
                'proxyControlType': False,
                'proxyControlOffset': False
            },
            'lowerLid_01': {
                'locator': False,
                'parent': False,
                'translate': [0, 0, 0],
                'rotate': [30, 0, 0],
                'angleQuery': False,
                'proxyControl': False,
                'proxyControlType': False,
                'proxyControlOffset': False
            },
            'upperLid_02': {
                'locator': False,
                'parent': False,
                'translate': [0, 0, 2],
                'rotate': [0, 0, 0],
                'angleQuery': 'upper',
                'proxyControl': True,
                'proxyControlType': 'sphere',
                'proxyControlOffset': False
            },
            'lowerLid_02': {
                'locator': False,
                'parent': False,
                'translate': [0, 0, 2],
                'rotate': [0, 0, 0],
                'angleQuery': 'lower',
                'proxyControl': True,
                'proxyControlType': 'sphere',
                'proxyControlOffset': False
            }
        }

        self.suffix = '_ProxyLoc'
        self.groupSuffix = '_ProxyGrp'
        self.controlSuffix = '_ControlProxy'
        self.part = self.module.replace('_module', ' ')

        if self.offset > 0:
            self.side = 'L'
        if self.offset < 0:
            self.side = 'R'

        # Init Rig
        self.eyeSetupProcess()

    def eyeSetupProcess(self):
        ''' Construct the eye system in maya '''
        for key in self.eyeComponents.keys():
            self.eyeComponents[key]['locator'] = self.setF.addSpaceLoc(self.part + '_' + self.side + '_' +
                                                                       self.name + '_' + key + self.suffix)

        self.setF.parentNodes(self.eyeComponents['pupil']['locator'],
                              self.eyeComponents['center']['locator'])

        self.setF.parentNodes(self.eyeComponents['center']['locator'],
                              self.eyeComponents['socket']['locator'])

        self.setF.parentNodes(self.eyeComponents['upperLid_02']['locator'],
                              self.eyeComponents['upperLid_01']['locator'])

        self.setF.parentNodes(self.eyeComponents['lowerLid_02']['locator'],
                              self.eyeComponents['lowerLid_01']['locator'])

        for key in self.eyeComponents.keys():
            tx = self.eyeComponents[key]['translate'][0]
            ty = self.eyeComponents[key]['translate'][1]
            tz = self.eyeComponents[key]['translate'][2]
            rx = self.eyeComponents[key]['rotate'][0]
            ry = self.eyeComponents[key]['rotate'][1]
            rz = self.eyeComponents[key]['rotate'][2]
            self.setF.moveNode(self.eyeComponents[key]['locator'], tx, ty, tz, t=True)
            self.setF.moveNode(self.eyeComponents[key]['locator'], rx, ry, rz, ro=True)

        group = self.setF.group([self.eyeComponents['socket']['locator'],
                                 self.eyeComponents['upperLid_01']['locator'],
                                 self.eyeComponents['lowerLid_01']['locator']],
                                self.part + '_' + self.side + '_' + self.name + self.groupSuffix)

        self.setF.moveNode(group, self.offset, 0, 0, t=True)

        for key in self.eyeComponents.keys():
            angle = self.eyeComponents[key]['angleQuery']
            if angle:
                if angle == 'center':
                    center = self.eyeComponents[key]['locator'][0]
                elif angle == 'upper':
                    upper = self.eyeComponents[key]['locator'][0]
                elif angle == 'lower':
                    lower = self.eyeComponents[key]['locator'][0]

        self.setF.angleQuery(group, center, upper, lower)

        for key in self.eyeComponents.keys():
            locator = self.eyeComponents[key]['locator'][0]
            controlType = self.eyeComponents[key]['proxyControlType']
            offset = self.eyeComponents[key]['proxyControlOffset']

            if self.eyeComponents[key]['proxyControl']:
                ctrl = self.setF.proxyControl(
                    controlType, offset, self.part + '_' + self.side + '_' + self.name + '_' + key + self.controlSuffix)                
                self.setF.parentNodes(ctrl, locator)
                self.setF.moveNode(ctrl, 0, 0, 0, t=True)
        self.group = group
