from Bio import SeqIO


if __name__ == '__main__':
    reads = list(SeqIO.parse("reads.fasta", "fasta"))
    for read in reads:
        d = read.description
        lista = d.split(" ")
        start = lista[2]
        start = int(start[6:-1])
        end = lista[3]
        end = int(end[4:])
        length = str(end-start)
        lista[3] = "length=" + length
        d = ' '.join(lista)
        read.description = d
    SeqIO.write(reads, "reads_mod.fasta", "fasta")

