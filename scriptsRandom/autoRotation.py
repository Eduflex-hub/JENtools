import pymel.core as pm
import maya.cmds as mc
import maya.mel as mel
import os

class Wagon(object):
    def __init__(self):
        # Main Wagon:
        assetNameSpace = "SNOWPIERCER_3RD_CLASS_TAIL_mdl_0:"
        self.animMesh = assetNameSpace + 'anim_nxnull'
        self.renderMesh = assetNameSpace + 'render_nxnull'
        # Bogey:
        self.wheelVertexAlignmentDict = {
            'axel_drive_3_cn_geo': {
                'wheel_0': '.vtx[36418:36457]',
                'wheel_1': '.vtx[60192:60231]',
                'wheel_2': '.vtx[83966:84005]',
                'wheel_3': '.vtx[12644:12683]'
            },
            'axel_drive_0_cn_geo': {
                'wheel_0': '.vtx[12644:12683]',
                'wheel_1': '.vtx[36418:36457]',
                'wheel_2': '.vtx[83966:84005]',
                'wheel_3': '.vtx[60192:60231]'
            }
        }
        self.alignWheel()
    def gettingObject(self, type):
        # Reading Bogeys
        allBogeys = []
        allWheels = []
        allCarriages = []
        for bogey in range(0, 2):
            index = range(0, 2).index(bogey)
            nameSpace = "SNOWPIERCER_BOGEY_mdl_{}:".format(str(index))
            allBogeys.append(nameSpace)
        # Reading Wheels
        for wheel in range(0, 16):
            index = range(0, 16).index(wheel)
            nameSpace = "SNOWPIERCER_ALL_CLASS_WHEEL_mdl_{}:".format(str(index))
            allWheels.append(nameSpace)
        # Reading underCarriage
        nameSpace = "SNOWPIERCER_3RD_CLASS_UNDER_CARRIAGE_mdl_0:"
        allCarriages.append(nameSpace)
        if type is 'bogey':
            return allBogeys
        if type is 'wheel':
            return allWheels
        if type is 'underCarriage':
            return allCarriages
    def alignWheel(self):
        allBogeys = self.gettingObject(type='bogey')
        allWheels = self.gettingObject(type='wheel')
        allCarriages = self.gettingObject(type='underCarriage')
        mc.parentConstraint('Body_Ctrl', self.animMesh, mo=1)
        mc.parentConstraint('Body_Ctrl', self.renderMesh, mo=1)
        mc.scaleConstraint('All_Ctrl', self.animMesh)
        mc.scaleConstraint('All_Ctrl', self.renderMesh)
        mc.addAttr('All_Ctrl', ln='underCarriageVis', at='long', min=0, max=1, dv=1, k=1)
        mc.addAttr('All_Ctrl', ln='bogeyGackVis', at='long', min=0, max=1, dv=1, k=1)
        allAutoRotate = []
        for bogeyNameSpace in allBogeys:
            bogeyIndex = allBogeys.index(bogeyNameSpace)
            mc.connectAttr('All_Ctrl.bogeyGackVis', bogeyNameSpace + 'gack.v')
            if bogeyIndex < 1:
                l_axelMesh = bogeyNameSpace + self.wheelVertexAlignmentDict.keys()[1]
                r_axelMesh = bogeyNameSpace + self.wheelVertexAlignmentDict.keys()[0]
                bogeyLoc = mc.spaceLocator(n='bogeyBack' + str(bogeyIndex) + '_loc')
                # mc.setAttr(bogeyLoc[0] + '.v', 0)
                mc.parent(bogeyLoc, 'Body_Ctrl')
                mc.parentConstraint(bogeyLoc, bogeyNameSpace + 'render_nxnull')
                for wheelNameSpace in allWheels:
                    wheelIndex = allWheels.index(wheelNameSpace)
                    wheelMesh = wheelNameSpace + 'render_nxnull'
                    if wheelIndex < 8:
                        if wheelIndex < 4:
                            vertex = self.wheelVertexAlignmentDict[l_axelMesh.split(':')[1]][
                                'wheel_{}'.format(wheelIndex)]
                            vertexSelection = l_axelMesh + vertex
                            # Aligning wheel Mesh to correct place on Bogey:
                            mc.select(vertexSelection)
                            clu = mc.cluster()
                            mc.delete(mc.pointConstraint(clu, wheelMesh, mo=0))
                            mc.delete(clu)
                            txValue = mc.getAttr(wheelMesh + '.tx')
                            mc.setAttr(wheelMesh + '.tx', txValue - 43.281)
                            # Creating Controls for wheels:
                            driver = self.createControl(wheelNameSpace, 'L_WheelBack')
                            group = driver[0]
                            control = driver[1]
                            allAutoRotate.append(driver[2])
                            mc.delete(mc.pointConstraint(wheelMesh, group, mo=0))
                            mc.parentConstraint(control, wheelMesh, mo=1)
                            mc.parent(group, bogeyLoc)
                        if wheelIndex > 3:
                            vertex = self.wheelVertexAlignmentDict[r_axelMesh.split(':')[1]][
                                'wheel_{}'.format(wheelIndex - 4)]
                            vertexSelection = r_axelMesh + vertex
                            # Aligning wheel Mesh to correct place on Bogey:
                            mc.select(vertexSelection)
                            clu = mc.cluster()
                            mc.delete(mc.pointConstraint(clu, wheelMesh, mo=0))
                            mc.delete(clu)
                            mc.setAttr(wheelMesh + '.rotateY', 180)
                            txValue = mc.getAttr(wheelMesh + '.tx')
                            mc.setAttr(wheelMesh + '.tx', txValue + 43.281)
                            # Creating Controls for wheels:
                            driver = self.createControl(wheelNameSpace, 'R_WheelBack')
                            group = driver[0]
                            control = driver[1]
                            allAutoRotate.append(driver[2])
                            mc.delete(mc.pointConstraint(wheelMesh, group, mo=0))
                            mc.parentConstraint(control, wheelMesh, mo=1)
                            mc.parent(group, bogeyLoc)
            if bogeyIndex > 0:
                l_axelMesh = bogeyNameSpace + self.wheelVertexAlignmentDict.keys()[1]
                r_axelMesh = bogeyNameSpace + self.wheelVertexAlignmentDict.keys()[0]
                bogeyLoc = mc.spaceLocator(n='bogeyFront' + str(bogeyIndex) + '_loc')
                # mc.setAttr(bogeyLoc[0] + '.v', 0)
                mc.parent(bogeyLoc, 'Body_Ctrl')
                mc.parentConstraint(bogeyLoc, bogeyNameSpace + 'render_nxnull')
                for wheelNameSpace in allWheels:
                    wheelIndex = allWheels.index(wheelNameSpace)
                    wheelMesh = wheelNameSpace + 'render_nxnull'
                    if wheelIndex > 7:
                        if wheelIndex < 12:
                            vertex = self.wheelVertexAlignmentDict[l_axelMesh.split(':')[1]][
                                'wheel_{}'.format(wheelIndex - 8)]
                            vertexSelection = l_axelMesh + vertex
                            # Aligning wheel Mesh to correct place on Bogey:
                            mc.select(vertexSelection)
                            clu = mc.cluster()
                            mc.delete(mc.pointConstraint(clu, wheelMesh, mo=0))
                            mc.delete(clu)
                            txValue = mc.getAttr(wheelMesh + '.tx')
                            mc.setAttr(wheelMesh + '.tx', txValue - 43.281)
                            # Creating Controls for wheels:
                            driver = self.createControl(wheelNameSpace, 'L_WheelFront')
                            group = driver[0]
                            control = driver[1]
                            allAutoRotate.append(driver[2])
                            mc.delete(mc.pointConstraint(wheelMesh, group, mo=0))
                            mc.parentConstraint(control, wheelMesh, mo=1)
                            mc.parent(group, bogeyLoc)
                        if wheelIndex > 11:
                            vertex = self.wheelVertexAlignmentDict[r_axelMesh.split(':')[1]][
                                'wheel_{}'.format(wheelIndex - 12)]
                            vertexSelection = r_axelMesh + vertex
                            # Aligning wheel Mesh to correct place on Bogey:
                            mc.select(vertexSelection)
                            clu = mc.cluster()
                            mc.delete(mc.pointConstraint(clu, wheelMesh, mo=0))
                            mc.delete(clu)
                            mc.setAttr(wheelMesh + '.rotateY', 180)
                            txValue = mc.getAttr(wheelMesh + '.tx')
                            mc.setAttr(wheelMesh + '.tx', txValue + 43.281)
                            # Creating Controls for wheels:
                            driver = self.createControl(wheelNameSpace, 'R_WheelFront')
                            group = driver[0]
                            control = driver[1]
                            allAutoRotate.append(driver[2])
                            mc.delete(mc.pointConstraint(wheelMesh, group, mo=0))
                            mc.parentConstraint(control, wheelMesh, mo=1)
                            mc.parent(group, bogeyLoc)
        # setting autoRotation:
        wheelControls = []
        for x in allAutoRotate:
            control = mc.listRelatives(x, c=1)[0]
            wheelControls.append(control)
        self.autoRotateWheels(wheelControls, 'Body_Ctrl', 'All_Ctrl')
        # Creating Export Nodes:
        for eachNameSpace in allWheels:
            node = eachNameSpace + 'SNOWPIERCER_ALL_CLASS_WHEEL_rcnull'
            self.createExportNode(rcnull=node)
            mc.parent(node, 'geo')
            mc.scaleConstraint('All_Ctrl', node)
        for eachNameSpace in allBogeys:
            node = eachNameSpace + 'SNOWPIERCER_BOGEY_rcnull'
            self.createExportNode(rcnull=node)
            mc.parent(node, 'geo')
            mc.scaleConstraint('All_Ctrl', node)
        for eachNameSpace in allCarriages:
            node = eachNameSpace + 'SNOWPIERCER_3RD_CLASS_UNDER_CARRIAGE_rcnull'
            self.createExportNode(rcnull=node)
            mc.parent(node, 'geo')
            mc.scaleConstraint('All_Ctrl', node)
            nxNode = eachNameSpace + 'render_nxnull'
            carriageLoc = mc.spaceLocator(n='underCarriage' + '_loc')
            mc.parent(carriageLoc, 'Body_Ctrl')
            mc.parentConstraint(carriageLoc, nxNode)
            mc.connectAttr('All_Ctrl.underCarriageVis', node + '.v')

    def createControl(self, nameSpace, name):
        wheelCurve = 'curve -d 1 -p -92.855164 116.512421 116.512421 -p 92.855164 116.512421 116.512421 -p 92.855164 116.512421 -116.512421 -p -92.855164 116.512421 -116.512421 -p -92.855164 116.512421 116.512421 -p -92.855164 -116.512421 116.512421 -p 92.855164 -116.512421 116.512421 -p 92.855164 116.512421 116.512421 -p 92.855164 116.512421 -116.512421 -p 92.855164 -116.512421 -116.512421 -p 92.855164 -116.512421 116.512421 -p -92.855164 -116.512421 116.512421 -p -92.855164 -116.512421 -116.512421 -p 92.855164 -116.512421 -116.512421 -p 92.855164 116.512421 -116.512421 -p -92.855164 116.512421 -116.512421 -p -92.855164 -116.512421 -116.512421 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;'
        number = nameSpace.split('_')[-1]
        number = number.split(':')[0]
        grp = mc.createNode('transform', name=name + number + '_grp')
        autoGrp = mc.createNode('transform', name=name + number + '_autoRotationGrp', p=grp)
        control = mel.eval(wheelCurve)
        control = mc.rename(control, name + number + '_ctrl')
        mc.parent(control, autoGrp)
        return grp, control, autoGrp
    def autoRotateWheels(self, vals, driver, static):
        # original by Bade / extracted from mrx GitLab / modified for this purpose
        '''
        Create 4 cylinders to match the circumference and position of the car tires
        Select the cylinders and run the script
        2 groups will be created - dynamic locs and static locs
        Parent the dynamic locs group under the ctrl you want to drive the auto wheel rotation eg. Body ctrl or Cog Ctrl
        Parent the static locs under the All_Ctrl
        '''
        cyl_list = vals
        static_locs = []
        dynamic_locs = []
        for cyl in cyl_list:
            cylBB = pm.PyNode(cyl)
            diameter = cylBB.boundingBox().height()
            cen = cylBB.boundingBox().center()
            cyl = mc.listRelatives(cyl, p=1)[0]
            loc_names = ['Driver', 'Null', 'MoveDriver', 'MoveNull', 'OrientDriver', 'OrientNull']
            loc_objs = []
            for index, name in enumerate(loc_names):
                loc = pm.spaceLocator(n=cyl.replace('_Ctrl', loc_names[index]) + '_Loc')
                pm.move(loc, cen)
                loc_objs.append(loc)
            main_locs = []
            main_locs.extend([loc_objs[0], loc_objs[5]])
            for index, loc in enumerate(main_locs):
                loc.addAttr('offset', at='double', dv=0)
                loc.offset.set(e=True, k=True)
            for index, obj in enumerate(loc_objs):
                if index % 2 != 0:
                    pm.parent(loc_objs[index], loc_objs[index - 1])
                    static_locs.append(loc_objs[index - 1])
            main_locs[0].addAttr('autoRotation', at='long', min=0, max=1)
            main_locs[0].autoRotation.set(e=True, k=True)
            orient_constraints = {loc_objs[0]: loc_objs[2], loc_objs[2]: loc_objs[4]}
            point_constraints = {loc_objs[0]: loc_objs[2], loc_objs[3]: loc_objs[5]}
            for key, value in orient_constraints.items():
                pm.orientConstraint(key, value, mo=True)
            for key, value in point_constraints.items():
                pm.pointConstraint(key, value, mo=True)
                newExpression = '''
                    if (''' + loc_objs[0] + '''.autoRotation == 1)
                    {
                        $diff = ''' + loc_objs[5] + '''.translateZ - ''' + loc_objs[0] + '''.offset -''' + loc_objs[5] + '''.offset;
                        ''' + loc_objs[5] + '''.rotateX -= $diff * -360 / (1*3.14);
                        ''' + loc_objs[5] + '''.offset = ''' + loc_objs[5] + '''.translateZ;
                    };
                    if (''' + loc_objs[0] + '''.autoRotation == 0)
                    {
                        ''' + loc_objs[5] + '''.rotateX = 0;
                        ''' + loc_objs[5] + '''.offset = 0;
                    };'''
            pm.expression(name=cyl + 'AutoRotate', s=newExpression)
            div_name = cyl.replace('_Ctrl', "Diameter_MD")  # giving the nodes a name to make tracking diameter easier
            div = pm.createNode('multiplyDivide', n=div_name)
            div.input2X.set(diameter)
            div.operation.set(2)
            loc_objs[5].rx >> div.input1X
            div.outputX >> loc_objs[1].rx
            pm.orientConstraint(loc_objs[1], cyl, mo=True)
            loc_objs[0].autoRotation.set(1)
            pm.select(loc_objs[0])
            dynamic_locs.append(loc_objs[0])
        static_locs_grp = pm.group(static_locs, name="AutoWheelsLocsStatic_Grp", p=static)
        dynamic_locs_grp = pm.group(dynamic_locs, name="AutoWheelsLocsDynamic_Grp", p=driver)
        # dynamic_locs_grp.setParent(world=True)
    def createExportNode(self, rcnull=None):
        # / extracted from mrx GitLab
        if not rcnull:
            pm.createNode('mayaExportNode')
            return
        try:
            rcnull_node = pm.PyNode(rcnull)
        except:
            pm.warning('Could not cast {0} as PyNode. Aborting'.format(rcnull))
            return
        if not (rcnull_node.getShape().type() == 'rigCenterNode' or rcnull_node.type() == 'rigCenterNode'):
            pm.warning('Node is not an rcnull. Aborting')
            return
        if not rcnull_node.type() == 'rigCenterNode':
            rcnull_node = rcnull_node.getShape()
        export_node = pm.createNode('mayaExportNode', name=rcnull_node.assetString.get() + '_ExportNodeShape')
        export_node.assetString.set(rcnull_node.assetString.get())
        low = False
        high = False
        for nxnull in pm.ls(type='nexNullNode'):
            if nxnull.lodName == 1:
                high = True
            if nxnull.lodName == 3:
                low = True
        if low and high:
            export_node.assetType.set('hero')
        else:
            export_node.assetType.set('export')
        export_node.assetShot.set(os.environ['SHOT'])
        if pm.objExists('All_Ctrl'):
            all_ctrl = pm.PyNode('All_Ctrl')
            all_ctrl.message >> export_node.rigTopNode
            all_ctrl.scaleX >> export_node.attributes[0]
            all_ctrl.scaleY >> export_node.attributes[1]
            all_ctrl.scaleZ >> export_node.attributes[2]
        rcnull_node.message >> export_node.rigCenter
        if pm.objExists('extras'):
            export_node.getParent().setParent('extras')