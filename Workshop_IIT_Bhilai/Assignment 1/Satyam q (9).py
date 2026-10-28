# Shaqib q9.py

def is_isogram(s):
    """
    Return True if the string has no repeating letters.
    Ignore case and non-letters.
    """
    seen = set()
    for char in s.lower():
        if char.isalpha():
            if char in seen:
                return False
            seen.add(char)
    return True
