from ont_fast5_api.fast5_interface import get_fast5_file

import matplotlib.pyplot as plt
import numpy as np

import os

fast5Folder = "./1-FAST5-files/raw_signals"

def parseRawSignals(filename, n):
	with get_fast5_file(filename, mode="r") as f5:
        	for read in f5.get_reads():
            		raw_data = read.get_raw_data()
            		print("Signal" + str(n) + ":")
            		print(" the length: " + str(len(raw_data)))
            		print(" the mean value: " + str(np.median(raw_data)))
            		
            		plt.subplot(5, 2, n)
            		plt.title("Signal" + str(n))
            		plt.plot(raw_data)
	print()


fig = plt.figure(1)
fig.suptitle("Raw signals")

n = 1
for filename in os.listdir(fast5Folder):
	f = os.path.join(fast5Folder, filename)
		
	if os.path.isfile(f):
		parseRawSignals(f, n)
		n += 1

plt.tight_layout()

plt.show()



