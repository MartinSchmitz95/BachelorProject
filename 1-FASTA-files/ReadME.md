## Intro:
In this tutorial you will learn how to deal with FAST/FASTQ files.
### FASTA format

For gentle introduction, please read [Wikipedia FASTA page](https://en.wikipedia.org/wiki/FASTA_format).

Example of FASTA format:

```python
>SEQUENCE_1
MTEITAAMVKELRESTGAGMMDCKNALSETNGDFDKAVQLLREKGLGKAAKKADRLAAEG
LVSVKVSDDFTIAAMRPSYLSYEDLDMTFVENEYKALVAELEKENEERRRLKDPNKPEHK
IPQFASRKQLSDAILKEAEEKIKEELKAQGKPEKIWDNIIPGKMNSFIADNSQLDSKLTL
MGQFYVMDDKKTVEQVIAEKEKEFGGKIKIVEFICFEVGEGLEKKTEDFAAEVAAQL
>SEQUENCE_2
SATVSEINSETDFVAKNDQFIALTKDTTAHIQSNSLQSVEELHSSTINGVKFEEYLKSQI
ATIGENLVVRRFATLKAGANGVVNGYIHTNGRVGVVIAAACDSAEVASKSRDLLRQICMH
```

Notice different letters in the sequence. Different unknown nucleotide variations are coded with different letters. Please refer to the table on Wikipedia Page.

### FASTQ format

FASTQ format contains quality indexes for each nucleotide (i.e. the probability that the corresponding base call is incorrect). Gentle introduction is available at [Wikipedia FASTQ](https://en.wikipedia.org/wiki/FASTQ_format)

Example:
```python
@SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
+
!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65
```


Observe the two files in this folder:

**reference.fasta** 
Is a reference genome. It contains a around a 2 million nucleotides long part of the human chromosome 19

**reads.fasta**
This file stores reads from the reference. The typical file type for reads is FASTQ, which additionally includes information about the certainty of a nucleotide in the sequence. However, the given file contains synthetic, perfect reads, so the certainty is always 100%. In this tutorial we only deal with FASTA files, but keep in mind that FASTQ files can be handled the same.

Every read in a FASTA or FASTQ file has a header where different information can be inserted. For example a read in this FASTA file has the header:
>**id** strand=**B**, start=**S**, end=**E**

**id** is the id of the read

**b** = **+** or **-** shows if the reads is from the negative or positve strand

**S** = Start of the read on the reference position

**E** = ENd of the read on the reference position

To parse FASTA/FASTQ files we recommend to use the python package [SeqIO](https://biopython.org/wiki/SeqIO)


## Assignments:

### 1 Modify FASTA description
Modify the file reads.fasta so that the heder of the reads looks like following:
>**id** strand=**B**, start=**S**, length=**L**

where **L** is the length of the read.


### 2 Coverage
* How long is the reference sequence?

* How long is the combined sequence of the reads?

* The coverage is the factor how much larger the set of reads is compared to the reference length. It describes how often the reference is covered by the set of reads.

* What is the coverage of the given dataset?

### 3 Compare different regions
Create and save a fasta file *A.fasta* which contains all reads from the file *reads.fasta* which starts in the region 500,000-600,000 and another FASTA file *B.fasta* with all reads which start in the region 1,500,000-1,600,000.
The reads in the new files should have IDs 1,2,3,...n.

* What is the coverage of read set *A* and what is the coverage of read set *B*?

* Are they the same? Why or why not?

### 4 Output statistics of reads
Use your file A.fasta to answer the following questions:

* How large is the shortest read in the file?

* How many reads are contained in the file?

* What is the average length?
