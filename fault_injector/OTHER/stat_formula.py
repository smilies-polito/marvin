import math

def compute_e(n: int, N: int, p: float, t: float) -> float:
    """
    Compute the error rate (e) given the number of faults to inject (n),
    the total number of parameters (N), probability of a fault (p),
    and the confidence level factor (t).
    
    :param n: The number of faults to inject
    :param N: The total number of parameters
    :param p: The probability of a fault
    :param t: The desired confidence level
    :return: The computed error rate (e)
    """
    if n <= 0 or N <= 1 or p <= 0 or p >= 1 or t <= 0:
        raise ValueError("Invalid input values. Ensure N > 1, 0 < p < 1, n > 0, and t > 0.")
    
    e_squared = ((N / n) - 1) * (t**2 * p * (1 - p)) / (N - 1)
    
    if e_squared < 0:
        raise ValueError("Computed e^2 is negative, check input values.")
    
    return math.sqrt(e_squared)

# Example usage
n = 5000
#N = 4*32*2629
N = 32*353904*2629
p = 0.5
t = 2.58
print(N)
e = compute_e(n, N, p, t)
print(f"Computed error rate e: {e}")

#Errore 0.01029 su registers single bit e multi bit N = 4*32*2629
#Errore memoria 0.01824