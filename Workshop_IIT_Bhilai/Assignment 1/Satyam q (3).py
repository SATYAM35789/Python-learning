# Shaqib q3.py

def trailing_zeros(n):
    """
    Return the number of trailing zeros in n! by counting
    how many times 5 divides factors up to n.
    """
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count
