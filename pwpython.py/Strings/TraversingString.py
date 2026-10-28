name1 = 'Collage Wallah'
# 1. Using for loop
for i in name1:
    print(i)

# Using list comprehension :  Hum string ko list bana denge , phir us list ko traverse
list = [char for char in name1]
for j in list:
    print(j)

# Finding the lenght of a string
print(len(name1))

#Find a char/substring in a string
# strung find(): returns the index of first occance of the char/substring and returns -1 if not found the char/substring
print(name1.find('e'))
print(name1.find('age'))
print(name1.find(' '))

# Slicing a string :- Used to get the part of the string  syntex: strinname[start:end] start is inclusive and end is wxclusive
# Slicing from start:- syntex: stringname[:end]
# Slicing from end:- syntex: stringname[start:]
# Negative indexing is possible. 

name1[1:8]
name1[:8]
name1[1:]
name1[-1:-8]

