
from Bio import SeqIO

filename = "datasets/sample.fasta"
file_format = "fasta"

results = []

for record in SeqIO.parse(filename, file_format):

    seq_str = str(record.seq)
    gc_count = seq_str.count('G') + seq_str.count('C')
    gc_percent = (gc_count/len(seq_str))*100

    results.append((gc_percent, record.id))


results.sort()
highest_gc, highest_label = results[-1]

print(highest_label)
print(f"{highest_gc:.6f}")