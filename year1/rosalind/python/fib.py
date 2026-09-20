
from functools import lru_cache

def fibonacci_rabbits(n, k):
    """Given: Positive integers n ≤ 40 and k ≤ 5.
        Return: The total number of rabbit pairs that will be present after n
        months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
        rabbit pairs (instead of only 1 pair)."""
    
    @lru_cache(maxsize=None)
    def helper(month):
        if month == 1 or month == 2:
            return 1
        return fibonacci_rabbits(month-1, k) + k * fibonacci_rabbits(month-2, k)
    return helper(n)

n, k = 30, 4
print(fibonacci_rabbits(n, k))