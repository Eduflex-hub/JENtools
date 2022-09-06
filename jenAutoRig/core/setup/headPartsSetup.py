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


class HeadParts(object):
    def __init__(self, module='', offset=0):
        self.setF = setFunc.setupFunctionsClass()
        
        self.module = module
        self.offset = offset        
        self.side = 'C'
        self.headPartComp = {
            'lowerHead': {
                'locator': False,
                'parent': False,
                'translate': [0, -5, 0],
                'rotate': [0, 0, 0],
                'angleQuery': False,
                'proxyControl': True,
                'proxyControlType': 'lowerUpperHeadCircle',
                'proxyControlOffset': 0
            },
            'upperHead': {
                'locator': False,
                'parent': False,
                'translate': [0, 5, 0],
                'rotate': [0, 0, 0],
                'angleQuery': False,
                'proxyControl': True,
                'proxyControlType': 'lowerUpperHeadCircle',
                'proxyControlOffset': 0
            }
        }

        self.suffix = '_ProxyLoc'
        self.groupSuffix = '_ProxyGrp'
        self.controlSuffix = '_ControlProxy'
        self.part = self.module.replace('_module', ' ')
        self.name = False

        self.upperControl = False
        self.lowerControl = False

        if self.offset > 0:
            self.side = 'L'
        if self.offset < 0:
            self.side = 'R'
        if self.offset is 0:
            self.side = 'C'

        # Init Rig
        self.headPartsProcces()

    def headPartsProcces(self):
        ''' Construct the head Parts setup in maya '''
        for key in self.headPartComp.keys():
            self.headPartComp[key]['locator'] = self.setF.addSpaceLoc(self.part + '_' + self.side + '_' + key + self.suffix)

        # self.setF.parentNodes(self.headPartComp['lowerHead']['locator'], self.parent)

        # self.setF.parentNodes(self.headPartComp['upperHead']['locator'], self.parent)
       

        for key in self.headPartComp.keys():
            tx = self.headPartComp[key]['translate'][0]
            ty = self.headPartComp[key]['translate'][1]
            tz = self.headPartComp[key]['translate'][2]
            rx = self.headPartComp[key]['rotate'][0]
            ry = self.headPartComp[key]['rotate'][1]
            rz = self.headPartComp[key]['rotate'][2]
            self.setF.moveNode(self.headPartComp[key]['locator'], tx, ty, tz, t=True)
            self.setF.moveNode(self.headPartComp[key]['locator'], rx, ry, rz, ro=True)        

        for key in self.headPartComp.keys():
            self.name = key
            locator = self.headPartComp[key]['locator'][0]
            controlType = self.headPartComp[key]['proxyControlType']
            offset = self.headPartComp[key]['proxyControlOffset']

            if self.headPartComp[key]['proxyControl']:
                ctrl = self.setF.proxyControl(
                    controlType, offset, self.part + '_' + self.side + '_' + key + self.controlSuffix)                
                self.setF.parentNodes(ctrl, locator)
                self.setF.moveNode(ctrl, 0, 0, 0, t=True)
            if self.name.startswith('upper'):
                self.upperControl = self.headPartComp['upperHead']['locator'][0]
            if self.name.startswith('lower'):
                self.lowerControl = self.headPartComp['lowerHead']['locator'][0]
