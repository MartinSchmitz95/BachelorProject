import csv
import sys
import ctypes
 # increase max list size

#def avgqual(s): #wrong quality...
    #q = []
    #for x in s:
        #q.append(ord(x)-33)
    #return(sum(q)/len(q))

if __name__ == '__main__':
    maxInt = sys.maxsize
    csv.field_size_limit(int(ctypes.c_ulong(-1).value//2))
    fajl = open("alignment.sam")
    por = csv.reader(fajl, delimiter="\t")
    i = 0
    for line in por:
        if i < 2: #skip header
            i += 1
            continue

        if line[2] == '*': #skip if the read is not mapped
            continue
        #print(line[0], line[4]) to check if avg quality is right
        if i == 2:
            last_id = line[0] #initialize to later check if it's the same read as last one
            read = [line[0], 1, line[3], int(line[4])]
            i += 1
            continue

        if last_id == line[0]:
            read[1] += 1
            read[2] = read[2] + ", " + line[3]
            read[3] += int(line[4])
        else:
            last_id = line[0]
            read[3] = read[3]/read[1]

            read[1] = str(read[1])
            read[3] = str(read[3])
            print('\t'.join(read))

            read = [line[0], 1, line[3], int(line[4])]




