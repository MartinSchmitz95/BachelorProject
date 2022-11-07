from ont_fast5_api.fast5_interface import get_fast5_file
from ont_fast5_api import fast5_read

import os
import h5py

fast5FolderBase = "./1-FAST5-files/basecalled_signals"
fast5Folder = "./solutions/fast5/guppy_out/workspace"

def parseBasecalledSignals(filename, filenameBase, n):
	print("Signal" + str(n) + ":")
	
	mapBaseSummary = {}
	with get_fast5_file(filename, mode="r") as f5:
		analysesList = f5.list_analyses()
		for element in analysesList:
			elementType, elementValue = element
			mapBaseSummary[elementValue] = f5.get_summary_data(elementValue)

	with get_fast5_file(filenameBase, mode="r") as f5:
		analysesList = f5.list_analyses()
		for element in analysesList:
			elementType, elementValue = element
			if elementValue in mapBaseSummary:
				data = f5.get_summary_data(elementValue)
				if mapBaseSummary[elementValue] != data:
					for key in data:
						if key in mapBaseSummary[elementValue]:
							for attribute in data[key]:
								if attribute in mapBaseSummary[elementValue][key]:
									if (data[key][attribute] != mapBaseSummary[elementValue][key][attribute]):
										print(elementValue + " " + key + " " + attribute)
								else:
									print("additional: " + elementValue + " " + key + " " + attribute)

						else:
							print("additional: " + elementValue + " " + key)
					for key in mapBaseSummary[elementValue]:
						if key not in data:
							print("missing: " + elementValue + " " + key)
						else:
							for attribute in mapBaseSummary[elementValue][key]:
								if attribute not in data[key]:
									print("misssing: " + elementValue + " " + key + " " + attribute) 
			else:
				print("additional: " + elementValue)
	
	print()


n = 0
for filename in os.listdir(fast5Folder):
	f = os.path.join(fast5Folder, filename)
	f_base = os.path.join(fast5FolderBase, filename)
	
	if os.path.isfile(f):
		if os.path.isfile(f_base):
			n += 1
			parseBasecalledSignals(f, f_base, n)

