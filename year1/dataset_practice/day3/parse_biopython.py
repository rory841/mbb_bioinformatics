
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

filename = "target_homologs.fasta"
file_format = "fasta"

for records in SeqIO.parse(filename, file_format):
    print(f"ID: {records.id}")
    print(f"Description: {records.description}")
    print(f"Length: {len(records.seq)} bp")
    #gc = (records.seq.count("G") + records.seq.count("C"))/len(records.seq) * 100 if len(records.seq) != 0.0 else 0.0
    #print(f"GC countent: {gc:.2f}% ")
    print(f"GC countent: {round(gc_fraction(records.seq)*100, 2)}%\n ")