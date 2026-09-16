
import os

filepath = "datasets/rosalind_iprb.txt"

def readfile(filepath: str):
    """return k m n read from dataset file"""
    with open(filepath, "r")as file:
        return map(int, file.read().strip().split())
        



def dominant_probability(k: int, m: int, n: int) -> float:
    """
    Calculates probability of producing an offspring with a 
    dominant phenotype.
    k: AA count
    m: Aa count
    n: aa count

    return float complementary probability for dominant phenotype
    """
    # AA Aa aa
    # k  m  n
    # 2  2  2
    # Calculating the complementary probability reduces the number of mating 
    # combinations you must account for from six down to three, 
    # making your code cleaner and less prone to math errors.
    # N = k + m + n = 6
    # total pairs
    # Aa x Aa = 25%  ->  m(m-1)     * 1/4
    # AA x Aa = 50%  ->  2km        * 1/2
    # aa x aa = 100% -> n(n-1)      * 1/1

    # P(aa) = (0.25.m(m-1)) + 0.5(2km) + 1.n(n-1) /N(N-1)
    # P(Dominant) = 1 - P(aa)

    total_pop = k+m+n
    total_pairs = total_pop*(total_pop-1)
    # Sum total probability of producing homozygous recessive (aa) offspring
    prob_recessive = (
        (m*(m-1)*0.25) + (2*m*n*0.5) + (n*(n-1))
    ) / total_pairs

    # Complementary probability for dominant phenotype
    return 1-prob_recessive


if __name__ == "__main__":

    if os.path.exists(filepath):
        k, m, n = readfile(filepath)
        result = dominant_probability(k, m, n)
        print(f"{result:.5f}")
    else:
        print(f"File path {filepath} couldnt be located!")