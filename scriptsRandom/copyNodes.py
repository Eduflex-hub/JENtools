import maya.cmds as mc
import json
import getpass


class CopyNodes:
    def __init__(self, action):
        user = getpass.getuser()
        print user
        self.folderPath = r'C:/Users/Eduflex/Dropbox/JENtools/scriptsRandom/copyNodesData'
        self.file = 'CopyNodesTemp_' + user + '.json'
        self.copyNodesDict = {}
        self.nameSpace = 'tempNameSpaceCopyNodes'
        if action is 'copy':
            self.copy()
        elif action is 'paste':
            self.paste()
    # Store the node data into a Json file

    def copy(self):
        sel = mc.ls(sl=1)
        for node in sel:
            nodeDataDict = {}
            # Asking for the typeNode
            nodeType = mc.nodeType(node)
            nodeDataDict['type'] = nodeType
            # Listing all attributes
            attributes = mc.listAttr(node, s=1, hd=1, m=1)
            attrDict = {}
            for attr in attributes:
                value = mc.getAttr(node + '.' + attr)
                attrDict[attr] = value
            nodeDataDict['attributes'] = attrDict
            # Extracting inputs and outputs
            inputConnections = mc.listConnections(node, s=1, d=0, p=1, c=1)
            # Storing data on dictionaries
            nodeDataDict['inputs'] = inputConnections
            self.copyNodesDict[node] = nodeDataDict
        with open(self.folderPath + self.file, 'w') as outfile:
            json.dump(self.copyNodesDict, outfile, sort_keys=1, indent=4)
    # Calls the Json file and create the nodes

    def paste(self):
        jsonPath = self.folderPath + self.file
        fIn = open(jsonPath, 'r')
        mainDict = json.load(fIn)
        nodeNames = mainDict.keys()
        pastedNodes = []
        tempNamespace = mc.namespace(add=self.nameSpace)
        for nodeName in nodeNames:
            # Calling nodeType
            type = mainDict.get(nodeName).get('type')
            allAttributes = mainDict.get(nodeName).get('attributes')
            # Creating Node:
            newNode = mc.createNode(type, n=tempNamespace + ':' + nodeName)
            # Setting Attr:
            attrList = allAttributes.keys()
            for attr in attrList:
                value = allAttributes.get(attr)
                mc.setAttr(newNode + '.' + attr, value)
            pastedNodes.append(newNode)
        # Connecting Nodes:
        for x in nodeNames:
            inputs = mainDict.get(x).get('inputs')
            if inputs is not None:
                tupList = tuple(inputs)
                for target, source in self.pairwise(tupList):
                    if mc.objExists(tempNamespace + ':' + source) is True:
                        mc.connectAttr(tempNamespace + ':' + source,
                                       tempNamespace + ':' + target, f=1)
        mc.namespace(removeNamespace=self.nameSpace,
                     mergeNamespaceWithRoot=True)
    # Pairing every two elements on tuple

    def pairwise(self, it):
        it = iter(it)
        while True:
            yield next(it), next(it)
