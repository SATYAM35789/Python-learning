#  Python collections (Array)
#  Lists Tuple Set Dictionary :- They are called python collection because thsee are builtin data
#  types in python help us to store the collection of items in one variable.
# 1. Lists :- Allow us to store multiple items in single variable
#  EX. fruits = ["apple", "bananna", "chery"] : stored 3 items as string.

# Things to remember about the list
# 1. Indexed:- List items indexed. Zero base index. 
# 2. Items are ordered. The way in which we put our item,  they remains in that way.
# 3. Mutable : Able to changeor uodate a list.
# 4. Duplicates are allow .
# 5. Any  datatypes can be stored 
# 6. Mix of different different datatypes.  
# example:- 
fruits = ["apple", "Bananna", "Bananna" ,"Cherry"]  # Create a list
print(fruits)  # Printing a list
print(type(fruits)) # Check type of list
print(len(fruits)) # Check a lenght of list

# Checking if an item is present inn a list 
if "Bananna" in fruits:
    print("The bananna is the part of the list")

# Checking if an item is not present in a list.
if "Mango" not in fruits:
    print("Mango is not a part of a list")