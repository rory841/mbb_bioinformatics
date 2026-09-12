
import os


def parse_fasta_file(filename: str)->dict:

    sequences = {}
    current_header = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith('>'):
                current_header = line[1:]
                sequences[current_header] = []

            else:
                if current_header:
                    sequences[current_header].append(line.upper())

    for header in sequences:
        sequences[header] = "".join(sequences[header])

    return sequences

filename = "target_homologs.fasta"

if os.path.exists(filename):
    record_dict = parse_fasta_file(filename)

    for header, seq in record_dict.items():
        gc_val = round((seq.count('G') + seq.count('C')/len(seq)) * 100, 2)
        print(f"Header: {header}")
        print(f"  Length: {len(seq)} bp | GC Content: {gc_val}%\n")