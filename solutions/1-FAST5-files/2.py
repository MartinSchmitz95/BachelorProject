from ont_fast5_api.fast5_interface import get_fast5_file
import os
import numpy as np
import matplotlib.pyplot as plt

def print_all_data():
    #i = 1
    for filename in os.listdir("basecalled_signals"):
        fast5_filepath = "basecalled_signals/" + filename  # This can be a single- or multi-read file
        with get_fast5_file(fast5_filepath, mode="r") as f5:
            for read in f5.get_reads():
                print(read)

def print_all_data2():
    #i = 1
    for filename in os.listdir("raw_signals"):
        fast5_filepath = "raw_signals/" + filename  # This can be a single- or multi-read file
        with get_fast5_file(fast5_filepath, mode="r") as f5:
            for read in f5.get_reads():
                print(read)

if __name__ == '__main__':
    print_all_data()
    print()
    print_all_data2()

#don't know what to detect!