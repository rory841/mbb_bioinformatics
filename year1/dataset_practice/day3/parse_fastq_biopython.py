
from Bio import SeqIO

filename = "diagnostic_reads.fastq"
file_format = "fastq"

for record in SeqIO.parse(filename, file_format):

    scores = record.letter_annotations["phred_quality"]
    avg_scores = sum(scores)/len(scores)

    print(f"ID: {record.id}")
    print(f"Sequence: {record.seq}")
    print(f"Mean Quality Score: {round(avg_scores, 2)}")

    if avg_scores < 30:
        print(" [Warning]: Read Failed Q30 quality threshold!\n")
    else: 
        print(" [PASS]: High quality read.\n")