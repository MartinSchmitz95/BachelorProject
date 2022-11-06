from Bio import SeqIO


if __name__ == '__main__':
    reads = list(SeqIO.parse("reads_mod.fasta", "fasta"))
    readsA = []
    lengthA = 0
    A = 1
    for read in reads:
        d = read.description
        lista = d.split(" ")
        start = lista[2]
        start = int(start[6:-1])
        length = lista[3]
        length = int(length[7:])
        if (start>=500000 and start<=600000):
            lengthA = lengthA + length
            lista = lista[1:]
            read.id = str(A)
            read.description = (' ').join(lista)
            A += 1
            readsA.append(read)
    SeqIO.write(readsA, "A.fasta", "fasta")

    reads = list(SeqIO.parse("reads_mod.fasta", "fasta"))
    readsB = []
    lengthB = 0
    B = 1
    for read in reads:
        d = read.description
        lista = d.split(" ")
        start = lista[2]
        start = int(start[6:-1])
        length = lista[3]
        length = int(length[7:])
        if (start >= 1500000 and start <= 1600000):
            lengthB += length
            lista = lista[1:]
            read.id = str(B)
            read.description = (' ').join(lista)
            B += 1
            readsB.append(read)
    SeqIO.write(readsB, "B.fasta", "fasta")

    ref = list(SeqIO.parse("reference.fasta", "fasta"))
    reflen = len(ref[0].seq)

    print("Coverage A: " + str(lengthA/reflen))
    print("Coverage B: " + str(lengthB/reflen))