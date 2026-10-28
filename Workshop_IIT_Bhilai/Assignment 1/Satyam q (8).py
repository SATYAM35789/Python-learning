# Shaqib q8.py

def is_perfect(n):
    """
    A perfect number equals the sum of its proper divisors (excluding itself).
    """
    if n <= 1:
        return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n
