from Bio import SeqIO


if __name__ == '__main__':
    reads = list(SeqIO.parse("A.fasta", "fasta"))
    lengths = []
    for read in reads:
        d = read.description
        lista = d.split(" ")
        length = lista[3]
        length = int(length[7:])
        lengths.append(length)
    print("Shortest read length: " + str(min(lengths)))
    print("Number of reads: " + str(len(lengths)))
    print("Average read length: " + str(sum(lengths)/len(lengths)))