from ngSkinTools.importExport import *


def ngSkinExportData(*args):
	selected = cmds.ls(sl=1)

	# if len(selected) == 0:
	#ngMeshes = []
	#ngNodes = cmds.ls(type='ngSkinLayerData')
	# for node in ngNodes:
	# ngMeshes.append(node.replace(''))

	assetPath = getAssetPath()
	jsonPath = assetPath + '/4_rig/work/setup/skin/'

	for sel in selected:
		fileName = assetPath.split('/')[-1] + '_' + sel
		layerData = LayerData()
		layerData.loadFrom(sel)
		exporter = JsonExporter()
		jsonContents = exporter.process(layerData)  # string data
		# convert from string to dictinary
		jsonContents = json.loads(jsonContents)

		with open(jsonPath + fileName + '.json', 'w') as outfile:
			json.dump(jsonContents, outfile, sort_keys=1,
					  indent=4, separators=(',', ': '))
			print(jsonPath + fileName + '.json')

		# end


def ngSkinImportData(*args):
	#selected = cmds.ls(sl=1)
	assetPath = getAssetPath()
	jsonPath = assetPath + '/4_rig/work/setup/skin/'

	for ngFile in os.listdir(jsonPath):
		if ngFile.endswith('.json') == True:
			assetName = assetPath.split('/')[-1]
			assetNameLen = len(assetName) + 1
			skinnedMesh = ngFile[assetNameLen:].replace('.json', '')

			if cmds.objExists(skinnedMesh) == True:
				print(skinnedMesh)
				with open(jsonPath + ngFile) as json_data:
					data = json.load(json_data)  # dict
					# convert from dict to string
					data = json.dumps(data)

				importer = JsonImporter()
				layerData = importer.process(data)

				try:
					layerData.saveTo(skinnedMesh)
					print('Loaded: ' + jsonPath + ngFile)
				except:
					cmds.warning('# ERROR: transfer skin to ' + skinnedMesh)

			else:
				print('... ' + skinnedMesh + ' not exist.')