
import os

filename = "datasets/rosalind_gc.txt"


def parse_fasta(filename:str):
    """Parses a Fasta file into a dictiionary of headers
        and combined sequence strings
    """
    sequences = {}
    current_label = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_label = line[1:]
                sequences[current_label] = []
            else:
                sequences[current_label].append(line)

    return {label:"".join(seq_list) for label, seq_list in sequences.items()}

def calc_gc(sequence):
    """Calculates percentage of GC in DNA sequence"""
    gc_count = sequence.count('G') + sequence.count("C")
    return (gc_count/len(sequence)) * 100

def highest_gc_content(filename:str):
    fasta_dict = parse_fasta(filename)
    max_label = None
    max_gc = -1.0

    for label, sequence in fasta_dict.items():
        gc_val = calc_gc(sequence)
        if gc_val > max_gc:
            max_gc = gc_val
            max_label = label

    return max_gc, max_label

if __name__ == '__main__':
    if os.path.exists(filename):
        gc_content, label = highest_gc_content(filename)
        print(f"{label}")
        print(f"{gc_content:.6f}")
    else:
        print(f"File {filename} doesnt exit") 