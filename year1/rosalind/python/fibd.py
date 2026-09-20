
def mortal_fibonacci(n: int, m: int)->int:
    """ Given: Positive integers n ≤ 100 and m ≤ 20.
        Return: The total number of pairs of rabbits that will remain after 
        the n-th month if all rabbits live for m
        months"""
    # ages[i] stores the count of rabbit pairs that are i months old
    ages = [0] * m      # 0 0 0
    # Index 0 = newborns, Index m-1 = rabbits in their final month of life
    ages[0] = 1         # 1 0 0

    for _ in range(1, n):
        # Only mature rabbits (age >= 1) reproduce each month
        newborns = sum(ages[1:]) #Reproduction

        # Shift age groups right by 1 month. 
        # Rabbits reaching age m are automatically dropped (die).
        ages = [newborns] + ages[:-1] #Mortality    
        # Slicing the array shifts every group's age up by 1 month and discards 
        # rabbits older than m-1 months, naturally accounting for their death.

    return sum(ages)


if __name__ == "__main__":
    print(mortal_fibonacci(96, 17))


# ```
# Array Structure (m = 3):
# +--------------------+------------------+------------------------+
# |  Index 0: Age 0    |  Index 1: Age 1  |  Index 2: Age 2        |
# |  (Newborns)        |  (Adults)        |  (Oldest - dies next)  |
# +--------------------+------------------+------------------------+

# Monthly Step Mechanism:
# 1. NEWBORNS  = sum(Age 1 + Age 2)      <-- Only mature rabbits reproduce
# 2. SHIFT     = [ Newborns ] + [ Age 0, Age 1 ]  <-- Age 2 gets pushed off and dies!

# ```

# ---

# ### Step-by-Step Array Trace (`n = 6`, `m = 3`)

# | Month | ages[0](0 mo. old) | ages[1](1 mo. old) | ages[2](2 mo. old) | What Happens in the Code | Total Rabbits |

# | **1** | **1** | **0** | **0** | Initialize array: 1 pair of newborns born.                          | **1** |
# | **2** | **0** | **1** | **0** | Shift right: No adults yet, so 0 newborns born.                     | **1** |
# | **3** | **1** | **0** | **1** | Adults at age 1 reproduce (`+1`). Array shifts right.               | **2** |
# | **4** | **1** | **1** | **0** | Adult at age 2 reproduces (`+1`). **Oldest pair dies** (dropped off right side). | **2** |
# | **5** | **1** | **1** | **1** | Adult at age 1 reproduces (`+1`). Array shifts right.               | **3** |
# | **6** | **2** | **1** | **1** | Adults at ages 1 & 2 reproduce (`+2`). **Oldest pair dies**.        | **4** |

# ---

# ### Code Mapping

# newborns = sum(ages[1:])
# Sums up indices `1` and `2` (rabbits age >= 1 month) to see how many new pairs are born.
# ages[:-1]
# Takes all elements except the last one (drops index `2`), which automatically simulates death after m=3 months.
# [newborns] + ages[:-1]
# Prepends the new births at index `0` and shifts everyone else 1 box to the right.