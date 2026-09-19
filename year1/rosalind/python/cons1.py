
from Bio import SeqIO, motifs

filepath = "datasets/rosalind_cons.fasta"

def find_consensus_and_profile(filepath):
    """ Given: A collection of at most 10 
        DNA strings of equal length (at most 1 kbp) in FASTA format.
        Return: A consensus string and profile matrix for the collection. 
        (If several possible consensus strings exist, return
        any one of them.)"""

    sequences = [str(r.seq) for r in SeqIO.parse(filepath, "fasta")]
    m = motifs.create(sequences)
    print(m.consensus) # Print consensus sequence
    # Print profile with integer counts (no decimals)
    for base in ["A", "C", "G", "T"]:
        counts_str = ' '.join(str(int(count)) for count in m.counts[base])
        print(f"{base}: {counts_str}")


if __name__ == "__main__":
    find_consensus_and_profile(filepath)