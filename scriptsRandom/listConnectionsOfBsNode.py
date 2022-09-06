# -*- coding: utf-8 -*-
##--------------------------------------------------------------------------------------------
##
## TO DO:
##
##--------------------------------------------------------------------------------------------

# IMPORTS
import maya.cmds as mc
import json
import os
import sys

jtools = os.getenv("JENTOOLS")
sys.path.append(jtools)

from functions import abstractFunctions as absFunc
reload(absFunc)


def saveConnections():

    tempDict = r'G:/GoT_CONQUEST/ASSETS/CHARACTERS/Brennon_Knight/Rigging/Dictionaries'

    bsNode = 'C_facialExpressions_BSNODE'

    connections = mc.listConnections(bsNode, p=1, t='remapValue')
    connectionsDict = {}

    for x in connections:
        inputV = mc.listConnections(x, p=1)[0]     

        connectionsDict[inputV] = x

    with open(tempDict + r'/' + 'tempConnectionData' + '.json', 'w') as outfile:
        json.dump(connectionsDict, outfile, sort_keys=1, indent=4)


def loadConnections():

    tempDict = r'G:/GoT_CONQUEST/ASSETS/CHARACTERS/Brennon_Knight/Rigging/Dictionaries/tempConnectionData.json'

    bsNode = 'C_facialExpressions_BSNODE'

    connections = mc.listAttr(bsNode, m=1, k=1)

    for a in connections:
    	   		
    	if a.endswith('_SOFI'):
    		b=a.split('_SOFI')[0] 
    		dataB = absFunc.getSimpleJson(tempDict, bsNode+ '.' + b)

    		if dataB != None:
        		mc.connectAttr(dataB, bsNode + '.' + a, f=1)

        else:
	        data = absFunc.getSimpleJson(tempDict, bsNode+ '.' + a)      
	        
	        if data != None:
	        	mc.connectAttr(data, bsNode + '.' + a, f=1)

       	
        
		
#saveConnections()
loadConnections()


