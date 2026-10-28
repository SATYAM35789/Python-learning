# Given a dictionary in python, write a python program to fond the sum of all items 
# in  the dictionary.
# input: { 'a': 100,'y':200, 'c':300 }
# Output:- 600
# dict.keys()  // Print all keys of the dictionary.
# dict.values()  // Print all the values of dictionary. 
# We get all values and than we find the sum of dictionary.

dict = {
    'a': 100,'y':200, 'c':300
}
print(dict.values())
# To add all the values we have sum() fun
print("The sum of the dic",sum(dict.values()))