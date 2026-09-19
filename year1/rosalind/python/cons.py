
from Bio import SeqIO

filepath = "datasets/rosalind_cons.fasta"


def find_consensus_and_profile(filepath):

    """Given: A collection of at most 10 
        DNA strings of equal length (at most 1 kbp) in FASTA format.
        Return: A consensus string and profile matrix for the collection. 
        (If several possible consensus strings exist, return
        any one of them.)"""
    # 1. Read all sequences into memory
    records = [str(r.seq) for r in SeqIO.parse(filepath, "fasta")]
    seq_len = len(records[0])

    # 2. Initialize profile matrix with zeros matching sequence length
    profile = {
        "A": [0] * seq_len,
        "C": [0] * seq_len,
        "G": [0] * seq_len,
        "T": [0] * seq_len
    }
    # 3. Fill profile counts column by column
    for seq in records:
        for i, base in enumerate(seq):
            profile[base][i] += 1

    # 4. Build consensus string by finding the most frequent base at position i
    consensus = []
    for i in range(seq_len):
        most_common_bases = max(["A", "C", "G", "T"], key=lambda b: profile[b][i])
        consensus.append(most_common_bases)
    consensus_str = "".join(consensus)

    print(consensus_str)
    for base in ["A", "C", "G", "T"]:
        print(f"{base}: {' '.join(map(str, profile[base]))}")



if __name__ == "__main__":

    find_consensus_and_profile(filepath)
