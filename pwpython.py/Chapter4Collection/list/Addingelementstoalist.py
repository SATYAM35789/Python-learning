# Adding elements in a list ex list=[10,20,30,40]
# append() :- it adds item to the end of the list. ex list.append(50) now list=[10,20,30,40,50]
# insert()  :- It is used to insert the value at the index. list.insert(2,50) 
#  now list=[10,20,50,30,40]
# extend():- used when we want to append another list to the end of the current list
# ex list.extend(list2)

# Adding element to the list
fruits = ["Apple", "Mango", "Bananna","Cherry"]
print(fruits)

# Append()
fruits.append("kiwi")
print(fruits)

# insert()
fruits.insert(2, "Grapes")
print(fruits)

# Creating a another list
more_fruits = ["Papaya","Orange"]

# Using extend()
fruits.extend(more_fruits)
print(fruits)