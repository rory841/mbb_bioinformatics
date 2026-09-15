
from functools import lru_cache

def fibonacci_rabbits(n, k):
    @lru_cache(maxsize=None)
    def helper(month):
        if month == 1 or month == 2:
            return 1

        return fibonacci_rabbits(month-1, k) + k * fibonacci_rabbits(month-2, k)
    return helper(n)

n, k = 30, 4
print(fibonacci_rabbits(n, k))