
def fibd(n,m=1):
  ages = [1] + [0]*(m-1)
  for _ in range(1, n):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

print(fibd(6, 3))