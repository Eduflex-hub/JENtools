import os
import sys
jtools = os.getenv("JENTOOLS")
sys.path.append(jtools)
from functions.Qt import QtCore, QtWidgets
from functions.Qt import __binding__

if __binding__ in ('PySide2', 'pyQt5'):
	import pyside2uic
	import shiboken2

elif __binding__ in ('PySide', 'pyQt4'):
	import pysideuic
	import shiboken
else:
	print ('No Qt binding available')

import maya.OpenMayaUI
import xml.etree.ElementTree as xml
from cStringIO import StringIO

 
##--------------------------------------------------------------------------------------------
##Gets the main Maya Window
##--------------------------------------------------------------------------------------------
 
def getMayaWindow():
	maya_window_util = maya.OpenMayaUI.MQtUtil.mainWindow()
	if maya_window_util is not None:

		if __binding__ in ('PySide2', 'pyQt5'):
			return shiboken2.wrapInstance(long( maya_window_util ), QtWidgets.QWidget)

		elif __binding__ in ('PySide', 'pyQt4'):
			return shiboken.wrapInstance(long( maya_window_util ), QtWidgets.QWidget)
		
##--------------------------------------------------------------------------------------------
## Load UI qtdesigner file
##--------------------------------------------------------------------------------------------
 
def loadUi_file(uiFile):
		parsed = xml.parse(uiFile)
		widget_class = parsed.find('widget').get('class')
		form_class = parsed.find('class').text
 
		with open(uiFile, 'r') as f:
			o = StringIO()
			frame = {}
			if __binding__ in ('PySide', 'pyQt4'):
				pysideuic.compileUi(f, o, indent=0)
			elif __binding__ in ('PySide2', 'pyQt5'):
				pyside2uic.compileUi(f, o, indent=0) 

			
			pyc = compile(o.getvalue(), '<string>', 'exec')
			exec pyc in frame
			 
			#Fetch the base_class and form class based on their type in the xml from designer
			form_class = frame['Ui_%s'%form_class]
			base_class = eval('QtWidgets.%s'%widget_class)
 
		return form_class, base_class
 
##--------------------------------------------------------------------------------------------
## Compile UI qtdesigner file using maya 
##--------------------------------------------------------------------------------------------
 
def compile_ui(uiFile):
		uic = uiFile + ".py"
		pyfile = open(uic, 'w')

		if __binding__ in ('PySide', 'pyQt4'):
			pysideuic.compileUi(uiFile, pyfile, False, 4,False)
		elif __binding__ in ('PySide2', 'pyQt5'):
			pyside2uic.compileUi(uiFile, pyfile, False, 4,False)
		
		pyfile.close()
 
 
#========================================================================
#---->  Nathan Horne's wrapinstance  
#========================================================================
 
def wrapinstance( ptr, base = None ):
	if ptr is None:
		return None
		
	ptr = long( ptr ) #Ensure type
	if __binding__ in ('PySide', 'pyQt4'):
		if globals().has_key( 'shiboken' ):
			if base is None:
				qObj = shiboken.wrapInstance( long( ptr ), QtCore.QObject )
				metaObj = qObj.metaObject()
				cls = metaObj.className()
				superCls = metaObj.superClass().className()
				if hasattr( QtWidgets, cls ):
					base = getattr( QtWidgets, cls )
						 
				elif hasattr( QtWidgets, superCls ):
					base = getattr( QtWidgets, superCls )               
				else:
					base = QtWidgets.QWidget               
				return shiboken.wrapInstance( long( ptr ), base )
			else:
				return None
			
		elif __binding__ in ('PySide2', 'pyQt5'):
		 	if globals().has_key( 'shiboken2' ):
				if base is None:
					qObj = shiboken.wrapInstance( long( ptr ), QtCore.QObject )
					metaObj = qObj.metaObject()
					cls = metaObj.className()
					superCls = metaObj.superClass().className()
					if hasattr( QtWidgets, cls ):
						base = getattr( QtWidgets, cls )
							 
					elif hasattr( QtWidgets, superCls ):
						base = getattr( QtWidgets, superCls )               
					else:
						base = QtWidgets.QWidget               
				return shiboken.wrapInstance( long( ptr ), base )
			else:
				return None

		elif globals().has_key( 'sip' ):
			base = QtCore.QObject
				
			return sip.wrapinstance( long( ptr ), base )
			
		else:
			return None
	else:
			return None

def main():
	pass

if __name__=='__main__':
	main()