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
from jen.functions import abstractFunctions as absFunc
reload(absFunc)
reload(setFunc)


class faceProxy(object):
    def __init__(self, module=''):
        self.setF = setFunc.setupFunctionsClass()
        self.module = module
        self.part = self.module.replace('_module', ' ')
        self.suffix = '_ProxyLoc'
        self.groupSuffix = '_ProxyGrp'
        self.side = 'C'
        self.controlSuffix = '_ControlProxy'
        self.faceGroup = False
        self.faceControl = False
        self.lowerUpperHead = False
        self.eyebrowControl = False
        self.eyesControl = False
        self.upperCheekControl = False
        self.lowerCheekControl = False
        self.earsControl = False
        self.noseControl = False
        self.mouthControl = False
        self.chinControl = False
        self.faceComponents = {
            'face': {
                'name': False,
                'parent': False,
                'proxyControlType': 'face',
                'attributes': ['faceType', 'lowerUpperHead', 'eyebrow', 'eyes', 'upperCheek', 'lowerCheek', 'ears', 'nose', 'mouth', 'chin'],
                'attributeContent': ['deformers:FACS', 'no:yes', 'no:yes', 'no:yes', 'no:yes', 'no:yes', 'no:yes', 'no:yes', 'no:yes', 'no:yes'],
                'connectTo': False
            },
            'lowerUpperHead': {
                'name': False,
                'parent': 'face',
                'proxyControlType': 'lowerUpperHead',
                'attributes': ['showSetup'],
                'attributeContent': ['hide:show'],
                'connectTo': 'face'
            },
            'eyebrow': {
                'name': False,
                'parent': 'face',
                'proxyControlType': 'eyebrow',
                'attributes': ['showSetup', 'mirror'],
                'attributeContent': ['hide:show', 'no:yes'],
                'connectTo': 'face'
            },            
            'eyes': {
                'name': False,
                'parent': 'face',
                'proxyControlType': 'eyes',
                'attributes': ['showSetup', 'mirror'],
                'attributeContent': ['hide:show', 'no:yes'],
                'connectTo': 'face'
            },
            'upperCheek': {
                'name': False,
                'parent': 'face',
                'proxyControlType': 'upperCheek',
                'attributes': ['showSetup', 'mirror'],
                'attributeContent': ['hide:show', 'no:yes'],
                'connectTo': 'face'
            },
            'lowerCheek': {
                'name': False,
                'parent': 'face',
                'proxyControlType': 'lowerCheek',
                'attributes': ['showSetup', 'mirror'],
                'attributeContent': ['hide:show', 'no:yes'],
                'connectTo': 'face'
            },
            'ears': {
                'name': False,
                'parent': 'face',
                'proxyControlType': 'ears',
                'attributes': ['showSetup', 'mirror'],
                'attributeContent': ['hide:show', 'no:yes'],
                'connectTo': 'face'
            },
            'nose': {
                'name': False,
                'parent': 'face',
                'proxyControlType': 'nose',
                'attributes': ['showSetup', 'mirror'],
                'attributeContent': ['hide:show', 'no:yes'],
                'connectTo': 'face'
            },
            'mouth': {
                'name': False,
                'parent': 'face',
                'proxyControlType': 'mouth',
                'attributes': ['showSetup', 'mirror'],
                'attributeContent': ['hide:show', 'no:yes'],
                'connectTo': 'face'
            },
            'chin': {
                'name': False,
                'parent': 'face',
                'proxyControlType': 'chin',
                'attributes': ['showSetup', 'mirror'],
                'attributeContent': ['hide:show', 'no:yes'],
                'connectTo': 'face'
            }
        }

        # Init function
        self.mainFaceProxyControls()

    def mainFaceProxyControls(self):
        for key in self.faceComponents.keys():
            controlType = self.faceComponents[key]['proxyControlType']

            if controlType:
                self.faceComponents[key]['name'] = self.setF.proxyControl(
                    controlType, 0, self.part + '_' + self.side + '_' + key + self.controlSuffix)                

        for key in self.faceComponents.keys():
            parentString = self.faceComponents[key]['parent']
            if parentString:
                parent = self.faceComponents[parentString]['name']                
                 
                self.setF.parentNodes(self.faceComponents[key]['name'], parent)

            attr = self.faceComponents[key]['attributes']
            attrContent = self.faceComponents[key]['attributeContent']

            self.setF.addAttr(self.faceComponents[key]['name'], 'enum', attr, attrContent)

        for i in self.faceComponents['face']['attributes']:
            if i is not 'faceType':
                if i == self.faceComponents[i]['proxyControlType']:                    
                    connectionString = self.faceComponents[i]['connectTo']
                    destiny = self.faceComponents[i]['name']
                    if connectionString:
                        connect = self.faceComponents[connectionString]['name']
                        self.setF.connectAttr(connect, i, destiny, 'v')

        self.faceGroup = self.setF.group([self.faceComponents['face']['name']], self.part + '_' +
                                         self.side + '_' + self.faceComponents['face']['proxyControlType'] + self.groupSuffix)
        
        for key in self.faceComponents.keys():
            absFunc.lockHide(self.faceComponents[key]['name'], 'all')

        self.faceControl = self.faceComponents['face']['name']
        self.lowerUpperHead = self.faceComponents['lowerUpperHead']['name']
        self.eyebrowControl = self.faceComponents['eyebrow']['name']
        self.eyesControl = self.faceComponents['eyes']['name']
        self.upperCheekControl = self.faceComponents['upperCheek']['name']
        self.lowerCheekControl = self.faceComponents['lowerCheek']['name']
        self.earsControl = self.faceComponents['ears']['name']
        self.noseControl = self.faceComponents['face']['name']
        self.mouthControl = self.faceComponents['face']['name']
        self.chinControl = self.faceComponents['face']['name']
