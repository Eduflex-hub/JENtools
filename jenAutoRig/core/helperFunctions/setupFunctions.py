import maya.cmds as mc
import maya.mel as mel
from jen.functions import abstractFunctions as absFunc
reload(absFunc)


class setupFunctionsClass():
    def __init__(self):
        pass

    def group(self, nodes, name):
        ''' group nodes and return transform Node
            Args:
                nodes (string) maya nodes, must be a list
                name (string) given name
        '''
        grp = mc.createNode('transform', n=name)

        for child in nodes:
            self.parentNodes(child, grp)
        return grp

    def createTransform(self, name):
        return mc.createNode('transform', n = name)

    def addSpaceLoc(self, name):
        ''' returns a maya spacelocator node '''
        loc = mc.spaceLocator(n=name)
        mc.setAttr(loc[0] + '.localScaleX', 0.8)
        mc.setAttr(loc[0] + '.localScaleY', 0.8)
        mc.setAttr(loc[0] + '.localScaleZ', 0.8)
        return loc

    def moveNode(self, node, x, y, z, t=False, ro=False):
        ''' moves node to given location '''
        if t:
            mc.xform(node, t=(x, y, z), os=1)
        if ro:
            mc.xform(node, ro=(x, y, z), os=1)

    def parentNodes(self, child, parent):
        '''
        parent nodes
        Args:
            child (string) maya child node
            parent (string) maya parent node
        '''
        mc.parent(child, parent)

    def angleQuery(self, showObject, centerObj, upperObj, lowerObject):
        '''
        calculate a real time angle difference bettwen nodes
        Args:
            showObject (string) maya node where is the angle attr
            centerObj (string) maya node pivot angle
            UpperObj (string) maya node upper Vector
            lowerObject (string) maya node lower Vector
        '''

        mc.addAttr(showObject, ln='lidsAngle', at='float', k=1)

        baseDeComp = mc.createNode('decomposeMatrix', n=centerObj + '_deCompBase')
        targetDeComp = mc.createNode('decomposeMatrix', n=lowerObject + '_deCompTarget')
        poseDeComp = mc.createNode('decomposeMatrix', n=upperObj + '_deCompPose')

        mc.connectAttr(centerObj + '.worldMatrix[0]', baseDeComp + '.inputMatrix')
        mc.connectAttr(lowerObject + '.worldMatrix[0]', targetDeComp + '.inputMatrix')
        mc.connectAttr(upperObj + '.worldMatrix[0]', poseDeComp + '.inputMatrix')

        pma1 = mc.createNode('plusMinusAverage', n=centerObj + '_angleExtractPMA1')
        pma2 = mc.createNode('plusMinusAverage', n=centerObj + '_angleExtractPMA2')
        mc.setAttr(pma1 + '.operation', 2)
        mc.setAttr(pma2 + '.operation', 2)

        mc.connectAttr(targetDeComp + '.outputTranslate', pma1 + '.input3D[0]')
        mc.connectAttr(baseDeComp + '.outputTranslate', pma1 + '.input3D[1]')

        mc.connectAttr(baseDeComp + '.outputTranslate', pma2 + '.input3D[1]')
        mc.connectAttr(poseDeComp + '.outputTranslate', pma2 + '.input3D[0]')

        angle = mc.createNode('angleBetween', n=centerObj + '_AB')

        mc.connectAttr(pma1 + '.output3D', angle + '.vector1')
        mc.connectAttr(pma2 + '.output3D', angle + '.vector2')

        pmaResult = mc.createNode('plusMinusAverage', n=centerObj + '_RESULT')
        mc.connectAttr(angle + '.angle', pmaResult + '.input1D[0]')
        mc.connectAttr(pmaResult + '.output1D', showObject + '.lidsAngle')

    def proxyControl(self, controlType, offset, name):
        '''
        create the proxy controls under an object
        Args:
            parent (string) parent of control
            controlType (string) shape control (sphere or circle)
            offset (float) move the shape of the control
            name (string) name of the control
        '''
        control = False
        if controlType == 'circle':
            control = mc.circle(n=name, nr=(0, 0, 1), r=1, c=(0, 0, offset))[0]

        if controlType == 'sphere':
            control = mel.eval('curve -d 1 -p 0 1 0 -p -0.5 0.866025 0 -p -0.866025 0.5 0 -p -1 0 0 -p -0.866025 -0.5 0 -p -0.5 -0.866025 0 -p 0 -1 0 -p 0.5 -0.866025 0 -p 0.866025 -0.5 0 -p 1 0 0 -p 0.866025 0.5 0 -p 0.5 0.866025 0 -p 0 1 0 -p 0 0.866025 -0.5 -p 0 0.5 -0.866025 -p 0 0 -1 -p 0 -0.5 -0.866025 -p 0 -0.866025 -0.5 -p 0 -1 0 -p 0 -0.866025 0.5 -p 0 -0.5 0.866025 -p 0 0 1 -p 0 0.5 0.866025 -p 0 0.866025 0.5 -p 0 1 0 -p 0 0.866025 -0.5 -p 0 0.5 -0.866025 -p 0 0 -1 -p 0.707107 0 -0.707107 -p 1 0 0 -p 0.707107 0 0.707107 -p 0 0 1 -p -0.707107 0 0.707107 -p -1 0 0 -p -0.707107 0 -0.707107 -p 0 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 ;')
            control = mc.rename(control, name)
            mc.setAttr(control + '.sx', 0.5)
            mc.setAttr(control + '.sy', 0.5)
            mc.setAttr(control + '.sz', 0.5)
            mc.makeIdentity(control, a=1)

        if controlType == 'face':
            control = mc.circle(n=name, r=8, nr=(0, 0, 1))[0]
            absFunc.setCurveColor(control, 'pink')

        if controlType == 'lowerUpperHead':
            control = mc.circle(n=name, nr=(0, 0, 1), r=2, c=(0, 0, offset))[0]

        if controlType == 'lowerUpperHeadCircle':
            control = mc.circle(n=name, nr=(0, 1, 0), r=5, c=(0, offset, 0))[0]

        if controlType == 'eyebrow':
            control = mel.eval('curve -d 3 -p -5 3 0 -p -4.355556 3.384615 0 -p -3.066667 4.153846 0 -p -0.733333 4.384615 0 -p 0 2.307692 0 -p 0.733333 4.384615 0 -p 3.066667 4.153846 0 -p 4.355556 3.384615 0 -p 5 3 0 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 6 -k 6 ;')
            control = mc.rename(control, name)
            absFunc.setCurveColor(control, 'pink')

        if controlType == 'mouth':
            control = mel.eval('curve -d 3 -p -5 -2 0 -p -2 -4 0 -p 2 -4 0 -p 5 -2 0 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 ;')
            control = mc.rename(control, name)
            absFunc.setCurveColor(control, 'pink')

        if controlType == 'eyes':
            control = mel.eval('curve -d 1 -p -2 2 0 -p -3 3 0 -p -4 2 0 -p -3 1 0 -p -2 2 0 -p 2 2 0 -p 3 1 0 -p 4 2 0 -p 3 3 0 -p 2 2 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;')
            control = mc.rename(control, name)
            absFunc.setCurveColor(control, 'pink')

        if controlType == 'nose':
            control = mel.eval('curve -d 1 -p 0 2 0 -p -1 0 0 -p 0 -1 0 -p 1 0 0 -p 0 2 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
            control = mc.rename(control, name)
            absFunc.setCurveColor(control, 'pink')

        if controlType == 'chin':
            control = mel.eval('curve -d 1 -p 0 -6 0 -p -0.5 -6.5 0 -p 0 -7 0 -p 0.5 -6.5 0 -p 0 -6 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
            control = mc.rename(control, name)            
            absFunc.setCurveColor(control, 'pink')

        if controlType == 'ears':
            control = mel.eval('curve -d 1 -p 6.931967 3.933404 0 -p 8 4.5 0 -p 8.5 6 0 -p 10 3.5 0 -p 9 1 0 -p 7.730341 1.965982 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 ;')
            control = mc.rename(control, name)
            absFunc.setCurveColor(control, 'pink')

        if controlType == 'upperCheek':
            control = mel.eval('curve -d 1 -p -5 0.5 0 -p -3 0 0 -p -1.5 0.5 0 -p 1.5 0.5 0 -p 3 0 0 -p 5 0.5 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 ;')
            control = mc.rename(control, name)
            absFunc.setCurveColor(control, 'pink')

        if controlType == 'lowerCheek':
            control = mel.eval('curve -d 1 -p 6 0 0 -p 5.5 -1 0 -p 6 -2 0 -p 6.5 -1 0 -p 6 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
            control = mc.rename(control, name)
            absFunc.setCurveColor(control, 'pink')

        if not control:
            mc.warning('NO CONTROL')
        return control

    def addAttr(self, node,  attrType, attrs, attrContent):
        if attrType == 'enum':
            for attr in attrs:
                index = attrs.index(attr)
                mc.addAttr(node, ln=attr, at='enum', en=attrContent[index], k=1)

    def connectAttr(self, nodeA, attrA, nodeB, attrB):        
        mc.connectAttr(nodeA + '.' + attrA, nodeB + '.' + attrB)

    def masterEyeControlProxy(self, name):
        masterEyeControl = mc.circle(n=name, nr=(0, 0, 1), r=3, c=(0, 0, 0))[0]
        

    def curveOnPoints(self, name, groupName, points, rebuild = 1, rigType =''):
        pointList = mc.ls(points)      
        curveCoords=[]
        for j in pointList:
            pointCoord=mc.xform(j, q=1, t=1, ws=1)
            curveCoords.append(pointCoord)
        
        curve=mc.curve( ep=curveCoords, d=3)
        curve=mc.rename(curve, name)        
        group = self.group([curve], groupName)

        if rebuild:
            if rigType == 'upperCheek':
                mel.eval('rebuildCurve -ch 0 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s 3 -d 3 -tol 0.01 "{}";'.format(curve))

            if rigType == 'eyebrow':                
                mel.eval('rebuildCurve -ch 0 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s 5 -d 2 -tol 0.01 "{}";'.format(curve))                

        for i in points:
            index = points.index(i)
            cluName = name + '_proxyCLU'

            if rigType == 'upperCheek':                
                if index == 0:
                    vertexGroup = '.cv[0:1]'
                if index == 1:
                    vertexGroup = '.cv[2:3]'
                if index == 2:
                    vertexGroup = '.cv[4:5]'

            if rigType == 'eyebrow':
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

                cvPos = mc.xform(curve + vertexGroup, q=1, t=1, ws=1)
                mc.xform(i, t=cvPos, ws=1)

            mc.select(curve + vertexGroup)
            cluster = mc.cluster()[1]
            mc.setAttr(cluster + '.v', 0)
            cluster = mc.rename(cluster, cluName)
            self.parentNodes(cluster, i)

        absFunc.lockHide(curve, 'all', freeze=1)

        return group
