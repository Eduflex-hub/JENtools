# -*- coding: utf-8 -*-
import PySide2.QtWidgets as wdg
from PySide2 import QtCore as core
import os
import sys
jtools = os.getenv("JENTOOLS")
sys.path.append(jtools)
from jenAutoRig.core.loaduifile import loadUi_file, compile_ui, getMayaWindow
from jen.functions.Qt import QtCore as core
from jen.functions.Qt import QtWidgets as wdg


#####################################################
# EXTERNAL FILES // CFG + UI + Globals
#####################################################

app_folder_win = os.path.dirname(__file__)
ui_main = app_folder_win + "/" + "jenAutorig_v2_UserInterface.ui"
form, base = loadUi_file(ui_main)


class jenUI(base, form):
    def __init__(self, parent=getMayaWindow()):
        super(jenUI, self).__init__(parent)
        self.setAttribute(core.Qt.WA_DeleteOnClose, True)
        # startup FUNCTIONS
        self.setupUi(self)
        self.setConnections()
        self.reloadUI()

    # INITIALIZE UI
    def reloadUI(self):
        self.initVars(self)
        print '-' * 60
        print '-' * 60
        print "Starting", self._appName, "version:", self._version
        print "Author:", self._author
        print '-' * 60
        print '-' * 60

    def initVars(self, item):
        self._version = "2.0"
        self._appName = "JEN AUTORIG"
        self._author = "Eduflex - Copyright 2016-2020 All Rights Reserved"

    def setConnections(self):

        self.mnu_Close.triggered.connect(self.closeApp)

        self.pushButton_LimbAdd.clicked.connect(self.addLimbBox)

    def closeApp(self):
        self.close()

    def addLimbBox(self):
        limbBox = wdg.QGroupBox("Limbs_01")
        self.verticalLayout_Limbs.addWidget(limbBox)
        self.verticalLayout_Limbs.setAlignment(core.Qt.AlignTop)

        limbBoxLyt = wdg.QFormLayout(limbBox)
        limbBoxLyt.setContentsMargins(5, 5, 5, 5)
        limbBox.setFixedSize(580, 100)

        testBtn = wdg.QPushButton("boton pe")
        testBtn.setFixedSize(60, 30)
        limbBoxLyt.addWidget(testBtn)

def runApp():
    for qt in wdg.QApplication.topLevelWidgets():
        try:
            qtname = qt.objectName()
            if qtname == "jenAutorig_v2_MainWindow":
                print "found qtmainwindow of script instance match, closing..."
                qt.close()
        except:
            pass
    app = jenUI()
    app.show()


runApp()
