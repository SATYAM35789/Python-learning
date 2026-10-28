# Shaqib q4.py

def is_palindrome(s):
    """
    Return True if string s reads the same forwards and backwards.
    Ignore case and non-alphanumeric characters.
    """
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
