# Shaqib q7.py

def swap(a, b):
    """
    Swap two integers without using a third variable.
    Return the new pair (a, b).
    """
    a = a + b
    b = a - b
    a = a - b
    return (a, b)
