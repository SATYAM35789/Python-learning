# Removing elements from a list  ex. list=[10,20,30,40]
# remove() :- removes specified item ex. list.remove(20) now list=[10,30,40]
# pop() :- removes items at given index or last item ex list.pop(1) now list=[10,30,40]
#  ex2. list.pop() now list=[10,20,30]

fruits = ["Apple", "Mango", "Bananna","Cherry"]
print(fruits)

# Remove()
fruits.remove("Apple")
print("Current list =", fruits)

fruits.pop(1)
print("current list =", fruits)

fruits.pop() # removes last element from currnt list
print("current list =", fruits)
