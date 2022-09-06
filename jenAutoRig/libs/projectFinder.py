import maya.cmds as mc
import os

self.ui = projectUI(self.labelFolder)


self.btn_subfolder.clicked.connect(lambda: self.ui.openFolder())

class projectUI():
    ''' '''
    def __init__(self, _projectTextEdit, _folderLabel, _browseButton, _cboxAssetName, _cboxAssetType):
        self.lbl_Folder = _folderLabel
        self.comboBox_assetType = _cboxAssetType
        self.comboBox_assetName = _cboxAssetName


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


    def createSubFolder(self):
        ''' Crea subcarpetas de folder'''
        finalPath=mc.getAttr('jenAutorig_projectPathNode.finalPath')            
        if not os.path.exists(finalPath+r'/skin/skinWeights'):
            os.makedirs(finalPath+r'/skin/skinWeights')
        if not os.path.exists(finalPath+r'/mask/maskData'):
            os.makedirs(finalPath+r'/mask/maskData')
        if not os.path.exists(finalPath+r'/setup/setupData'):
            os.makedirs(finalPath+r'/setup/setupData')          

    def openFolder(self):
        ''' Abre explorer la carpeta '''
        #finalPath=mc.getAttr('jenAutorig_projectPathNode.finalPath')
        finalPath=self.lbl_Folder.text()
        os.startfile(finalPath)

    def openJsonCfg(self):
        pass