
import os

def parse_fasta_file(file_path: str):
    """
    Parses a single-record FASTA file. skips header lines,
    concatenates multiline sequence data, and calculate metrics
    """
    header = ""
    sequence_chunks = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                header = line[1:]
            else:
                sequence_chunks.append(line)


    full_seq = "".join(sequence_chunks).upper()

    seq_len = len(full_seq)
    g_count = full_seq.count('G')
    c_count = full_seq.count('C')
    gc_percentage = ((g_count+c_count) / seq_len) * 100 if seq_len > 0 else 0.0

    return header, full_seq, seq_len, round(gc_percentage, 2)



filename = "BRCA1_fragment.fasta"

if os.path.exists(filename):
    hdr, seq, len, gc = parse_fasta_file(filename)
    print(f"Header ID: {hdr}")
    print(f"Sequence lenght: {len} bp")
    print(f"GC content: {gc}%")
else:
    print(f"Error: {filename} does not exist in the current directory")