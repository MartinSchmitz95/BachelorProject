from Bio import SeqIO

with open("./1-FASTA-files/chr19_two_mio/reads.fasta", "r") as input_file, open("./1-FASTA-files/chr19_two_mio/reads.fasta", "r+") as output_file:
    for sequence in SeqIO.parse(input_file, "fasta"):
        des_length = " len=" + str(len(sequence.seq))
        sequence.description = ' '.join(sequence.description.split()[:3]) + des_length
        
        SeqIO.write(sequence, output_file, "fasta")
