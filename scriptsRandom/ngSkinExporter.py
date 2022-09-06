import maya.cmds as mc
from ngSkinTools.importExport import *
import os
import json


class ImportExportNgLayers:
    def __init__(self, action):
        self.currentFile = mc.file(q=True, sn=True)
        self.fileName = self.currentFile.split('/')[-1]
        path = os.path.dirname(self.currentFile)
        skinFolder = '/skinWeights'
        self.jsonPath = path + skinFolder
        self.selection = mc.ls(sl=1)
        self.windowName = 'Import Ng Layers'
        self.selectedVersion = None
        self.currentVersion = None
        if action is 'import':
            self.importUI()
        elif action is 'export':
            self.ngSkinExportData()

    def ngSkinExportData(self):
        if not os.path.exists(self.jsonPath):
            os.makedirs(self.jsonPath)
        if len(self.selection) is 0:
            mc.warning('# ERROR: Nothing selected')
        else:
            print '#'*30, 'NG EXPORTER REPORT', '#'*30
            for sel in self.selection:
                layerData = LayerData()
                layerData.loadFrom(sel)
                exporter = JsonExporter()
                jsonContents = exporter.process(layerData)  # string data
                # convert from string to dictionary
                jsonContents = json.loads(jsonContents)
                with open(self.jsonPath + '/' + sel + '.json', 'w') as outfile:
                    json.dump(jsonContents, outfile, sort_keys=1,
                              indent=4, separators=(',', ': '))                    
                    print'Saving:...', sel + '.json'
            print 'NG skin layers correctly saved in:...', self.jsonPath

    def ngSkinImportData(self, *args):
        for ngFile in os.listdir(self.jsonPath):
            if ngFile.endswith('.json'):
                skinnedMesh = ngFile.split('.')[0]
                if self.selectedVersion in skinnedMesh:
                    selectedMesh = skinnedMesh.replace(
                        self.selectedVersion, self.currentVersion)
                    if mc.objExists(selectedMesh):
                        if selectedMesh in self.selection:
                            print '-' * 50
                            print 'Mesh:', skinnedMesh
                            print 'Loading from:... ', self.jsonPath + '/' + ngFile
                            with open(self.jsonPath + '/' + ngFile) as json_data:
                                data = json.load(json_data)  # dict
                                # convert from dict to string
                                data = json.dumps(data)
                            importer = JsonImporter()
                            layerData = importer.process(data)
                            try:
                                layerData.saveTo(selectedMesh)
                                print 'Loaded from:... ', skinnedMesh, 'TO', selectedMesh
                            except:
                                mc.warning(
                                    '# ERROR: transfer skin to ' + selectedMesh)
                    else:
                        print'Mesh:...' + selectedMesh + ' does not exists.'

    def importUI(self):
        if mc.window('importNgVarWin', exists=True):
            mc.deleteUI('importNgVarWin')
        win = mc.window('importNgVarWin', title=self.windowName,
                        widthHeight=(170, 55), s=0)
        mc.columnLayout(adj=1)
        versions = []
        for ngFile in os.listdir(self.jsonPath):
            if ngFile.endswith('.json'):
                components = ngFile.split('_')
                for i in components:
                    if ':' in i:
                        version = i.split(':')[0]
                        versions.append(version)
        ordererVersions = []
        for x in versions:
            if x not in ordererVersions:
                ordererVersions.append(x)
        ordererVersions.sort()
        # VersionBox
        mc.columnLayout()
        combo = mc.optionMenu(label='Version:', w=170, cc=self.pickVersion)
        for content in ordererVersions:
            mc.menuItem(label=content)
        mc.setParent('..')
        mc.separator()
        # Import Button
        mc.columnLayout()
        mc.button(label='Import NG Layers', align='center',
                  w=170, command=self.ngSkinImportData)
        # Setting the initial value  of the version
        if len(self.selection) is not 0:
            self.selectedVersion = mc.optionMenu(combo, q=1, v=1)
            self.currentVersion = self.queryCurrentVersion()
            mc.showWindow(win)
        else:
            mc.warning('# ERROR: nothing selected')

    def pickVersion(self, item):
        self.selectedVersion = item

    def queryCurrentVersion(self):
        firstObj = self.selection[0].split('_')
        for x in firstObj:
            if ':' in x:
                self.currentVersion = x.split(':')[0]
                return self.currentVersion
