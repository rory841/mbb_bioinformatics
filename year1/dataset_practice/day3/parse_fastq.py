
import os

def phred33_to_q(char:str)-> int:
    """Converts a Phred+33 ASCII char to a num Q-score"""
    return ord(char)-33

def parse_fastq(filepath: str):
    """
    Reads a FASTQ file line by line and"""
    records = []

    with open(filepath, 'r') as handle:
        while True:
            header = handle.readline().strip()
            if not header:
                break

            sequence = handle.readline().strip()
            plus_line = handle.readline().strip()
            qual_string = handle.readline().strip()

            q_scores = [phred33_to_q(char) for char in qual_string]
            avg_q = sum(q_scores)/len(q_scores) if q_scores else 0.0

            records.append({
                "id": header[1:],
                "length": len(sequence),
                "avg_quality": round(avg_q, 2),
                "q_scores": q_scores
            })
    return records

filename = "diagnostic_reads.fastq"

if os.path.exists(filename):
    parsed_reads = parse_fastq(filename)
    for idx, read in enumerate(parsed_reads, 1):
        print(f"Read {idx}: {read['id']}")
        print(f"  Length: {read['length']} bp")
        print(f"  Average Quality (Q): {read['avg_quality']}")
        print(f"  First 5 Base Q-scores: {read['q_scores'][:5]}\n")        
        