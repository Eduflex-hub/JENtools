# -*- coding: utf-8 -*-
########################################
# IMPORTS
########################################
import sys
import os
import json
import maya.cmds as mc
########################################
# WRAPING PySide and PySide2
########################################
jtools = os.getenv("JENTOOLS")
sys.path.append(jtools)
from jen.functions.Qt import QtCore as core
from jen.functions.Qt import QtWidgets as wdg
########################################
import jen.ui.QtFunctions as QtF
reload(QtF)


mainWindow = None
__version__ = "2.0"


class jenUI(wdg.QMainWindow):
    def __init__(self):
        super(jenUI, self).__init__()

        self.setWindowTitle("JEN AUTORIG v{}".format(__version__))
        self.resize(680, 400)
        self.createUI()
        self.setConnections()

    def setConnections(self):
        
        self.pushButton_addLimbBox.clicked.connect(self.customGroupBox)

    def createUI(self):

        ########################################
        # MAIN WIDGET
        ########################################
        centralWidget = QtF.QtContainerWidget(self, Central=True)
        mainLayout = QtF.QtLayout(Parent=centralWidget, V=True)
        self.mainTabWdg = QtF.QtTabWidget(self, Parent=mainLayout)

        ########################################
        # MODULES TAB
        ########################################
        self.modulesWdg = QtF.QtContainerWidget(self, Parent=self.mainTabWdg, ParentType="tab", NameTab="Modules")
        modulesLyt = QtF.QtLayout(Parent=self.modulesWdg, V=True)
        self.moduleTabWdg = QtF.QtTabWidget(self, Parent=modulesLyt)

        # HIP TAB ##############################
        hipWdg = QtF.QtContainerWidget(self, Parent=self.moduleTabWdg, ParentType="tab", NameTab="Hip")
        hipLyt = QtF.QtLayout(Parent=hipWdg, H=True, M1=5, M2=5, M3=5, M4=5)
        QtF.QtScrollArea(Parent=hipLyt, V=True, R=True)

        # SPINE TAB ##############################
        spineWdg = QtF.QtContainerWidget(self, Parent=self.moduleTabWdg, ParentType="tab", NameTab="Spine")
        spineLyt = QtF.QtLayout(Parent=spineWdg, H=True, M1=5, M2=5, M3=5, M4=5)
        QtF.QtScrollArea(Parent=spineLyt, V=True, R=True)

        # CONNECTOR TAB ##############################
        connectorWdg = QtF.QtContainerWidget(self, Parent=self.moduleTabWdg, ParentType="tab", NameTab="Connector")
        connectorLyt = QtF.QtLayout(Parent=connectorWdg, H=True, M1=5, M2=5, M3=5, M4=5)
        QtF.QtScrollArea(Parent=connectorLyt, V=True, R=True)

        # LIMBS TAB ##############################
        limbsWdg = QtF.QtContainerWidget(self, Parent=self.moduleTabWdg, ParentType="tab", NameTab="Limbs")
        limbsLyt = QtF.QtLayout(Parent=limbsWdg, H=True, Align="Top", M1=5, M2=5, M3=5, M4=5)
        limbScroll = QtF.QtScrollArea(Parent=limbsLyt, V=True, R=True)

        limbScrollWdg = QtF.QtContainerWidget(self, Parent=limbScroll, ParentType="widget")
        self.LimbScrollLyt = QtF.QtLayout(Parent=limbScrollWdg, H=True, Align="Top", M1=5, M2=5, M3=5, M4=5)

        addButtonsLyt = QtF.QtLayout(Parent=limbsLyt, ParentType="Layout", V=True, Align="Top")

        self.pushButton_addLimbBox = QtF.QtPushButton(Parent=addButtonsLyt, Name="+")
        self.pushButton_removeLimbBox = QtF.QtPushButton(Parent=addButtonsLyt, Name="-")

        # FINGERS TAB ##############################
        fingersWdg = QtF.QtContainerWidget(self, Parent=self.moduleTabWdg, ParentType="tab", NameTab="Fingers")
        fingersLyt = QtF.QtLayout(Parent=fingersWdg, H=True, M1=5, M2=5, M3=5, M4=5)
        QtF.QtScrollArea(Parent=fingersLyt, V=True, R=True)

        # FEET TAB ##############################
        feetWdg = QtF.QtContainerWidget(self, Parent=self.moduleTabWdg, ParentType="tab", NameTab="Feet")
        feetLyt = QtF.QtLayout(Parent=feetWdg, H=True, M1=5, M2=5, M3=5, M4=5)
        QtF.QtScrollArea(Parent=feetLyt, V=True, R=True)

        # HEAD TAB ##############################
        headWdg = QtF.QtContainerWidget(self, Parent=self.moduleTabWdg, ParentType="tab", NameTab="Head")
        headLyt = QtF.QtLayout(Parent=headWdg, H=True, M1=5, M2=5, M3=5, M4=5)
        QtF.QtScrollArea(Parent=headLyt, V=True, R=True)

        # FACE TAB ##############################
        faceWdg = QtF.QtContainerWidget(self, Parent=self.moduleTabWdg, ParentType="tab", NameTab="Face")
        faceLyt = QtF.QtLayout(Parent=faceWdg, H=True, M1=5, M2=5, M3=5, M4=5)
        QtF.QtScrollArea(Parent=faceLyt, V=True, R=True)

        ########################################
        # MESHES TAB
        ########################################
        meshesWdg = wdg.QWidget()
        self.mainTabWdg.addTab(meshesWdg, "Meshes")

        meshesTab = wdg.QScrollArea()
        meshesTab.setWidgetResizable(True)
        meshesTab.setVerticalScrollBarPolicy(core.Qt.ScrollBarAlwaysOn)
        meshesTab.setHorizontalScrollBarPolicy(core.Qt.ScrollBarAlwaysOff)

        '''

        meshesTabContents = wdg.QWidget()
        meshesTab.setWidget(meshesTabContents)

        self.tabWdg.addTab(meshesTab, "Meshes")



        '''

    def customGroupBox(self):
        QtF.addCustomGroupBox(Layout=self.LimbScrollLyt, _Name="Limb_01")


def run():
    global mainWindow
    if not mainWindow or not mc.window(mainWindow, q=True, exists=True):
        mainWindow = jenUI()

    mainWindow.show()


if __name__ == '__main__':
    run()
