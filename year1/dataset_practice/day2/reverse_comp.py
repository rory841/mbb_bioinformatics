
from Bio import SeqIO

input_file = "sample.fasta"
output_file = "reverse_complements.fasta"
modified_record = []

try:
    for record in SeqIO.parse(input_file, "fasta"):
        rev_seq = record.seq.reverse_complement()
        record.seq = rev_seq

        record.id = f"{record.id}_RC"
        record.description = f"{record.id} | Reverse Complement (5'->3')"

        modified_record.append(record)

    recs_written = SeqIO.write(modified_record, output_file, "fasta")

    print(f"Successfully processed and wrote {recs_written} records to {output_file}")

except FileNotFoundError:
    print(f"File - {input_file} does not exit.")