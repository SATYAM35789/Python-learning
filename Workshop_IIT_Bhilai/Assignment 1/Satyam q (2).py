# Shaqib q2.py

def is_armstrong(n):
    """
    An Armstrong number is an n-digit number that equals
    the sum of each digit raised to the power n.
    """
    s = str(n)
    power = len(s)
    total = sum(int(digit) ** power for digit in s)
    return total == n
