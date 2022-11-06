from Bio import SeqIO


if __name__ == '__main__':
    ref = list(SeqIO.parse("reference.fasta", "fasta"))
    reads = list(SeqIO.parse("reads.fasta", "fasta"))
    reflen = len(ref[0].seq)
    print("The reference seq length: "+ str(reflen))
    total = 0
    for read in reads:
        total = total + len(read.seq)
    print("Combined reads length: " + str(total))
    coverage = total/reflen
    print("Coverage: "+ str(coverage))