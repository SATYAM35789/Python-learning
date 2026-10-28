# List Comprehension :- Used when we want to make a new list from an items of existing list.
# example :-  list=[40,20,30,10]  We want a list grater then 20 from this list.
#  sol1 : Traverse each element in a list and check and append if greater.
# sol2 (listcom) :- newlist= [ i  for i in list if i > 25]

fruits = ["Apple", "Mango", "Bananna","Cherry"]
print(fruits)
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

# Making a  Copy  list from orginal list
new_fruits = fruits.copy() # returning the fruits value which is stored in new_fruits
print("Copy list",new_fruits )

# Concinate Two list
new_fruits = fruits + new_fruits
print("After adding two List",new_fruits)

