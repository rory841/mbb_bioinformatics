
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

filename = "datasets/sample.fasta"

best_gc = max(
    SeqIO.parse(filename, "fasta"),
    key= lambda seq: gc_fraction(seq)
)

print(best_gc.id)
print(f"{gc_fraction(best_gc.seq)*100:.6f}")