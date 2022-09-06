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
import sys
#from PySide import QtGui, QtCore
from math import pow,sqrt

jtools = os.getenv("JENTOOLS")
sys.path.append(jtools)
print jtools


from jen.functions.Qt import QtCore, QtWidgets
from RigTool.core.loaduifile import loadUi_file, compile_ui, getMayaWindow

##--------------------------------------------------------------------------------------------
## EXTERNAL FILES // CFG + UI + Globals
##--------------------------------------------------------------------------------------------
app_folder_win = os.path.dirname(__file__)
ui_main = app_folder_win + "/" + "ui" + "/" + "main_ui.ui"
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
		self.mnuReset.triggered.connect(self.reloadUI)
		self.mnuClose.triggered.connect(self.closeApp)
		self.mnuNGTools.triggered.connect(self.ngTools)
		self.mnuSublime.triggered.connect(self.sublime)

		# Control Creator
		self.circleButton.clicked.connect(lambda: self.controlCreator(shapeControl='circle'))
		self.squareButton.clicked.connect(lambda: self.controlCreator(shapeControl='square'))
		self.cubeButton.clicked.connect(lambda: self.controlCreator(shapeControl='cube'))
		self.sphereButton.clicked.connect(lambda: self.controlCreator(shapeControl='sphere'))
		self.arrowButton.clicked.connect(lambda: self.controlCreator(shapeControl='arrow'))
		self.doubleArrowButton.clicked.connect(lambda: self.controlCreator(shapeControl='dArrow'))
		self.ballonButton.clicked.connect(lambda: self.controlCreator(shapeControl='ballon'))
		self.doubleBallonButton.clicked.connect(lambda: self.controlCreator(shapeControl='dSideBallon'))
		self.arrowCrossButton.clicked.connect(lambda: self.controlCreator(shapeControl='cross'))
		self.xButton.clicked.connect(lambda: self.controlCreator(shapeControl='equis'))
		self.semiSphereButton.clicked.connect(lambda: self.controlCreator(shapeControl='semiSphere'))
		self.pyramidButton.clicked.connect(lambda: self.controlCreator(shapeControl='pyramid'))
		self.curvedCrossButton.clicked.connect(lambda: self.controlCreator(shapeControl='curvedCross'))
		self.curvedDArrowButton.clicked.connect(lambda: self.controlCreator(shapeControl='curvedDArrow'))

		# Color Applying
		self.redColorButton.clicked.connect(lambda: self.colorApply(colorSelected='red'))
		self.greenLightColorButton.clicked.connect(lambda: self.colorApply(colorSelected='green'))
		self.yellowColorButton.clicked.connect(lambda: self.colorApply(colorSelected='yellow'))
		self.blueDarkColorButton.clicked.connect(lambda: self.colorApply(colorSelected='blue'))
		self.orangeColorButton.clicked.connect(lambda: self.colorApply(colorSelected='orange'))
		self.blackColorButton.clicked.connect(lambda: self.colorApply(colorSelected='black'))
		self.grayColorButton.clicked.connect(lambda: self.colorApply(colorSelected='gray'))
		self.pinkColorButton.clicked.connect(lambda: self.colorApply(colorSelected='pink'))
		self.blueLightColorButton.clicked.connect(lambda: self.colorApply(colorSelected='blueLight'))
		self.greenDarkColorButton.clicked.connect(lambda: self.colorApply(colorSelected='greenDark'))

		# Helpers
		self.ikHandleButton.clicked.connect(self.ikSelected)
		self.locatorButton.clicked.connect(self.createLocator)
		self.clusterButton.clicked.connect(self.cluster)

		# Usefull Tools
		self.alignButton.clicked.connect(self.align)
		self.localRotationAxesButton.clicked.connect(self.LRA)
		self.localGroupButton.clicked.connect(self.localGroup)
		self.getDistanceButton.clicked.connect(self.getDistance)

		# Copy Attr

		self.copyButton.clicked.connect(self.copyAttributes)

		# Constraints

		self.parentButton.clicked.connect((lambda: self.constraints(consType='parent')))
		self.pointButton.clicked.connect((lambda: self.constraints(consType='point')))
		self.orientConsButton.clicked.connect((lambda: self.constraints(consType='orient')))
		self.scaleButton.clicked.connect((lambda: self.constraints(consType='scale')))
		self.aimButton.clicked.connect((lambda: self.constraints(consType='aim')))
		self.pointOnPolyButton.clicked.connect((lambda: self.constraints(consType='pointOnPoly')))
		#ends.
		self.parentToEndButton.clicked.connect((lambda: self.constraints(consType='parToEnd')))
		self.pointToEndButton.clicked.connect((lambda: self.constraints(consType='pointToEnd')))
		self.orientToEndButton.clicked.connect((lambda: self.constraints(consType='orientToEnd')))
		self.scaleToEndButton.clicked.connect((lambda: self.constraints(consType='scaleToEnd')))
		# Joint Tools
		self.createJointButton.clicked.connect(self.createJoint)



	#Initialize UI
	def reloadUI(self):
		self.initVars()
		print "RigTool started, version: ", self._version


	def initVars(self):
		self._version = "0.1"
		self._appName = "Edu Rig Tool"


##--------------------------------------------------------------------------------------------
## UI FUNCTIONS MENU & BUTTONS
##--------------------------------------------------------------------------------------------    

	def closeApp(self):
		self.close()

	def ngTools(self):
		from ngSkinTools.ui.mainwindow import MainWindow
		MainWindow.open()

	def sublime(self):
		# Close ports if they were already open under another configuration
		try: mc.commandPort(name=":7001", close=True)
		except: mc.warning('Could not close port 7001 (maybe it is not opened yet...)')
		try: mc.commandPort(name=":7002", close=True)
		except: mc.warning('Could not close port 7002 (maybe it is not opened yet...)')

		# Open new ports
		mc.commandPort(name=":7001", sourceType="mel")
		mc.commandPort(name=":7002", sourceType="python")

##--------------------------------------------------------------------------------------------
## RIG TOOLS FUNCTIONS
##--------------------------------------------------------------------------------------------    
	# Control Creator
	def controlCreator(self, shapeControl):
		allControl = mc.ls('C_shape_*_CTRL')
		amount = len(allControl) + 1
		name = 'C_shape' + str(amount) + '_CTRL'		
		sel = mc.ls(sl=1)
		
		# List of controls
		
		square='curve -d 1 -p 1 0 1 -p 1 0 -1 -p -1 0 -1 -p -1 0 1 -p 1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
		cube='curve -d 1 -p 0.781349 0.781349 0.781349 -p 0.781349 0.781349 -0.781349 -p -0.781349 0.781349 -0.781349 -p -0.781349 -0.781349 -0.781349 -p 0.781349 -0.781349 -0.781349 -p 0.781349 -0.781349 0.781349 -p -0.781349 -0.781349 0.781349 -p -0.781349 0.781349 0.781349 -p 0.781349 0.781349 0.781349 -p 0.781349 -0.781349 0.781349 -p 0.781349 -0.781349 -0.781349 -p 0.781349 0.781349 -0.781349 -p -0.781349 0.781349 -0.781349 -p -0.781349 0.781349 0.781349 -p -0.781349 -0.781349 0.781349 -p -0.781349 -0.781349 -0.781349 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
		sphere='curve -d 1 -p 0 1 0 -p -0.5 0.866025 0 -p -0.866025 0.5 0 -p -1 0 0 -p -0.866025 -0.5 0 -p -0.5 -0.866025 0 -p 0 -1 0 -p 0.5 -0.866025 0 -p 0.866025 -0.5 0 -p 1 0 0 -p 0.866025 0.5 0 -p 0.5 0.866025 0 -p 0 1 0 -p 0 0.866025 -0.5 -p 0 0.5 -0.866025 -p 0 0 -1 -p 0 -0.5 -0.866025 -p 0 -0.866025 -0.5 -p 0 -1 0 -p 0 -0.866025 0.5 -p 0 -0.5 0.866025 -p 0 0 1 -p 0 0.5 0.866025 -p 0 0.866025 0.5 -p 0 1 0 -p 0 0.866025 -0.5 -p 0 0.5 -0.866025 -p 0 0 -1 -p 0.707107 0 -0.707107 -p 1 0 0 -p 0.707107 0 0.707107 -p 0 0 1 -p -0.707107 0 0.707107 -p -1 0 0 -p -0.707107 0 -0.707107 -p 0 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 ;'
		arrow='curve -d 1 -p -0.5 0 1 -p 0.5 0 1 -p 0.5 0 -0.5 -p 1 0 -0.5 -p 0 0 -1.5 -p -1 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
		doubleArrow='curve -d 1 -p -0.5 0 -1.5 -p -1 0 -1.5 -p 0 0 -2.5 -p 1 0 -1.5 -p 0.5 0 -1.5 -p 0.5 0 1.5 -p 1 0 1.5 -p 0 0 2.5 -p -1 0 1.5 -p -0.5 0 1.5 -p -0.5 0 -1.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 ;'
		ballon='curve -d 1 -p 0.866025 0 2.5 -p 0.866025 0 3.5 -p -1.49012e-007 0 4 -p -0.866026 0 3.5 -p 0.866025 0 2.5 -p 0 0 2 -p -0.866025 0 2.5 -p -0.866026 0 3.5 -p -1.49012e-007 0 4 -p 0.866025 0 3.5 -p -0.866025 0 2.5 -p 0 0 2 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;'
		doubleBallon='curve -d 1 -p 0.866025 0 3.5 -p 0.866025 0 2.5 -p 0 0 2 -p -0.866025 0 2.5 -p -0.866026 0 3.5 -p -1.49012e-007 0 4 -p 0.866025 0 3.5 -p -0.866025 0 2.5 -p 0 0 2 -p 0.866025 0 2.5 -p -0.866026 0 3.5 -p -0.866025 0 2.5 -p 0 0 2 -p -1.49012e-007 0 -2 -p 0.866025 0 -2.5 -p -0.866025 0 -3.5 -p 0 0 -4 -p 0.866025 0 -3.5 -p -0.866026 0 -2.5 -p -0.866025 0 -3.5 -p 0 0 -4 -p 0.866025 0 -3.5 -p 0.866025 0 -2.5 -p -1.49012e-007 0 -2 -p -0.866026 0 -2.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;'
		cross='curve -d 1 -p -0.5 0 -1.5 -p -1 0 -1.5 -p 0 0 -2.5 -p 1 0 -1.5 -p 0.5 0 -1.5 -p 0.5 0 -0.5 -p 1.5 0 -0.5 -p 1.5 0 -1 -p 2.5 0 0 -p 1.5 0 1 -p 1.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 1.5 -p 1 0 1.5 -p 0 0 2.5 -p -1 0 1.5 -p -0.5 0 1.5 -p -0.5 0 0.5 -p -1.5 0 0.5 -p -1.5 0 1 -p -2.5 0 0 -p -1.5 0 -1 -p -1.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 -1.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;'
		equis='curve -d 1 -p 0.555556 0 0 -p 1.666667 0 -1.111111 -p 1.666667 0 -1.666667 -p 1.111111 0 -1.666667 -p 0 0 -0.555556 -p -1.111111 0 -1.666667 -p -1.666667 0 -1.666667 -p -1.666667 0 -1.111111 -p -0.555556 0 0 -p -1.666667 0 1.111111 -p -1.666667 0 1.666667 -p -1.111111 0 1.666667 -p 0 0 0.555556 -p 1.111111 0 1.666667 -p 1.666667 0 1.666667 -p 1.666667 0 1.111111 -p 0.555556 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;'
		semiSphere='curve -d 1 -p 1 0 0 -p 0.866025 0.5 0 -p 0.5 0.866025 0 -p 0 1 0 -p -0.5 0.866025 0 -p -0.866025 0.5 0 -p -1 0 0 -p -0.707107 0 -0.707107 -p 0 0 -1 -p 0.707107 0 -0.707107 -p 1 0 0 -p 0.707107 0 0.707107 -p 0 0 1 -p 0 0.5 0.866025 -p 0 0.866025 0.5 -p 0 1 0 -p 0 0.866025 -0.5 -p 0 0.5 -0.866025 -p 0 0 -1 -p -0.707107 0 -0.707107 -p -1 0 0 -p -0.707107 0 0.707107 -p 0 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 ;'
		pyramid='curve -d 1 -p 0 0.709829 0 -p 0.707107 0.00272189 0 -p -3.09086e-008 0.00272189 0.707107 -p -0.707107 0.00272189 -6.18172e-008 -p 0 0.709829 0 -p -3.09086e-008 0.00272189 0.707107 -p -0.707107 0.00272189 -6.18172e-008 -p 9.27258e-008 0.00272189 -0.707107 -p 0.707107 0.00272189 0 -p 0 0.709829 0 -p 9.27258e-008 0.00272189 -0.707107 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 ;'
		curvedCross='curve -d 1 -p 0.495887 -0.0652843 -0.500166 -p 0.483123 -0.162234 -0.991772 -p 0.462093 -0.321973 -1.466408 -p 0.916278 -0.412316 -1.466408 -p 0.433156 -0.541769 -1.915956 -p 0 -0.79185 -2.332719 -p -0.433155 -0.541768 -1.915956 -p -0.916277 -0.412316 -1.466408 -p -0.462091 -0.321973 -1.466408 -p -0.483121 -0.162234 -0.991772 -p -0.495885 -0.0652841 -0.500166 -p -0.983286 -0.162234 -0.500166 -p -1.453863 -0.321973 -0.500166 -p -1.416442 -0.412316 -0.991772 -p -1.899563 -0.541768 -0.500166 -p -2.332722 -0.791845 1.01683e-005 -p -1.899566 -0.541764 0.500175 -p -1.416443 -0.412313 0.991781 -p -1.453865 -0.321969 0.500175 -p -0.983287 -0.162229 0.500175 -p -0.495886 -0.065279 0.500175 -p -0.483122 -0.16223 0.991781 -p -0.462092 -0.321971 1.466418 -p -0.916277 -0.412314 1.466418 -p -0.433155 -0.541767 1.915964 -p 0 -0.79185 2.332727 -p 0.433156 -0.541767 1.915964 -p 0.916278 -0.412314 1.466418 -p 0.462092 -0.321971 1.466418 -p 0.483123 -0.16223 0.991781 -p 0.495886 -0.0652791 0.500175 -p 0.983288 -0.162229 0.500175 -p 1.453865 -0.321969 0.500175 -p 1.416443 -0.412313 0.991781 -p 1.899566 -0.541764 0.500175 -p 2.332723 -0.791846 1.01683e-005 -p 1.899564 -0.541769 -0.500166 -p 1.416442 -0.412316 -0.991772 -p 1.453863 -0.321973 -0.500166 -p 0.983287 -0.162234 -0.500166 -p 0.495887 -0.0652843 -0.500166 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 ;'
		curvedDoubleArrow='curve -d 1 -p 0 -0.79185 -2.332719 -p -0.433155 -0.541768 -1.915956 -p -0.916277 -0.412316 -1.466408 -p -0.462091 -0.321973 -1.466408 -p -0.483121 -0.162234 -0.991772 -p -0.495885 -0.0652841 -0.500166 -p -0.500165 -0.0327758 1.01683e-005 -p -0.495886 -0.065279 0.500175 -p -0.483122 -0.16223 0.991781 -p -0.462092 -0.321971 1.466418 -p -0.916277 -0.412314 1.466418 -p -0.433155 -0.541767 1.915964 -p 0 -0.79185 2.332727 -p 0.433156 -0.541767 1.915964 -p 0.916278 -0.412314 1.466418 -p 0.462092 -0.321971 1.466418 -p 0.483123 -0.16223 0.991781 -p 0.495886 -0.0652791 0.500175 -p 0.500166 -0.0327759 1.01683e-005 -p 0.495887 -0.0652843 -0.500166 -p 0.483123 -0.162234 -0.991772 -p 0.462093 -0.321973 -1.466408 -p 0.916278 -0.412316 -1.466408 -p 0.433156 -0.541769 -1.915956 -p 0 -0.79185 -2.332719 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;'

		# Calling Controls

		if self.onSelectCheckBox.isChecked():
			if len(sel)>0:
				for x in sel:
					index=sel.index(x)
					node = mc.createNode('transform', n= x.replace('JNT', 'CTRL'))
					grp=mc.createNode('transform', n= node.replace('CTRL', 'ZTR'))
					mc.parent(node, grp)
					mc.delete(mc.parentConstraint(x, grp, mo=0))
					
					if shapeControl == 'circle':
						
						shape =  mc.circle(r=2, nr=(1, 0, 0))
						getShape = mc.listRelatives(shape, shapes=True)
						mc.select(getShape)
						mc.select(node, add=1)
						mel.eval('parent -r -s;')
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'square':
						shape = mel.eval( square)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape,x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'cube':
						shape = mel.eval( cube)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'sphere':
						shape = mel.eval( sphere)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'arrow':
						shape = mel.eval( arrow)
						mc.rotate( 0, '-90deg', 0, r=True )
						mc.makeIdentity(apply=True, r=1)                     
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                                       
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)                                        
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)		


					if shapeControl == 'dArrow':
						shape = mel.eval( doubleArrow)
						getShape = mc.listRelatives(shape, shapes=True)
						mc.select(getShape)
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'ballon':
						shape = mel.eval( ballon)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)								
							
							
					if shapeControl == 'dSideBallon':
						shape = mel.eval( doubleBallon)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'cross':
						shape = mel.eval( cross)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'equis':
						shape = mel.eval( equis)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'semiSphere':
						shape = mel.eval( semiSphere)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'pyramid':
						shape = mel.eval( pyramid)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if shapeControl == 'curvedCross':
						shape = mel.eval( curvedCross)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)


					if shapeControl == 'curvedDArrow':
						shape = mel.eval( curvedDoubleArrow)
						getShape = mc.listRelatives(shape, shapes=True)                   
						mc.select(getShape)                    
						mc.select(node, add=1)
						mel.eval('parent -r -s;')                    
						mc.rename(getShape, x.replace('JNT', 'CTRLShape'))
						mc.delete(shape)
						mc.select(cl=1)
						if len(sel)>1:
							mc.select(cl=1)
						else:
							mc.select(node)

					if self.constrainedCheckBox.isChecked():
						if mc.objectType(x) == 'joint': 							
							if index > 0:
								parent=mc.listRelatives(x, p=1)[0]							
								ctrlPar=parent.replace('_JNT','_CTRL')							
								mc.parent(grp, ctrlPar)
							mc.parentConstraint(node, x, mo=1)			
	
			else:
				mc.warning( "Nothing selected, please select a Joint or turn off 'On Select' checkBox." )


		elif not self.onSelectCheckBox.isChecked():
			if shapeControl == 'circle':
				mc.select(cl=1)
				mc.circle(n= name, r=2, nr=(1, 0, 0))

			if shapeControl == 'square':
				mc.select(cl=1)
				mel.eval(square) 
				mc.rename(name)


			if shapeControl == 'cube':
				mc.select(cl=1)
				mel.eval(cube) 
				mc.rename(name)

			if shapeControl == 'sphere':
				mc.select(cl=1)
				mel.eval(sphere) 
				mc.rename(name)

			if shapeControl == 'arrow':
				mc.select(cl=1)
				mel.eval(arrow) 
				mc.rename(name)
			
			if shapeControl == 'dArrow':
				mc.select(cl=1)
				mel.eval(doubleArrow) 
				mc.rename(name)
			
			if shapeControl == 'ballon':
				mc.select(cl=1)
				mel.eval(ballon) 
				mc.rename(name)
			
			if shapeControl == 'dSideBallon':
				mc.select(cl=1)
				mel.eval(doubleBallon) 
				mc.rename(name)
			
			if shapeControl == 'cross':
				mc.select(cl=1)
				mel.eval(cross) 
				mc.rename(name)
			
			if shapeControl == 'equis':
				mc.select(cl=1)
				mel.eval(equis) 
				mc.rename(name)
			
			if shapeControl == 'semiSphere':
				mc.select(cl=1)
				mel.eval(semiSphere) 
				mc.rename(name)
			
			if shapeControl == 'pyramid':
				mc.select(cl=1)
				mel.eval(pyramid) 
				mc.rename(name)
			
			if shapeControl == 'curvedCross':
				mc.select(cl=1)
				mel.eval(curvedCross) 
				mc.rename(name)
			
			if shapeControl == 'curvedDArrow':
				mc.select(cl=1)
				mel.eval(curvedDoubleArrow) 
				mc.rename(name)
			
	# Override Color Apply
	def colorApply(self, colorSelected):

		sel= mc.ls(sl=1)
		print sel
		print len(sel)
		if len(sel) > 0:
			for x in sel:
				if colorSelected == 'red':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 13)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 13)

				if colorSelected == 'green':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 14)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 14)

				if colorSelected == 'yellow':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 17)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 17)

				if colorSelected == 'blue':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 15)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 15)

				if colorSelected == 'orange':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 12)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 12)

				if colorSelected == 'black':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 1)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 1)

				if colorSelected == 'gray':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 2)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 2)

				if colorSelected == 'pink':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 9)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 9)

				if colorSelected == 'blueLight':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 18)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 18)

				if colorSelected == 'greenDark':
					if mc.getAttr(x+'Shape.overrideEnabled')==0:
						mc.setAttr(x + 'Shape.overrideEnabled', 1)
						mc.setAttr(x + 'Shape.overrideColor', 7)
					else:
						mc.setAttr(x + 'Shape.overrideColor', 7)
		else:
			mc.warning( "Nothing selected, please select a curve for colorize.")

	# Helpers

	def ikSelected(self):
		sel=mc.ls(sl=1)
		if len(sel)!=0:
			if mc.objectType(sel[0]) == 'joint':					
				handle=mc.ikHandle(sj=sel[0], ee=sel[1], sol='ikRPsolver', n=sel[1].replace('_JNT' ,'_ikHandle'))
			else:
				mc.warning('Objects are not Joints.')
		else:
			mc.warning('Nothing Selected.')

	def createLocator(self):
		sel=mc.ls(sl=1, fl=1)		
		if len(sel)==0:
			mc.spaceLocator(n='C_locator_01')
		else:
			for x in sel:
				pos=mc.xform(x, q=1, t=1, ws=1)
				ori=mc.xform(x, q=1, ro=1, ws=1)
				loc=mc.spaceLocator(n='C_locator_01')
				
				mc.xform(loc[0], t=pos, ws=1)
				mc.xform(loc[0], ro=ori, ws=1)

	def cluster(self):
		sel=mc.ls(sl=1)
		
		if len(sel)!=0:			
			mc.cluster()
		else:
			mc.warning('Nothing selected')


	# Usefull Tools
	def align(self):
		sel=mc.ls(sl=1)
		
		if self.positionCheckBox.isChecked():
			mc.delete(mc.pointConstraint(sel[1], sel[0], mo=0))
		
		if self.orientationCheckBox.isChecked():
			mc.delete(mc.orientConstraint(sel[1], sel[0], mo=0))	


	def LRA(self):
		mel.eval('ToggleLocalRotationAxes')


	def localGroup(self):
		sel=mc.ls(sl=1)

		for x in sel:
		    coord = mc.xform(x, q=1, t=1, ws=1)
		    orient= mc.xform(x, q=1, ro=1, ws=1)
		    grp=mc.createNode('transform',n= x+'_GRP')
		    mc.xform(grp, t=coord, ws=1)
		    mc.xform(grp, ro=orient, ws=1)
		    mc.parent(x, grp)

	def getDistance(self):
		sel=mc.ls(sl=1)		
		
		if len(sel)==2:
			gObjA = mc.xform(sel[0], q=True, t=True, ws=True)
			gObjB = mc.xform(sel[1], q=True, t=True, ws=True)
			distance = sqrt(pow(gObjA[0]-gObjB[0],2)+pow(gObjA[1]-gObjB[1],2)+pow(gObjA[2]-gObjB[2],2))
			print distance
			self.distanceText.setText(str(distance))
		else:
			mc.warning('2 objects are required')

	# Copy Attributes

	def copyAttributes(self):
		sel=mc.ls(sl=1)

		left= self.prefixLeftTextBox.text()
		rigth= self.prefixRigthTextBox.text()


		for x in sel:
			if self.allCheckBox.isChecked():
				transform=mc.listAttr(x,  k=1, s=1, v=1, u=1)

			elif not self.allCheckBox.isChecked():

				if self.userDefinedCheckBox.isChecked():
					transform=mc.listAttr(x,  k=1, ud=1)

				if self.transformCheckBox.isChecked():
					transform=mc.listAttr(x,  k=1, s=1, v=1, u=1, st=['translate*','rotate*', 'scale*'])
			
		if self.isMirrorCheckBox.isChecked():
			for x in sel:				
				for i in transform:
					value=mc.getAttr(x+'.'+i)

					if i.endswith('translateX') or i.endswith('rotateZ') or i.endswith('rotateY')==True:

						if x.startswith(left)==True:
							
							y=x.replace(left, rigth)
							mc.setAttr(y+'.'+i, value*-1)
						if x.startswith(rigth)==True:
							
							y=x.replace(rigth, left)
							mc.setAttr(y+'.'+i, value*-1)

					else:
						if x.startswith(left)==True:
							
							y=x.replace(left, rigth)
							mc.setAttr(y+'.'+i, value)
						if x.startswith(rigth)==True:
							
							y=x.replace(rigth, left)
							mc.setAttr(y+'.'+i, value)

		elif not self.isMirrorCheckBox.isChecked():
			for x in sel:
				transform=mc.listAttr(x,  k=1, s=1, v=1, u=1, st=['translate*','rotate*', 'scale*'])
				
				for i in transform:
					value=mc.getAttr(x+'.'+i)
					
					if x.startswith(left)==True:
						
						y=x.replace(left, rigth)
						mc.setAttr(y+'.'+i, value)
					if x.startswith(rigth)==True:
						
						y=x.replace(rigth, left)
						mc.setAttr(y+'.'+i, value)	



		

		elif not self.onSelectCheckBox.isChecked():
			pass
	

	#Constraints			
	
	def constraints(self, consType):
		sel=mc.ls(sl=1)
		obj1=sel[0]
		obj2=sel[1]
		

		obj=[]

		if consType=='parent':
			if self.motionOffsetCheckBox.isChecked():
				mc.parentConstraint( mo=1)

			elif not self.motionOffsetCheckBox.isChecked():
				mc.parentConstraint( mo=0)

		if consType=='point':
			if self.motionOffsetCheckBox.isChecked():
				mc.pointConstraint( mo=1)

			elif not self.motionOffsetCheckBox.isChecked():
				mc.pointConstraint( mo=0)

		if consType=='orient':
			if self.motionOffsetCheckBox.isChecked():
				mc.orientConstraint( mo=1)

			elif not self.motionOffsetCheckBox.isChecked():
				mc.orientConstraint(obj1, obj2, mo=0)

		if consType=='scale':
			if self.motionOffsetCheckBox.isChecked():
				mc.scaleConstraint(obj1, obj2, mo=1)

			elif not self.motionOffsetCheckBox.isChecked():
				mc.scaleConstraint(obj1, obj2, mo=0)

		if consType=='aim':
			if self.motionOffsetCheckBox.isChecked():
				mc.aimConstraint(obj1, obj2, mo=1)

			elif not self.motionOffsetCheckBox.isChecked():
				mc.aimConstraint(obj1, obj2, mo=0)

		if consType=='pointOnPoly':
			if self.motionOffsetCheckBox.isChecked():
				mel.eval('doCreatePointOnPolyConstraintArgList 2 {   "0" ,"0" ,"0" ,"1" ,"" ,"1" ,"0" ,"0" ,"0" ,"0" };')

			elif not self.motionOffsetCheckBox.isChecked():
				mel.eval('doCreatePointOnPolyConstraintArgList 2 {   "0" ,"0" ,"0" ,"1" ,"" ,"1" ,"0" ,"0" ,"0" ,"0" };')


		if consType=='parToEnd':
			if self.motionOffsetCheckBox.isChecked():
				for x in sel:
					if x == sel[-1]:
						pass
					else:
						obj.append(x)

				for x in obj:
					mc.parentConstraint(sel[-1], x, mo=1)


			elif not self.motionOffsetCheckBox.isChecked():
				for x in sel:
					if x == sel[-1]:
						pass
					else:
						obj.append(x)

				for x in obj:
					mc.parentConstraint(sel[-1], x, mo=0)

		if consType=='pointToEnd':
			if self.motionOffsetCheckBox.isChecked():
				for x in sel:
					if x == sel[-1]:
						pass
					else:
						obj.append(x)

				for x in obj:
					mc.pointConstraint(sel[-1], x, mo=1)


			elif not self.motionOffsetCheckBox.isChecked():
				for x in sel:
					if x == sel[-1]:
						pass
					else:
						obj.append(x)

				for x in obj:
					mc.pointConstraint(sel[-1], x, mo=0)

		if consType=='orientToEnd':
			if self.motionOffsetCheckBox.isChecked():
				for x in sel:
					if x == sel[-1]:
						pass
					else:
						obj.append(x)

				for x in obj:
					mc.orientConstraint(sel[-1], x, mo=1)


			elif not self.motionOffsetCheckBox.isChecked():
				for x in sel:
					if x == sel[-1]:
						pass
					else:
						obj.append(x)

				for x in obj:
					mc.orientConstraint(sel[-1], x, mo=0)

		if consType=='scaleToEnd':
			if self.motionOffsetCheckBox.isChecked():
				for x in sel:
					if x == sel[-1]:
						pass
					else:
						obj.append(x)

				for x in obj:
					mc.scaleConstraint(sel[-1], x, mo=1)


			elif not self.motionOffsetCheckBox.isChecked():
				for x in sel:
					if x == sel[-1]:
						pass
					else:
						obj.append(x)

				for x in obj:
					mc.scaleConstraint(sel[-1], x, mo=0)


	# Joint Tools
	def createJoint(self):
		mel.eval('JointTool;')

##--------------------------------------------------------------------------------------------
## MAIN
##-------------------------------------------------------------------------------------------- 

def runApp():
	for qt in QtWidgets.QApplication.topLevelWidgets():
		try:
			qtname = qt.objectName()
			if qtname == "RigTools_Window":
				print "found qtmainwindow of script instance match, destroy it"
				qt.close()
		except:
			pass
	app = ProgramUI()
	app.show()

runApp()