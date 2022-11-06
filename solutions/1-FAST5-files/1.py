from ont_fast5_api.fast5_interface import get_fast5_file
import os
import numpy as np
import matplotlib.pyplot as plt

def print_all_raw_data():
    #i = 1
    for filename in os.listdir("raw_signals"):
        fast5_filepath = "raw_signals/" + filename  # This can be a single- or multi-read file
        with get_fast5_file(fast5_filepath, mode="r") as f5:
            for read in f5.get_reads():
                raw_data = read.get_raw_data()
                length = len(raw_data)
                avg = np.average(raw_data)
                print(read.read_id + "; Length = " + str(length) + "; Mean value = " + str(avg))
                plt.figure(1)
                plt.title(read.read_id)
                #plt.subplot(10, 1, i).title.set_text(read.read_id) uncomment all to plot signals as subplots
                #i += 1
                plt.plot(raw_data)
                plt.show()
if __name__ == '__main__':
    print_all_raw_data()