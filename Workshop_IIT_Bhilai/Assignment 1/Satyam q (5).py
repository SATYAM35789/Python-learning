# Shaqib q5.py

def count_letters(text):
    """
    Return a tuple (vowels, consonants) in the text.
    Count only English letters, ignore case.
    """
    vowels_set = set('aeiou')
    vowels = consonants = 0
    for char in text.lower():
        if char.isalpha():
            if char in vowels_set:
                vowels += 1
            else:
                consonants += 1
    return (vowels, consonants)
