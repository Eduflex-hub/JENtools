# -*- coding: utf-8 -*-
##--------------------------------------------------------------------------------------------
##
## TO DO:
##
##--------------------------------------------------------------------------------------------

# IMPORTS


import maya.cmds as mc
import maya.mel as mel
import os
from math import pow,sqrt
import sys
import json

jtools = os.getenv("JENTOOLS")
sys.path.append(jtools)
#print (jtools)

from jen.functions.Qt import QtCore, QtWidgets
from jenAutoRig.core.loaduifile import loadUi_file, compile_ui, getMayaWindow
from jen.functions import abstractFunctions as absFunc

import jenAutoRig.core.setup.faceProxyControlsSetup as prF
import jenAutoRig.core.setup.headPartsSetup as headSetup
import jenAutoRig.core.setup.eyeSetup as eyeSetup
import jenAutoRig.core.setup.upperCheekSetup as uprCheek
import jenAutoRig.core.setup.eyebrowSetup as eyebr

reload(headSetup)
reload(absFunc)
reload(eyeSetup)
reload(prF)
reload(uprCheek)
reload(eyebr)

##--------------------------------------------------------------------------------------------
## EXTERNAL FILES // CFG + UI + Globals
##--------------------------------------------------------------------------------------------
app_folder_win = os.path.dirname(__file__)
ui_main = app_folder_win + "/" + "ui" + "/" + "jenAutorigUserInterface.ui"
form, base = loadUi_file(ui_main)

##--------------------------------------------------------------------------------------------
## Class: Main UI
##--------------------------------------------------------------------------------------------


class ProgramUI(base, form):
    def __init__(self, parent=getMayaWindow()):
        super(ProgramUI,self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        # startup FUNCTIONS
        self.setupUi(self)
        self.setConnections()
        self.reloadUI()

    ##--------------------------------------------------------------------------------------------
    ## CONNECTIONS & INIT FUNCTIONS
    ##--------------------------------------------------------------------------------------------

    # Connections
    def setConnections(self):
        # Menu Bar
        
        self.mnu_close.triggered.connect(self.closeApp) 

        # Set Project
        self.pushButton_browse.clicked.connect(lambda: self.setProject(state='browse'))
        self.comboBox_assetType.currentIndexChanged.connect(lambda: self.setProject(state='typeChanged'))
        self.comboBox_assetName.currentIndexChanged.connect(lambda: self.setProject(state='nameChanged'))
        self.pushButton_createSubFolder.clicked.connect(lambda: self.setProject(state='createSubFolderPushed'))
        self.pushButton_openFolder.clicked.connect(lambda: self.setProject(state='openFolder'))
        self.pushButton_loadModel.clicked.connect(lambda: self.loadFiles(fType='model'))
        self.pushButton_loadshading.clicked.connect(lambda: self.loadFiles(fType='shading'))
        self.pushButton_loadRig.clicked.connect(lambda: self.loadFiles(fType='rigging'))
        self.pushButton_loadSetup.clicked.connect(lambda: self.loadFiles(fType='loadSetup'))
        self.pushButton_loadSkinFile.clicked.connect(lambda: self.loadFiles(fType='loadSkin'))

        #Pointers
        self.pushButton_insertFaceMesh.clicked.connect(lambda: self.createPointers(button='faceMesh'))
        self.pushButton_insertAdditionaFaceMeshes.clicked.connect(lambda: self.createPointers(button='addFaceMesh'))
        self.pushButton_insertStickyMeshes.clicked.connect(lambda: self.createPointers(button='stickyMesh'))
        self.pushButton_insertSquashMeshes.clicked.connect(lambda: self.createPointers(button='squashMesh'))
        self.pushButton_insertSquashControls.clicked.connect(lambda: self.createPointers(button='squashControls'))
        self.pushButton_insertEyelashMeshes.clicked.connect(lambda: self.createPointers(button='eyeLashMesh'))
        self.pushButton_eyesMeshes.clicked.connect(lambda: self.createPointers(button='eyesMeshes'))
        self.pushButton_lowerTeeth.clicked.connect(lambda: self.createPointers(button='lowerTeeth'))
        self.pushButton_upperTeeth.clicked.connect(lambda: self.createPointers(button='upperTeeth'))
        self.pushButton_tongue.clicked.connect(lambda: self.createPointers(button='tongue'))
        self.pushButton_savePointerData.clicked.connect(lambda: self.createPointers(button='saveData'))
        self.pushButton_loadFromJson.clicked.connect(lambda: self.createPointers(button='loadData'))
        self.pushButton_createMaskScene.clicked.connect(self.createMask)

        # Setup
        self.pushButton_importBiped.clicked.connect(self.importBipedTemplate)
        self.pushButton_toggleMesh.clicked.connect(self.toggleMesh)
        self.pushButton_deleteMesh.clicked.connect(self.deleteMesh)
        self.pushButton_toggleMeshDisplay.clicked.connect(self.toggleMeshLayerDisplay)
        self.pushButton_generateModules.clicked.connect(self.modules)
        self.pushButton_deleteModule.clicked.connect(self.deleteMod)
        self.pushButton_mirrorParameters.clicked.connect(self.mirrorParameters)
        
        self.pushButton_loadData.clicked.connect(self.loadModData)
        self.pushButton_storeData.clicked.connect(self.storeData)
        self.pushButton_generateRig.clicked.connect(self.generateRig)

        

        # loMesh
        self.pushButton_separateMesh.clicked.connect(self.separateMesh)
        self.pushButton_mirrorSelected.clicked.connect(self.mirrorSelected)


    # Initialize UI
    def reloadUI(self):
        self.initVars()
        print ('-'*60)
        print ('-'*60)
        print ("Starting", self._appName, "version:", self._version)
        print ("Author:", self._author)
        print ('-'*60)
        print ('-'*60)


    def initVars(self):
        self._version = "0.01 BETA"
        self._appName = "--JEN AUTORIG--"
        self._author = "Eduflex - Copyright 2016-2019 All Rights Reserved"


    ##--------------------------------------------------------------------------------------------
    ## UI FUNCTIONS MENU & BUTTONS
    ##--------------------------------------------------------------------------------------------    

    def closeApp(self):
        self.close()

    

    ##--------------------------------------------------------------------------------------------
    ## JEN AUTORIG FUNCTIONS
    ##--------------------------------------------------------------------------------------------    
    #---------------------------------------------------
    # SetProject #--------------------------------------
    #---------------------------------------------------
    def setProject(self, state):
        if state=='browse':
            self.comboBox_assetType.setCurrentIndex(0)
            self.comboBox_assetName.clear()
            self.label_projectPath.setText('None')
            self.label_activeAsset.setText('None')
            path=mc.fileDialog2( fm=3, okc='Pick', cc='Cancel', cap='Select your path', dir='G:')[0]
            
            self.lineEdit_Project.setText(str(path))
            characterPath= path+r'/ASSETS/CHARACTERS'
            propsPath= path+ r'/ASSETS/PROPS'
            dirInChar = []
            assetInChar=[]
            for each in os.listdir(characterPath):
                fp = os.path.join(characterPath, each)
                if os.path.isdir(fp):                   
                    fp=fp.replace('\\','/')
                    if "$" not in fp: 
                        dirInChar.append(fp)
                
                    cd=fp.split('/')
                    n=len(cd)
                    n=cd[n-1]
                    if n.startswith('$')==False:
                        assetInChar.append(n)   

            dirInProp = []
            assetInProp=[]
            for each in os.listdir(propsPath):
                fp = os.path.join(propsPath, each)
                if os.path.isdir(fp):
                    fp=fp.replace('\\','/')
                    if "$" not in fp: 
                        dirInProp.append(fp)
                
                    cd=fp.split('/')
                    n=len(cd)
                    n=cd[n-1]
                    if n.startswith('$')==False:
                        assetInProp.append(n)

            if mc.objExists('jenAutorig_projectPathNode')==True:
                mc.delete('jenAutorig_projectPathNode')
            mc.createNode('transform', n='jenAutorig_projectPathNode', ss=1)
            mc.setAttr('jenAutorig_projectPathNode.hiddenInOutliner', 1)

            mc.addAttr('jenAutorig_projectPathNode',longName='dirInChar', dt="string")
            mc.addAttr('jenAutorig_projectPathNode',longName='assetInChar', dt="string")
            mc.addAttr('jenAutorig_projectPathNode',longName='dirInProp', dt="string")
            mc.addAttr('jenAutorig_projectPathNode',longName='assetInProp', dt="string")
            mc.addAttr('jenAutorig_projectPathNode',longName='finalPath', dt="string")
            mc.addAttr('jenAutorig_projectPathNode',longName='publishedPath', dt="string")

            mc.setAttr('jenAutorig_projectPathNode.dirInChar', dirInChar, type='string')
            mc.setAttr('jenAutorig_projectPathNode.assetInChar', assetInChar, type='string')
            mc.setAttr('jenAutorig_projectPathNode.dirInProp', dirInProp, type='string')
            mc.setAttr('jenAutorig_projectPathNode.assetInProp', assetInProp, type='string')

        if state=='typeChanged':
            if self.comboBox_assetType.currentText()=='Character':
                charPathData=eval(mc.getAttr('jenAutorig_projectPathNode.dirInChar'))
                charAssetData=eval(mc.getAttr('jenAutorig_projectPathNode.assetInChar'))                
                self.comboBox_assetName.clear()
                for i in charAssetData:
                    self.comboBox_assetName.addItem(i)

            if self.comboBox_assetType.currentText()=='Prop':
                propPathData=eval(mc.getAttr('jenAutorig_projectPathNode.dirInProp'))
                propAssetData=eval(mc.getAttr('jenAutorig_projectPathNode.assetInProp'))                
                self.comboBox_assetName.clear()
                for i in propAssetData:
                    self.comboBox_assetName.addItem(i)

        if state=='nameChanged':
            if self.comboBox_assetType.currentText()=='Character':
                charPathData=eval(mc.getAttr('jenAutorig_projectPathNode.dirInChar'))
                charAssetData=eval(mc.getAttr('jenAutorig_projectPathNode.assetInChar'))
                currentIndex = str(self.comboBox_assetName.currentIndex())                      
                for x in charPathData:
                    index=charPathData.index(x)
                                
                    if str(index) == currentIndex:                      
                        self.label_projectPath.setText(x)
                
                for x in charAssetData:
                    index=charAssetData.index(x)
                    
                    if str(index) == currentIndex:                      
                        self.label_activeAsset.setText(x)

                finalPath=self.label_projectPath.text()+r'/Rigging'
                publishedPath=self.label_projectPath.text()+r'/Published'


                mc.setAttr('jenAutorig_projectPathNode.finalPath', finalPath, type='string')
                mc.setAttr('jenAutorig_projectPathNode.publishedPath', publishedPath, type='string')
                
            if self.comboBox_assetType.currentText()=='Prop':
                propPathData=eval(mc.getAttr('jenAutorig_projectPathNode.dirInProp'))
                propAssetData=eval(mc.getAttr('jenAutorig_projectPathNode.assetInProp'))
                currentIndex = str(self.comboBox_assetName.currentIndex())
                for x in propPathData:
                    index=propPathData.index(x)
                                
                    if str(index) == currentIndex:
                        self.label_projectPath.setText(x)
                
                for x in propAssetData:
                    index=propAssetData.index(x)
                    
                    if str(index) == currentIndex:
                        self.label_activeAsset.setText(x)

                finalPath=self.label_projectPath.text()+r'/Rigging'
                publishedPath=self.label_projectPath.text()+r'/Published'

                
                mc.setAttr('jenAutorig_projectPathNode.finalPath', finalPath, type='string')
                mc.setAttr('jenAutorig_projectPathNode.publishedPath', publishedPath, type='string')
            
            #JEN NODE to Json#--------------------------------------------------------------------------------------------      
            absFunc.storeNodeAttrAsJson(finalPath, 'jenAutorig_projectPathNode')

        #Sub-Folders#--------------------------------------------------------------------------------------------       
        if state=='createSubFolderPushed':
            finalPath=mc.getAttr('jenAutorig_projectPathNode.finalPath')            
            if not os.path.exists(finalPath+r'/skin/skinWeights'):
                os.makedirs(finalPath+r'/skin/skinWeights')
            if not os.path.exists(finalPath+r'/mask/maskData'):
                os.makedirs(finalPath+r'/mask/maskData')
            if not os.path.exists(finalPath+r'/setup/setupData'):
                os.makedirs(finalPath+r'/setup/setupData')          
        #Open Folder#--------------------------------------------------------------------------------------------       
        if state=='openFolder':
            #finalPath=mc.getAttr('jenAutorig_projectPathNode.finalPath')
            finalPath=self.label_projectPath.text()         
            os.startfile(finalPath)

    #Load Buttons#--------------------------------------------------------------------------------------------      
    def loadFiles(self, fType):
        jsonPath=self.label_projectPath.text()+r'/Rigging/jenAutorig_projectPathNode.json'
        publishedPath = absFunc.getSimpleJson(jsonPath, 'publishedPath')
        riggingPath = absFunc.getSimpleJson(jsonPath, 'savedIn')
        setupPath = riggingPath + r'/setup/'
        skinPath = riggingPath + r'/skin/'
        publishFiles=[]
        riggingFiles=[]
        setupFiles=[]
        skinFiles=[]
        pubItems = os.listdir(publishedPath)
        rigItems=os.listdir(riggingPath)
        if os.path.exists(setupPath):
            setupItems=os.listdir(setupPath)
        if os.path.exists(skinPath):
            skinItems=os.listdir(skinPath)            
        if fType == 'model':

            for file in pubItems:
                if ".ma" in file:
                    publishFiles.append(file)

            for x in publishFiles:
                if x.startswith('MOD_'):
                    filePath=publishedPath+r'/'+x                   
                    if os.path.exists(filePath):
                        print ('Opening:'+ filePath)
                        mc.file( filePath, o=True, force=True )
                    if not mc.objExists('jenAutorig_projectPathNode'):
                        print ('jenNode not found, loading jen')
                        absFunc.loadJenNode(jsonPath)
                else:
                    mc.warning('File does not exists')


        if fType=='shading':

            for file in pubItems:
                if ".ma" in file:
                    publishFiles.append(file)

            for x in publishFiles:
                if x.startswith('SHD_')==True:
                    filePath=publishedPath+r'/'+x
                    
                    if os.path.exists(filePath):
                        print ('Opening:'+ filePath)
                        mc.file( filePath, o=True, force=True )
                    if not mc.objExists('jenAutorig_projectPathNode'):
                        print ("jenNode not found, loading jen")
                        absFunc.loadJenNode(jsonPath)
                else:
                    mc.warning('File does not exists')

        if fType=='rigging':

            for file in rigItems:                       
                if ".ma" in file:
                    if file.startswith('RIG_'+self.label_activeAsset.text()+'.')==True:
                        riggingFiles.append(file)
                        print (file)

            allArchives=[]
            for x in riggingFiles:              
                if x.startswith('RIG_'+self.label_activeAsset.text()+'.')==True:
                    filePath=riggingPath+r'/'+x
                    allArchives.append(filePath)
            if len(allArchives) >0:
                if os.path.exists(allArchives[-1]):
                    mc.file( allArchives[-1], o=True, force=True )
            else:
                mc.warning('File does not exists')

            if not mc.objExists('jenAutorig_projectPathNode'):
                print ("jenNode not found, loading jenNode")
                absFunc.loadJenNode(jsonPath)
        
        if fType=='loadSetup':
            
            for file in setupItems:             
                if ".ma" in file:
                    if file.startswith('RIG_'+self.label_activeAsset.text()+'_setup.')==True:
                        setupFiles.append(file)

            allArchives=[]
            for x in setupFiles:                
                if x.startswith('RIG_'+self.label_activeAsset.text()+'_setup.')==True:
                    filePath=setupPath+r'/'+x
                    allArchives.append(filePath)            
            if len(allArchives) >0:
                if os.path.exists(allArchives[-1]):
                    mc.file( allArchives[-1], o=True, force=True )
            else:
                mc.warning('File does not exists')

            if not mc.objExists('jenAutorig_projectPathNode'):
                print ("jenNode not found, loading jenNode")
                absFunc.loadJenNode(jsonPath)

        if fType=='loadSkin':
            
            for file in skinItems:             
                if ".ma" in file:
                    if file.startswith('RIG_'+self.label_activeAsset.text()+'_skin.')==True:
                        skinFiles.append(file)

            allArchives=[]
            for x in skinFiles:                
                if x.startswith('RIG_'+self.label_activeAsset.text()+'_skin.')==True:
                    filePath=skinPath+r'/'+x
                    allArchives.append(filePath)            
            if len(allArchives) >0:
                if os.path.exists(allArchives[-1]):
                    mc.file( allArchives[-1], o=True, force=True )
            else:
                mc.warning('File does not exists')

            if not mc.objExists('jenAutorig_projectPathNode'):
                print ("jenNode not found, loading jenNode")
                absFunc.loadJenNode(jsonPath)

    def createPointers(self, button):
    
        sel=mc.ls(sl=1)
        texto = ""      
        for x in sel:
            asset=x.split('_')
            asset= asset[0]+'_'+asset[1]
            if x == sel[-1]:
                texto = texto + asset
            else:
                texto = texto + asset + ","

            
            if button == 'faceMesh':
                self.lineEdit_faceMesh.setText(texto)
                self.lineEdit_faceMesh.setToolTip(texto)

            if button == 'addFaceMesh':
                self.lineEdit_addFaceMesh.setText(texto)
                self.lineEdit_addFaceMesh.setToolTip(texto)

            if button == 'stickyMesh':
                self.lineEdit_stickyMesh.setText(texto)
                self.lineEdit_stickyMesh.setToolTip(texto)

            if button == 'squashMesh':
                self.lineEdit_squashMeshes.setText(texto)
                self.lineEdit_squashMeshes.setToolTip(texto)

            if button == 'squashControls':
                self.lineEdit_squashControls.setText(texto)
                self.lineEdit_squashControls.setToolTip(texto)

            if button == 'eyeLashMesh':
                self.lineEdit_eyelashMeshes.setText(texto)
                self.lineEdit_eyelashMeshes.setToolTip(texto)

            if button == 'eyesMeshes':
                self.lineEdit_eyesMeshes.setText(texto)
                self.lineEdit_eyesMeshes.setToolTip(texto)
            

            if button == 'lowerTeeth':
                self.lineEdit_lowerTeeth.setText(texto)
                self.lineEdit_lowerTeeth.setToolTip(texto)


            if button == 'upperTeeth':
                self.lineEdit_upperTeeth.setText(texto)
                self.lineEdit_upperTeeth.setToolTip(texto)


            if button == 'tongue':
                self.lineEdit_tongue.setText(texto)
                self.lineEdit_tongue.setToolTip(texto)

            if button== 'saveData':
                setupDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData'
                pointersDict={
                        'faceMesh': self.lineEdit_faceMesh.text(),
                        'additionalFaceMesh':   self.lineEdit_addFaceMesh.text(),
                        'stickyMesh':   self.lineEdit_stickyMesh.text(),
                        'squashMeshes': self.lineEdit_squashMeshes.text(),
                        'squashControls':   self.lineEdit_squashControls.text(),
                        'eyeLashMeshes':    self.lineEdit_eyelashMeshes.text(),
                        'eyesMeshes':   self.lineEdit_eyesMeshes.text(),
                        'lowerTeethMesh':   self.lineEdit_lowerTeeth.text(),
                        'upperTeethMesh':   self.lineEdit_upperTeeth.text(),
                        'tongue':   self.lineEdit_tongue.text(),
                        }
            jsonPath= setupDataPath
            with open(jsonPath + r'/' + 'pointersData'+ '.json', 'w') as outfile:
                json.dump(pointersDict, outfile, sort_keys=1, indent=4)
            sys.stdout.write("Pointers Data Saved.")

        if button== 'loadData':
            
            jsonPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/pointersData.json'
            if os.path.exists(jsonPath):
                self.lineEdit_faceMesh.setText(absFunc.getSimpleJson(jsonPath, "faceMesh"))
                self.lineEdit_addFaceMesh.setText(absFunc.getSimpleJson(jsonPath, "additionalFaceMesh"))
                self.lineEdit_stickyMesh.setText(absFunc.getSimpleJson(jsonPath, "stickyMesh"))
                self.lineEdit_squashMeshes.setText(absFunc.getSimpleJson(jsonPath, "squashMeshes"))
                self.lineEdit_squashControls.setText(absFunc.getSimpleJson(jsonPath, "squashControls"))
                self.lineEdit_eyelashMeshes.setText(absFunc.getSimpleJson(jsonPath, "eyeLashMeshes"))
                self.lineEdit_eyesMeshes.setText(absFunc.getSimpleJson(jsonPath, "eyesMeshes"))
                self.lineEdit_lowerTeeth.setText(absFunc.getSimpleJson(jsonPath, "lowerTeethMesh"))
                self.lineEdit_upperTeeth.setText(absFunc.getSimpleJson(jsonPath, "upperTeethMesh"))
                self.lineEdit_tongue.setText(absFunc.getSimpleJson(jsonPath, "tongue"))
                mc.warning("Data loaded.")
            else:
                mc.warning("File doesn't exists.")

    def createMask(self):
        jsonPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/pointersData.json'
        suffix='_01__MSH'
        _faceMeshLine=self.lineEdit_faceMesh.text()
        _addFaceMeshLine=self.lineEdit_addFaceMesh.text()
        _eyesMeshesLine=self.lineEdit_eyesMeshes.text()
        _lowerteethLine=self.lineEdit_lowerTeeth.text()
        _upperTeethLine=self.lineEdit_upperTeeth.text()
        _tongueLine=self.lineEdit_tongue.text()


        if os.path.exists(jsonPath):
            #----------------------------
            #Getting Face Mesh:
            #----------------------------
            
            faceMesh=[]
            addFaceMeshC=[]
            addFaceMeshL=[]
            addFaceMeshR=[]
            absFunc.getPointer(_faceMeshLine, False, faceMesh, False)
            absFunc.getPointer(_addFaceMeshLine, addFaceMeshL, addFaceMeshC, addFaceMeshR)
            faceMesh=''.join(map(str,faceMesh))
            addFaceMeshC=''.join(map(str,addFaceMeshC))
            addFaceMeshL=''.join(map(str,addFaceMeshL))
            addFaceMeshR=''.join(map(str,addFaceMeshR))
            
            #----------------------------
            #Getting Eyes Mesh:
            #----------------------------
            lEyeMesh=[]
            rEyeMesh=[]
            cEyeMesh=[]
            absFunc.getPointer(_eyesMeshesLine, lEyeMesh, cEyeMesh, rEyeMesh)
            lEyeMesh=''.join(map(str,lEyeMesh))
            rEyeMesh=''.join(map(str,rEyeMesh))
            cEyeMesh=''.join(map(str,cEyeMesh))

            # ----------------------------
            # Getting teeth and tongue Mesh:
            # ----------------------------
            lowerTeethMesh=[]
            upperTeethMesh=[]
            tongueMesh=[]
            absFunc.getPointer(_lowerteethLine, False, lowerTeethMesh, False)
            absFunc.getPointer(_upperTeethLine, False, upperTeethMesh, False)
            absFunc.getPointer(_tongueLine, False, tongueMesh, False)
            lowerTeethMesh=''.join(map(str,lowerTeethMesh))
            upperTeethMesh=''.join(map(str,upperTeethMesh))
            tongueMesh=''.join(map(str,tongueMesh))

            
            #preBSList = ['C_'+faceMesh+'_mouthForwardBSMesh', 'C_'+ faceMesh +'_mouthBackwardBSMesh', 'C_'+faceMesh+'_mouthNorthBSMesh', 'C_'+faceMesh+'_mouthSouthBSMesh', 'C_'+faceMesh+'_mouthEastBSMesh', 'C_'+faceMesh+'_mouthWestBSMesh', 'C_'+faceMesh+'_mouthTwistClockwiseBSMesh', 'C_'+faceMesh+'_mouthTwistAnticlockwiseBSMesh', 'C_'+lowerTeethMesh+'_twistClockwiseBSMesh', 'C_'+lowerTeethMesh+'_twistAnticlockwiseBSMesh', 'C_'+upperTeethMesh+'_twistClockwiseBSMesh', 'C_'+upperTeethMesh+'_twistAnticlockwiseBSMesh', 'C_'+tongueMesh+'_twistClockwiseBSMesh', 'C_'+tongueMesh+'_twistAnticlockwiseBSMesh', 'C_'+faceMesh+'_bendEastBSMesh', 'C_'+faceMesh+'_bendWestBSMesh', 'C_'+faceMesh+'_squashBSMesh', 'C_'+faceMesh+'_stretchBSMesh', 'L_'+faceMesh+'_cheekInBSMesh', 'R_'+faceMesh+'_cheekInBSMesh', 'L_'+faceMesh+'_cheekOutBSMesh', 'R_'+faceMesh+'_cheekOutBSMesh', 'L_'+faceMesh+'_cheekSquintNorthBSMesh', 'R_'+faceMesh+'_cheekSquintNorthBSMesh', 'L_'+faceMesh+'_eyebrowEastBSMesh', 'R_'+faceMesh+'_eyebrowEastBSMesh', 'L_'+faceMesh+'_eyebrowInNorthBSMesh', 'R_'+faceMesh+'_eyebrowInNorthBSMesh', 'L_'+faceMesh+'_eyebrowInSouthBSMesh', 'R_'+faceMesh+'_eyebrowInSouthBSMesh', 'L_'+faceMesh+'_eyebrowMidNorthBSMesh', 'R_'+faceMesh+'_eyebrowMidNorthBSMesh', 'L_'+faceMesh+'_eyebrowMidSouthBSMesh', 'R_'+faceMesh+'_eyebrowMidSouthBSMesh', 'L_'+faceMesh+'_eyebrowOutNorthBSMesh', 'R_'+faceMesh+'_eyebrowOutNorthBSMesh', 'L_'+faceMesh+'_eyebrowOutSouthBSMesh', 'R_'+faceMesh+'_eyebrowOutSouthBSMesh', 'L_'+faceMesh+'_eyebrowWestBSMesh', 'R_'+faceMesh+'_eyebrowWestBSMesh', 'L_'+faceMesh+'_lipCornerFrownBSMesh', 'R_'+faceMesh+'_lipCornerFrownBSMesh', 'L_'+faceMesh+'_lipCornerNarrowBSMesh', 'R_'+faceMesh+'_lipCornerNarrowBSMesh', 'L_'+faceMesh+'_lipCornerSmileBSMesh', 'R_'+faceMesh+'_lipCornerSmileBSMesh', 'L_'+faceMesh+'_lipCornerWideBSMesh', 'R_'+faceMesh+'_lipCornerWideBSMesh', 'L_'+faceMesh+'_lowerLipRollInBSMesh', 'R_'+faceMesh+'_lowerLipRollInBSMesh', 'L_'+faceMesh+'_lowerLipRollOutBSMesh', 'R_'+faceMesh+'_lowerLipRollOutBSMesh', 'L_'+faceMesh+'_noseSneerNorthBSMesh', 'R_'+faceMesh+'_noseSneerNorthBSMesh', 'L_'+faceMesh+'_upperLipRollInBSMesh', 'R_'+faceMesh+'_upperLipRollInBSMesh', 'L_'+faceMesh+'_upperLipRollOutBSMesh', 'R_'+faceMesh+'_upperLipRollOutBSMesh', lEyeMesh+'_pupilCloseBSMesh', rEyeMesh+'_pupilCloseBSMesh', lEyeMesh+'_pupilOpenBSMesh', rEyeMesh+'_pupilOpenBSMesh', lEyeMesh+'_irisCloseBSMesh', rEyeMesh+'_irisCloseBSMesh', lEyeMesh+'_irisOpenBSMesh', rEyeMesh+'_irisOpenBSMesh']
            lipBlendshapes = ['L_'+faceMesh+'_cornerLipUpBSMesh', 'L_'+ faceMesh +'_cornerLipDownBSMesh', 'L_'+ faceMesh +'_cornerLipOutBSMesh', 'L_'+ faceMesh +'_cornerLipInBSMesh', 'R_'+faceMesh+'_cornerLipUpBSMesh', 'R_'+ faceMesh +'_cornerLipDownBSMesh', 'R_'+ faceMesh +'_cornerLipOutBSMesh', 'R_'+ faceMesh +'_cornerLipInBSMesh' ]
            #jawBlendshapes1 = ['C_'+faceMesh+'_jawNorthBSMesh', 'C_'+faceMesh+'_jawSouthBSMesh', 'C_'+faceMesh+'_jawEastBSMesh', 'C_'+faceMesh+'_jawWestBSMesh', 'C_'+faceMesh+'_jawBackwardBSMesh', 'C_'+faceMesh+'_jawForwardBSMesh', 'C_'+lowerTeethMesh+'_jawSouthBSMesh', 'C_'+lowerTeethMesh+'_jawEastBSMesh', 'C_'+lowerTeethMesh+'_jawWestBSMesh', 'C_'+lowerTeethMesh+'_jawBackwardBSMesh', 'C_'+lowerTeethMesh+'_jawForwardBSMesh', 'C_'+tongueMesh+'_jawSouthBSMesh', 'C_'+tongueMesh+'_jawEastBSMesh', 'C_'+tongueMesh+'_jawWestBSMesh', 'C_'+tongueMesh+'_jawBackwardBSMesh', 'C_'+tongueMesh+'_jawForwardBSMesh', 'C_'+tongueMesh+'_tongueTipBackwardBSMesh', 'C_'+tongueMesh+'_tongueTipForwardBSMesh', 'C_'+tongueMesh+'_tongueTipNorthBSMesh', 'C_'+tongueMesh+'_tongueTipSouthBSMesh', 'C_'+tongueMesh+'_tongueTipWestBSMesh', 'C_'+tongueMesh+'_tongueTipEastBSMesh', 'C_'+tongueMesh+'_upBSMesh', 'C_'+tongueMesh+'_downBSMesh']
            
            #eyelidBlendshapes1 = ['L_'+faceMesh+'_upperLidInNorthBSMesh', 'R_'+faceMesh+'_upperLidInNorthBSMesh', 'L_'+faceMesh+'_upperLidMidNorthBSMesh', 'R_'+faceMesh+'_upperLidMidNorthBSMesh', 'L_'+faceMesh+'_upperLidOutNorthBSMesh', 'R_'+faceMesh+'_upperLidOutNorthBSMesh', 'L_'+faceMesh+'_upperLidInSouthBSMesh', 'R_'+faceMesh+'_upperLidInSouthBSMesh', 'L_'+faceMesh+'_upperLidMidSouthBSMesh', 'R_'+faceMesh+'_upperLidMidSouthBSMesh', 'L_'+faceMesh+'_upperLidOutSouthBSMesh', 'R_'+faceMesh+'_upperLidOutSouthBSMesh', 'L_'+faceMesh+'_lowerLidInNorthBSMesh', 'R_'+faceMesh+'_lowerLidInNorthBSMesh', 'L_'+faceMesh+'_lowerLidMidNorthBSMesh', 'R_'+faceMesh+'_lowerLidMidNorthBSMesh', 'L_'+faceMesh+'_lowerLidOutNorthBSMesh', 'R_'+faceMesh+'_lowerLidOutNorthBSMesh', 'L_'+faceMesh+'_lowerLidInSouthBSMesh', 'R_'+faceMesh+'_lowerLidInSouthBSMesh', 'L_'+faceMesh+'_lowerLidMidSouthBSMesh', 'R_'+faceMesh+'_lowerLidMidSouthBSMesh', 'L_'+faceMesh+'_lowerLidOutSouthBSMesh', 'R_'+faceMesh+'_lowerLidOutSouthBSMesh']
            #eyelidBlendshapes2 = ['L_'+faceMesh+'_upperLidNorthBSMesh', 'R_'+faceMesh+'_upperLidNorthBSMesh', 'L_'+faceMesh+'_upperLidSouthBSMesh', 'R_'+faceMesh+'_upperLidSouthBSMesh', 'L_'+faceMesh+'_lowerLidNorthBSMesh', 'R_'+faceMesh+'_lowerLidNorthBSMesh', 'L_'+faceMesh+'_lowerLidSouthBSMesh', 'R_'+faceMesh+'_lowerLidSouthBSMesh']
        else:
            mc.warning('No Data.')
        
    # ---------------------------------------------------
    # Setup #--------------------------------------
    # ---------------------------------------------------
    def toggleMesh(self):
        char = self.label_activeAsset.text()
        jsonPath=self.label_projectPath.text()+r'/Rigging/jenAutorig_projectPathNode.json'      
        publishedPath=absFunc.getSimpleJson(jsonPath, 'publishedPath')
        publishFiles=[]
        pubItems = os.listdir(publishedPath)
        if char == 'None':
            mc.warning('No character is active.')
            return

        if mc.objExists('mesh_layer') == False:
            mc.createDisplayLayer(n='mesh_layer', e=1)
            for file in pubItems:
                if ".ma" in file:
                    publishFiles.append(file)

            for x in publishFiles:
                if x.startswith('MOD_') is True:
                    filePath=publishedPath + r'/' + x                   
                    if os.path.exists(filePath):
                        mc.file(filePath, i=True, namespace='tempModel')

            for e in mc.ls('tempModel:*', type='transform'):
                mc.editDisplayLayerMembers('mesh_layer', e)

        elif mc.objExists('mesh_layer') == True:
            if mc.getAttr('mesh_layer.visibility') == 1:
                mc.setAttr('mesh_layer.visibility', 0)
            else:
                mc.setAttr('mesh_layer.visibility', 1)

    def deleteMesh(self):
        char = self.label_activeAsset.text()

        if char == 'None':
            mc.warning('No character is active.')
            return

        try:
            mc.delete('mesh_layer')
        except: 0

        absFunc.removeMesh()    

    def toggleMeshLayerDisplay(self):
        if mc.objExists('mesh_layer') == True:
            if mc.getAttr('mesh_layer.displayType') == 0:
                mc.setAttr('mesh_layer.displayType', 1)             

            elif mc.getAttr('mesh_layer.displayType') == 1:
                mc.setAttr('mesh_layer.displayType', 2)             

            elif mc.getAttr('mesh_layer.displayType') == 2:
                mc.setAttr('mesh_layer.displayType', 0)

    def importBipedTemplate(self):
        bipedPath=app_folder_win + "/" + "libs" + "/" + "jen_bipedTemplate.ma"
        mc.file(bipedPath, i=1 )

    def modules(self):
        #Creating a Root Control###############################################################################
        if mc.objExists('C_root_01_CTRL') ==False:  
            grp=mc.createNode('transform', n='rig')
            root=mc.circle(n='C_root_01_CTRL', r=50, nr=(0,1,0))[0]
            main=mc.circle(n='C_main_01_CTRL', r=40, nr=(0,1,0))[0]
            absFunc.setCurveColor(root, 'black')
            absFunc.setCurveColor(main, 'gray')

            mc.parent(main, root)       
            mc.addAttr('C_root_01_CTRL', ln='pointData', dt='string')
            dftGrp=mc.createNode('transform', n='dft_GRP')
            jointsGrp=mc.createNode('transform', n='joints_group')
            controlsGrp=mc.createNode('transform', n='controls_group')
            mc.parent(dftGrp, grp)
            mc.parent(jointsGrp, grp)
            mc.parent(controlsGrp, grp)
            mc.parent(root, controlsGrp)


        #Creating Modules#####################################################################################
        points = mc.ls('*_point')
        for i in points:            
            if mc.listRelatives(i,p=1)[0]=='Points':                
                firstPoint=i
                break           
         
        mc.select(firstPoint, hi=1)
        hi=mc.ls(sl=1)
        for rounded in hi:
            tempcoord=mc.xform(rounded, q=1, t=1, os=1)         

            posX=mc.getAttr(rounded+'.tx')
            posY=mc.getAttr(rounded+'.ty')
            posZ=mc.getAttr(rounded+'.tz')          
            mc.setAttr(rounded+'.tx', round(posX,4))
            mc.setAttr(rounded+'.ty', round(posY,4))
            mc.setAttr(rounded+'.tz', round(posZ,4))
            tempcoord=mc.xform(rounded, q=1, t=1, os=1)        
        
        #Modules##########################################################################################
        if mc.objExists('modules_group') ==False:
            mc.createNode('transform',n='modules_group')

        for joint in points:
            
            mod = joint.replace('_point','')
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Module: '+mod,2000)         
            mc.select(cl=1)
            jointPos=mc.xform(joint,q=1, t=1, ws=1)
            jointOrient=mc.xform(joint,q=1, ro=1, ws=1)

            index = points.index(joint)


            parent=mc.listRelatives(joint, p=1)
            child=mc.listRelatives(joint, c=1)
            
            # Edit Progres Bar################################      
    
            

            if mc.objExists(mod+'_module') ==False:

                sphere = mc.polySphere(n=mod+'_module',sa=8, sh=8, r=1 )[0]
                mel.eval('polyColorPerVertex -r 1 -g 1 -b 0 -a 0.4 -cdo;')
                grp= mc.createNode('transform',n=mod+'_moduleGrp' )
                mc.parent(grp, 'modules_group')
                sphereGrp=mc.createNode('transform', n=mod+'_sphereGrp')
                mc.parent(sphere, sphereGrp)
                
                for x in child:
                    if x.endswith('endpoint')==True:
                        child =x
                
                mc.pointConstraint(joint, child, sphereGrp, mo=0)
                mc.parent(sphereGrp, grp)
                absFunc.lockHide(sphere, 'all')

                mc.addAttr(sphere, ln='moduleType', at='enum', en='flow:ikStart:ikEnd:foot:hand:face:hip:ikMono:fk', k=1)
                mc.addAttr(sphere, ln='controlType', at='enum', en='box:circle:square', k=1)
                mc.addAttr(sphere, ln='showOrientation', at='enum', en='no:yes', k=1)
                mc.addAttr(sphere, ln='fkTranslate', at='enum', en='no:yes', k=1)
                mc.addAttr(sphere, ln='ribbon', at='enum', en='no:yes', k=1)
                mc.addAttr(sphere, ln='twistJoints', at='long', min=1, max=10, dv=6,  k=1)
                mc.addAttr(sphere, ln='sleeve', at='enum', en='no:yes', k=1)
                mc.addAttr(sphere, ln='customPart', at='enum', en='no:yes', k=1)                
                mc.addAttr(sphere, ln='dynamicStart', at='enum', en='no:yes', k=1)
                mc.addAttr(sphere, ln='dynamicEnd', at='enum', en='no:yes', k=1)
                mc.addAttr(sphere, ln='rotateOffset', at='float', dv=0,  k=1)
                mc.addAttr(sphere, ln='sizeA', at='float', min=0.01, dv=1,  k=1)
                mc.addAttr(sphere, ln='sizeB', at='float', min=0.01, dv=1,  k=1)
                mc.addAttr(sphere, ln='width', at='float', min=0.01, dv=1,  k=1)
                mc.addAttr(sphere, ln='depth', at='float', min=0.01, dv=1,  k=1)
            
            
            #Create orientMeshes########################################################################################        


                mc.polyTorus(r=1.2, sr=0.1, sx=12, sy=6, cuv=0, ax=(0,1,0), n='_orientMesh_')
                mc.polyColorPerVertex(r=0, b=0, g=0.6078, a=1, cdo=1)

                mc.polyTorus(r=1.2, sr=0.1, sx=12, sy=6, cuv=0, ax=(1,0,0), n='_orientMesh_')
                mc.polyColorPerVertex(r=0.667, b=0, g=0, a=1, cdo=1)

                mc.polyTorus(r=1.2, sr=0.1, sx=12, sy=6, cuv=0, ax=(0,0,1), n='_orientMesh_')
                mc.polyColorPerVertex(r=0, b=0.667, g=0, a=1, cdo=1)

                mc.polyCylinder(r=0.05, h=1.2, sx=6, sy=1, sz=0, ax=(0,1,0), n='_orientMesh_')
                mc.move(0,0.58,0)
                mc.polyColorPerVertex(r=0, b=0, g=0.6078, a=1, cdo=1)

                mc.polyCylinder(r=0.05, h=1.2, sx=6, sy=1, sz=0, ax=(1,0,0), n='_orientMesh_')
                mc.move(0.58,0,0)
                mc.polyColorPerVertex(r=0.667, b=0, g=0, a=1, cdo=1)

                mc.polyCylinder(r=0.05, h=1.2, sx=6, sy=1, sz=0, ax=(0,0,1), n='_orientMesh_')
                mc.move(0,0,0.58)
                mc.polyColorPerVertex(r=0, b=0.667, g=0, a=1, cdo=1)
                #orient sphereOrientMeshes############################################################################
                child= mc.listRelatives(joint, c=1)
                mc.select(mc.ls('_orientMesh*'))
                orientMesh=mc.polyUnite(ch=0, n=mod +'_orientMesh')
                orientGrp=mc.createNode('transform', n = mod +'_orientGrp')
                mc.parent(orientMesh, orientGrp)
                mc.parent(orientGrp,mod+'_moduleGrp')
                mc.pointConstraint(joint, orientGrp, mo=0)

                mc.xform(orientGrp, ro=jointOrient, ws=1)
                '''
                if joint.startswith('R_')==True:
                    aim=mc.aimConstraint(child, orientGrp, mo=0, wut='objectrotation', wuo=joint, aim=(1,0,0),wu=(0,0,1), u=(0,0,1))
                
                else:
                    aim=mc.aimConstraint(child, orientGrp, mo=0, wut='objectrotation', wuo=joint, aim=(0,0,0),wu=(0,0,1), u=(0,0,-1))
                '''
                mc.connectAttr(mod+'_module.showOrientation', mod+'_orientGrp.v' )
                mc.select(cl=1)
            

            #HIP###################################

                hipCircle=mc.circle(n=joint.replace('_point', '_hipModHipControlProxy'), r=11, nr=(0,1,0))
                hipSquare=mel.eval('curve -d 1 -p -12 0 -12 -p -12 0 12 -p 12 0 12 -p 12 0 -12 -p -12 0 -12 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
                hipSquare=mc.rename(hipSquare, joint.replace('_point', '_hipModBodyControlProxy'))

                hipProxyGrp=mc.createNode('transform', n=joint.replace('_point', '_hipModTextGrp'))
                mc.parent(hipCircle, hipProxyGrp)
                mc.parent(hipSquare, hipProxyGrp)
                mc.parent(hipProxyGrp, mod+'_moduleGrp')
                mc.pointConstraint(joint, hipProxyGrp, mo=0)
                mc.delete(hipSquare, hipCircle, ch=1)

                hipProxyCond=mc.createNode('condition', n=joint.replace('_point', '_hipModCond'))
                mc.connectAttr(mod+'_module.moduleType', hipProxyCond+'.firstTerm')
                mc.setAttr(hipProxyCond+'.secondTerm', 6)
                mc.setAttr(hipProxyCond+'.colorIfTrueR', 1)
                mc.setAttr(hipProxyCond+'.colorIfFalseR', 0)

                mc.connectAttr(hipProxyCond+'.outColorR', hipProxyGrp+'.v')



            #FOOT########################################################################
                footLocGrp=mc.createNode('transform', n=joint.replace('_point', '_proxyFootGRP'))
                heelLoc=mc.spaceLocator(n=joint.replace('_point', '_03FootProxyLoc'))
                tipLoc=mc.spaceLocator(n=joint.replace('_point', '_04FootProxyLoc'))
                bankExtLoc=mc.spaceLocator(n=joint.replace('_point', '_01FootProxyLoc'))
                bankIntLoc=mc.spaceLocator(n=joint.replace('_point', '_02FootProxyLoc'))
                footLoc=mc.spaceLocator(n=joint.replace('_point', '_05FootProxyLoc'))               
                mc.xform(heelLoc, t=(0,0,-3))
                mc.xform(tipLoc, t=(0,0,3))
                mc.xform(footLoc, t=(0,0,1.5))
                mc.xform(bankExtLoc, t=(3,0,0))
                mc.xform(bankIntLoc, t=(-3,0,0))


                mc.parent(heelLoc, tipLoc, bankIntLoc, bankExtLoc, footLoc, footLocGrp)
                mc.pointConstraint(joint, footLocGrp, mo=0)
                mc.parent(footLocGrp, mod+'_moduleGrp')

                footLocCond=mc.createNode('condition', n=joint.replace('_point', '_footLocGRPCond'))
                mc.connectAttr(mod+'_module.moduleType', footLocCond+'.firstTerm')
                mc.setAttr(footLocCond+'.secondTerm', 3)
                mc.setAttr(footLocCond+'.colorIfTrueR', 1)
                mc.setAttr(footLocCond+'.colorIfFalseR', 0)
                mc.connectAttr(footLocCond+'.outColorR', footLocGrp+'.v')

                footProxyCTRL=mel.eval('curve -d 1 -p -6 0 13 -p 6 0 13 -p 6 0 -15 -p -6 0 -15 -p -6 0 13 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
                footProxyCTRL=mc.rename(joint.replace('_point', '_footControlProxy'))
                footProxyGrp=mc.createNode('transform',n=joint.replace('_point', 'Grp'), p=mod+'_moduleGrp')
                mc.parent(footProxyCTRL, footProxyGrp)
                mc.pointConstraint(joint, footProxyGrp, mo=0)

                footProxyCTRLCond=mc.createNode('condition', n=joint.replace('_point', '_footLocGRPCond'))
                mc.connectAttr(mod+'_module.moduleType', footProxyCTRLCond+'.firstTerm')
                mc.setAttr(footProxyCTRLCond+'.secondTerm', 3)
                mc.setAttr(footProxyCTRLCond+'.colorIfTrueR', 1)
                mc.setAttr(footProxyCTRLCond+'.colorIfFalseR', 0)
                mc.connectAttr(footProxyCTRLCond+'.outColorR', footProxyGrp+'.v')

            #ikControlsProxy###################################################################################
                #ikHandleProxy#####
                if mc.listRelatives(joint, p=1) != None:
                    
                    ikCircleProxy=mc.circle(n= mod+'_ikControlProxy', nr=(1,0,0), r=5)[0]
                    
                    mc.delete(ch=1)

                    mc.addAttr(ikCircleProxy, ln='ikType', at='enum', en='ikHandle:ikSpline', k=1)
                    mc.addAttr(ikCircleProxy, ln='ikSplineControls', at='long', min=1, dv=1,  k=1)
                    mc.addAttr(ikCircleProxy, ln='fkSplineControls', at='long', min=1, dv=2,  k=1)
                    mc.addAttr(ikCircleProxy, ln='ikSplineTwistAxis', at='enum', en='x:y:z', k=1)
                    mc.addAttr(ikCircleProxy, ln='spaceSelect', at='enum', en='no:yes', k=1)


                    ikCircleProxyGrp=mc.createNode('transform', n= mod+'_ikControlProxyGrp')
                    mc.parent(ikCircleProxy, ikCircleProxyGrp)
                    mc.parent(ikCircleProxyGrp, mod+'_moduleGrp')
                    mc.pointConstraint(child[0], ikCircleProxyGrp, mo=0)
                    mc.orientConstraint(joint, ikCircleProxyGrp, mo=0)

                    cond=mc.createNode('condition', n=mod+'_ikControlProxyCondition')

                    mc.connectAttr(mod + '_module.moduleType', cond+'.firstTerm')
                    mc.setAttr(cond+'.secondTerm', 2)
                    mc.setAttr(cond+'.colorIfTrueR', 1)
                    mc.setAttr(cond+'.colorIfFalseR', 0)
                    mc.connectAttr(cond+'.outColorR', ikCircleProxyGrp + '.v')
                    
                #Proxy FK Control###########################################################################
                    
                    modCubeControl=mel.eval('curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')
                    modCircleControl=mc.circle(n=mod+'_fKCircleControlProxy', r=1, nr=(1,0,0))[0]
                    modSquareControl=mel.eval('curve -d 1 -p 0 0.8 0.8 -p 0 0.8 -0.8 -p 0 -0.8 -0.8 -p 0 -0.8 0.8 -p 0 0.8 0.8 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
                    modSquareControl=mc.rename(modSquareControl, mod+'_fKSquareControlProxy')
                    modCubeControl=mc.rename(modCubeControl, mod+'_fKCubeControlProxy')
                    
                    circleList=mc.ls(modCircleControl)
                    cubeList=mc.ls(modCubeControl)
                    squareList=mc.ls(modSquareControl)
                    proxyList=cubeList+circleList+squareList
                    
                    for x in proxyList:
                        index= proxyList.index(x)
                        controlCond=mc.createNode('condition', n=mod+'_fkControlTypeCondition')
                        mc.setAttr(controlCond+'.secondTerm', (index))
                        mc.setAttr(controlCond+'.operation', 0)
                        mc.setAttr(controlCond+'.colorIfTrueR', 1)
                        mc.setAttr(controlCond+'.colorIfFalseR', 0)
                        mc.connectAttr(mod+'_module.controlType', controlCond+'.firstTerm')
                        mc.connectAttr(controlCond+'.outColorR', x+'.v')
                        mc.setAttr(x + '.overrideEnabled', 1)
                        mc.setAttr(x + '.overrideColor', 1)
                    
                    mc.xform(modCubeControl,piv=(-0.5,0,0))
                    mc.xform(modCubeControl,t=(0.5,0,0))
                    mc.makeIdentity(modCubeControl, a=1)
                    modCubeControlGrp=mc.createNode('transform',n= mod+'_fKControlProxyGrp')
                    modCubeControlZtr=mc.createNode('transform',n= mod+'_fKControlProxyZtr')
                    distGrp=mc.createNode('transform', n=mod+'_distScaleGrp')

                    bsTargetA=mc.duplicate(modCubeControl, n=mod+'_bsSizeTargetA')[0]
                    bsTargetB=mc.duplicate(modCubeControl, n=mod+'_bsSizeTargetB')[0]

                    mc.select(bsTargetA+'.cv[0]')
                    mc.select(bsTargetA+'.cv[3:5]', add=1)
                    mc.select(bsTargetA+'.cv[10:13]', add=1)
                    clu1=mc.cluster()
                    mc.xform(clu1, s=(2.4,2.4,2.4))

                    mc.select(bsTargetB+'.cv[1:2]')
                    mc.select(bsTargetB+'.cv[6:9]', add=1)
                    mc.select(bsTargetB+'.cv[14:15]', add=1)
                    clu2=mc.cluster()
                    mc.xform(clu2, s=(2.4,2.4,2.4))

                    mc.delete(bsTargetA, ch=1)
                    mc.delete(bsTargetB, ch=1)

                    bsSizeNode=mc.blendShape(bsTargetA, bsTargetB, modCubeControl, n=mod+'_sizeBS')[0]
                    mc.delete(bsTargetA)
                    mc.delete(bsTargetB)

                    sizePlusMinus=mc.createNode('plusMinusAverage', n= mod+'_fixSizePlusMinus')
                    mc.setAttr(sizePlusMinus+'.operation', 1)


                    mc.connectAttr(mod+'_module.sizeA', sizePlusMinus+'.input2D[0].input2Dx')
                    mc.connectAttr(mod+'_module.sizeB', sizePlusMinus+'.input2D[0].input2Dy')

                    mc.setAttr(sizePlusMinus+'.input2D[1].input2Dx', -0.7)
                    mc.setAttr(sizePlusMinus+'.input2D[1].input2Dy', -0.7)

                    mc.connectAttr(sizePlusMinus+'.output2D.output2Dx', bsSizeNode+'.'+mod+'_bsSizeTargetA')
                    mc.connectAttr(sizePlusMinus+'.output2D.output2Dy', bsSizeNode+'.'+mod+'_bsSizeTargetB')

                    mc.distanceDimension(ep=(0,0,1), sp= (0,0,10))
                    loc1=mc.rename('locator1', mod+'_StartModuleLoc')
                    loc2=mc.rename('locator2', mod+'_EndModuleLoc')
                    dist=mc.rename('distanceDimension1', mod+'_ScaleDistDimension')
                    mc.setAttr(distGrp+'.v', 0)
                    for x in child:
                        if x.endswith('endpoint')==True:
                            child =x

                    mc.pointConstraint(joint, loc1, mo=0)
                    mc.pointConstraint(child, loc2, mo=0)
                    
                    mc.parent(modCubeControl, modCubeControlGrp)
                    mc.parent(modCircleControl, modCubeControlGrp)
                    mc.parent(modSquareControl, modCubeControlGrp)

                    mc.parent(modCubeControlGrp, modCubeControlZtr)
                    mc.parent(modCubeControlZtr, grp )
                    mc.parent(loc1, distGrp)
                    mc.parent(loc2, distGrp)
                    mc.parent(dist, distGrp)
                    mc.parent(distGrp, grp)

                    mc.xform(modCubeControlZtr, t=jointPos, ws=1)
                    mc.xform(modCubeControlZtr, ro=jointOrient, ws=1)
                    
                    mc.aimConstraint(child, modCubeControlZtr, wuo=mod+'_point', wut='objectrotation', wu=(0,0,1), u=(0,0,1))
                    mc.pointConstraint(joint, modCubeControlZtr)

                    mc.connectAttr(dist+'.distance', modCubeControl+'.sx')
                    mc.connectAttr(mod+'_module.rotateOffset', modCubeControlGrp+'.rx')                    
                    
                    mc.connectAttr(mod+'_module.width', modCubeControlGrp+'.sz')
                    mc.connectAttr(mod+'_module.depth', modCubeControlGrp+'.sy')

                #Hand---------------------------------------------------------------------------
                hControl=mel.eval('curve -d 1 -p 0 0 -0.1 -p 0.2 0 -0.1 -p 0.2 0 -0.5 -p 0.4 0 -0.5 -p 0.4 0 0.5 -p 0.2 0 0.5 -p 0.2 0 0.1 -p 0 0 0.1 -p -0.2 0 0.1 -p -0.2 0 0.5 -p -0.4 0 0.5 -p -0.4 0 -0.5 -p -0.2 0 -0.5 -p -0.2 0 -0.1 -p 0 0 -0.1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 ;')
                hControl=mc.rename(mod+'_handControlProxy')
                hGRP=mc.createNode('transform', n=mod+'_handControlProxyGrp')
                mc.parent(hControl, hGRP)
                mc.parent(hGRP, mod+'_moduleGrp')
                mc.pointConstraint(joint, hGRP, mo=0)
                mc.orientConstraint(joint, hGRP, mo=0)

                cond=mc.createNode('condition', n=mod+'_handControlProxyCondition')
                mc.connectAttr(mod + '_module.moduleType', cond+'.firstTerm')
                mc.setAttr(cond+'.secondTerm', 4)
                mc.setAttr(cond+'.colorIfTrueR', 1)
                mc.setAttr(cond+'.colorIfFalseR', 0)
                mc.connectAttr(cond+'.outColorR', hGRP + '.v')

                mc.addAttr(hControl, ln='curlAxis', at='enum', en='z:y:X', k=1)
                mc.addAttr(hControl, ln='spreadAxis', at='enum', en='y:x:z', k=1)

                #SleeveTwist-----------------------------------------------------------------------
                sleeveGrp=mc.createNode('transform', n=mod+'_sleeveProxyGrp', p=mod+'_moduleGrp')
                mainControl=mc.circle(n=mod+'_sleeveMainControlProxy', r=4, nr=(1,0,0))[0]
                mc.parent(mainControl, sleeveGrp)
                '''
                if mod.startswith('R_')==True:
                    mc.setAttr(sleeveGrp+'.sx', -1)
                '''
                for i in range (0,4):
                    index= range(0,4).index(i)
                    sleeveControl=mel.eval('curve -d 1 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')
                    sleeveControl=mc.rename(mod+'_'+str(index)+'_sleeveControlProxy')
                    sleeveControlGRP=mc.createNode('transform', n=mod+'_'+str(index)+'_sleeveControlProxyGrp', p=mainControl)
                    mc.parent(sleeveControl, sleeveControlGRP)                    
                    if index ==0:
                        mc.setAttr(sleeveControlGRP+'.ty', 3)
                    elif index==1:
                        mc.setAttr(sleeveControlGRP+'.tz', 3)
                    elif index==2:
                        mc.setAttr(sleeveControlGRP+'.ty', -3)
                    elif index==3:
                        mc.setAttr(sleeveControlGRP+'.tz', -3)
                    
                mc.delete(mc.pointConstraint(joint, sleeveGrp, mo=0))
                mc.parentConstraint(joint, sleeveGrp, mo=1)

                cond=mc.createNode('condition', n=mod+'_sleeveControlProxyCondition')
                mc.connectAttr(mod + '_module.sleeve', cond+'.firstTerm')
                mc.setAttr(cond+'.secondTerm', 1)
                mc.setAttr(cond+'.colorIfTrueR', 1)
                mc.setAttr(cond+'.colorIfFalseR', 0)
                mc.connectAttr(cond+'.outColorR', sleeveGrp + '.v')
                
                # Face Module Setup-------------------------------------------------------------------------------------
                # Face Main Control-------------------------------------------------------------------------------------
                self.facePR = prF.faceProxy(mod)
                mc.parent(self.facePR.faceGroup, mod + '_moduleGrp')

                cond=mc.createNode('condition', n=mod+'_faceControlProxyCondition')
                mc.connectAttr(mod + '_module.moduleType', cond+'.firstTerm')
                mc.setAttr(cond+'.secondTerm', 5)
                mc.setAttr(cond+'.colorIfTrueR', 1)
                mc.setAttr(cond+'.colorIfFalseR', 0)
                mc.connectAttr(cond+'.outColorR', self.facePR.faceGroup + '.v')

                # Head Parts-------------------------------------------------------------------------------------------------                
                self.headPartsSetup = headSetup.HeadParts(mod, 0)                
                mc.parent(self.headPartsSetup.upperControl, self.facePR.lowerUpperHead)
                mc.parent(self.headPartsSetup.lowerControl, self.facePR.lowerUpperHead)
                mc.connectAttr(self.facePR.lowerUpperHead + '.showSetup', self.headPartsSetup.upperControl + '.v')
                mc.connectAttr(self.facePR.lowerUpperHead + '.showSetup', self.headPartsSetup.lowerControl + '.v')

                # Eye-------------------------------------------------------------------------------------------------                
                self.eyeRigL = eyeSetup.eyeRigSetup('eye', mod, 3)
                self.eyeRigR = eyeSetup.eyeRigSetup('eye', mod, -3)
                mc.parent(self.eyeRigL.group, self.facePR.eyesControl)
                mc.parent(self.eyeRigR.group, self.facePR.eyesControl)
                mc.connectAttr(self.facePR.eyesControl + '.showSetup', self.eyeRigL.group + '.v')
                mc.connectAttr(self.facePR.eyesControl + '.showSetup', self.eyeRigR.group + '.v')
                
                # Eyebrow --------------------------------------------------------------------------------------------
                
                self.eyebrow = eyebr.eyebrowSetup('eyebrow', module = mod, height = 3)               
                mc.parent(self.eyebrow.maingroup, self.facePR.eyebrowControl)                
                mc.connectAttr(self.facePR.eyebrowControl + '.showSetup', self.eyebrow.maingroup + '.v')                
                
                mc.parent(self.eyebrow.curveGroup, mod + '_moduleGrp')                
                mc.connectAttr(self.facePR.eyebrowControl + '.showSetup', self.eyebrow.curveGroup + '.v')
                
                # UpperCheek------------------------------------------------------------------------------------------

                self.upperCheekL = uprCheek.upperChSetup('upperCheek', module = mod, mirror = False, height = -2)
                self.upperCheekR = uprCheek.upperChSetup('upperCheek', module =  mod, mirror = True, height = -2)
                mc.parent(self.upperCheekL.maingroup, self.facePR.upperCheekControl)
                mc.parent(self.upperCheekR.maingroup, self.facePR.upperCheekControl)
                mc.connectAttr(self.facePR.upperCheekControl + '.showSetup', self.upperCheekL.maingroup + '.v')
                mc.connectAttr(self.facePR.upperCheekControl + '.showSetup', self.upperCheekR.maingroup + '.v')
                
                mc.parent(self.upperCheekL.curveGroup, mod + '_moduleGrp')
                mc.parent(self.upperCheekR.curveGroup, mod + '_moduleGrp')
                mc.connectAttr(self.facePR.upperCheekControl + '.showSetup', self.upperCheekL.curveGroup + '.v')
                mc.connectAttr(self.facePR.upperCheekControl + '.showSetup', self.upperCheekR.curveGroup + '.v')
                

                mc.pointConstraint(joint, child, self.facePR.faceGroup)

            #mc.refresh()
        #mirroring orientations######################################################################
        leftOrient=mc.ls('L_*_orientMesh')
        for x in leftOrient:
            y=x.replace('L_', 'R_')
            axisMD=mc.createNode('multiplyDivide', n=x.replace('_orientMesh','_AxisMirrorMD'))
            axisPM=mc.createNode('plusMinusAverage', n=x.replace('_orientMesh','_AxisMirrorPM'))
            

            mc.connectAttr(x+'.rx', axisPM+'.input1D[0]')
            mc.connectAttr(axisPM+'.output1D', y+'.rx')
            
            mc.connectAttr(x+'.ry', axisMD+'.input1Y')
            mc.connectAttr(axisMD+'.outputY', y+'.ry')
            
            mc.connectAttr(x+'.rz', axisMD+'.input1Z')
            mc.connectAttr(axisMD+'.outputZ', y+'.rz')

        #mirroring sleeves--------------------------------------------------------------------------
        '''
        leftSleeves=mc.ls('L_*_sleeve*ontrolProxy')
        
        for x in leftSleeves:
            y=x.replace('L_', 'R_')
            
            mc.connectAttr(x+'.t', y+'.t')
            mc.connectAttr(x+'.r', y+'.r')
            mc.connectAttr(x+'.s', y+'.s')
        '''
        

        self.statusBar.setStyleSheet("QStatusBar{color:rgb(3, 255, 11);background-color: rgb(30, 30, 30);}")
        self.statusBar.showMessage('Modules Created', 15000)

    def deleteMod(self):
        sel=mc.ls(sl=1) 

        for x in sel:
            if x.endswith('_module'):
                mel.eval('pickWalk -d up;')
                mel.eval('pickWalk -d up;')
                mc.delete()
            else:
                pass

    def mirrorParameters(self):
    
        leftSide=mc.ls('L_*_module')
        footLocators=mc.ls('L_*ProxyLoc')
        proxyControls=mc.ls('L_*ControlProxy')
        for x in leftSide:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Mirroring: '+x,2000)
            y=x.replace('L_', 'R_')
            mc.copyAttr(x, y, values=1)
            roOff=mc.getAttr(y+'.rotateOffset')*-1
            mc.setAttr(y+'.rotateOffset',roOff)

        for x in footLocators:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Mirroring: '+x,2000)
            y=x.replace('L_', 'R_')
            coord=mc.xform(x, q=1, t=1, ws=1)
            tx=coord[0]*-1
            ty=coord[1]
            tz=coord[2]

            mc.xform(y, t=(tx, ty, tz), ws=1)

        for x in proxyControls:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Mirroring: '+x,2000)
            y=x.replace('L_', 'R_')
            mc.copyAttr(x, y, values=1)     

        self.statusBar.setStyleSheet("QStatusBar{color:rgb(3, 255, 11);background-color: rgb(30, 30, 30);}")
        self.statusBar.showMessage('Mirrored', 15000)

    def separateMesh(self):
        sel = mc.ls(sl=1)
        mc.ConvertSelectionToVertices()
        selObj = sel[0].split('.')[0]
        mc.polySplitEdge(sel, operation=1)
        objs = mc.polySeparate(selObj)

        for o in objs[0:-1]:
            mc.polyCloseBorder(o)
            mc.xform(o, cp=1)
            # mc.polyColorPerVertex(o, cdo=1)

        for o in objs:
            try:
                mc.parent(o, 'loMesh_group')
            except: 0

        mc.select(mc.listRelatives('loMesh_group', c=1), r=1)
        mc.delete(ch=1)

        mc.select(d=1)

    def mirrorSelected(self):
        sel = mc.ls(sl=1)
        tNode = mc.createNode('transform')
        dups = []
        for e in sel:
            if e[0] == 'L':
                mirName = 'R'+e[1:]
            elif e[0] == 'R':
                mirName = 'L'+e[1:]
            else:
                mirName = e+'Mirror'

            dup = mc.duplicate(e, n=mirName)[0]
            mc.select(dup)
            dups.append(dup)
            mc.parent(dup, tNode)
            #joint = mc.getAttr(dup+'.joint')
            #if joint[0] == 'L':
                #joint = joint.replace('L_', 'R_')
            #elif joint[0] == 'R':
                #joint = joint.replace('R_', 'L_')

            #mc.setAttr(dup+'.joint', joint, type='string')

        mc.setAttr(tNode+'.sx', -1)

        for e in dups:
            mc.parent(e, 'loMesh_group')
            mc.makeIdentity(e, apply=1)
            mc.select(e, r=1)
            mc.polySetToFaceNormal()
            mc.polyAverageNormal()

            mc.delete(tNode)

    def storeData(self):
        moduleDict={}

        modules=mc.ls('*_module')
        for i in modules:
            attributes=mc.listAttr(i, ud=1, hd=1)           
            attrsDict = {}
            for x in attributes:
                attrValue=mc.getAttr(i+'.'+x)
                attrsDict[x]= attrValue
            moduleDict[i] = attrsDict                   
        
        setupDataPath= self.label_projectPath.text()+r'/Rigging/setup/setupData'
        with open(setupDataPath + r'/' + 'modulesData'+ '.json', 'w') as outfile:
            json.dump(moduleDict, outfile, sort_keys=1, indent=4)
        
        #___Controls______________________
        controlProxyDict={}

        controls=mc.ls('*ControlProxy')

        for i in controls:
            attributes=mc.listAttr(i, k=1)
            attrsControlDict={}
            for x in attributes:
                attrValue=mc.getAttr(i+'.'+x)
                attrsControlDict[x]=attrValue
            controlProxyDict[i]=attrsControlDict
        
        with open(setupDataPath + r'/' + 'proxyControlsData'+ '.json', 'w') as outfile:
            json.dump(controlProxyDict, outfile, sort_keys=1, indent=4)

        #____Locators_________________
        locProxyDict={}
        locators=mc.ls('*ProxyLoc')

        for i in locators:
            attributes=mc.listAttr(i, k=1)
            attrsLocatorsDict={}
            for x in attributes:
                attrValue=mc.getAttr(i+'.'+x)
                attrsLocatorsDict[x]=attrValue
            locProxyDict[i]=attrsLocatorsDict
        
        with open(setupDataPath + r'/' + 'proxyLocatorsData'+ '.json', 'w') as outfile:
            json.dump(locProxyDict, outfile, sort_keys=1, indent=4)

        #____Orientations_____________
        orientationMeshesDict={}
        orientMeshes=mc.ls('*orientMesh')

        for i in orientMeshes:
            attributes=mc.listAttr(i, k=1)
            attrsOrientMeshesDict={}
            for x in attributes:
                attrValue=mc.getAttr(i+'.'+x)
                attrsOrientMeshesDict[x]=attrValue
            orientationMeshesDict[i]=attrsOrientMeshesDict
        
        with open(setupDataPath + r'/' + 'orientMeshesData'+ '.json', 'w') as outfile:
            json.dump(orientationMeshesDict, outfile, sort_keys=1, indent=4)

        #______sleeves______________

        sleevesDict={}
        sleevesControl=mc.ls('*sleeve*ontrolProxy')

        for i in sleevesControl:            
            attributes=mc.listAttr(i, k=1)
            attrsSleeveDict={}
            for x in attributes:
                attrValue=mc.getAttr(i+'.'+x)
                attrsSleeveDict[x]=attrValue
            sleevesDict[i]=attrsSleeveDict
        
        
        with open(setupDataPath + r'/' + 'sleevesData'+ '.json', 'w') as outfile:
            json.dump(sleevesDict, outfile, sort_keys=1, indent=4)

        #____Groups_________________
        grpProxyDict={}
        groups=mc.ls('*ProxyGrp')

        for i in groups:
            attributes=mc.listAttr(i, k=1)
            attrsGroupsDict={}
            for x in attributes:
                attrValue=mc.getAttr(i+'.'+x)
                attrsGroupsDict[x]=attrValue
            grpProxyDict[i]=attrsGroupsDict
        
        with open(setupDataPath + r'/' + 'proxyGroupsData'+ '.json', 'w') as outfile:
            json.dump(grpProxyDict, outfile, sort_keys=1, indent=4)


        ##################################
        #setupData for generation:########
        ##################################
        points=mc.ls('*point')      
        #_Dicts________
        hipModule={}
        ikModule={}
        footModule={}
        handModule={}
        jointsData={}
        ikMonoModule={}
        sleevesModule={}
        headModule={}
        wireDict={}

        faceLowerUpperHeadDict={}
        faceEyeDict={}
        faceEyebrowDict={}
        faceUpperCheekDict={}
        
        #______________ 
        hip=[]  
        for x in points:
            parent=mc.listRelatives(x, p=1)[0]
            if parent.endswith('point')==False:
                hip.append(x)
                break

        mc.select(hip,hi=1)
        allPoints=mc.ls(sl=1)
        skinJoints=[]

        for x in allPoints:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Saving: '+x,2000)

            finalPath=mc.getAttr('jenAutorig_projectPathNode.finalPath')
            if not os.path.exists(finalPath+r'/setup/setupData/setupGenerateData'):
                os.makedirs(finalPath+r'/setup/setupData/setupGenerateData')

            setupGenerateDir=finalPath+r'/setup/setupData/setupGenerateData'

            skinJoint=x.replace('point', 'JNT')
            module=x.replace('point', 'module')
            orientMesh=x.replace('point','orientMesh')
            if mc.objExists(module)==True:
                module=x.replace('point', 'module')
                moduleType=mc.getAttr(module+'.moduleType')
                ribbon=mc.getAttr(module+'.ribbon')
                sleeve=mc.getAttr(module+'.sleeve')

                #HIP#-------------------------------------------------------------------------------
                if moduleType==6:
                    hipPos=mc.xform(x,q=1, t=1, ws=1)
                    hipOrient=mc.xform(orientMesh, q=1, ro=1, ws=1)
                    name=x.replace('point', 'JNT')
                    bodyControl=x.replace('point', 'hipModBodyControlProxy')
                    hipControl=x.replace('point', 'hipModHipControlProxy')

                    hipModule['name']=name
                    hipModule['translate']=hipPos
                    hipModule['orientation']=hipOrient
                    hipModule['bodyControl']=bodyControl
                    hipModule['hipControl']=hipControl
                    with open(setupGenerateDir + r'/' + 'hipData'+ '.json', 'w') as outfile:
                        json.dump(hipModule, outfile, sort_keys=1, indent=4)

                #IK#--------------------------------------------------------------------------------                            
                
                if moduleType==1:
                    jointDict={}
                    ikJoints=[]
                    #ikStart=[]
                    #ikEnd=[]                   
                    keyNameJoint=x.replace('point', 'JNT')

                    mc.select(x, hi=1)
                    ikSel=mc.ls(sl=1)
                    for i in ikSel:
                        index=ikSel.index(i)
                        
                        if index==0:
                            start=i.replace('point','JNT')
                            #ikStart.append(start)
                            ikStart=start
                            if mc.listRelatives(i, p=1)!=None:
                                ikStartParent=mc.listRelatives(i, p=1)[0]
                                ikStartParent=ikStartParent.replace('point', 'JNT')
                            else:
                                ikStartParent='None'

                        content=i.replace('point','JNT')
                        ikJoints.append(content)
                        
                        mTyp=mc.getAttr(i.replace('point', 'module')+'.moduleType')                     
                        if mTyp == 2:
                            child=mc.listRelatives(i, c=1, type='joint')
                            if mc.listRelatives(child, c=1, type='joint')!=None:
                                ikEndChild=mc.listRelatives(child, c=1, type='joint')
                                ikEndChild=ikEndChild[0].replace('point', 'JNT')
                            else:
                                ikEndChild='None'

                            child=child[0].replace('point','JNT')
                            ikJoints.append(child)
                            #ikEnd.append(child)
                            ikEnd=child
                            ikControl=i.replace('point', 'ikControlProxy')

                            break
                    jointDict['ikJoints']=ikJoints
                    jointDict['ikStart']=ikStart
                    jointDict['ikEnd']=ikEnd
                    jointDict['ikControl']=ikControl
                    jointDict['ikEndChild']=ikEndChild
                    jointDict['ikStartParent']=ikStartParent
                    ikModule[keyNameJoint] = jointDict
                    with open(setupGenerateDir + r'/' + 'ikData'+ '.json', 'w') as outfile:
                        json.dump(ikModule, outfile, sort_keys=1, indent=4)

                #FOOT-----------------------------------------------------------------------------
                
                if moduleType==3:
                    #Joints:
                    footJointDict={}
                    footJoints=[]
                    keyNameJoint=x.replace('point','JNT')
                    dad=mc.listRelatives(x, p=1)
                    switch=dad[0].replace('point', 'switchCTRL')
                    footIkControl=x.replace('point','footControlProxy')

                    footLocators=[]

                    temp=mc.select(x, hi=1)
                    temp=mc.ls(sl=1)
                    for j in temp:
                        k=j.replace('point', 'JNT')
                        footJoints.append(k)
                    
                    footJointDict['joints']=footJoints

                    #Locators:
                    locators=mc.ls(x.replace('point','*FootProxyLoc'))
                    for i in locators:
                        footLocators.append(i)
                    footParent=dad[0].replace('point', 'JNT')
                    
                    footJointDict['locators']=footLocators
                    footJointDict['switchControl']=switch
                    footJointDict['mainJoint']=keyNameJoint
                    footJointDict['footParent']=footParent
                    footJointDict['footIkControl']=footIkControl
                    
                    footModule[keyNameJoint]=footJointDict
                    with open(setupGenerateDir + r'/' + 'footData'+ '.json', 'w') as outfile:
                        json.dump(footModule, outfile, sort_keys=1, indent=4)

                #HAND-------------------------------------------------------------------------
                
                if moduleType ==4:

                    handDict={}

                    keyNameJoint=x.replace('point','JNT')
                    setupControl=x.replace('point', 'handControlProxy')
                    dad=mc.listRelatives(x, p=1)
                    switch=dad[0].replace('point', 'switchCTRL')

                    fingerJoints=[]
                    
                    temp=mc.select(x, hi=1)
                    temp=mc.ls(sl=1)
                    for i in temp:
                        index=temp.index(i)
                        y=i.replace('point','JNT')
                        if index ==0:
                            handJoint=y
                        else:
                            fingerJoints.append(y)

                    attrs=mc.listAttr(setupControl, ud=1)

                    handDict['handJoint']=handJoint
                    handDict['fingerJoints']=fingerJoints
                    handDict['handControl']=setupControl
                    handDict['switchControl']=switch

                    handModule[keyNameJoint]=handDict
                    with open(setupGenerateDir + r'/' + 'handData'+ '.json', 'w') as outfile:
                        json.dump(handModule, outfile, sort_keys=1, indent=4)
                #IKMONO--------------------------------------------------------------------------
                if moduleType ==7:

                    ikMonoDict={}

                    keyNameJoint=x.replace('point','JNT')
                    parent=mc.listRelatives(x, p=1)[0].replace('point','JNT')
                    child=mc.listRelatives(x, c=1)[0].replace('point','JNT')
                    ikMonoList=[keyNameJoint]+[child]

                    ikMonoDict['joint']=keyNameJoint
                    ikMonoDict['parent']=parent
                    ikMonoDict['child']=child
                    ikMonoDict['ikMonoList']=ikMonoList

                    ikMonoModule[keyNameJoint]=ikMonoDict
                    with open(setupGenerateDir + r'/' + 'ikMono'+ '.json', 'w') as outfile:
                        json.dump(ikMonoModule, outfile, sort_keys=1, indent=4)

                #sleeves--------------------------------------------------------------------------
                if ribbon==1:
                    if sleeve==1:
                        keyNameJoint=x.replace('point','JNT')
                        name=x.replace('point', '')
                        sleeveDict={}
                        sleeveMain=x.replace('point', 'sleeveMainControlProxy')
                        controls=mc.ls(name+'*sleeveControlProxy')
                        
                        sleeveDict['main']=sleeveMain
                        sleeveDict['controls']=controls

                        sleevesModule[keyNameJoint]=sleeveDict
                    with open(setupGenerateDir + r'/' + 'sleeveData'+ '.json', 'w') as outfile:
                        json.dump(sleevesModule, outfile, sort_keys=1, indent=4)

                #face--------------------------------------------------------------------------
                if moduleType == 5:                   

                    headPos=mc.xform(x,q=1, t=1, ws=1)
                    headOrient=mc.xform(orientMesh, q=1, ro=1, ws=1)
                    name=x.replace('point', 'JNT')
                    parent=mc.listRelatives(x, p=1)[0].replace('point','JNT')
                    child=mc.listRelatives(x, c=1)[0].replace('point','JNT')

                    headModule['name']=name
                    headModule['translate']=headPos
                    headModule['orientation']=headOrient
                    headModule['parent']=parent
                    headModule['child']=child
                    
                    with open(setupGenerateDir + r'/' + 'headData'+ '.json', 'w') as outfile:
                        json.dump(headModule, outfile, sort_keys=1, indent=4)

                    #ProxyFaceWires--------------------------------------------------------------------
                    
                    wires={}
                    part = x.replace('point', '')
                    wiresControl = mc.ls(part +'*CurveWireProxy')

                    curves = []
                    for i in wiresControl:
                        parent=mc.listRelatives(i, p=1)[0]
                        if mc.getAttr(parent + '.v') == 1:
                            curves.append(i)
                        
                    wires['joint'] = name
                    wires['allCurves'] = curves

                    wireDict[name]=wires
                    with open(setupGenerateDir + r'/' + 'faceWireData'+ '.json', 'w') as outfile:
                            json.dump(wireDict, outfile, sort_keys=1, indent=4)

                    # Proxy face Components -----------------------------------------------------------------
                    # Upper/Lower Head
                    lowerUpperHeadComp = {}
                    if mc.getAttr(part + 'C_face_ControlProxy.lowerUpperHead') == 1:
                        lowerUpperHeadComp['C_upperHeadCtrl'] = part + 'C_upperHead_ControlProxy'
                        lowerUpperHeadComp['C_upperHeadLOC'] = part + 'C_upperHead_ProxyLoc'
                        lowerUpperHeadComp['C_lowerHeadCtrl'] = part + 'C_lowerHead_ControlProxy'
                        lowerUpperHeadComp['C_lowerHeadLOC'] = part + 'C_lowerHead_ProxyLoc'
                        

                    faceLowerUpperHeadDict[name]=lowerUpperHeadComp
                    with open(setupGenerateDir + r'/' + 'faceLowerUpperHeadCompData'+ '.json', 'w') as outfile:
                        json.dump(faceLowerUpperHeadDict, outfile, sort_keys=1, indent=4)

                    #Eyebrows
                    eyebrowComponents = {}
                    if mc.getAttr(part + 'C_face_ControlProxy.eyebrow') == 1:
                        eyebrowComponents['L_innerCtrl'] = part + 'L_eyebrow_inner_ControlProxy'
                        eyebrowComponents['L_innerLOC'] = part + 'L_eyebrow_inner_ProxyLoc'
                        eyebrowComponents['R_innerCtrl'] = part + 'R_eyebrow_inner_ControlProxy'
                        eyebrowComponents['R_innerLOC'] = part + 'R_eyebrow_inner_ProxyLoc'

                        eyebrowComponents['L_midCtrl'] = part + 'L_eyebrow_mid_ControlProxy'
                        eyebrowComponents['L_midLOC'] = part + 'L_eyebrow_mid_ProxyLoc'
                        eyebrowComponents['R_midCtrl'] = part + 'R_eyebrow_mid_ControlProxy'
                        eyebrowComponents['R_midLOC'] = part + 'R_eyebrow_mid_ProxyLoc'

                        eyebrowComponents['L_outerCtrl'] = part + 'L_eyebrow_outer_ControlProxy'
                        eyebrowComponents['L_outerLOC'] = part + 'L_eyebrow_outer_ProxyLoc'
                        eyebrowComponents['R_outerCtrl'] = part + 'R_eyebrow_outer_ControlProxy'
                        eyebrowComponents['R_outerLOC'] = part + 'R_eyebrow_outer_ProxyLoc'

                        eyebrowComponents['C_centerCtrl'] = part + 'C_eyebrow_center_ControlProxy'
                        eyebrowComponents['C_centerLOC'] = part + 'C_eyebrow_center_ProxyLoc'

                        eyebrowComponents['L_masterCtrl'] = part + 'L_eyebrow_master_ControlProxy'
                        eyebrowComponents['L_masterLOC'] = part + 'L_eyebrow_master_ProxyLoc'

                        eyebrowComponents['R_masterCtrl'] = part + 'R_eyebrow_master_ControlProxy'
                        eyebrowComponents['R_masterLOC'] = part + 'R_eyebrow_master_ProxyLoc'

                    faceEyebrowDict[name]=eyebrowComponents
                    with open(setupGenerateDir + r'/' + 'faceEyebrowComponentsData'+ '.json', 'w') as outfile:
                        json.dump(faceEyebrowDict, outfile, sort_keys=1, indent=4)

                    # Eyes
                    eyeComponents = {}
                    if mc.getAttr(part + 'C_face_ControlProxy.eyes') == 1:                        
                        #AngleGroup
                        eyeComponents['L_angle'] = mc.getAttr(part + 'L_eye_ProxyGrp.lidsAngle')
                        eyeComponents['R_angle'] = mc.getAttr(part + 'R_eye_ProxyGrp.lidsAngle')

                        #Socket
                        eyeComponents['L_socketCtrl'] = part + 'L_eye_socket_ControlProxy'
                        eyeComponents['R_socketCtrl'] = part + 'R_eye_socket_ControlProxy'
                        eyeComponents['L_socketLOC'] = part + 'L_eye_socket_ProxyLoc'
                        eyeComponents['R_socketLOC'] = part + 'R_eye_socket_ProxyLoc'

                        #Center
                        eyeComponents['L_eyeCtrl'] = part + 'L_eye_center_ControlProxy'
                        eyeComponents['R_eyeCtrl'] = part + 'R_eye_center_ControlProxy'
                        eyeComponents['L_eyeLOC'] = part + 'L_eye_center_ProxyLoc'
                        eyeComponents['R_eyeLOC'] = part + 'R_eye_center_ProxyLoc'

                        #Pupil
                        eyeComponents['L_pupilLOC'] = part + 'L_eye_pupil_ProxyLoc'
                        eyeComponents['R_pupilLOC'] = part + 'R_eye_pupil_ProxyLoc'

                        #UpperLid2
                        eyeComponents['L_upperLidCtrl'] = part + 'L_eye_upperLid_02_ControlProxy'
                        eyeComponents['R_upperLidCtrl'] = part + 'R_eye_upperLid_02_ControlProxy'
                        eyeComponents['L_upperLidLOC'] = part + 'L_eye_upperLid_02_ProxyLoc'
                        eyeComponents['R_upperLidLOC'] = part + 'R_eye_upperLid_02_ProxyLoc'

                        #LowerLid2
                        eyeComponents['L_lowerLidCtrl'] = part + 'L_eye_lowerLid_02_ControlProxy'
                        eyeComponents['R_lowerLidCtrl'] = part + 'R_eye_lowerLid_02_ControlProxy'
                        eyeComponents['L_lowerLidLOC'] = part + 'L_eye_lowerLid_02_ProxyLoc'
                        eyeComponents['R_lowerLidLOC'] = part + 'R_eye_lowerLid_02_ProxyLoc'

                        #UpperLid1                        
                        eyeComponents['L_upperLidBaseLOC'] = part + 'L_eye_upperLid_01_ProxyLoc'
                        eyeComponents['R_upperLidBaseLOC'] = part + 'R_eye_upperLid_01_ProxyLoc'

                        #LowerLid1                        
                        eyeComponents['L_lowerLidBaseLOC'] = part + 'L_eye_lowerLid_01_ProxyLoc'
                        eyeComponents['R_lowerLidBaseLOC'] = part + 'R_eye_lowerLid_01_ProxyLoc'

                    faceEyeDict[name]=eyeComponents
                    with open(setupGenerateDir + r'/' + 'faceEyeComponentsData'+ '.json', 'w') as outfile:
                            json.dump(faceEyeDict, outfile, sort_keys=1, indent=4)

                    # UpperCheek
                    upperCheekComponents = {}

                    if mc.getAttr(part + 'C_face_ControlProxy.upperCheek') == 1:
                        upperCheekComponents['L_innerCtrl'] = part + 'L_upperCheek_inner_ControlProxy'
                        upperCheekComponents['L_innerLOC'] = part + 'L_upperCheek_inner_ProxyLoc'
                        upperCheekComponents['R_innerCtrl'] = part + 'R_upperCheek_inner_ControlProxy'
                        upperCheekComponents['R_innerLOC'] = part + 'R_upperCheek_inner_ProxyLoc'

                        upperCheekComponents['L_midCtrl'] = part + 'L_upperCheek_mid_ControlProxy'
                        upperCheekComponents['L_midLOC'] = part + 'L_upperCheek_mid_ProxyLoc'
                        upperCheekComponents['R_midCtrl'] = part + 'R_upperCheek_mid_ControlProxy'
                        upperCheekComponents['R_midLOC'] = part + 'R_upperCheek_mid_ProxyLoc'

                        upperCheekComponents['L_outerCtrl'] = part + 'L_upperCheek_outer_ControlProxy'
                        upperCheekComponents['L_outerLOC'] = part + 'L_upperCheek_outer_ProxyLoc'
                        upperCheekComponents['R_outerCtrl'] = part + 'R_upperCheek_outer_ControlProxy'
                        upperCheekComponents['R_outerLOC'] = part + 'R_upperCheek_outer_ProxyLoc'

                    faceUpperCheekDict[name]=upperCheekComponents
                    with open(setupGenerateDir + r'/' + 'faceUpperCheekComponentsData'+ '.json', 'w') as outfile:
                        json.dump(faceUpperCheekDict, outfile, sort_keys=1, indent=4)
                    

            #FK-------------------------------------------------------------------------
            fkData={}
            keyName=x.replace('point','JNT')
            jointPosition=mc.xform(x, q=1,t=1, ws=1)    

            jointOrientationX=mc.getAttr(x+'.jointOrientX')
            jointOrientationY=mc.getAttr(x+'.jointOrientY')
            jointOrientationZ=mc.getAttr(x+'.jointOrientZ')
            jointOrientation=[jointOrientationX, jointOrientationY, jointOrientationZ]  
            if mc.objExists(orientMesh)==True:
                worldOrientation=mc.xform(orientMesh, q=1, ro=1, ws=1)
                attr=mc.getAttr(module+'.controlType')
                if attr==0:
                    fkControlName=x.replace('point', 'fKCubeControlProxy')
                elif attr==1:
                    fkControlName=x.replace('point', 'fKCircleControlProxy')
                elif attr==2:
                    fkControlName=x.replace('point', 'fKSquareControlProxy')
            else:
                pass
        
            fkData['translate']=jointPosition
            fkData['jointOrient']=jointOrientation
            if mc.objExists(orientMesh)==True:
                fkData['worldOrient']=worldOrientation
                fkData['controlName']=fkControlName
            else:
                fkData['worldOrient']='None'
                fkData['controlName']='None'
            

            jointsData[keyName]=fkData
            
            with open(setupGenerateDir + r'/' + 'jointsData'+ '.json', 'w') as outfile:
                json.dump(jointsData, outfile, sort_keys=1, indent=4)
            

        self.statusBar.setStyleSheet("QStatusBar{color:rgb(3, 255, 11);background-color: rgb(30, 30, 30);}")
        self.statusBar.showMessage('Modules Data Saved', 15000)
        sys.stdout.write("Modules Data Saved.")

    def loadModData(self):
        modulePath=self.label_projectPath.text()+r'/Rigging/setup/setupData/modulesData.json'
        modules=mc.ls('*_module')
        controlsPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/proxyControlsData.json'
        controls=mc.ls('*ControlProxy')
        locatorsPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/proxyLocatorsData.json'
        locators=mc.ls('*ProxyLoc')
        orientMeshesPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/orientMeshesData.json'
        orientMeshes=mc.ls('*orientMesh')
        sleevesPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/sleevesData.json'
        sleeves=mc.ls('L_*_sleeve*ontrolProxy')
        groupsPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/proxyGroupsData.json'
        groups=mc.ls('*ProxyGrp')

        for x in modules:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Loading: '+x,2000)  
            attributes=mc.listAttr(x, ud=1, hd=1)
            for i in attributes:
                value=absFunc.getDoubleDictJson(modulePath, x, i)
                try:
                    mc.setAttr(x+'.'+i, value)                      
                except: 0

        for x in controls:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Loading: '+x,2000)  
            attributes=mc.listAttr(x, k=1)
            for i in attributes:
                value=absFunc.getDoubleDictJson(controlsPath, x, i)
                try:
                    mc.setAttr(x+'.'+i, value)
                except: 0
                                            

        for x in locators:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Loading: '+x,2000)
            attributes=mc.listAttr(x, k=1)
            for i in attributes:
                value=absFunc.getDoubleDictJson(locatorsPath, x, i)
                try:
                    mc.setAttr(x+'.'+i, value)
                except:0 

        for x in orientMeshes:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Loading: '+x,2000)
            attributes=mc.listAttr(x, k=1)
            for i in attributes:
                value=absFunc.getDoubleDictJson(orientMeshesPath, x, i)
                try:
                    mc.setAttr(x+'.'+i, value)
                except: 0

        for x in sleeves:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Loading: '+x,2000)
            attributes=mc.listAttr(x, k=1)
            for i in attributes:
                value=absFunc.getDoubleDictJson(sleevesPath, x, i)
                try:
                    mc.setAttr(x+'.'+i, value)
                except: 0

        for x in groups:
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Loading: '+x,2000)
            attributes=mc.listAttr(x, k=1)
            for i in attributes:
                value=absFunc.getDoubleDictJson(groupsPath, x, i)
                try:
                    mc.setAttr(x+'.'+i, value)
                except:0

        self.statusBar.setStyleSheet("QStatusBar{color:rgb(3, 255, 11);background-color: rgb(30, 30, 30);}")
        self.statusBar.showMessage('All data loaded', 15000)

    def generateRig(self):
        #DICTS-----------------------------------------------------------------------------------------
        footDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/footData.json'
        handDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/handData.json'
        hipDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/hipData.json'
        ikDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/ikData.json'
        jointsDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/jointsData.json'
        modulesDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/modulesData.json'
        ikMonoDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/ikMono.json'
        sleeveDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/sleeveData.json'
        headDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/headData.json'
        wireDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/faceWireData.json'
        eyebrowDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/faceEyebrowComponentsData.json'
        eyesDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/faceEyeComponentsData.json'
        upperCheekDataPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/faceUpperCheekComponentsData.json'
        lowerUpperHeadPath=self.label_projectPath.text()+r'/Rigging/setup/setupData/setupGenerateData/faceLowerUpperHeadCompData.json'
        
        #--------------------------------------------------------------------------------------------------
        #Generating skinJoints-----------------------------------------------------------------------------------
        points=mc.ls('*_point')
        hipPoint=[]
        skinJoints=[]
        for x in points:
            parent=mc.listRelatives(x, p=1)[0]          
            if parent.endswith('point')==False:
                hipPoint.append(x)
                break

        mc.select(hipPoint,hi=1)
        allPoints=mc.ls(sl=1)
        scalableJoints=mc.createNode('transform',n='scalableJoints', p='joints_group')
        driverJoints=mc.createNode('transform',n='driverJoints_GRP', p='joints_group')
        mc.parent(driverJoints, 'rig')
        scalableDriverJoints=mc.createNode('transform',n='scalableDriverJoints_GRP', p='joints_group')
        mc.parent(scalableDriverJoints, driverJoints)


        mc.scaleConstraint('C_root_01_CTRL', scalableDriverJoints)
        mc.scaleConstraint('C_root_01_CTRL', scalableJoints)
        for i in allPoints:
            jointName=i.replace('point', 'JNT')
            skinJoints.append(jointName)
            jointTranslate=absFunc.getDoubleDictJson(jointsDataPath, jointName, 'translate')
            jointOrient=absFunc.getDoubleDictJson(jointsDataPath, jointName, 'jointOrient')
            jointWorldOrient=absFunc.getDoubleDictJson(jointsDataPath, jointName, 'worldOrient')

            
            index=allPoints.index(i)            
            mc.select(cl=1)

            if index==0:
                joint=mc.joint(n=i.replace('point', 'JNT'),p=jointTranslate,rad=1)
                mc.parent(joint, scalableJoints)

            else:
                jointParent=mc.listRelatives(i, p=1)[0]
                jointParent=jointParent.replace('point', 'JNT')
                joint=mc.joint(n=i.replace('point', 'JNT'),p=jointTranslate,rad=1)
                mc.parent(joint, jointParent)
            
            mc.joint(joint, e=1, o=(jointOrient[0],jointOrient[1],jointOrient[2]))

        #Resoluting Modules---------------------------------------------------------------------------------        
        for joint in skinJoints:
            statusIndex=skinJoints.index(joint)
            self.statusBar.setStyleSheet("QStatusBar{color:rgb(255, 203, 14);background-color: rgb(30, 30, 30);}")
            self.statusBar.showMessage('Generating: '+joint,15000)
            #self.progressBar.setValue()
            # jointBuilder
            #print ('Generating...'+joint)
            module=joint.replace('JNT', 'module')

            #HIP-------------------------------------------------------------           
            if joint == absFunc.getSimpleJson(hipDataPath,'name'):
                #transformData----------------------------------------------------
                translate=absFunc.getSimpleJson(hipDataPath,'translate')
                orientation=absFunc.getSimpleJson(hipDataPath,'orientation')

                #identify transforms-----------------------------------------------------------
                bodyZTR=mc.createNode('transform', n='C_body_01_ZTR', p='C_main_01_CTRL')
                bodyCTRL=mc.createNode('transform', n='C_body_01_CTRL', p=bodyZTR)
                bodyControlShape=absFunc.getSimpleJson(hipDataPath,'bodyControl')

                hipZTR=mc.createNode('transform', n=joint.replace('JNT','ZTR'), p=bodyCTRL)
                hipCTRL=mc.createNode('transform', n=joint.replace('JNT','CTRL'), p=hipZTR)
                hipControlShape=absFunc.getSimpleJson(hipDataPath,'hipControl')

                mc.xform(bodyZTR, t=(translate[0],translate[1], translate[2]), ws=1)
                mc.xform(bodyZTR, ro=(orientation[0],orientation[1], orientation[2]), ws=1)

                absFunc.extractControl(bodyCTRL, bodyControlShape)
                absFunc.extractControl(hipCTRL, hipControlShape)

                absFunc.setCurveColor(bodyCTRL,'red')
                absFunc.setCurveColor(hipCTRL,'green')
                mc.parentConstraint(hipCTRL, joint, mo=1)

            #IK START-------------------------------------------------------------
            if joint == absFunc.getDoubleDictJson(ikDataPath, joint, 'ikStart'):
                
                #Defining Variables---------------------------------------------------------    
                allJoints=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikJoints')
                ikStart=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikStart')
                ikEnd=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikEnd')
                ikEndChild=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikEndChild')
                ikControl=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikControl')
                ikStartParent=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikStartParent')
                #---------------------------------------------------------------------------
                #IK Type----------------------------------------------------------------
                ikType=mc.getAttr(ikControl+'.ikType')
                #IK Spline---------------------------------------------------------------               
                if ikType==1:
                    curveCoords=[]
                    for j in allJoints:
                        jointCoord=mc.xform(j, q=1, t=1, ws=1)
                        curveCoords.append(jointCoord)
                    curve=mc.curve( ep=curveCoords, d=3)
                    curve=mc.rename(curve, ikStart.replace('_JNT','_ikCurve' ))

                    #ik lower and upper Joints###########################################################                   
                    upperName =ikEndChild.replace('JNT','ikEndDrvJoint')
                    midName =ikEnd.replace('JNT','ikMidDrvJoint')
                    lowerName =ikStart.replace('JNT','ikStartDrvJoint')

                    mc.select(cl=1)
                    upperIkJoint=mc.joint(n=upperName)

                    mc.select(cl=1)
                    lowerIkJoint=mc.joint(n=lowerName)
                    
                    mc.select(cl=1)
                    midIkJoint=mc.joint(n=midName)

                    ikSplineJoints=[upperIkJoint]+[lowerIkJoint]+[midIkJoint]
                    for x in ikSplineJoints:
                        mc.select(cl=1)
                        motionNode=mc.pathAnimation( x, n='C_motionNode_Temp' ,c=curve, fa='x' ,wu=(0,0,1), fm=1, bank=True )
                        mc.cutKey(motionNode, at='uValue', time = (0, 1000), clear = True)
                        if x == upperName:
                            mc.setAttr(motionNode+'.uValue', 1)
                        if x == lowerName:
                            mc.setAttr(motionNode+'.uValue', 0)
                        if x == midIkJoint:
                            mc.setAttr(motionNode+'.uValue', 0.5)
                        mc.delete(x, mp=1)
                        mc.parent(x, scalableDriverJoints)
                        mc.makeIdentity(x, a=1)
                
                    bodyCTRL='C_body_01_CTRL'

                    #-------------------------------------------------
                    ikSplineSkinCluster=mc.skinCluster(ikSplineJoints, curve, n=curve.replace('ikCurve', 'curveSkinCluster'), dr=4.0)[0]
                    curveVertex=mc.ls(curve+'.cv[*]', fl=1)
                    curveVertexCount=float(len(curveVertex))                
                    
                    if curveVertexCount==10:
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[0], tv=[(upperIkJoint,0), (midIkJoint, 0), (lowerIkJoint, 1)])
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[1], tv=[(upperIkJoint,0), (midIkJoint, 0.2), (lowerIkJoint, 0.8)])
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[2], tv=[(upperIkJoint,0), (midIkJoint, 0.5), (lowerIkJoint, 0.5)])
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[3], tv=[(upperIkJoint,0), (midIkJoint, 0.8), (lowerIkJoint, 0.2)])
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[4], tv=[(upperIkJoint,0.1), (midIkJoint, 0.8), (lowerIkJoint, 0.1)])
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[5], tv=[(upperIkJoint,0.1), (midIkJoint, 0.8), (lowerIkJoint, 0.1)])
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[6], tv=[(upperIkJoint,0.2), (midIkJoint, 0.8), (lowerIkJoint, 0)])
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[7], tv=[(upperIkJoint,0.5), (midIkJoint, 0.5), (lowerIkJoint, 0)])
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[8], tv=[(upperIkJoint,0.8), (midIkJoint, 0.2), (lowerIkJoint, 0)])
                        mc.skinPercent(ikSplineSkinCluster, curveVertex[9], tv=[(upperIkJoint,1), (midIkJoint, 0), (lowerIkJoint, 0)])
                    #-----------------------------------------------
                    mc.parent(curve, 'dft_GRP')
                    controlCoord=absFunc.getDoubleDictJson(jointsDataPath, ikEndChild, 'translate')
                    controlOrient=absFunc.getDoubleDictJson(jointsDataPath, ikEndChild, 'worldOrient')
                    upperGRP=mc.createNode('transform', n=upperName.replace('ikEndDrvJoint','ikZTR'))

                    upperControl=mc.createNode('transform', n=upperName.replace('ikEndDrvJoint','ikCTRL'), p=upperGRP)
                    
                    if ikEndChild!=None:
                        upperTemp=absFunc.getDoubleDictJson(jointsDataPath, ikEndChild, 'controlName' )
                        
                        if upperTemp ==None:                            
                            upperTemp=absFunc.getDoubleDictJson(jointsDataPath, ikEnd, 'controlName' )

                    else:                       
                        upperTemp=absFunc.getDoubleDictJson(jointsDataPath, ikEnd, 'controlName' )
                    tempAttr=mc.listAttr(upperTemp, k=1)

                    mc.xform(upperGRP, t=controlCoord, ws=1)
                    mc.xform(upperGRP, ro=controlOrient, ws=1)

                    absFunc.extractControl(upperControl, upperTemp)
                    absFunc.setCurveColor(upperControl,'green')
                    
                    mc.parentConstraint(upperControl, upperIkJoint, mo=1)                   
                    
                    lowerControl=ikStartParent.replace('JNT', 'CTRL')
                    mc.parentConstraint(lowerControl, lowerIkJoint, mo=1)

                    midGRP=mc.createNode('transform', n=midIkJoint.replace('ikMidDrvJoint','ikMidZTR'))
                    midControl=mc.circle(n=midIkJoint.replace('ikMidDrvJoint','ikCTRL'), r=16, nr=(0,1,0))[0]
                    mc.addAttr(midControl, ln='squashFactor', at='float', min=-1, max=1, dv=0, k=1)                    
                    mc.addAttr(midControl, ln='type', at='enum', en='uncompressed:compressed',dv=0, k=1)
                    absFunc.setCurveColor(midControl,'green')

                    mc.parent(midControl, midGRP)
                    mc.delete(mc.pointConstraint(midIkJoint, midGRP, mo=0))
                    mc.parentConstraint(midControl, midIkJoint, mo=1)                   

                    mc.parent(upperGRP, bodyCTRL)
                    mc.parent(midGRP, bodyCTRL)
                    
                    #----------------------------------------------

                    fkSpineControl1=mel.eval('curve -d 1 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 1.431811 -15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p -5.991438 -1.431811 15.7761 -p -5.991438 1.431811 15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p 5.991438 -1.431811 -15.7761 -p 5.991438 1.431811 -15.7761 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;')
                    fkSpineControl1=mc.rename(fkSpineControl1, allJoints[1].replace('JNT','fkCTRL'))
                    fkSpineZTR1=mc.createNode('transform', n=fkSpineControl1.replace('fkCTRL','fkZTR'))
                    absFunc.setCurveColor(fkSpineControl1,'red')
                    
                    mc.parent(fkSpineControl1, fkSpineZTR1)
                    mc.makeIdentity(fkSpineControl1, a=1)
                    mc.delete(mc.pointConstraint(midControl, lowerControl, fkSpineZTR1, mo=0))
                    mc.parent(fkSpineZTR1, bodyCTRL)

                    fkSpineControl2=mel.eval('curve -d 1 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 1.431811 -15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 1.431811 15.7761 -p 5.991438 1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p -5.991438 -1.431811 15.7761 -p -5.991438 1.431811 15.7761 -p -5.991438 1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 15.7761 -p 5.991438 -1.431811 -15.7761 -p -5.991438 -1.431811 -15.7761 -p 5.991438 -1.431811 -15.7761 -p 5.991438 1.431811 -15.7761 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;')
                    fkSpineControl2=mc.rename(fkSpineControl2, allJoints[2].replace('JNT','fkCTRL'))
                    fkSpineZTR2=mc.createNode('transform', n=fkSpineControl2.replace('fkCTRL','fkZTR'))
                    absFunc.setCurveColor(fkSpineControl2,'red')
                    
                    mc.parent(fkSpineControl2, fkSpineZTR2)
                    mc.makeIdentity(fkSpineControl2, a=1)
                    mc.delete(mc.pointConstraint(upperControl, midControl, fkSpineZTR2, mo=0))
                    mc.parent(fkSpineZTR2, fkSpineControl1)

                    mc.parentConstraint(fkSpineControl1, midGRP, mo=1)
                    mc.parentConstraint(fkSpineControl2, upperGRP, mo=1)
                    #-----------------------------------------------------
                    splineIK = mc.ikHandle(sj=ikStart, ee=ikEnd, sol='ikSplineSolver', c=curve,scv=0, fj=1,pcv=0, n=curve.replace('_ikCurve','_ikSplineHandle'))[0] 
                    mc.parent(splineIK, 'dft_GRP')

                    mc.setAttr(splineIK+'.dTwistControlEnable',1)
                    mc.setAttr(splineIK+'.dWorldUpType',4)

                    mc.setAttr(splineIK+'.dForwardAxis',2)
                    mc.setAttr(splineIK+'.dWorldUpAxis',3)

                    mc.setAttr(splineIK+'.dWorldUpVectorY',0)
                    mc.setAttr(splineIK+'.dWorldUpVectorX',0)
                    mc.setAttr(splineIK+'.dWorldUpVectorZ',1)

                    mc.setAttr(splineIK+'.dWorldUpVectorEndX',0)
                    mc.setAttr(splineIK+'.dWorldUpVectorEndY',0)
                    mc.setAttr(splineIK+'.dWorldUpVectorEndZ',1)

                    mc.connectAttr(lowerControl+'.worldMatrix[0]', splineIK+'.dWorldUpMatrix')
                    mc.connectAttr(upperControl+'.worldMatrix[0]', splineIK+'.dWorldUpMatrixEnd')

                    #Squash/Stretch___________________________________________________________________
                    
                    ci=mc.createNode('curveInfo', n=curve.replace('ikCurve', 'CI'))

                    mc.connectAttr(curve+'Shape.worldSpace[0]', ci+'.inputCurve')

                    mdFix=mc.createNode('multiplyDivide', n=curve.replace('_ikCurve', '_scaleFixMD'))
                    mc.connectAttr('C_root_01_CTRL.scaleX', mdFix+'.input2X')
                    mc.connectAttr(ci+'.arcLength', mdFix+'.input1X')
                    mc.setAttr(mdFix+'.operation', 2)

                    mdStretch=mc.createNode('multiplyDivide', n=curve.replace('_ikCurve', '_stretchMD'))
                    mc.connectAttr(mdFix+'.outputX', mdStretch+'.input1X')
                    mc.setAttr(mdStretch+'.operation', 2)
                    attr=mc.getAttr(mdStretch+'.input1X')
                    mc.setAttr(mdStretch+'.input2X', attr)

                    cond=mc.createNode('condition', n=curve.replace('_ikCurve', '_stretchCOND'))
                    mc.setAttr(cond+'.operation', 2)
                    mc.setAttr(cond+'.secondTerm', 1)
                    mc.connectAttr(mdStretch+'.outputX', cond+'.firstTerm')
                    mc.connectAttr(mdStretch+'.outputX', cond+'.colorIfTrueR')

                    remap=mc.createNode('remapValue', n=curve.replace('_ikCurve', '_stretchREMAP'))            
                    mc.connectAttr(midControl + '.type',remap + '.inputValue')
                    mc.connectAttr(remap + '.outValue', cond + '.operation')
                    mc.setAttr(remap+'.outputMin',2)
                    mc.setAttr(remap+'.outputMax',1)  

                    mdSquash=mc.createNode('multiplyDivide', n=curve.replace('_ikCurve', '_squashMD'))
                    mc.setAttr(mdSquash+'.operation', 3)    
                    mc.connectAttr(mdStretch+'.outputX', mdSquash+'.input1X')                    
                    mc.connectAttr(midControl+'.squashFactor', mdSquash+'.input2X')

                    squashCond=mc.createNode('condition', n=curve.replace('_ikCurve', '_squashCOND'))
                    mc.setAttr(squashCond+'.operation', 1)
                    mc.setAttr(squashCond+'.secondTerm', 1)
                    mc.connectAttr(mdSquash+'.outputX', squashCond+'.firstTerm')
                    mc.connectAttr(mdSquash+'.outputX', squashCond+'.colorIfTrueR')

                    for x in allJoints: 
                        if x != ikEnd:
                            mc.connectAttr(cond+'.outColorR', x+'.scaleY')
                            mc.connectAttr(squashCond+'.outColorR', x+'.scaleX')
                            mc.connectAttr(squashCond+'.outColorR', x+'.scaleZ')
                    mc.parentConstraint(upperControl, ikEndChild, mo=1)
                    mc.orientConstraint(upperControl, ikEnd, mo=1)
                #----------------------------------------------------------------------------
                #ikHandle--------------------------------------------------------------------
                #----------------------------------------------------------------------------

                if ikType==0:
                    allJoints=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikJoints')
                    ikStart=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikStart')
                    ikEnd=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikEnd')
                    ikEndChild=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikEndChild')
                    ikControl=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikControl')
                    ikStartParent=absFunc.getDoubleDictJson(ikDataPath, joint, 'ikStartParent')

                    #ik Joints_______________________________________________________________
                    ikZTRSwitch=[]
                    for x in allJoints:
                        coord=absFunc.getDoubleDictJson(jointsDataPath, x, 'translate')
                        orient=absFunc.getDoubleDictJson(jointsDataPath, x, 'jointOrient')
                        worldOrient=absFunc.getDoubleDictJson(jointsDataPath, x, 'worldOrient')
                        controlOrient=absFunc.getDoubleDictJson(jointsDataPath, ikEndChild, 'worldOrient')
                        controlCoord=absFunc.getDoubleDictJson(jointsDataPath, ikEndChild, 'translate')

                        if x == ikStart:
                            ikGRP=mc.createNode('transform', n=x.replace('JNT','ikJNT_GRP'))
                            mc.parent(ikGRP, scalableDriverJoints)
                            mc.select(cl=1)
                        newJoint=mc.joint(n=x.replace('JNT', 'ikJNT'))

                        if x == ikStart:
                            mc.joint(newJoint, e=1, p=coord ,o=(worldOrient[0],worldOrient[1],worldOrient[2]))
                            mc.parent(newJoint, ikGRP)
                        else:
                            mc.joint(newJoint, e=1, p=coord ,o=(orient[0],orient[1],orient[2]))

                        if x ==ikEnd:
                            ikZTR=mc.createNode('transform', n=ikEndChild.replace('JNT','ikZTR'), p='C_main_01_CTRL')
                            ikCONS=mc.createNode('transform', n=ikEndChild.replace('JNT','ikCONS'), p=ikZTR)
                            ikCTRL=mc.createNode('transform', n=ikEndChild.replace('JNT','ikCTRL'), p=ikCONS)
                            ikTempCTRL=absFunc.getDoubleDictJson(jointsDataPath, ikEndChild, 'controlName')                         
                            mc.xform(ikZTR, t=controlCoord, ws=1)
                            mc.xform(ikZTR, ro=controlOrient, ws=1)

                            if ikCTRL.startswith('R_') is True:
                                mc.setAttr(ikZTR + '.scaleX', -1)
                                mc.setAttr(ikZTR + '.scaleY', -1)
                                mc.setAttr(ikZTR + '.scaleZ', -1)

                            absFunc.extractControl(ikCTRL, ikTempCTRL)
                            if ikCTRL.startswith('L_') is True:
                                absFunc.setCurveColor(ikCTRL,'blueLight')
                            elif ikCTRL.startswith('R_') is True:
                                absFunc.setCurveColor(ikCTRL,'greenDark')
                            ikZTRSwitch.append(ikZTR)
                        mc.makeIdentity(newJoint, a=1)

                    #fk Joints______________________________________________________________
                    fkZTRSwitch=[]                  
                    for x in allJoints:
                        index=allJoints.index(x)
                        coord=absFunc.getDoubleDictJson(jointsDataPath, x, 'translate')
                        orient=absFunc.getDoubleDictJson(jointsDataPath, x, 'jointOrient')
                        worldOrient=absFunc.getDoubleDictJson(jointsDataPath, x, 'worldOrient')
                        controlOrient=absFunc.getDoubleDictJson(jointsDataPath, ikEndChild, 'worldOrient')
                        controlCoord=absFunc.getDoubleDictJson(jointsDataPath, ikEndChild, 'translate')
                        if x == ikStart:
                            fkGRP=mc.createNode('transform', n=x.replace('JNT','fkJNT_GRP'))
                            mc.parent(fkGRP, scalableDriverJoints)
                            mc.select(cl=1)

                        newJoint=mc.joint(n=x.replace('JNT', 'fkJNT'))
                        
                        if x == ikStart:
                            mc.joint(newJoint, e=1, p=coord ,o=(worldOrient[0],worldOrient[1],worldOrient[2]))
                            mc.parent(newJoint, fkGRP)
                        else:
                            mc.joint(newJoint, e=1, p=coord ,o=(orient[0],orient[1],orient[2]))

                        if x == ikStart:
                            tempBase=ikStartParent.replace('JNT', 'CTRL')                           
                            if mc.objExists(tempBase)==True:
                                chainBase=ikStartParent.replace('JNT', 'CTRL')                          
                            else:
                                parentOrient=absFunc.getDoubleDictJson(jointsDataPath, ikStartParent, 'worldOrient')
                                parentCoord=absFunc.getDoubleDictJson(jointsDataPath, ikStartParent, 'translate')


                                tempParentParent=mc.listRelatives(ikStartParent, p=1)[0]
                                parentParent=tempParentParent.replace('JNT', 'ikCTRL')

                                fkZTR=mc.createNode('transform', n=ikStartParent.replace('JNT','ZTR'), p=parentParent)
                                fkCONS=mc.createNode('transform', n=ikStartParent.replace('JNT','CONS'), p=fkZTR)
                                fkCTRL=mc.createNode('transform', n=ikStartParent.replace('JNT','CTRL'), p=fkCONS)
                                mc.xform(fkZTR, t=parentCoord, ws=1)
                                mc.xform(fkZTR, ro=parentOrient, ws=1)                                

                                fkTempCTRL=absFunc.getDoubleDictJson(jointsDataPath, ikStartParent, 'controlName')                              
                                absFunc.extractControl(fkCTRL, fkTempCTRL)

                                if fkCTRL.startswith('L_') is True:
                                    absFunc.setCurveColor(fkCTRL,'blueLight')
                                elif fkCTRL.startswith('R_') is True:
                                    absFunc.setCurveColor(fkCTRL,'greenDark')

                                mc.parentConstraint(fkCTRL, ikStartParent)

                                chainBase=fkCTRL
                                
                                

                        if x.endswith('endJNT')==False:
                            tempPapi=mc.listRelatives(x, p=1)[0]
                            tempPapi=tempPapi.replace('JNT', 'fkCTRL')
                            tempPapi2=tempPapi.replace('fkCTRL', 'CTRL')
                            fkCont=ikStart.replace('JNT', 'fkZTR')

                            if index==0:
                                fkZTR=mc.createNode('transform', n=x.replace('JNT','fkZTR'), p=chainBase)
                                fkZTRSwitch.append(fkZTR)
                            else:
                                fkZTR=mc.createNode('transform', n=x.replace('JNT','fkZTR'), p=fkCont)
                            fkCONS=mc.createNode('transform', n=x.replace('JNT','fkCONS'), p=fkZTR)
                            fkCTRL=mc.createNode('transform', n=x.replace('JNT','fkCTRL'), p=fkCONS)
                            mc.xform(fkZTR, t=coord, ws=1)
                            mc.xform(fkZTR, ro=worldOrient, ws=1)
                            if index !=0:
                                if mc.objExists(tempPapi)== True:
                                    mc.parentConstraint(tempPapi, fkCONS, mo=1)
                                else:
                                    mc.parentConstraint(tempPapi2, fkCONS, mo=1)                    

                            fkTempCTRL=absFunc.getDoubleDictJson(jointsDataPath, x, 'controlName')
                            absFunc.extractControl(fkCTRL, fkTempCTRL)
                            if fkCTRL.startswith('L_') is True:
                                absFunc.setCurveColor(fkCTRL,'blueLight')
                            elif fkCTRL.startswith('R_') is True:
                                absFunc.setCurveColor(fkCTRL,'greenDark')
                            mc.makeIdentity(newJoint, a=1)
                            mc.parentConstraint(fkCTRL, newJoint, mo=1)
                            mc.connectAttr(fkCTRL+'.s', newJoint+'.s')                          
                            mc.select(newJoint)

                        else:
                            fkZTR=mc.createNode('transform', n=ikEndChild.replace('JNT','fkZTR'), p=fkCont)
                            fkCONS=mc.createNode('transform', n=ikEndChild.replace('JNT','fkCONS'), p=fkZTR)
                            fkCTRL=mc.createNode('transform', n=ikEndChild.replace('JNT','fkCTRL'), p=fkCONS)
                            mc.xform(fkZTR, t=controlCoord, ws=1)
                            mc.xform(fkZTR, ro=controlOrient, ws=1)

                            tempPapi=mc.listRelatives(x, p=1)[0]
                            tempPapi=tempPapi.replace('JNT', 'fkCTRL')
                            if mc.objExists(tempPapi)== True:
                                mc.parentConstraint(tempPapi, fkCONS, mo=1)

                            fkTempCTRL=absFunc.getDoubleDictJson(jointsDataPath, ikEndChild, 'controlName')
                            absFunc.extractControl(fkCTRL, fkTempCTRL)
                            if fkCTRL.startswith('L_') is True:
                                absFunc.setCurveColor(fkCTRL,'blueLight')
                            elif fkCTRL.startswith('R_') is True:
                                absFunc.setCurveColor(fkCTRL,'greenDark')
                            mc.makeIdentity(newJoint, a=1)

                            mc.parentConstraint(fkCTRL, newJoint, mo=1)
                            mc.connectAttr(fkCTRL+'.s', newJoint+'.s')
                            mc.select(newJoint)
                    
                    #Constraints and switch kinematics_______________________________________
                    ikA=ikStart.replace('JNT', 'ikJNT')
                    ikC=ikEnd.replace('JNT', 'ikJNT')                   
                    ikB=allJoints[-2].replace('JNT', 'ikJNT')

                    ikBase=ikStartParent.replace('JNT', 'CTRL')
                    mc.parentConstraint(ikBase,ikA, mo=1)

                    switchCtrl=mel.eval("curve -d 1 -p -0.5 0 -1.5 -p -1 0 -1.5 -p 0 0 -2.5 -p 1 0 -1.5 -p 0.5 0 -1.5 -p 0.5 0 -0.5 -p 1.5 0 -0.5 -p 1.5 0 -1 -p 2.5 0 0 -p 1.5 0 1 -p 1.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 1.5 -p 1 0 1.5 -p 0 0 2.5 -p -1 0 1.5 -p -0.5 0 1.5 -p -0.5 0 0.5 -p -1.5 0 0.5 -p -1.5 0 1 -p -2.5 0 0 -p -1.5 0 -1 -p -1.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 -1.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;")
                    switchCtrl=mc.rename(switchCtrl, ikC.replace('ikJNT', 'switchCTRL'))
                    switchGrp=mc.createNode('transform', n=ikC.replace('ikJNT', 'switchGRP'))
                    absFunc.setCurveColor(switchCtrl,'red')
                           
                    mc.parent(switchCtrl, switchGrp)
                    pos1=absFunc.getDoubleDictJson(jointsDataPath, ikEnd, 'translate')
                    orient1=absFunc.getDoubleDictJson(jointsDataPath, ikEnd, 'worldOrient')                 
                    if orient1=='None':
                        orient1=mc.xform(ikEnd, q=1, ro=1, ws=1)

                    pos2=mc.xform(ikB, q=1, t=1, ws=1)
                    orient2=mc.xform(ikB, q=1, ro=1, ws=1)                    

                    locSwitch=mc.spaceLocator(n='switchLoc')
                    locSwitchGrp=mc.createNode('transform', n='switchLocGrp')
                    mc.parent(locSwitch,locSwitchGrp)

                    mc.xform(locSwitchGrp, t=pos1, ws=1)
                    if orient1=='None':
                        mc.xform(locSwitchGrp, ro=orient2, ws=1)
                    else:
                        mc.xform(locSwitchGrp, ro=(orient1[0],orient1[1],orient1[2]), ws=1)

                    locSwitch2=mc.spaceLocator(n='switchLoc2')
                    mc.xform(locSwitch2, t=pos2, ws=1)
                    mc.parent(locSwitch2, locSwitch)

                    mc.xform(switchGrp, t=pos1, ws=1)                    

                    #mc.parentConstraint(locSwitch, switchGrp, mo=1)
                    mc.xform(locSwitch, ro=(0,0,-90), os=1)
                    #mc.delete(switchGrp+'_parentConstraint1')
                    mc.delete(mc.pointConstraint(locSwitch2, switchCtrl))
                    mc.delete(locSwitchGrp)
                    mc.xform(switchCtrl, ro=(0,0,-90), os=1)    
                    mc.makeIdentity(switchCtrl, a=1)

                    mc.addAttr(switchCtrl, ln='IK_FK', at='float', min=0, max=1, k=1)
                    mc.addAttr(switchCtrl, ln='ikSpace', at='enum', en='root:main:ikParent:',dv=2, k=1)
                    mc.addAttr(switchCtrl, ln='fkSpace', at='enum', en='root:main:fkParent',dv=2, k=1)
                    mc.addAttr(switchCtrl, ln='squashFactor', at='float', min=0, max=1, k=1)
                    mc.addAttr(switchCtrl, ln='lenght', at='float', dv=1, k=1)


                    rev=mc.createNode('reverse', n=switchCtrl.replace('switchCTRL', 'reverse'))
                    mc.connectAttr(switchCtrl+'.IK_FK', rev+'.inputX')              

                    for a in allJoints:
                        ik = a.replace('JNT', 'ikJNT')
                        fk = a.replace('JNT', 'fkJNT')
                        
                        blend=mc.createNode('blendColors', n=a.replace('JNT', 'BC'))
                        mc.connectAttr(switchCtrl+'.IK_FK', blend+'.blender')
                        mc.connectAttr(ik+'.scaleX', blend+'.color2R')
                        mc.connectAttr(ik+'.scaleY', blend+'.color2G')
                        mc.connectAttr(ik+'.scaleZ', blend+'.color2B')

                        mc.connectAttr(fk+'.scaleX', blend+'.color1R')
                        mc.connectAttr(fk+'.scaleY', blend+'.color1G')
                        mc.connectAttr(fk+'.scaleZ', blend+'.color1B')

                        mc.connectAttr(blend+'.outputR', a+'.scaleX')
                        mc.connectAttr(blend+'.outputG', a+'.scaleY')
                        mc.connectAttr(blend+'.outputB', a+'.scaleZ')

                        oriCons=mc.orientConstraint(ik, fk, a, mo=1)                        
                        mc.setAttr(oriCons[0]+'.interpType', 2)
                        mc.connectAttr(switchCtrl+'.IK_FK', oriCons[0]+'.'+fk+'W1')
                        mc.connectAttr(rev+'.outputX', oriCons[0]+'.'+ik+'W0')
                        if a == ikStart:
                            pointCons=mc.pointConstraint(ik, fk, a, mo=1)
                            mc.connectAttr(switchCtrl+'.IK_FK', pointCons[0]+'.'+fk+'W1')
                            mc.connectAttr(rev+'.outputX', pointCons[0]+'.'+ik+'W0')
                    
                    mc.disconnectAttr(ikEnd+'.scale',ikEndChild+'.inverseScale')
                    mc.parent(switchGrp, 'C_main_01_CTRL')
                    mc.parentConstraint(ikEnd, switchGrp, mo=1)
                    

                    #ikSystem________________________________________________________________

                    handle = mc.ikHandle(sj=ikA, ee=ikC, sol='ikRPsolver', n=ikC.replace('ikJNT','ikHandle'))[0]
                    handleGrp=mc.createNode('transform', n= handle.replace('Handle', 'HandleGrp'))
                    handleCoord=mc.xform(handle, q=1, t=1, ws=1)
                    mc.xform(handleGrp, t=handleCoord, ws=1)
                    mc.parent(handle, handleGrp)
                    mc.parent(handleGrp, 'dft_GRP')
                    
                    poleLoc = mc.spaceLocator(n=ikA.replace('ikJNT','ikPoleLoc'))[0]
                    poleGrp = mc.createNode('transform', n=ikA.replace('ikJNT','ikPoleLocGrp'))
                    mc.connectAttr(handle+'.poleVector', poleLoc+'.translate')
                    mc.disconnectAttr(handle+'.poleVector', poleLoc+'.translate')
                    mc.parent(poleLoc, poleGrp)
                    ikAPos=mc.xform(ikA, q=1,t=1,ws=1)
                    mc.xform(poleGrp, t=ikAPos, ws=1)

                    mc.delete(mc.aimConstraint(ikA, ikC, poleLoc, aim=(0,0,-1), u=(0,1,0), wut='object', wuo=handle))

                    rotPoleLoc=mc.spaceLocator(n=ikA.replace('ikJNT','ikRotPoleLoc'))[0]
                    rotPoleLocGrp=mc.createNode('transform', n=ikA.replace('ikJNT','ikRotPoleLocGrp'))
                    mc.parent(rotPoleLoc, rotPoleLocGrp)
                    mc.delete(mc.pointConstraint(ikA, ikC, rotPoleLocGrp, mo=0))
                    mc.delete(mc.orientConstraint(poleLoc, rotPoleLocGrp, mo=0))
                    mc.parent(poleGrp, rotPoleLoc)
                    mc.xform(rotPoleLoc, ro=(-90,0,0), os=1, r=1)

                    poleLocPos=mc.xform(poleLoc, q=1,t=1,ws=1)
                    poleControl=mel.eval('curve -d 1 -p 0 1 0 -p 0 0.707107 0.707107 -p 0 0 1 -p 0 -0.707107 0.707107 -p 0 -1 0 -p 0 -0.707107 -0.707107 -p 0 0 -1 -p 0 0.707107 -0.707107 -p 0 1 0 -p -0.707107 0.707107 0 -p -1 0 0 -p -0.707107 -0.707107 0 -p 0 -1 0 -p 0.707107 -0.707107 0 -p 1 0 0 -p 0.707107 0.707107 0 -p 0 1 0 -p 0 0.707107 -0.707107 -p 0 0 -1 -p 0.707107 0 -0.707107 -p 1 0 0 -p 0.707107 0 0.707107 -p 0 0 1 -p -0.707107 0 0.707107 -p -1 0 0 -p -0.707107 0 -0.707107 -p 0 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 ;')
                    poleControl=mc.rename(poleControl, ikA.replace('ikJNT','PoleVector_ikCTRL'))
                    if poleControl.startswith('L_') is True:
                        absFunc.setCurveColor(poleControl,'blueLight')
                    elif poleControl.startswith('R_') is True:
                        absFunc.setCurveColor(poleControl,'greenDark')         
                    mc.xform(poleControl, t=poleLocPos, ws=1  )
                    mc.poleVectorConstraint(poleControl, handle)
                    mc.delete(rotPoleLocGrp)
                    papi=absFunc.localGrp(poleControl)

                    ikZTRSwitch.append(mc.listRelatives(poleControl, p=1)[0])
                    
                    mc.parent(papi, 'C_main_01_CTRL')

                    mc.addAttr(poleControl, ln='space', at='enum', en='world:ikParent:ikChild', k=1)

                    
                    #Squash/Stretch___________________________________________________________
                    aCoord=absFunc.getDoubleDictJson(jointsDataPath, ikStart, 'translate')
                    bCoord=absFunc.getDoubleDictJson(jointsDataPath, ikEnd, 'translate')
                    
                    allDistances=[]
                    jointQty = len(allJoints)-1

                    for j in allJoints:
                        index=allJoints.index(j)
                        if index < jointQty:
                            child=mc.listRelatives(j, c=1, type='joint')[0]
                            mc.distanceDimension(sp=(0, 0, 0), ep=(1, 1, 1))
                            loc1=mc.rename('locator1', ikA.replace('ikJNT', 'distLocTEMP'))
                            loc2=mc.rename('locator2', ikC.replace('endikJNT', 'distLocTEMP'))
                            dist=mc.rename('distanceDimension1', ikC.replace('endikJNT', 'distDimensionTEMP'))
                            mc.pointConstraint(j, loc1)
                            mc.pointConstraint(child, loc2)
                            distNum=mc.getAttr(dist+'Shape.distance')                           
                            allDistances.append(distNum)
                            mc.delete(dist)
                            mc.delete(loc1)
                            mc.delete(loc2)  
                    
                    mc.distanceDimension(sp=(0, 0, 0), ep=(1, 1, 1))
                    loc1=mc.rename('locator1', ikA.replace('ikJNT', 'distLoc'))
                    loc2=mc.rename('locator2', ikC.replace('endikJNT', 'distLoc'))
                    dist=mc.rename('distanceDimension1', ikC.replace('endikJNT', 'distDimension'))
                    mc.xform(loc1, t=(aCoord[0], aCoord[1], aCoord[2]), ws=1)
                    mc.xform(loc2, t=(bCoord[0], bCoord[1], bCoord[2]), ws=1)
                        
                    distGrp=mc.createNode('transform', n=ikA.replace('ikJNT', 'distGRP'))
                    
                    _obj=[loc1, loc2, dist]
                    grpList=absFunc.localGrp(_obj)              
                    
                    mc.parent(grpList, distGrp)
                    mc.parent(distGrp, 'dft_GRP')

                    mdFixStretch=mc.createNode('multiplyDivide', n=ikA.replace('ikJNT', 'StretchFix_MD'))
                    mdStretch=mc.createNode('multiplyDivide', n=ikA.replace('ikJNT', 'Stretch_MD'))
                    condStretch=mc.createNode('condition', n=ikA.replace('ikJNT', 'Stretch_COND'))

                    mc.connectAttr(dist+'Shape.distance', mdFixStretch+'.input1X')
                    mc.connectAttr('C_root_01_CTRL.scaleX', mdFixStretch+'.input2X')
                    mc.setAttr(mdFixStretch+'.operation', 2)

                    mc.connectAttr(mdFixStretch+'.outputX', mdStretch +'.input1X')                    

                    
                    distanceValue=sum(allDistances)                    
                    mc.setAttr(mdStretch+'.input2X', distanceValue)
                    mc.setAttr(mdStretch+'.operation', 2)

                    mc.connectAttr(mdStretch+'.outputX', condStretch+'.firstTerm')
                    mc.connectAttr(mdStretch+'.outputX', condStretch+'.colorIfTrueR')
                    mc.setAttr(condStretch+'.secondTerm', 1)
                    mc.setAttr(condStretch+'.colorIfFalse', 1,1,1)
                    mc.setAttr(condStretch+'.operation', 3)
                    

                    mdSquash=mc.createNode('multiplyDivide', n=ikA.replace('ikJNT', '_squashMD'))
                    mc.setAttr(mdSquash+'.operation', 3)
                    mc.connectAttr(mdStretch+'.outputX', mdSquash+'.input1X')
                    mc.setAttr(mdSquash+'.input2X', -1)
                    

                    squashCond=mc.createNode('condition', n=ikA.replace('ikJNT', '_squashCOND'))
                    mc.setAttr(squashCond+'.operation', 4)
                    mc.setAttr(squashCond+'.secondTerm', 1)
                    mc.connectAttr(mdSquash+'.outputX', squashCond+'.firstTerm')
                    mc.connectAttr(mdSquash+'.outputX', squashCond+'.colorIfTrueR')

                    squashCond=mc.createNode('condition', n=ikA.replace('ikJNT', '_squashCOND'))
                    mc.setAttr(squashCond+'.operation', 1)
                    mc.setAttr(squashCond+'.secondTerm', 1)
                    mc.connectAttr(mdSquash+'.outputX', squashCond+'.firstTerm')
                    mc.connectAttr(mdSquash+'.outputX', squashCond+'.colorIfTrueR')                    

                    squashActivator=mc.createNode('blendColors', n=ikA.replace('ikJNT', 'ActivatorBC'))

                    mc.connectAttr(switchCtrl+'.squashFactor', squashActivator+'.blender')

                    mc.connectAttr(squashCond+'.outColorR', squashActivator+'.color1R')

                    mc.setAttr(squashActivator + '.color2R', 1)

                    # Lenght------------------------------------------------------------------                     
                    mc.connectAttr(switchCtrl + '.lenght', condStretch + '.colorIfFalseR')

                    # conenct To skinJoints-----------------------------------------------------
                    for x in allJoints:
                        ik=x.replace('JNT', 'ikJNT')

                        if x != ikEnd:
                            mc.connectAttr(condStretch+'.outColorR', ik+'.scaleX')
                            mc.connectAttr(squashActivator +'.outputR', ik+'.scaleY')
                            mc.connectAttr(squashActivator +'.outputR', ik+'.scaleZ')
                            

                    #Binding ikControls to Joints___________________________________________________________                                        
                    mc.parentConstraint(ikCTRL, grpList[1], mo=1)
                    mc.parentConstraint(ikStartParent.replace('JNT','CTRL'),grpList[0], mo=1)
                    mc.parentConstraint(ikCTRL, handleGrp, mo=1)
                    mc.orientConstraint(ikCTRL, ikC, mo=1)
                    mc.addAttr(ikCTRL, ln='size', at='float', min=0.01,dv=1, k=1)
                    mc.connectAttr(ikCTRL+'.size', ikCTRL+'.scaleX')
                    mc.connectAttr(ikCTRL+'.size', ikCTRL+'.scaleY')
                    mc.connectAttr(ikCTRL+'.size', ikCTRL+'.scaleZ')
                    mc.connectAttr(ikCTRL+'.s', ikC+'.s')
                    #----------------------------------------------------------------------------------------
                    #Spaces----------------------------------------------------------------------------------
                    #----------------------------------------------------------------------------------------
                    spaceRoot='C_root_01_CTRL'
                    spaceMain='C_main_01_CTRL'
                    spaceParent=ikStartParent.replace('JNT', 'CTRL')

                    parents=[spaceRoot]+[spaceMain]+[spaceParent]                   
                    parentSpaces=[]
                    for e in parents:
                        if mc.objExists(e.replace('CTRL', 'parentSpaceZTR'))==True:
                            parentSpaceZTR=e.replace('CTRL', 'parentSpaceZTR')
                            parentSpace=e.replace('CTRL', 'parentSpace')
                        else:
                            parentSpaceZTR=mc.createNode('transform',n=e.replace('CTRL', 'parentSpaceZTR'))
                            parentSpace=mc.createNode('transform',n=e.replace('CTRL', 'parentSpace'), p=parentSpaceZTR)                     
                            mc.delete(mc.pointConstraint(e, parentSpaceZTR, mo=0))
                            mc.parent(parentSpaceZTR, e)
                        parentSpaces.append(parentSpace)                    
                    
                    #IK Space--------------------------------------------------------------------
                    ikCTRL=ikEndChild.replace('JNT', 'ikCTRL')
                    ikZTR=ikCTRL.replace('ikCTRL', 'ikZTR')
                    ikCONS=ikCTRL.replace('ikCTRL', 'ikCONS')
                    ikSpaceGRP=mc.createNode('transform', n=ikCTRL.replace('ikCTRL', 'ikSpaceGRP')) 
                    ikSpace=mc.createNode('transform', n=ikCTRL.replace('ikCTRL', 'ikSpace'),p=ikSpaceGRP)                  
                    mc.delete(mc.pointConstraint(ikCTRL, ikSpaceGRP, mo=0))
                    mc.parent(ikSpaceGRP, ikZTR)
                    mc.parent(ikCONS, ikSpace)
                    # FKSpace--------------------------------------------------------------------
                    fkCTRL=ikStart.replace('JNT', 'fkCTRL')
                    fkZTR=fkCTRL.replace('fkCTRL', 'fkZTR')
                    fkCONS=fkCTRL.replace('fkCTRL', 'fkCONS')
                    fkSpaceGRP=mc.createNode('transform', n=fkCTRL.replace('fkCTRL', 'fkSpaceGRP')) 
                    fkSpace=mc.createNode('transform', n=fkCTRL.replace('fkCTRL', 'fkSpace'),p=fkSpaceGRP)                  
                    mc.delete(mc.pointConstraint(fkCTRL, fkSpaceGRP, mo=0))
                    mc.parent(fkSpaceGRP, fkZTR)
                    mc.parent(fkCONS, fkSpace)
                    #spaceConstraining----------------------------------------------------------
                    #ik:
                    mc.select(parentSpaces)
                    mc.select(ikSpace, add=1)
                    spaceConstraint=mc.parentConstraint(mo=1)
                    for s in parentSpaces:
                        index=parentSpaces.index(s)
                        remap=mc.createNode('remapValue', n=s.replace('parentSpace', ikSpace.split('_')[0]+ikSpace.split('_')[1]+'remapSpace'))
                        mc.setAttr(remap+'.value[2].value_FloatValue', 1)
                        mc.setAttr(remap+'.value[2].value_Position', 0.5)
                        mc.setAttr(remap+'.value[1].value_FloatValue', 0)
                        mc.setAttr(remap+'.value[1].value_Position', 1)
                        mc.setAttr(remap+'.value[2].value_Interp', 1)
                        mc.connectAttr(switchCtrl+'.ikSpace',remap+'.inputValue')
                        mc.connectAttr(remap+'.outValue', spaceConstraint[0]+'.'+s+'W'+str(index))
                        mc.setAttr(remap+'.inputMin',index-1)
                        mc.setAttr(remap+'.inputMax',index+1)   
                    #fk:
                    mc.select(parentSpaces)
                    mc.select(fkSpace, add=1)
                    spaceConstraint=mc.orientConstraint(mo=1)
                    for s in parentSpaces:
                        index=parentSpaces.index(s)
                        remap=mc.createNode('remapValue', n=s.replace('parentSpace',fkSpace.split('_')[0]+fkSpace.split('_')[1]+'remapSpace'))
                        mc.setAttr(remap+'.value[2].value_FloatValue', 1)
                        mc.setAttr(remap+'.value[2].value_Position', 0.5)
                        mc.setAttr(remap+'.value[1].value_FloatValue', 0)
                        mc.setAttr(remap+'.value[1].value_Position', 1)
                        mc.setAttr(remap+'.value[2].value_Interp', 1)
                        mc.connectAttr(switchCtrl+'.fkSpace',remap+'.inputValue')
                        mc.connectAttr(remap+'.outValue', spaceConstraint[0]+'.'+s+'W'+str(index))
                        mc.setAttr(remap+'.inputMin',index-1)
                        mc.setAttr(remap+'.inputMax',index+1)

                    #visibility----------------------------------------------------
                    reverse=switchCtrl.replace('switchCTRL', 'reverse') 
                    for i in fkZTRSwitch:
                        mc.connectAttr(switchCtrl+'.IK_FK', i+'.v')                 
                    for i in ikZTRSwitch:
                        mc.connectAttr(reverse+'.outputX', i+'.v')              

            #HAND------------------------------------------------------------------------------------------
            #----------------------------------------------------------------------------------------------
            #----------------------------------------------------------------------------------------------
            if joint == absFunc.getDoubleDictJson(handDataPath, joint, 'handJoint'):
                #defining variables----------------------------------------------------------------
                handJoint=absFunc.getDoubleDictJson(handDataPath, joint, 'handJoint')
                fingerList=absFunc.getDoubleDictJson(handDataPath, joint, 'fingerJoints')
                handControlData=absFunc.getDoubleDictJson(handDataPath, joint, 'handControl')
                switchCtrl=absFunc.getDoubleDictJson(handDataPath, joint, 'switchControl')
                jointPos=absFunc.getDoubleDictJson(jointsDataPath, joint, 'translate')
                jointOri=absFunc.getDoubleDictJson(jointsDataPath, joint, 'worldOrient')
                #----------------------------------------------------------------------------------
                if mc.objExists(switchCtrl)==True:
                    mc.addAttr(switchCtrl, ln='____', at='enum', en='fingerAttr:', k=1)
                    mc.addAttr(switchCtrl, ln='spread', at='float', k=1)
                    mc.addAttr(switchCtrl, ln='fist', at='float',  k=1)                 

                handGroup=mc.createNode('transform', n=joint.replace('JNT', 'GRP'), p='C_main_01_CTRL' )
                handZTR=mc.createNode('transform', n=joint.replace('JNT', 'ZTR'), p=handGroup )
                mc.xform(handGroup, t=(jointPos[0], jointPos[1], jointPos[2]), ws=1)
                mc.xform(handGroup, ro=(jointOri[0], jointOri[1], jointOri[2]), ws=1)
                mc.parentConstraint(joint, handGroup, mo=1)
                mc.scaleConstraint(joint, handGroup, mo=1)
                #definingFingersQuantity---------------------------------------------------------
                tempList=[]
                for i in fingerList:
                    if i.endswith('endJNT')==False:
                        tempList.append(i.split('_')[1])
                tempList=set(tempList)
                tempList=list(tempList)
                fingerCount=len(tempList)
                mult=180/fingerCount                
                #---------------------------------------------------------------------------------
                spreadJoints=[]             
                for x in fingerList:
                    if x.endswith('endJNT')==False:
                        xCoord=absFunc.getDoubleDictJson(jointsDataPath, x, 'translate')
                        xOrient=absFunc.getDoubleDictJson(jointsDataPath, x, 'worldOrient')
                        #-----------------------------------------------------------------------------------
                        index=fingerList.index(x)                       
                        dad=mc.listRelatives(x, p=1)[0]                     
                        if dad == joint:
                            group=mc.createNode('transform', n=x.replace('JNT', 'GRP'), p=handZTR )
                        else:
                            group=mc.createNode('transform', n=x.replace('JNT', 'GRP'), p=dad.replace('JNT', 'CTRL'))
                        
                        CONS=mc.createNode('transform', n=x.replace('JNT', 'CONS'), p=group)
                        ZTR=mc.createNode('transform', n=x.replace('JNT', 'ZTR'), p=CONS)
                        

                        spreadGRP=mc.createNode('transform', n=x.replace('JNT', 'spreadCONS'), p=CONS)
                        fistGRP=mc.createNode('transform', n=x.replace('JNT', 'fistCONS'), p=spreadGRP)                     

                        CTRL=mc.createNode('transform', n=x.replace('JNT', 'CTRL'), p=fistGRP)

                        mc.xform(group, t=(xCoord[0],xCoord[1],xCoord[2]), ws=1)
                        mc.xform(group, ro=(xOrient[0],xOrient[1],xOrient[2]), ws=1)                        

                        tempCTRL=absFunc.getDoubleDictJson(jointsDataPath, x, 'controlName')
                        absFunc.extractControl(CTRL, tempCTRL)                        
                        absFunc.setCurveColor(CTRL,'yellow')
                                         
                        mc.parentConstraint(CTRL, x)
                        #-fingerAttr-----------------------------------------------------------------------------
                        if mc.objExists(switchCtrl)==True:
                            if mc.getAttr(handControlData+'.spreadAxis')==0:
                                spreadAxis = 'Y'
                            elif mc.getAttr(handControlData+'.spreadAxis')==1:
                                spreadAxis = 'X'
                            elif mc.getAttr(handControlData+'.spreadAxis')==2:
                                spreadAxis = 'Z'

                            if mc.getAttr(handControlData+'.curlAxis')==0:
                                curlAxis = 'Z'
                            elif mc.getAttr(handControlData+'.curlAxis')==1:
                                curlAxis = 'Y'
                            elif mc.getAttr(handControlData+'.curlAxis')==2:
                                curlAxis = 'X'

                            if not 'Thumb' in x:
                                if x.endswith('01_JNT') == True:
                                    pass                                
                                    #spread---------------------------------------------------------------------------
                                    #spreadJoints.append(spreadGRP)
                                    #mc.connectAttr(switchCtrl+'.spread', spreadGRP+'.rotate'+spreadAxis)
                                if dad != joint:
                                    #fist--------------------------------------------------------------------------
                                    #fistJoints.append(fistGRP)
                                    mc.connectAttr(switchCtrl+'.fist', fistGRP+'.rotate'+curlAxis)                              

            #FOOT---------------------------------------------------------------------------------------------
            if joint == absFunc.getDoubleDictJson(footDataPath, joint, 'mainJoint'):
                #Defining Variables
                locatorsList=absFunc.getDoubleDictJson(footDataPath, joint, 'locators')
                footJoints=absFunc.getDoubleDictJson(footDataPath, joint, 'joints')
                switchCtrl=absFunc.getDoubleDictJson(footDataPath, joint, 'switchControl')
                footParent=absFunc.getDoubleDictJson(footDataPath, joint, 'footParent')
                ikHandleGRP=footParent.replace('JNT', 'ikHandleGrp')
                stretchIKLoc=footParent.replace('endJNT', 'distLoc_GRP')
                ikControlModuleParent=joint.replace('JNT', 'ikCTRL')
                footIkParent=footParent.replace('JNT', 'ikJNT')
                footFkParent=footParent.replace('JNT', 'fkJNT')             
                #-----------------------------------------------------------------------------------------
                if mc.objExists(ikControlModuleParent.replace('ikCTRL', 'ikSpace_parentConstraint1'))==True:
                    oldConstraint=ikControlModuleParent.replace('ikCTRL', 'ikSpace_parentConstraint1')
                    remapList=mc.listConnections(oldConstraint,s=1, d=0, type='remapValue')         
                    outSpace=mc.listConnections(oldConstraint,s=0, d=1,sh=0, type='transform')[0]
                    outSpaceGRP=outSpace.replace('ikSpace', 'ikSpaceGRP')
                    ztr=mc.listRelatives(outSpaceGRP, p=1)[0]
                    cons=mc.listRelatives(outSpace, c=1)
                    for i in cons:
                        if i != oldConstraint:
                            cons=i
                            break
                    mc.parent(cons, ztr)
                    mc.parent(outSpaceGRP, w=1)         
                
                #ik Joints_______________________________________________________________
                ikJointsList=[]
                for x in footJoints:
                    index=footJoints.index(x)
                    jointCoord=absFunc.getDoubleDictJson(jointsDataPath, x, 'translate')
                    jointOrient=absFunc.getDoubleDictJson(jointsDataPath, x, 'jointOrient')
                    if index == 0:
                        mc.select(cl=1)
                        scaleGRP=mc.createNode('transform', n=x.replace('JNT', 'ikScaleGRP'))
                        mc.xform(scaleGRP, t=(jointCoord[0],jointCoord[1],jointCoord[2]), ws=1)

                    ikJoint=mc.joint(n=x.replace('JNT', 'ikJNT'))                   
                    
                    if index == 0:                      
                        mc.parent(ikJoint, footIkParent)
                        mc.parent(scaleGRP, footIkParent)
                        mc.joint(ikJoint, e=1, p=(jointCoord[0],jointCoord[1],jointCoord[2]) ,o=(jointOrient[0],jointOrient[1],jointOrient[2]))
                        mc.parent(ikJoint, scaleGRP)
                    else:
                        mc.joint(ikJoint, e=1, p=(jointCoord[0],jointCoord[1],jointCoord[2]) ,o=(jointOrient[0],jointOrient[1],jointOrient[2]))

                    mc.makeIdentity(ikJoint, a=1)
                    ikJointsList.append(ikJoint)

                controlCoord=absFunc.getDoubleDictJson(jointsDataPath, joint, 'translate')
                controlOrient=absFunc.getDoubleDictJson(jointsDataPath, joint, 'worldOrient')
                mc.disconnectAttr(footJoints[0]+'.scale',footJoints[1]+'.inverseScale')
                mc.disconnectAttr(footJoints[0].replace('JNT', 'ikJNT')+'.scale',footJoints[1].replace('JNT', 'ikJNT')+'.inverseScale')

                ikZTRSwitch=[]
                ikFootZTR=mc.createNode('transform', n=joint.replace('JNT','ikFootZTR'), p='C_main_01_CTRL')
                ikFootCONS=mc.createNode('transform', n=joint.replace('JNT','ikFootCONS'), p=ikFootZTR)
                ikCTRL=mc.createNode('transform', n=joint.replace('JNT','ikFootCTRL'), p=ikFootCONS)
                ikTempCTRL=absFunc.getDoubleDictJson(footDataPath, joint, 'footIkControl')
                mc.xform(ikFootZTR, t=controlCoord, ws=1)
                mc.xform(ikFootZTR, ro=controlOrient, ws=1)

                if ikCONS.startswith('R_'):
                    mc.setAttr(ikFootZTR + '.scaleX', -1)
                    mc.setAttr(ikFootZTR + '.scaleY', -1)
                    mc.setAttr(ikFootZTR + '.scaleZ', -1)

                absFunc.extractControl(ikCTRL, ikTempCTRL)
                if ikCTRL.startswith('L_') is True:
                    absFunc.setCurveColor(ikCTRL,'blueLight')
                elif ikCTRL.startswith('R_') is True:                    
                    absFunc.setCurveColor(ikCTRL,'greenDark') 
                ikZTRSwitch.append(ikFootZTR)

                #visibility------------------------------------------------
                reverse=switchCtrl.replace('switchCTRL', 'reverse')                 
                
                for i in ikZTRSwitch:
                    mc.connectAttr(reverse+'.outputX', i+'.v')
                #----------------------------------------------------------

                if mc.objExists(ikControlModuleParent.replace('ikCTRL', 'ikSpace_parentConstraint1'))==True:
                    mc.parent(outSpaceGRP, ikFootZTR)
                    mc.parent(ikFootCONS, outSpace)

                mc.select(ikCTRL +'.cv[*]')
                mc.move(0,y=1)

                mc.addAttr(ikCTRL, ln='____', at='enum', en='footAttr:', k=1)
                mc.addAttr(ikCTRL, ln='footRoll', at='float', dv=0,  k=1)
                mc.addAttr(ikCTRL, ln='rollAngle', at='float', dv=20,  k=1)
                mc.addAttr(ikCTRL, ln='footBank', at='float', dv=0,  k=1)

                ############################
                #Create ikFoot Nodes_________________________________________________________________________
                ############################

                #BankNodes
                bankIn=mc.createNode('condition',n= joint.replace('JNT', 'bankInCOND'))
                bankExt=mc.createNode('condition',n= joint.replace('JNT', 'bankExtCOND'))

                mc.connectAttr(ikCTRL+'.footBank',bankIn+'.colorIfTrueR' )
                mc.connectAttr(ikCTRL+'.footBank',bankIn+'.firstTerm' )
                if joint.startswith('R_')==True:
                    mc.setAttr(bankIn+'.operation', 3)
                else:
                    mc.setAttr(bankIn+'.operation', 5)

                mc.setAttr(bankIn+'.colorIfFalseR', 0)
                mc.setAttr(bankIn+'.colorIfFalseG', 0)
                mc.setAttr(bankIn+'.colorIfFalseB', 0)

                mc.connectAttr(ikCTRL+'.footBank',bankExt+'.colorIfTrueR' )
                mc.connectAttr(ikCTRL+'.footBank',bankExt+'.firstTerm' )
                if joint.startswith('R_')==True:
                    mc.setAttr(bankExt+'.operation', 5)
                else:
                    mc.setAttr(bankExt+'.operation', 3)

                mc.setAttr(bankExt+'.colorIfFalseR', 0)
                mc.setAttr(bankExt+'.colorIfFalseG', 0)
                mc.setAttr(bankExt+'.colorIfFalseB', 0)

                #footRoll and Angle Nodes__________________________________________________________

                footFixDir=mc.createNode('multiplyDivide',n= joint.replace('JNT', 'fixDirectionMD'))
                mc.connectAttr(ikCTRL+'.rollAngle', footFixDir+'.input1X')
                mc.setAttr(footFixDir+'.input2X', -1)

                footPMA=mc.createNode('plusMinusAverage',n= joint.replace('JNT', 'PMA'))
                mc.connectAttr(ikCTRL+'.footRoll', footPMA+'.input2D[0].input2Dx')
                mc.connectAttr(footFixDir+'.outputX', footPMA+'.input2D[1].input2Dx')

                footA=mc.createNode('condition',n= joint.replace('JNT', 'ACOND'))
                mc.connectAttr(ikCTRL+'.footRoll',footA+'.colorIfTrueR' )
                mc.connectAttr(ikCTRL+'.footRoll',footA+'.firstTerm' )
                mc.connectAttr(ikCTRL+'.rollAngle',footA+'.secondTerm' )
                mc.connectAttr(ikCTRL+'.rollAngle',footA+'.colorIfFalseR' )
                mc.setAttr(footA+'.operation', 5)

                footB=mc.createNode('condition',n= joint.replace('JNT', 'BCOND'))
                mc.connectAttr(footPMA+'.output2Dx',footB+'.colorIfTrueR' )
                mc.connectAttr(ikCTRL+'.footRoll',footB+'.firstTerm' )
                mc.connectAttr(ikCTRL+'.rollAngle',footB+'.secondTerm' )
                mc.setAttr(footB+'.colorIfFalseR', 0 )
                mc.setAttr(footB+'.operation', 3)

                footC=mc.createNode('condition',n= joint.replace('JNT', 'CCOND'))   
                mc.connectAttr(ikCTRL+'.footRoll',footC+'.firstTerm')   
                mc.connectAttr(ikCTRL+'.footRoll', footC+'.colorIfFalseR' )
                mc.setAttr(footC+'.operation', 3)

                outputMD=mc.createNode('multiplyDivide',n= joint.replace('JNT', 'outputMD'))
                mc.connectAttr(footA+'.outColorR', outputMD+'.input1X')
                mc.connectAttr(footB+'.outColorR', outputMD+'.input1Y')
                mc.connectAttr(footC+'.outColorR', outputMD+'.input1Z') 

                footAOutput=mc.createNode('condition',n= joint.replace('JNT', 'AOutputCOND'))
                mc.connectAttr(outputMD+'.outputX',footAOutput+'.firstTerm' )
                mc.connectAttr(outputMD+'.outputX',footAOutput+'.colorIfFalseR' )
                mc.setAttr(footAOutput+'.operation', 5)
                
                #######################
                #ikFoot Inverse Drivers
                #######################
                
                footPos=absFunc.getDoubleDictJson(jointsDataPath, joint, 'translate')
                tempLoc=mc.spaceLocator(n='loca1')
                mc.xform(tempLoc, t=(footPos[0],footPos[1],footPos[2]), ws=1)
                tempList=mc.ls(tempLoc)
                allPoints=[joint] +locatorsList+tempList                
                mc.select(cl=1)
                allInverse=[]
                allOffsets = []
                for i in allPoints:
                    index=allPoints.index(i)
                    pos=mc.xform(i, q=1, t=1, ws=1)
                    rot=mc.xform(i, q=1, ro=1, ws=1)

                    inverseJoint=mc.joint(n=joint.replace('01_JNT', '0'+str(index)+'_ikInverseJoint'))
                    mc.xform(inverseJoint, t=(0,0,0), ws=1)
                    mc.xform(inverseJoint, ro=(0,0,0), ws=1)
                    mc.makeIdentity(inverseJoint, a=1)
                    if mc.listRelatives(inverseJoint, p=1)!=None:
                        tempDad=mc.listRelatives(inverseJoint, p=1)[0]
                    inverseGRP=mc.createNode('transform',n=joint.replace('01_JNT', '0'+str(index)+'_ikInverseJointGRP') )
                    inverseZTR=mc.createNode('transform',n=joint.replace('01_JNT', '0'+str(index)+'_ikInverseJointOffsetZTR'), p=inverseGRP )
                    
                    mc.parent(inverseJoint, inverseZTR)
                    allInverse.append(inverseJoint)
                    allOffsets.append(inverseZTR)
                    
                    if index ==0:
                        mc.xform(inverseGRP, t=(footPos[0],footPos[1],footPos[2]), ws=1)                        
                        mc.parent(inverseGRP, scalableDriverJoints)
                    #elif index==-1:
                        #mc.xform(inverseGRP, t=(footPos[0],footPos[1],footPos[2]), ws=1)
                        #mc.xform(inverseGRP, ro=rot, ws=1)
                    else:
                        mc.xform(inverseGRP, t=pos, ws=1)
                        mc.xform(inverseGRP, ro=rot, ws=1)
                        #mc.makeIdentity(inverseJoint, a=1)
                        mc.parent(inverseGRP, tempDad)
                    
                    if index==0:
                        mc.parentConstraint(ikCTRL, inverseGRP, mo=1)
                        mc.connectAttr(ikCTRL+'.s', inverseGRP+'.s', f=1)
                    if index==1:
                        mc.connectAttr(bankIn+'.outColorR', inverseGRP+'.rz')
                    if index==2:
                        mc.connectAttr(bankExt+'.outColorR', inverseGRP+'.rz')
                    if index==3:
                        mc.connectAttr(outputMD+'.outputZ', inverseGRP+'.rx')
                    if index==4:
                        mc.connectAttr(outputMD+'.outputY', inverseGRP+'.rx')
                        mc.orientConstraint(inverseJoint, ikJointsList[1], mo=1)
                    if index==5:
                        mc.connectAttr(footAOutput+'.outColorR', inverseGRP+'.rx')
                        mc.orientConstraint(inverseJoint, ikJointsList[0], mo=1)
                    mc.select(inverseJoint)
                mc.delete(tempLoc)              
                if mc.objExists(ikHandleGRP+'_parentConstraint1')==True:
                    mc.delete(ikHandleGRP+'_parentConstraint1')
                    mc.parentConstraint(allInverse[-1], ikHandleGRP, mo=1)                  
                    mc.setAttr(ikControlModuleParent+'.v', 0)
                    mc.addAttr(ikCTRL, ln='size', at='float', min=0.01,dv=1, k=1)
                    mc.connectAttr(ikCTRL+'.size', ikCTRL+'.scaleX')
                    mc.connectAttr(ikCTRL+'.size', ikCTRL+'.scaleY')
                    mc.connectAttr(ikCTRL+'.size', ikCTRL+'.scaleZ')
                    #mc.connectAttr(ikCTRL+'.s', footIkParent+'.s', f=1)
                    #mc.connectAttr(ikCTRL+'.s', scaleGRP+'.s', f=1)
                    #mc.scaleConstraint(ikCTRL, scaleGRP, mo=1)
                    mc.scaleConstraint(ikCTRL, footJoints[0].replace('JNT','ikJNT'), mo=1)
                    mc.orientConstraint(ikCTRL, footIkParent, mo=1)
                    
                if mc.objExists(stretchIKLoc+'_parentConstraint1')==True:
                    mc.delete(stretchIKLoc+'_parentConstraint1')
                    mc.parentConstraint(allInverse[-1], stretchIKLoc, mo=1)
                    toDelete=ikControlModuleParent.replace('CTRL', 'ZTR')                   
                    mc.delete(toDelete)

                
                
                #fk Joints____________________________________________________________________
                footJoints=absFunc.getDoubleDictJson(footDataPath, joint, 'joints')
                switchCtrl=absFunc.getDoubleDictJson(footDataPath, joint, 'switchControl')
                footParent=absFunc.getDoubleDictJson(footDataPath, joint, 'footParent')
                
                for x in footJoints:
                    index=footJoints.index(x)
                    jointCoord=absFunc.getDoubleDictJson(jointsDataPath, x, 'translate')
                    jointOrient=absFunc.getDoubleDictJson(jointsDataPath, x, 'jointOrient')
                    if index == 0:
                        mc.select(cl=1)
                    fkJoint=mc.joint(n=x.replace('JNT', 'fkJNT'))
                    
                    if index == 0:
                        fkParent=footParent.replace('JNT', 'fkJNT')
                        mc.parent(fkJoint, fkParent)
                        mc.joint(fkJoint, e=1, p=(jointCoord[0],jointCoord[1],jointCoord[2]) ,o=(jointOrient[0],jointOrient[1],jointOrient[2]))
                    else:
                        mc.joint(fkJoint, e=1, p=(jointCoord[0],jointCoord[1],jointCoord[2]) ,o=(jointOrient[0],jointOrient[1],jointOrient[2]))

                    mc.makeIdentity(fkJoint, a=1)               

                for i in footJoints:
                    controlCoord=absFunc.getDoubleDictJson(jointsDataPath, i, 'translate')
                    controlOrient=absFunc.getDoubleDictJson(jointsDataPath, i, 'worldOrient')
                    if i.endswith('endJNT')==False:
                        index=footJoints.index(i)
                        fkJoint=i.replace('JNT', 'fkJNT')                       
                        if index==0:
                            if mc.objExists(i.replace('JNT','fkZTR'))==True:
                                mc.delete(i.replace('JNT','fkZTR'))
                            tempGrandPa=mc.listRelatives(footParent, p=1)[0]
                            tempGrandPaCTRL=tempGrandPa.replace('JNT', 'fkCTRL')
                            tempGrandPa=tempGrandPa.replace('JNT', 'fkZTR')
                            tempGrandPa=mc.listRelatives(tempGrandPa, p=1)[0]
                            
                            fkFootZTR=mc.createNode('transform', n=i.replace('JNT','fkZTR'), p=tempGrandPa)                         
                        else:                           
                            fkFootZTR=mc.createNode('transform', n=i.replace('JNT','fkZTR'), p='C_main_01_CTRL')                    

                        fkFootCONS=mc.createNode('transform', n=i.replace('JNT','fkCONS'), p=fkFootZTR)
                        fkCTRL=mc.createNode('transform', n=i.replace('JNT','fkCTRL'), p=fkFootCONS)
                        tempCTRL=absFunc.getDoubleDictJson(jointsDataPath, i, 'controlName')
                        mc.xform(fkFootZTR, t=controlCoord, ws=1)
                        mc.xform(fkFootZTR, ro=controlOrient, ws=1)
                        absFunc.extractControl(fkCTRL, tempCTRL)
                        if fkCTRL.startswith('L_') is True:
                            absFunc.setCurveColor(fkCTRL,'blueLight')
                        elif fkCTRL.startswith('R_') is True:
                            absFunc.setCurveColor(fkCTRL,'greenDark')                       

                        if index == 0:
                            mc.parentConstraint(tempGrandPaCTRL, fkFootCONS, mo=1)
                            mc.parentConstraint(fkCTRL, fkJoint, mo=1)
                        elif index == 1:
                            mc.parentConstraint(footJoints[1], fkFootCONS, mo=1)
                            mc.scaleConstraint(footJoints[1], fkFootCONS, mo=1)
                            mc.parentConstraint(fkCTRL, footJoints[2], mo=1)
                            #mc.scaleConstraint(fkCTRL, footJoints[2], mo=1)

                for sj in footJoints:
                    if sj.endswith('endJNT')==False:
                        rev=switchCtrl.replace('switchCTRL', 'reverse')
                        ikj=sj.replace('JNT','ikJNT')
                        fkj=sj.replace('JNT','fkJNT')
                        blend=mc.createNode('blendColors', n=sj.replace('JNT', 'BC'))

                        mc.connectAttr(switchCtrl+'.IK_FK', blend+'.blender')
                        mc.connectAttr(ikj+'.scaleX', blend+'.color2R')
                        mc.connectAttr(ikj+'.scaleY', blend+'.color2G')
                        mc.connectAttr(ikj+'.scaleZ', blend+'.color2B')

                        mc.connectAttr(fkj+'.scaleX', blend+'.color1R')
                        mc.connectAttr(fkj+'.scaleY', blend+'.color1G')
                        mc.connectAttr(fkj+'.scaleZ', blend+'.color1B')

                        mc.connectAttr(blend+'.outputR', sj+'.scaleX')
                        mc.connectAttr(blend+'.outputG', sj+'.scaleY')
                        mc.connectAttr(blend+'.outputB', sj+'.scaleZ')                      
                        if a == ikStart:
                            pointCons=mc.pointConstraint(ik, fk, a, mo=1)
                            mc.connectAttr(switchCtrl+'.IK_FK', pointCons[0]+'.'+fk+'W1')
                            mc.connectAttr(rev+'.outputX', pointCons[0]+'.'+ik+'W0')
                        
                        oriCons=mc.orientConstraint(ikj, fkj, sj, mo=1)     
                        mc.setAttr(oriCons[0]+'.interpType', 2)
                        mc.connectAttr(switchCtrl+'.IK_FK', oriCons[0]+'.'+fkj+'W1')
                        mc.connectAttr(rev+'.outputX', oriCons[0]+'.'+ikj+'W0')         
            #IK MONO------------------------------------------------------------------------------------------
            #----------------------------------------------------------------------------------------------
            
            if joint == absFunc.getDoubleDictJson(ikMonoDataPath, joint, 'joint'):              

                base=absFunc.getDoubleDictJson(ikMonoDataPath, joint, 'joint')
                tip=absFunc.getDoubleDictJson(ikMonoDataPath, joint, 'child')
                parent=absFunc.getDoubleDictJson(ikMonoDataPath, joint, 'parent')
                parentDad=mc.listRelatives(parent, p=1)[0]
                if mc.objExists(parentDad.replace('JNT', 'CTRL'))==True:
                    dad=parentDad.replace('JNT', 'CTRL')
                elif mc.objExists(parentDad.replace('JNT', 'ikCTRL'))==True:
                    dad=parentDad.replace('JNT', 'ikCTRL')

                handleGRP=mc.createNode('transform', n=base.replace('JNT','ikHandleGRP'))
                handle = mc.ikHandle(sj=base, ee=tip, sol='ikSCsolver', n=base.replace('JNT','ikHandle'))[0]
                mc.delete(mc.pointConstraint(handle, handleGRP, mo=0))
                mc.parent(handle, handleGRP)

                baseCoord=absFunc.getDoubleDictJson(jointsDataPath, base, 'translate')
                tipCoord=absFunc.getDoubleDictJson(jointsDataPath, tip, 'translate')
                parentPos=absFunc.getDoubleDictJson(jointsDataPath, parent, 'translate')
                parentOrient=absFunc.getDoubleDictJson(jointsDataPath, base, 'worldOrient')
                mc.distanceDimension(ep=(0,0,1), sp= (0,0,10))
                loc1=mc.rename('locator1', base.replace('JNT', 'distLoc'))
                loc2=mc.rename('locator2', tip.replace('JNT', 'distLoc'))
                dist=mc.rename('distanceDimension1', tip.replace('JNT', 'distDimension'))
                mc.xform(loc1, t=(baseCoord[0],baseCoord[1],baseCoord[2]),ws=1)
                mc.xform(loc2, t=(tipCoord[0],tipCoord[1],tipCoord[2]),ws=1)
                distGrp=mc.createNode('transform', n=base.replace('JNT', 'distGRP'))
                mc.parent(handleGRP, distGrp)
                _obj=[loc1, loc2, dist]
                groups=absFunc.localGrp(_obj)               
                mc.parent(groups, distGrp)
                mc.parent(distGrp, 'dft_GRP')

                loc1Dad=mc.listRelatives(loc1, p=1)[0]
                loc2Dad=mc.listRelatives(loc2, p=1)[0]                

                ztr=mc.createNode('transform', n=base.replace('JNT','ZTR'))
                cons=mc.createNode('transform', n=base.replace('JNT','CONS'), p=ztr)
                CTRL=mc.createNode('transform', n=base.replace('JNT','CTRL'), p=cons)
                tempCtrl=absFunc.getDoubleDictJson(jointsDataPath, joint, 'controlName')

                mc.parent(ztr, dad )
                mc.xform(ztr, t=(parentPos[0], parentPos[1], parentPos[2]), ws=1)
                mc.xform(ztr, ro=(parentOrient[0], parentOrient[1], parentOrient[2]), ws=1)

                absFunc.extractControl(CTRL, tempCtrl)
                absFunc.setCurveColor(CTRL, 'red')
                mc.addAttr(CTRL, ln='squashFactor', at='float', min=-1, max=1, dv=0, k=1)
                mc.parentConstraint(CTRL, parent, mo=1)
                mc.parentConstraint(CTRL, loc1Dad, mo=1)
                mc.parentConstraint(handle, loc2Dad, mo=1)
                mc.parentConstraint(CTRL, handleGRP, mo=1)

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
                mc.connectAttr(CTRL+'.squashFactor', mdSquash+'.input2X')
                

                squashCond=mc.createNode('condition', n=base.replace('JNT', 'Squash_COND'))
                mc.setAttr(squashCond+'.operation', 4)
                mc.setAttr(squashCond+'.secondTerm', 1)
                mc.connectAttr(mdSquash+'.outputX', squashCond+'.firstTerm')
                mc.connectAttr(mdSquash+'.outputX', squashCond+'.colorIfTrueR')
                mc.connectAttr(mdSquash+'.outputX', squashCond+'.colorIfFalseR')

                mc.connectAttr(squashCond+'.outColorR', base+'.scaleX')
                mc.connectAttr(squashCond+'.outColorR', base+'.scaleZ')
            #Face-----------------------------------------------------------------------------------

            if absFunc.getDoubleDictJson(modulesDataPath, module, 'moduleType') ==5:
               
                base=absFunc.getSimpleJson(headDataPath, 'name')                
                parent=absFunc.getSimpleJson(headDataPath, 'parent')
                parentDad=mc.listRelatives(parent, p=1)[0]
                if mc.objExists(parentDad.replace('JNT', 'CTRL'))==True:
                    dad=parentDad.replace('JNT', 'CTRL')
                elif mc.objExists(parentDad.replace('JNT', 'ikCTRL'))==True:
                    dad=parentDad.replace('JNT', 'ikCTRL')

                Pos=absFunc.getDoubleDictJson(jointsDataPath, base, 'translate')
                Orient=absFunc.getDoubleDictJson(jointsDataPath, base, 'worldOrient')

                ztr=mc.createNode('transform', n=base.replace('JNT','ZTR'))
                cons=mc.createNode('transform', n=base.replace('JNT','CONS'), p=ztr)
                CTRL=mc.createNode('transform', n=base.replace('JNT','CTRL'), p=cons)
                tempCtrl=absFunc.getDoubleDictJson(jointsDataPath, joint, 'controlName')

                mc.parent(ztr, dad)
                mc.xform(ztr, t=(Pos[0], Pos[1], Pos[2]), ws=1)
                mc.xform(ztr, ro=(Orient[0], Orient[1], Orient[2]), ws=1)

                absFunc.extractControl(CTRL, tempCtrl)
                absFunc.setCurveColor(CTRL, 'red')
                mc.addAttr(CTRL, ln='space', at='enum', en='parent:hip', k=1)
                mc.parentConstraint(CTRL, base, mo=1)
                mc.connectAttr(CTRL+'.s', base+'.s')

                ikMonoEndLoc = parent.replace('endJNT', 'enddistLoc_ZTR')
                ikMonoEndHandle = parent.replace('endJNT', 'ikHandleGRP')
                if mc.objExists(ikMonoEndLoc.replace('ZTR', 'ZTR_parentConstraint1')) == True:
                    mc.delete(ikMonoEndLoc.replace('ZTR', 'ZTR_parentConstraint1'))
                    mc.parentConstraint(CTRL, ikMonoEndLoc, mo=1)
                else:
                    mc.parentConstraint(CTRL, ikMonoEndLoc, mo=1)

                if mc.objExists(ikMonoEndHandle.replace('GRP', 'GRP_parentConstraint1')) == True:
                    mc.delete(ikMonoEndHandle.replace('GRP', 'GRP_parentConstraint1'))
                    mc.parentConstraint(CTRL, ikMonoEndHandle, mo=1)
                else:
                    mc.parentConstraint(CTRL, ikMonoEndHandle, mo=1)
                # Head Space-------------------------------------------------------------------
                spaceHip='C_hip_01_CTRL'
              
                if mc.objExists(spaceHip.replace('CTRL', 'parentSpaceZTR'))==True:
                    parentSpaceZTR=spaceHip.replace('CTRL', 'parentSpaceZTR')
                    parentSpace=spaceHip.replace('CTRL', 'parentSpace')
                else:
                    parentSpaceZTR=mc.createNode('transform',n=spaceHip.replace('CTRL', 'parentSpaceZTR'))
                    parentSpace=mc.createNode('transform',n=spaceHip.replace('CTRL', 'parentSpace'), p=parentSpaceZTR)                     
                    mc.delete(mc.pointConstraint(spaceHip, parentSpaceZTR, mo=0))
                    mc.parent(parentSpaceZTR, spaceHip)

                mc.select(parentSpace)
                mc.select(cons, add=1)
                spaceConstraint=mc.orientConstraint(mo=1)

                mc.connectAttr(CTRL+'.space', spaceConstraint[0]+'.'+parentSpace+'W0')

                #FaceComponents-------------------------------------------------------------------------
                '''
                wireDataPath
                eyebrowDataPath
                eyesDataPath
                upperCheekDataPath
                lowerUpperHeadPath
                '''
                part = joint.replace('JNT', '')
                faceProxy = part + 'C_face_ControlProxy'                
                
                faceTypeDef = mc.getAttr(faceProxy + '.faceType')
                lowerUpperHead = mc.getAttr(faceProxy + '.lowerUpperHead')
                eyebrowExists = mc.getAttr(faceProxy + '.eyebrow')
                eyesExists = mc.getAttr(faceProxy + '.eyes')
                upperCheekExists = mc.getAttr(faceProxy + '.upperCheek')
                noseExists = mc.getAttr(faceProxy + '.nose')

                controlParent = joint.replace('JNT', 'CTRL')

                upperHeadControl = []
                upperHeadJoint = []

                if faceTypeDef == 0:
                    if lowerUpperHead:
                        upperHeadLoc = absFunc.getDoubleDictJson(lowerUpperHeadPath, joint, 'C_upperHeadLOC')
                        lowerHeadLoc = absFunc.getDoubleDictJson(lowerUpperHeadPath, joint, 'C_lowerHeadLOC')

                        allLocs = [upperHeadLoc] + [lowerHeadLoc]
                        for each in allLocs:                            
                            
                            proxyCtrl = each.replace('ProxyLoc', 'ControlProxy')

                            position = mc.xform(each, q=1, t=1, ws=1)
                            orientation = mc.xform(each, q=1, ro=1, ws=1)
                            ztr = mc.createNode('transform', n=each.replace('ProxyLoc', 'ZTR'), p=controlParent)
                            ctrl = mc.createNode('transform', n=each.replace('ProxyLoc', 'CTRL'), p=ztr)
                            mc.xform(ztr, t=position, ws=1)
                            mc.xform(ztr, ro=orientation, ws=1)

                            ctrl = absFunc.extractControl(ctrl, proxyCtrl)

                            tempJoint = mc.joint(n=each.replace('ProxyLoc', 'JNT'), rad=0.8)
                            mc.xform(tempJoint, t=position, ws=1)
                            mc.xform(tempJoint, ro=orientation, ws=1)
                            mc.makeIdentity(tempJoint, a=1)
                            mc.parent(tempJoint, joint)
                            mc.parentConstraint(ctrl, tempJoint, mo=1)
                            mc.connectAttr(ctrl + '.scale', tempJoint + '.scale')

                            if 'upperHead_CTRL' in ctrl:
                                upperHeadControl.append(ctrl)
                                upperHeadJoint.append(tempJoint)

                            

                    if upperCheekExists == 1:

                        innerLOC_L = absFunc.getDoubleDictJson(upperCheekDataPath, joint, 'L_innerLOC')
                        midLOC_L = absFunc.getDoubleDictJson(upperCheekDataPath, joint, 'L_midLOC')
                        outLOC_L = absFunc.getDoubleDictJson(upperCheekDataPath, joint, 'L_outerLOC')

                        innerLOC_R = absFunc.getDoubleDictJson(upperCheekDataPath, joint, 'R_innerLOC')
                        midLOC_R = absFunc.getDoubleDictJson(upperCheekDataPath, joint, 'R_midLOC')
                        outLOC_R = absFunc.getDoubleDictJson(upperCheekDataPath, joint, 'R_outerLOC')

                        upperCheekGroupSystem = mc.createNode('transform', n= part + 'upperCheekSystem_GRP', p=driverJoints)
                        leftLocs = [innerLOC_L] + [midLOC_L] + [outLOC_L]
                        rigthLocs = [innerLOC_R] + [midLOC_R] + [outLOC_R]

                        wireCurves = absFunc.getDoubleDictJson(wireDataPath, joint, 'allCurves')
                        upperCheekCurves = []
                        
                        for each in wireCurves:
                            if 'upperCheek' in each:                                
                                curve = mc.createNode('transform', n = each.replace('CurveWireProxy', 'CRV') )
                                curve = absFunc.extractControl(curve, each)
                                upperCheekCurves.append(curve)
                                mc.parent(curve, upperCheekGroupSystem)
                        
                        for l in leftLocs:                            
                            index = leftLocs.index(l)
                            r = l.replace('_L_', '_R_')
                            sides = [l] + [r]
                            for i in sides:
                                proxyCtrl = i.replace('ProxyLoc', 'ControlProxy')

                                position = mc.xform(i, q=1, t=1, ws=1)
                                orientation = mc.xform(i, q=1, ro=1, ws=1)
                                ztr = mc.createNode('transform', n=i.replace('ProxyLoc', 'ZTR'), p=controlParent)
                                ctrl = mc.createNode('transform', n=i.replace('ProxyLoc', 'CTRL'), p=ztr)
                                mc.xform(ztr, t=position, ws=1)
                                mc.xform(ztr, ro=orientation, ws=1)

                                ctrl = absFunc.extractControl(ctrl, proxyCtrl)                                

                                if i.startswith(part + 'R_'):
                                    mc.setAttr(ztr + '.sx', -1)

                        for c in upperCheekCurves:
                            if  c.startswith(part + 'L_'):
                                operandSide = leftLocs
                            if c.startswith(part + 'R_'):
                                operandSide = rigthLocs

                            for i in operandSide:
                                index = operandSide.index(i)
                                cluName = i.replace('ProxyLoc', 'CLU')
                                control = i.replace('ProxyLoc', 'CTRL')
                                if index == 0:
                                    vertexGroup = '.cv[0:1]'
                                if index == 1:
                                    vertexGroup = '.cv[2:3]'
                                if index == 2:
                                    vertexGroup = '.cv[4:5]'

                                mc.select(c + vertexGroup)
                                cluster = mc.cluster()[1]
                                mc.setAttr(cluster + '.v', 0)
                                mc.parent(cluster, upperCheekGroupSystem)
                                cluster = mc.rename(cluster, cluName)                                

                                if  c.startswith(part + 'L_'):
                                    mc.connectAttr(control + '.t', cluster + '.t', f=1)
                                    mc.connectAttr(control + '.r', cluster + '.r', f=1)
                                    mc.connectAttr(control + '.s', cluster + '.s', f=1)

                                if c.startswith(part + 'R_'):

                                    attr=mc.listAttr(control, k=1)
                                    md = mc.createNode('multiplyDivide', n= control.replace('CTRL', 'InverseMD'))
                                    mc.setAttr(md+'.input2X', -1)
                                    mc.setAttr(md+'.input2Y', -1)
                                    mc.setAttr(md+'.input2Z', -1)

                                    for x in attr:
                                        if x.startswith('translate') == True:
                                            if x == 'translateX':
                                                mc.connectAttr(control + '.' + x, md + '.input1X', f=1)
                                                mc.connectAttr(md + '.outputX', cluster + '.' + x, f=1)
                                            else: 
                                                mc.connectAttr(control + '.' + x, cluster + '.' + x, f=1)

                                        if x.startswith('rotate') == True:
                                            if x == 'rotateX':
                                                mc.connectAttr(control + '.' + x, cluster + '.' + x, f=1)

                                            elif  x == 'rotateY':
                                                mc.connectAttr(control + '.' + x, md +'.input1Y', f=1)
                                                mc.connectAttr(md + '.outputY', cluster + '.' + x, f=1)

                                            elif  x == 'rotateZ':
                                                mc.connectAttr(control + '.' + x, md + '.input1Z', f=1)
                                                mc.connectAttr(md + '.outputZ', cluster + '.' + x, f=1)

                                        if x.startswith('scale') == True:
                                            mc.connectAttr(control + '.s', cluster + '.s', f=1)

                    if eyebrowExists == 1:

                        innerLOC_L = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'L_innerLOC')
                        midLOC_L = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'L_midLOC')
                        outLOC_L = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'L_outerLOC')
                        centerLOC_C = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'C_centerLOC')
                        innerLOC_R = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'R_innerLOC')
                        midLOC_R = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'R_midLOC')
                        outLOC_R = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'R_outerLOC')
                        masterLOC_R = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'R_masterLOC')
                        masterLOC_L = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'L_masterLOC')

                        masterCTRL_L = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'L_masterCtrl')
                        masterCTRL_R = absFunc.getDoubleDictJson(eyebrowDataPath, joint, 'R_masterCtrl')



                        eyebrowGroupSystem = mc.createNode('transform', n= part + 'eyebrowSystem_GRP', p=driverJoints)
                        leftLocs = [outLOC_L] + [midLOC_L] + [innerLOC_L] 
                        rigthLocs = [innerLOC_R] + [midLOC_R] + [outLOC_R] 
                        centerLoc = [centerLOC_C]
                        mastersLocs = [masterLOC_R] + [masterLOC_L]
                        LCLocs = leftLocs + centerLoc
                        allLocs = leftLocs + centerLoc + rigthLocs


                        wireCurves = absFunc.getDoubleDictJson(wireDataPath, joint, 'allCurves')
                        eyebrowCurves = []

                        L_parentClues = []
                        R_parentClues = []

                        L_ConClues = []
                        R_ConClues = []

                        masterControl_L = []
                        masterControl_R = []

                        for each in wireCurves:
                            if 'eyebrow' in each:                                
                                curve = mc.createNode('transform', n = each.replace('CurveWireProxy', 'CRV') )
                                curve = absFunc.extractControl(curve, each)
                                eyebrowCurves.append(curve)
                                mc.parent(curve, eyebrowGroupSystem)
                        
                        for m in mastersLocs:                            
                            proxyCtrl = m.replace('ProxyLoc', 'ControlProxy')
                            position = mc.xform(m, q=1, t=1, ws=1)
                            orientation = mc.xform(m, q=1, ro=1, ws=1)
                            ztr = mc.createNode('transform', n=m.replace('ProxyLoc', 'ZTR'), p=controlParent)
                            ctrl = mc.createNode('transform', n=m.replace('ProxyLoc', 'CTRL'), p=ztr)
                            mc.xform(ztr, t=position, ws=1)
                            mc.xform(ztr, ro=orientation, ws=1)                            

                            ctrl = absFunc.extractControl(ctrl, proxyCtrl)
                            if m.startswith(part + 'R_'):
                                masterControl_R.append(ctrl)
                            if m.startswith(part + 'L_'):
                                masterControl_L.append(ctrl)

                            if m.startswith(part + 'R_'):
                                mc.setAttr(ztr + '.sx', -1)


                            cluGrp = mc.createNode('transform', n=m.replace('ProxyLoc', 'CLUGRP'), p=eyebrowGroupSystem)
                            cluParent = mc.createNode('transform', n=m.replace('ProxyLoc', 'CLUParent'), p=cluGrp)
                            mc.xform(cluGrp, t=position, ws=1)
                            mc.xform(cluGrp, ro=orientation, ws=1)

                            if m.startswith(part + 'L_'):
                                L_parentClues.append(cluGrp)
                                L_ConClues.append(cluParent)

                            if m.startswith(part + 'R_'):
                                R_parentClues.append(cluGrp)
                                R_ConClues.append(cluParent)
                                mc.setAttr(cluGrp + '.sx', -1)


                        for l in LCLocs:
                            index = LCLocs.index(l)
                            r = l.replace('_L_', '_R_')

                            if 'center' in l:
                                sides = [l]
                                
                            else:
                                sides = [l] + [r]
                                

                            for i in sides:
                                proxyCtrl = i.replace('ProxyLoc', 'ControlProxy')
                                position = mc.xform(i, q=1, t=1, ws=1)
                                orientation = mc.xform(i, q=1, ro=1, ws=1)
                                ztr = mc.createNode('transform', n=i.replace('ProxyLoc', 'ZTR'))
                                ctrl = mc.createNode('transform', n=i.replace('ProxyLoc', 'CTRL'), p=ztr)
                                
                                if i.startswith(part + 'L_') is True:
                                    mc.parent(ztr, masterControl_L[0])
                                elif i.startswith(part + 'R_') is True:
                                    mc.parent(ztr, masterControl_R[0])
                                elif i.startswith(part + 'C_') is True:
                                    mc.parent(ztr, controlParent)

                                mc.xform(ztr, t=position, ws=1)
                                mc.xform(ztr, ro=orientation, ws=1)

                                ctrl = absFunc.extractControl(ctrl, proxyCtrl)

                                if i.startswith(part + 'R_'):
                                    mc.setAttr(ztr + '.sx', -1)
                        
                        for c in allLocs:
                            
                            index = allLocs.index(c)

                            cluName = c.replace('ProxyLoc', 'CLU')
                            control = c.replace('ProxyLoc', 'CTRL')

                            if index == 0:
                                vertexGroup = '.cv[0]'
                            if index == 1:
                                vertexGroup = '.cv[1]'
                            if index == 2:
                                vertexGroup = '.cv[2]'
                            if index == 3:
                                vertexGroup = '.cv[3]'
                            if index == 4:
                                vertexGroup = '.cv[4]'
                            if index == 5:
                                vertexGroup = '.cv[5]'
                            if index == 6:
                                vertexGroup = '.cv[6]'

                            mc.select(eyebrowCurves[0] + vertexGroup)
                            cluster = mc.cluster()[1]
                            mc.setAttr(cluster + '.v', 0)
                            
                            
                            cluster = mc.rename(cluster, cluName)

                            cluContainer = absFunc.localGrp(cluster) 

                            if cluster.startswith(part + 'L_') is True:
                                mc.parent(cluContainer, L_ConClues[0])

                            elif cluster.startswith(part +'R_') is True:
                                mc.parent(cluContainer, R_ConClues[0])

                            elif cluster.startswith(part +'C_') is True:
                                mc.parent(cluContainer, eyebrowGroupSystem)

                            if c.startswith(part + 'R_'):

                                attr=mc.listAttr(control, k=1)
                                md = mc.createNode('multiplyDivide', n= control.replace('CTRL', 'InverseMD'))
                                mc.setAttr(md+'.input2X', -1)
                                mc.setAttr(md+'.input2Y', -1)
                                mc.setAttr(md+'.input2Z', -1)

                                for x in attr:
                                    if x.startswith('translate') == True:
                                        if x == 'translateX':
                                            mc.connectAttr(control + '.' + x, md + '.input1X', f=1)
                                            mc.connectAttr(md + '.outputX', cluster + '.' + x, f=1)
                                        else: 
                                            mc.connectAttr(control + '.' + x, cluster + '.' + x, f=1)

                                    if x.startswith('rotate') == True:
                                        if x == 'rotateX':
                                            mc.connectAttr(control + '.' + x, cluster + '.' + x, f=1)

                                        elif  x == 'rotateY':
                                            mc.connectAttr(control + '.' + x, md +'.input1Y', f=1)
                                            mc.connectAttr(md + '.outputY', cluster + '.' + x, f=1)

                                        elif  x == 'rotateZ':
                                            mc.connectAttr(control + '.' + x, md + '.input1Z', f=1)
                                            mc.connectAttr(md + '.outputZ', cluster + '.' + x, f=1)

                                    if x.startswith('scale') == True:
                                        mc.connectAttr(control + '.s', cluster + '.s', f=1)
                            
                            else:
                                mc.connectAttr(control + '.t', cluster + '.t', f=1)
                                mc.connectAttr(control + '.r', cluster + '.r', f=1)
                                mc.connectAttr(control + '.s', cluster + '.s', f=1)

                        for masterCon in mastersLocs:

                            control = masterCon.replace('ProxyLoc', 'CTRL')
                            masterChild = masterCon.replace('ProxyLoc', 'CLUParent')

                            mc.connectAttr(control + '.t', masterChild + '.t', f=1)
                            mc.connectAttr(control + '.r', masterChild + '.r', f=1)
                            mc.connectAttr(control + '.s', masterChild + '.s', f=1)

                              



                    if eyesExists == 1:
                        
                        eyesMainControlZTR = mc.createNode('transform', n = part + 'C_eyes_01_ZTR', p='C_main_01_CTRL')
                        eyesMainControlCONS = mc.createNode('transform', n = part + 'C_eyes_01_CONS', p=eyesMainControlZTR)
                        eyesMainControl = mc.circle(n='C_eyes_01_CTRL', nr=(0, 0, 1), r=5, c=(0, 0, 0))[0]
                        mc.parent(eyesMainControl, eyesMainControlCONS)

                        eyelidsGroupSystem = mc.createNode('transform', n= part + 'eyelidsSystem_GRP', p=driverJoints)

                        eyeCtrl_L = absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_eyeCtrl')
                        eyeCtrl_R = absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_eyeCtrl')

                        mc.delete(mc.pointConstraint(eyeCtrl_L, eyeCtrl_R, eyesMainControlZTR, mo=0))

                        mc.joint(n='C_eyelidsHolder_01_JNT', rad=0.8)
                        mc.select(cl=1)

                        mc.addAttr(eyesMainControl, ln='__', at='enum', en='pupils', k=1)
                        mc.addAttr(eyesMainControl, ln='lPupil', at='float', min=0.01, dv=1,  k=1)
                        mc.addAttr(eyesMainControl, ln='rPupil', at='float', min=0.01, dv=1,  k=1)
                        mc.addAttr(eyesMainControl, ln='___', at='enum', en='eyelids', k=1)
                        mc.addAttr(eyesMainControl, ln='fleshyEyelids', at='float', max=1, min=0, dv=1, k=1)
                        mc.addAttr(eyesMainControl, ln='lBlink', at='float', max=1, min=0, k=1)
                        mc.addAttr(eyesMainControl, ln='lBlinkPose', at='float', max=1, min=0, dv=0.8, k=1)
                        mc.addAttr(eyesMainControl, ln='rBlink', at='float', max=1, min=0, k=1)
                        mc.addAttr(eyesMainControl, ln='rBlinkPose', at='float', max=1, min=0, dv=0.8, k=1)
                        mc.addAttr(eyesMainControl, ln='space', at='enum', en='main:head', k=1)

                        spaceCons = mc.parentConstraint(controlParent, eyesMainControlCONS, mo=1)[0]                        
                        mc.connectAttr(eyesMainControl + '.space', spaceCons + '.' + controlParent + 'W0')

                        for x in range(0, 2):
                            index = range(0, 2).index(x)

                            if index == 0:                                
                                angle = absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_angle')
                                eyeSocketProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_socketLOC')
                                eyeCenterProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_eyeLOC')
                                eyePupilProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_pupilLOC')

                                eyeUpperLidParentProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_upperLidBaseLOC')
                                eyeLowerLidParentProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_lowerLidBaseLOC')

                                eyeUpperLidProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_upperLidLOC')
                                eyeLowerLidProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_lowerLidLOC') 

                                eyeControlProxy =   absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_eyeCtrl')
                                socketControlProxy =   absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_socketCtrl')

                                upperLidControlProxy =   absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_upperLidCtrl')
                                lowerLidControlProxy =   absFunc.getDoubleDictJson(eyesDataPath, joint, 'L_lowerLidCtrl')

                                
                                pupilAttr = 'lPupil'
                                blinkAttr = 'lBlink'
                                blinkPoseAttr = 'lBlinkPose'
                                side = 'L_'

                            elif index == 1:
                                angle = absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_angle')
                                eyeSocketProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_socketLOC')
                                eyeCenterProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_eyeLOC')
                                eyePupilProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_pupilLOC')

                                eyeUpperLidParentProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_upperLidBaseLOC')
                                eyeLowerLidParentProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_lowerLidBaseLOC')

                                eyeUpperLidProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_upperLidLOC')
                                eyeLowerLidProxy = absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_lowerLidLOC')

                                eyeControlProxy =   absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_eyeCtrl')
                                socketControlProxy =   absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_socketCtrl')

                                upperLidControlProxy =   absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_upperLidCtrl')
                                lowerLidControlProxy =   absFunc.getDoubleDictJson(eyesDataPath, joint, 'R_lowerLidCtrl')

                                pupilAttr = 'rPupil'
                                blinkAttr = 'rBlink'
                                blinkPoseAttr = 'rBlinkPose'
                                side = 'R_'

                            moveValue = 3

                            eyeSocketProxyPos = mc.xform(eyeSocketProxy, q=1, t=1, ws=1)
                            eyeSocketProxyRot = mc.xform(eyeSocketProxy, q=1, ro=1, ws=1)

                            eyeCenterProxyPos = mc.xform(eyeCenterProxy, q=1, t=1, ws=1)
                            eyeCenterProxyRot = mc.xform(eyeCenterProxy, q=1, ro=1, ws=1)

                            eyePupilProxyPos = mc.xform(eyePupilProxy, q=1, t=1, ws=1)
                            eyePupilProxyRot = mc.xform(eyePupilProxy, q=1, ro=1, ws=1)

                            eyeUpperLidParentProxyPos = mc.xform(eyeUpperLidParentProxy, q=1, t=1, ws=1)
                            eyeUpperLidParentProxyRot = mc.xform(eyeUpperLidParentProxy, q=1, ro=1, ws=1)

                            eyeLowerLidParentProxyPos = mc.xform(eyeLowerLidParentProxy, q=1, t=1, ws=1)
                            eyeLowerLidParentProxyRot = mc.xform(eyeLowerLidParentProxy, q=1, ro=1, ws=1)

                            eyeUpperLidProxyPos = mc.xform(eyeUpperLidProxy, q=1, t=1, ws=1)
                            eyeUpperLidProxyRot = mc.xform(eyeUpperLidProxy, q=1, ro=1, ws=1)

                            eyeLowerLidProxyPos = mc.xform(eyeLowerLidProxy, q=1, t=1, ws=1)
                            eyeLowerLidProxyRot = mc.xform(eyeLowerLidProxy, q=1, ro=1, ws=1)

                            eyeCenterControlProxyPos = mc.xform(eyeControlProxy, q=1, t=1, ws=1)
                            eyeCenterControlProxyRot = mc.xform(eyeControlProxy, q=1, ro=1, ws=1)

                            upperLidControlProxyPos = mc.xform(upperLidControlProxy, q=1, t=1, ws=1)
                            upperLidControlProxyRot = mc.xform(upperLidControlProxy, q=1, ro=1, ws=1)

                            lowerLidControlProxyPos = mc.xform(lowerLidControlProxy, q=1, t=1, ws=1)
                            lowerLidControlProxyRot = mc.xform(lowerLidControlProxy, q=1, ro=1, ws=1)

                            # Creating Joints------------------------------------------------

                            mc.select(cl=1)
                            socketJoint = mc.joint(n=part + side + 'socket_01_JNT', rad=1.5)
                            mc.xform(socketJoint, t=eyeSocketProxyPos, ws=1)
                            mc.xform(socketJoint, ro=eyeSocketProxyRot, ws=1)
                            mc.parent(socketJoint, upperHeadJoint[0])
                            mc.makeIdentity(socketJoint, a=1)                            
                            mc.select(cl=1)

                            eyeJoint = mc.joint(n=part + side + 'eye_01_JNT', rad=0.8)
                            mc.xform(eyeJoint, t=eyeCenterProxyPos, ws=1)
                            mc.xform(eyeJoint, ro=eyeCenterProxyRot, ws=1)
                            mc.setAttr(eyeJoint + '.rotateOrder', 1)
                            mc.parent(eyeJoint, socketJoint)
                            mc.makeIdentity(eyeJoint, a=1)                            
                            mc.select(cl=1)

                            pupilJoint = mc.joint(n=part + side + 'pupil_01_JNT', rad=0.8)
                            mc.xform(pupilJoint, t=eyePupilProxyPos, ws=1)
                            mc.xform(pupilJoint, ro=eyePupilProxyRot, ws=1)
                            mc.parent(pupilJoint, eyeJoint)
                            mc.makeIdentity(pupilJoint, a=1)                            
                            mc.select(cl=1)

                            upperLidParentJoint = mc.joint(n=part + side + 'upperLid_01_JNT', rad=0.8)
                            mc.xform(upperLidParentJoint, t=eyeUpperLidParentProxyPos, ws=1)
                            mc.xform(upperLidParentJoint, ro=eyeUpperLidParentProxyRot, ws=1)
                            mc.setAttr(upperLidParentJoint + '.rotateOrder', 1)
                            mc.parent(upperLidParentJoint, eyelidsGroupSystem)
                            mc.makeIdentity(upperLidParentJoint, a=1)                            
                            mc.select(cl=1)

                            upperLidJoint = mc.joint(n=part + side + 'upperLid_02_JNT', rad=0.8)
                            mc.xform(upperLidJoint, t=eyeUpperLidProxyPos, ws=1)
                            mc.xform(upperLidJoint, ro=eyeUpperLidProxyRot, ws=1)
                            mc.parent(upperLidJoint, upperLidParentJoint)
                            mc.makeIdentity(upperLidJoint, a=1)                            
                            mc.select(cl=1)

                            lowerLidParentJoint = mc.joint(n=part + side + 'lowerLid_01_JNT', rad=0.8)
                            mc.xform(lowerLidParentJoint, t=eyeLowerLidParentProxyPos, ws=1)
                            mc.xform(lowerLidParentJoint, ro=eyeLowerLidParentProxyRot, ws=1)
                            mc.setAttr(lowerLidParentJoint + '.rotateOrder', 1)
                            mc.parent(lowerLidParentJoint, eyelidsGroupSystem)
                            mc.makeIdentity(lowerLidParentJoint, a=1)                            
                            mc.select(cl=1)

                            lowerLidJoint = mc.joint(n=part + side + 'lowerLid_02_JNT', rad=0.8)
                            mc.xform(lowerLidJoint, t=eyeLowerLidProxyPos, ws=1)
                            mc.xform(lowerLidJoint, ro=eyeLowerLidProxyRot, ws=1)
                            mc.parent(lowerLidJoint, lowerLidParentJoint)
                            mc.makeIdentity(lowerLidJoint, a=1)                            
                            mc.select(cl=1)

                            # Creating Global Controls and system:
                            eyeSocketControlZTR = mc.createNode('transform', n=part + side + 'socket_01_ZTR', p=upperHeadControl[0])
                            eyeSocketControl = mc.createNode('transform', n=part + side + 'socket_01_CTRL', p=eyeSocketControlZTR)
                            mc.xform(eyeSocketControlZTR, t=eyeSocketProxyPos, ws=1)
                            mc.xform(eyeSocketControlZTR, ro=eyeSocketProxyRot, ws=1)
                            absFunc.extractControl(eyeSocketControl, socketControlProxy)
                            mc.parentConstraint(eyeSocketControl, socketJoint, mo=1)
                            mc.connectAttr(eyeSocketControl + '.s', socketJoint + '.s')

                            eyeControlGRP = mc.createNode('transform', n=part + side + 'eye_01_GRP', p=eyesMainControl)
                            eyeControlZTR = mc.createNode('transform', n=part + side + 'eye_01_ZTR', p=eyeControlGRP)
                            eyeControl = mc.createNode('transform', n=part + side + 'eye_01_CTRL', p=eyeControlZTR)
                            mc.xform(eyeControlGRP, t=eyeCenterControlProxyPos, ws=1)
                            mc.xform(eyeControlGRP, ro=eyeCenterControlProxyRot, ws=1)
                            absFunc.extractControl(eyeControl, eyeControlProxy)
                            mc.aimConstraint(eyeControl, eyeJoint, wuo=eyeSocketControl, wut='objectrotation', wu=(0, 1, 0), u=(0, 1, 0), aim=(0, 0, 1))
                            mc.disconnectAttr(socketJoint + '.scale', eyeJoint + '.inverseScale')

                            # Creating local Controls and system:
                            upperLidZTR = mc.createNode('transform', n=part + side + 'upperLid_01_ZTR', p=eyeSocketControl)
                            upperLidControl = mc.createNode('transform', n=part + side + 'upperLid_01_CTRL', p=upperLidZTR)                            
                            mc.xform(upperLidZTR, t=upperLidControlProxyPos, ws=1)
                            mc.xform(upperLidZTR, ro=upperLidControlProxyRot, ws=1)
                            absFunc.extractControl(upperLidControl, upperLidControlProxy)

                            lowerLidZTR = mc.createNode('transform', n=part + side + 'lowerLid_01_ZTR', p=eyeSocketControl)
                            lowerLidControl = mc.createNode('transform', n=part + side + 'lowerLid_01_CTRL', p=lowerLidZTR)                            
                            mc.xform(lowerLidZTR, t=lowerLidControlProxyPos, ws=1)
                            mc.xform(lowerLidZTR, ro=lowerLidControlProxyRot, ws=1)
                            absFunc.extractControl(lowerLidControl, lowerLidControlProxy)

                            followHelperGRP = mc.createNode('transform', n=part + side + 'eyeLidFinalRot_01_GRP', p=socketJoint)
                            followHelper = mc.createNode('transform', n=part + side + 'eyeLidFinalRot_01_CONS', p=followHelperGRP)
                            mc.xform(followHelperGRP, t=eyeCenterProxyPos, ws=1)
                            mc.xform(followHelperGRP, ro=eyeCenterProxyRot, ws=1)
                            mc.parentConstraint(eyeJoint, followHelper, mo=1)

                            # Creating NOdes----------------------------------------------------------------------
                            # Remaping translations:------------------------------------------------------------
                            lowLidVertRMP = mc.createNode('remapValue', n=part + side + 'lowerLid_vertical_01_REMAP')
                            mc.connectAttr(lowerLidControl + '.ty', lowLidVertRMP + '.inputValue')
                            mc.setAttr(lowLidVertRMP + '.inputMin', moveValue * -1)
                            mc.setAttr(lowLidVertRMP + '.inputMax', moveValue)
                            mc.setAttr(lowLidVertRMP + '.outputMin', angle)
                            mc.setAttr(lowLidVertRMP + '.outputMax', angle * -1)

                            lowLidSideRMP = mc.createNode('remapValue', n=part + side + 'lowerLid_side_01_REMAP')
                            mc.connectAttr(lowerLidControl + '.tx', lowLidSideRMP + '.inputValue')
                            mc.setAttr(lowLidSideRMP + '.inputMin', moveValue * -1)
                            mc.setAttr(lowLidSideRMP + '.inputMax', moveValue)
                            mc.setAttr(lowLidSideRMP + '.outputMin', -10)
                            mc.setAttr(lowLidSideRMP + '.outputMax', 10)

                            lowLidPMA = mc.createNode('plusMinusAverage', n=part + side + 'lowerLid_01_PMA')
                            mc.connectAttr(lowLidVertRMP + '.outValue', lowLidPMA + '.input3D[0].input3Dx')
                            mc.connectAttr(lowLidSideRMP + '.outValue', lowLidPMA + '.input3D[0].input3Dy')
                            # Connecting Side Move and Rotation:
                            mc.connectAttr(lowLidPMA + '.output3Dy', lowerLidParentJoint + '.ry')
                            mc.connectAttr(lowerLidControl + '.rz', lowerLidParentJoint + '.rz')

                            upLidVertRMP = mc.createNode('remapValue', n=part + side + 'upperLid_vertical_01_REMAP')
                            mc.connectAttr(upperLidControl + '.ty', upLidVertRMP + '.inputValue')
                            mc.setAttr(upLidVertRMP + '.inputMin', moveValue * -1)
                            mc.setAttr(upLidVertRMP + '.inputMax', moveValue)
                            mc.setAttr(upLidVertRMP + '.outputMin', angle)
                            mc.setAttr(upLidVertRMP + '.outputMax', angle * -1)

                            upLidSideRMP = mc.createNode('remapValue', n=part + side + 'upperLid_side_01_REMAP')
                            mc.connectAttr(upperLidControl + '.tx', upLidSideRMP + '.inputValue')
                            mc.setAttr(upLidSideRMP + '.inputMin', moveValue * -1)
                            mc.setAttr(upLidSideRMP + '.inputMax', moveValue)
                            mc.setAttr(upLidSideRMP + '.outputMin', -10)
                            mc.setAttr(upLidSideRMP + '.outputMax', 10)

                            upLidPMA = mc.createNode('plusMinusAverage', n=part + side + 'upperLid_01_PMA')
                            mc.connectAttr(upLidVertRMP + '.outValue', upLidPMA + '.input3D[0].input3Dx')
                            mc.connectAttr(upLidSideRMP + '.outValue', upLidPMA + '.input3D[0].input3Dy')
                            # Connecting Side Move and Rotation:
                            mc.connectAttr(upLidPMA + '.output3Dy', upperLidParentJoint + '.ry')
                            mc.connectAttr(upperLidControl + '.rz', upperLidParentJoint + '.rz')

                            # Starting fleshyEleyelids------------------------------------------------------
                            fleshyMD = mc.createNode('multiplyDivide', n=part + side + 'fleshyEyelid_01_MD')
                            mc.connectAttr(followHelper + '.rx', fleshyMD + '.input1X')
                            mc.connectAttr(followHelper + '.ry', fleshyMD + '.input1Y')
                            mc.connectAttr(followHelper + '.rz', fleshyMD + '.input1Z')
                            mc.connectAttr(eyesMainControl + '.fleshyEyelids', fleshyMD + '.input2X')
                            mc.connectAttr(eyesMainControl + '.fleshyEyelids', fleshyMD + '.input2Y')

                            # FleshyRemaps:
                            lowLidFollow = mc.createNode('remapValue', n=part + side + 'lowerLid_01_followREMAP')
                            mc.connectAttr(fleshyMD + '.outputX', lowLidFollow + '.inputValue')
                            mc.setAttr(lowLidFollow + '.inputMin', angle * -1)
                            mc.setAttr(lowLidFollow + '.inputMax', angle)
                            mc.setAttr(lowLidFollow + '.outputMin', angle * -1)
                            mc.setAttr(lowLidFollow + '.outputMax', angle)
                            mc.setAttr(lowLidFollow + '.value[0].value_FloatValue', 0.42)
                            mc.setAttr(lowLidFollow + '.value[0].value_Position', 0)
                            mc.setAttr(lowLidFollow + '.value[2].value_FloatValue', 0.5)
                            mc.setAttr(lowLidFollow + '.value[2].value_Position', 0.5)
                            mc.setAttr(lowLidFollow + '.value[1].value_FloatValue', 0.72)
                            mc.setAttr(lowLidFollow + '.value[1].value_Position', 1)
                            mc.setAttr(lowLidFollow + '.value[2].value_Interp', 1)

                            upLidFollow = mc.createNode('remapValue', n=part + side + 'upperLid_01_followREMAP')
                            mc.connectAttr(fleshyMD + '.outputX', upLidFollow + '.inputValue')
                            mc.setAttr(upLidFollow + '.inputMin', angle * -1)
                            mc.setAttr(upLidFollow + '.inputMax', angle)
                            mc.setAttr(upLidFollow + '.outputMin', angle * -1)
                            mc.setAttr(upLidFollow + '.outputMax', angle)
                            mc.setAttr(upLidFollow + '.value[0].value_FloatValue', 0.16)
                            mc.setAttr(upLidFollow + '.value[0].value_Position', 0)
                            mc.setAttr(upLidFollow + '.value[2].value_FloatValue', 0.5)
                            mc.setAttr(upLidFollow + '.value[2].value_Position', 0.5)
                            mc.setAttr(upLidFollow + '.value[1].value_FloatValue', 1)
                            mc.setAttr(upLidFollow + '.value[1].value_Position', 1)
                            mc.setAttr(upLidFollow + '.value[2].value_Interp', 1)

                            sideFollowRmp = mc.createNode('remapValue', n=part + side + 'eyeSide_01_followREMAP')
                            mc.connectAttr(fleshyMD + '.outputY', sideFollowRmp + '.inputValue')
                            mc.setAttr(sideFollowRmp + '.inputMin', angle * -1)
                            mc.setAttr(sideFollowRmp + '.inputMax', angle)
                            mc.setAttr(sideFollowRmp + '.outputMin', -10)
                            mc.setAttr(sideFollowRmp + '.outputMax', 10)

                            # Connecting with mains PMAs-------------------------------------------------------------

                            mc.connectAttr(lowLidFollow + '.outValue', lowLidPMA + '.input3D[1].input3Dx')
                            mc.connectAttr(sideFollowRmp + '.outValue', lowLidPMA + '.input3D[1].input3Dy')

                            mc.connectAttr(upLidFollow + '.outValue', upLidPMA + '.input3D[1].input3Dx')
                            mc.connectAttr(sideFollowRmp + '.outValue', upLidPMA + '.input3D[1].input3Dy')

                            # Blink----------------------------------------------------------------------------------
                            blinkPMA = mc.createNode('plusMinusAverage', n=part + side + 'eyeLidBlink_01_PMA')
                            mc.setAttr(blinkPMA + '.operation', 2)
                            mc.connectAttr(lowLidPMA + '.output3Dx', blinkPMA + '.input3D[0].input3Dx')
                            mc.connectAttr(upLidPMA + '.output3Dx', blinkPMA + '.input3D[1].input3Dx')
                            mc.setAttr(blinkPMA + '.input3D[2].input3Dx', angle * -1)

                            eyeLidBLinkMD = mc.createNode('multiplyDivide', n=part + side + 'eyelidBlink_01_MD')
                            mc.connectAttr(blinkPMA + '.output3Dx', eyeLidBLinkMD + '.input1X')
                            mc.connectAttr(eyesMainControl + '.' + blinkAttr, eyeLidBLinkMD + '.input2X')

                            # Blending blink with mains PMAs------------------------------------------------------------

                            lowerLidBlend = mc.createNode('blendColors', n=part + side + 'lowerLidBlend_01_BC')
                            mc.connectAttr(eyesMainControl + '.' + blinkPoseAttr, lowerLidBlend + '.blender')
                            mc.connectAttr(eyeLidBLinkMD + '.outputX', lowerLidBlend + '.color2R')
                            mc.setAttr(lowerLidBlend + '.color1R', 0)
                            mc.setAttr(lowerLidBlend + '.color1G', 0)
                            mc.setAttr(lowerLidBlend + '.color1B', 0)

                            upperLidBlend = mc.createNode('blendColors', n=part + side + 'upperLidBlend_01_BC')
                            mc.connectAttr(eyesMainControl + '.' + blinkPoseAttr, upperLidBlend + '.blender')
                            mc.connectAttr(eyeLidBLinkMD + '.outputX', upperLidBlend + '.color1R')
                            mc.setAttr(upperLidBlend + '.color2R', 0)
                            mc.setAttr(upperLidBlend + '.color2G', 0)
                            mc.setAttr(upperLidBlend + '.color2B', 0)

                            lowerBlinkPMA = mc.createNode('plusMinusAverage', n=part + side + 'lowerLidBlink_01_PMA')
                            mc.setAttr(lowerBlinkPMA + '.operation', 2)
                            mc.connectAttr(lowLidPMA + '.output3Dx', lowerBlinkPMA + '.input3D[0].input3Dx')
                            mc.connectAttr(lowerLidBlend + '.outputR', lowerBlinkPMA + '.input3D[1].input3Dx')

                            upperBlinkPMA = mc.createNode('plusMinusAverage', n=part + side + 'lowerLidBlink_01_PMA')
                            mc.connectAttr(upLidPMA + '.output3Dx', upperBlinkPMA + '.input3D[0].input3Dx')
                            mc.connectAttr(upperLidBlend + '.outputR', upperBlinkPMA + '.input3D[1].input3Dx')

                            # Connecting with lowerLidJoint-------------------------------------------------------------

                            mc.connectAttr(lowerBlinkPMA + '.output3Dx', lowerLidParentJoint + '.rx')

                            # Addtional Push Nodes for upperJoint-----------------------------------------------------------

                            upperPushPMA = mc.createNode('plusMinusAverage', n=part + side + 'upperPush_01_PMA')
                            mc.connectAttr(lowerLidParentJoint + '.rx', upperPushPMA + '.input3D[1].input3Dx')
                            mc.setAttr(upperPushPMA + '.input3D[0].input3Dx', angle)

                            upperPushClamp = mc.createNode('clamp', n=side + 'upperPush_01_CLAMP')
                            mc.setAttr(upperPushClamp + '.minR', angle * -1)
                            mc.connectAttr(upperBlinkPMA + '.output3Dx', upperPushClamp + '.inputR')
                            mc.connectAttr(upperPushPMA + '.output3Dx', upperPushClamp + '.maxR')

                            mc.connectAttr(upperPushClamp + '.outputR', upperLidParentJoint + '.rx')

                            # Connecting Pupils------------------------------------------------------------

                            mc.connectAttr(eyesMainControl + '.' + pupilAttr, pupilJoint + '.sx')
                            mc.connectAttr(eyesMainControl + '.' + pupilAttr, pupilJoint + '.sy')
                        


            
            #Ribbon---------------------------------------------------------------------------------
            if absFunc.getDoubleDictJson(modulesDataPath, module, 'ribbon') ==1:
                jointQty=absFunc.getDoubleDictJson(modulesDataPath, module, 'twistJoints')
                jointChild=mc.listRelatives(joint, c=1)[0]
                absFunc.applyLimbRibbon(joint, jointChild, jointQty, joint.replace('JNT', 'NURBS'))
                sleeve=absFunc.getDoubleDictJson(modulesDataPath, module, 'sleeve')
                #Sleeve------------------------
                if sleeve==1:
                    sleeveRibbon=absFunc.applyLimbRibbon(joint, jointChild, jointQty, joint.replace('JNT', 'sleeve_NURBS'), _sleeve=1)

                    controls=absFunc.getDoubleDictJson(sleeveDataPath, joint, 'controls')

                    maingrp=mc.createNode('transform', n=joint.replace('JNT', 'sleeveGRP'), p='C_main_01_CTRL')
                    maincons=mc.createNode('transform', n=joint.replace('JNT', 'sleeveCONS'), p=maingrp)
                    mainztr=mc.createNode('transform', n=joint.replace('JNT', 'sleeveZTR'), p=maincons)
                    #if maingrp.startswith('R_')==True:
                        #mc.setAttr(maingrp+'.scaleX', -1)
                    
                    tempMain=absFunc.getDoubleDictJson(sleeveDataPath, joint, 'main')
                    mainCoord=mc.xform(tempMain, q=1, t=1, ws=1)
                    mainOri=mc.xform(tempMain, q=1, ro=1, ws=1)
                    mc.xform(maingrp, t=mainCoord, ws=1)
                    mc.xform(maingrp, ro=mainOri, ws=1)

                    distances=[]
                    values=[]
                    locs=[]
                    for d in sleeveRibbon:
                        mc.distanceDimension(ep=(0,0,1), sp= (0,0,10))
                        loc1=mc.rename('locator1', d+'_startTempLoc')
                        loc2=mc.rename('locator2', d+'_EndTempLoc')
                        dist=mc.rename('distanceDimension1', d+'_tempDistDimension')
                        mc.pointConstraint(d, loc1)
                        mc.pointConstraint(maingrp, loc2)
                        value=mc.getAttr(dist+'.distance')
                        values.append(value)
                        distances.append(dist)
                        locs.append(loc1)
                        locs.append(loc2)
                    
                    minValue=min(values)

                    for s in distances:
                        value=mc.getAttr(s+'.distance')
                        if minValue==value:
                            miniJoint=s.replace('_tempDistDimension','')
                    mc.delete(locs)

                    mc.parentConstraint(miniJoint, maincons, mo=1)

                    curveCoords=[]
                    for j in controls:
                        controlCoord=mc.xform(j, q=1, t=1, ws=1)
                        curveCoords.append(controlCoord)

                    curve=mc.curve( ep=curveCoords, d=1)
                    curve=mc.rename(curve, joint.replace('JNT','sleeveCTRL'))
                    mc.closeCurve(curve,ch=1, ps=1, rpo=1, bb=0.5, bki=0, p=0.1)
                    absFunc.setCurveColor(curve, 'red')
                    mc.parent(curve, mainztr)
                    mc.xform(curve, cpc=1)
                    mc.makeIdentity(curve, a=1)

                    for i in controls:
                        coord=mc.xform(i,q=1, t=1, ws=1)
                        ori=mc.xform(i,q=1, ro=1, ws=1)
                        index=controls.index(i)
                        ztr=mc.createNode('transform', n=joint.replace('JNT', str(index)+'sleeveZTR'), p=curve)
                        CTRL=mc.createNode('transform', n=joint.replace('JNT', str(index)+'sleeveCTRL'), p=ztr)
                        mc.xform(ztr, t=coord, ws=1 )
                        mc.xform(ztr, ro=ori, ws=1 )
                        absFunc.extractControl(CTRL, i)
                        absFunc.setCurveColor(CTRL, 'yellow')

                        sleevejnt=mc.joint(n=joint.replace('JNT', str(index)+'sleeveJNT'), p=coord, o=ori)
                        mc.parent(sleevejnt, miniJoint)
                        mc.makeIdentity(sleevejnt, a=1)
                        mc.parentConstraint(CTRL, sleevejnt, mo=0)
                        mc.connectAttr(CTRL+'.s', sleevejnt+'.s')

            #FK---------------------------------------------------------------------------------            
            #if absFunc.getDoubleDictJson(modulesDataPath, module, 'fk') ==1:
                

        self.statusBar.setStyleSheet("QStatusBar{color:rgb(3, 255, 11);background-color: rgb(30, 30, 30);}")
        self.statusBar.showMessage('Rig Done', 15000)


            #Face-------------------------------------------------------------------------------------------

        
        '''
        if self.checkBox_finalRig.isChecked():
            pass

        elif not self.checkBox_finalRig.isChecked():
        '''





##--------------------------------------------------------------------------------------------
## MAIN
##-------------------------------------------------------------------------------------------- 

def runApp():
    for qt in QtWidgets.QApplication.topLevelWidgets():
        try:
            qtname = qt.objectName()
            if qtname == "jenAutorig_MainWindow":
                print ("found qtmainwindow of script instance match, closing...")
                qt.close()
        except:
            pass
    app = ProgramUI()
    app.show()

runApp()


