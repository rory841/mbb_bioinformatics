
from Bio import SeqIO

fasta_filename = "sample.fasta"

for record in SeqIO.parse(fasta_filename, "fasta"):

    seq_str = str(record.seq)
    seq_len = len(seq_str)

    gc_count = seq_str.count('G') + seq_str.count('C')
    gc_percentage = (gc_count/seq_len) * 100

    print(f"ID:             {record.id}") 
    print(f"Description:    {record.description}") 
    print(f"Length:         {seq_len} bp") 
    print(f"GC Content:     {gc_percentage:.2f}%") 
    print(f"-" * 45) 
