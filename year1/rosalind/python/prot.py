

codon_filepath = "text_files/raw_codon_table.txt"

def generate_codon_table(codon_filepath: str) -> dict:
    """Reads a codon table and generates a codon dict"""
    codon_table = {}

    with open(codon_filepath, "r") as file:
        for line in file:
            line = line.strip()
            codon = line.split()[0]
            peptide = line.split()[1]
            codon_table[codon] = peptide
    return codon_table


def match_codon(codon_filepath: str, dataset: str)-> str:
    """Returns an A.A sequence for an mRNA sequence"""
    codon_dict = generate_codon_table(codon_filepath)
    protein_seq = []

    for i in range(0, len(dataset), 3):
        codon = dataset[i: i+3]
        amino_acid = codon_dict.get(codon)

        if amino_acid == "Stop" or amino_acid is None:
            break
        protein_seq.append(amino_acid)

    return "".join(protein_seq)
        


if __name__ == "__main__":
    with open("datasets/rosalind_prot.txt", "r") as file:
        sample = file.read()
    
    print(match_codon(codon_filepath, sample))