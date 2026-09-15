
filepath = "datasets/rosalind_hamm.txt"

with open(filepath, 'r') as file:
    s = file.readline()
    t = file.readline()

count = 0

for i, char in enumerate(s):
    if char == t[i]:
        pass
    else:
        count += 1

print(count)