from ont_fast5_api.fast5_interface import get_fast5_file
from ont_fast5_api import fast5_read

import os
import h5py

fast5Folder = "./1-FAST5-files/basecalled_signals"
fast5FolderRaw = "./1-FAST5-files/raw_signals"

def parseBasecalledSignals(filename, filenameRaw, n):
	print("Signal" + str(n) + ":")

	with h5py.File(filenameRaw, "r") as f5_raw, h5py.File(filename, "r") as f5_base, get_fast5_file(filename, mode="r") as f5:
            	rawSignalItems = f5_raw.items()
            	signalItems = f5_base.items()
            	
            	raw_inf = []
            	for groupItems in rawSignalItems:
            		groupName, groupObj = groupItems
            		groupAttrs = groupObj.items()
            		for attribute in groupAttrs:
            			attributeName, attributeObj = attribute
            			raw_inf.append(attributeName)

            	for groupItem in signalItems:
            		groupName, groupObj = groupItem
            		groupAttrs = groupObj.items()
            		for attribute in groupAttrs:
            			attributeName, attributeObj = attribute
            			if attributeName not in raw_inf:
            				print(attributeObj.name)
            	

	print()

n = 0
for filename in os.listdir(fast5Folder):
	f = os.path.join(fast5Folder, filename)
	f_raw = os.path.join(fast5FolderRaw, filename)
	
	if os.path.isfile(f):
		if os.path.isfile(f_raw):
			n += 1
			parseBasecalledSignals(f, f_raw, n)

