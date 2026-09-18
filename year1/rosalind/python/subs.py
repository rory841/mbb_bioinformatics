

filepath = "datasets/rosalind_subs.txt"

def readdataset(filepath: str):
    with open(filepath, "r") as file:
        s = file.readline()
        t = file.readline()
    return s, t

def find_mortif(s: str, t: str)->list[int]:
    """Returns all 1-based starting locations of motif `t` in DNA string `s`."""
    locations = []
    len_s, len_t = len(s), len(t)

    for i in range(len_s - len_t + 1):
        if s[i : i + len_t] == t:
            locations.append(i+1)
    return locations
    

if __name__ == "__main__":
    s, t = readdataset(filepath)

    result = find_mortif(s, t)
    for i in result:
        print(f"{i} ", end="")
    print()