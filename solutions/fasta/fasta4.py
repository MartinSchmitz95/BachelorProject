from Bio import SeqIO

with open("./solutions/fasta/A.fasta", "r") as input_file:
    totalSeqLen = 0
    totalSeqNum = 0
    
    for sequence in SeqIO.parse(input_file, "fasta"):
        try:
            shortestValue
        except NameError as e:
            shortestValue = len(sequence.seq)

        if (shortestValue > len(sequence.seq)):
            shortestValue = len(sequence.seq)

        totalSeqLen += len(sequence.seq)
        totalSeqNum += 1

print("File contains " + str(totalSeqNum) + " reads.")
print("Length of the shortest read in the file is " + str(shortestValue))
print("The average length of the sequence is " + str(totalSeqLen / totalSeqNum))
