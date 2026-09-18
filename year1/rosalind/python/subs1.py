
from Bio.SeqUtils import nt_search

filepath = "datasets/rosalind_subs.txt"

def readdataset(filepath: str):
    with open(filepath, "r") as file:
        s = file.readline()
        t = file.readline()
    return s, t

def find_mortif(s: str, t: str) -> list[int]:
    """Finds all 1-based starting positions of sequence t in sequence s using Biopython."""

    # nt_search returns [pattern_regex, pos1, pos2, ...] using 0-based indexing
    raw_matches = nt_search(s, t)

    # Exclude element 0 (the pattern) and convert 0-based indices to 1-based indices
    locations = [pos + 1 for pos in raw_matches[1:]]

    return locations


if __name__ == "__main__":
    s, t = readdataset(filepath)

    result = find_mortif(s, t)

    print(*result)