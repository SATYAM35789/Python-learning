# TUPLE vs LIST
# Why to use tuple if we have list.
#  - Itrating through a 'tuple' is faster than in a 'list'.
#  - Althrough, 'Lists' are mutable whereas 'tuple' are immutable.
#  - Tuple that contain immutableelements can be used as a key for a dictionary.

# Reverse Tuple 
# Input: tuples=(10,11,12,13,14,15)
# Output: tuples=(15,14,13,12,11,10)

# reversed():- It is used to itrate through a sequence in a reverse order. 
input_tuple = (1,2,3,4,5,6)
list=[]

# adding reversed values in a list
for x in reversed(input_tuple):
    list.append(x)

output_tuple = tuple(list)  # typecast into tuple
print(output_tuple)