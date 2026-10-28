# Shaqib q1.py

def is_disarium(n):
    """
    A Disarium number is one where the sum of its digits
    raised to their positions equals the number itself.
    e.g. 135: 1^1 + 3^2 + 5^3 = 135
    """
    s = str(n)
    total = 0
    for i in range(len(s)):
        digit = int(s[i])
        power = i + 1
        total += digit ** power
    return total == n
