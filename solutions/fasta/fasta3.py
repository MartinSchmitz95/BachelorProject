from Bio import SeqIO

import re

with open("./1-FASTA-files/chr19_two_mio/reads.fasta", "r") as handler, open("./solutions/fasta/A.fasta", "w") as first_file, open("./solutions/fasta/B.fasta", "w") as second_file:
    nA = 1;
    nB = 1;
    
    for sequence in SeqIO.parse(handler, "fasta"):
    	
        startNumber = int(re.split(',|=', sequence.description)[3])

        if startNumber >= 500000 and startNumber <= 600000:
            sequence.id = str(nA)
            sequence.description = sequence.id + " " + ' '.join(sequence.description.split()[1:])

            nA += 1
        
            SeqIO.write(sequence, first_file, "fasta")
        elif startNumber >= 1500000 and startNumber <= 1600000:
            sequence.id = str(nB)
            sequence.description = sequence.id + " " + ' '.join(sequence.description.split()[1:])
            
            nB += 1
        
            SeqIO.write(sequence, second_file, "fasta")


def coverage(iterator, referenceLen):
    combinedSeqLen = 0;
    
    for sequence in iterator:
        combinedSeqLen += len(sequence.seq)

    return combinedSeqLen / referenceLen

with open("./solutions/fasta/A.fasta", "r") as first_file, open("./solutions/fasta/B.fasta", "r") as second_file, open("./1-FASTA-files/chr19_two_mio/reference.fasta", "r") as reference:
    iteratorA = SeqIO.parse(first_file, "fasta")
    iteratorB = SeqIO.parse(second_file, "fasta")

    referenceLen = len((next(SeqIO.parse(reference, "fasta"))).seq)
    
    coverageA = coverage(iteratorA, referenceLen)
    coverageB = coverage(iteratorB, referenceLen)

print("The coverage of read set A is " + str(coverageA))
print("The coverage of read set B is " + str(coverageB))

if coverageA != coverageB:
	print("The coverage is different because the sets of reads have different lengths.")
else:
	print("The coverage is same for both sets of reads because they have the same length.")



