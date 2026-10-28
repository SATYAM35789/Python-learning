# Changing in a list ex. list=[10,20,30]
# At an index :-  ex list[1]=40  now list=[10,40,30]
# In a range :-  ex list[1:3]=[50,50] now list[10,50,50]

fruits = ["Apple", "Mango", "Bananna","Cherry"]
print(fruits)

# Updatind/Changing items in a list
fruits[1]= "Kiwi"
print(fruits) # Mango has been change to kiwi

fruits[1:3]=["papaya","orange","watermelon"] # we should provide a list here if in range
print(fruits)

# Note ek sublist ko ek sublist se he karenge update