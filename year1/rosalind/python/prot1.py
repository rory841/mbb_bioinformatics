
from Bio.Seq import Seq

filepath = "datasets/rosalind_prot.txt"

def translate_mrna_file(filepath: str) -> str:
    """Reads an mRNA dataset file and translates it into a protein sequence."""
    with open(filepath, "r") as file:
        mrna_seq = Seq(file.read().strip())

        protein_seq = mrna_seq.translate(to_stop=True)

    return str(protein_seq)

if __name__ == "__main__":
    print(translate_mrna_file(filepath))
        