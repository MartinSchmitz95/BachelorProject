from Bio import SeqIO

with open("./1-FASTA-files/chr19_two_mio/reads.fasta", "r") as input_file, open("./1-FASTA-files/chr19_two_mio/reference.fasta", "r") as reference:

    referenceLen = len((next(SeqIO.parse(reference, "fasta"))).seq)

    combinedSeqLen = 0;
    for sequence in SeqIO.parse(input_file, "fasta"):
        combinedSeqLen += len(sequence.seq)


print("Length of the reference sequence: " + str(referenceLen))
print("Length of the combined sequence of the reads: " + str(combinedSeqLen))

print("Coverage of the given dataset: " + str(combinedSeqLen / referenceLen))
