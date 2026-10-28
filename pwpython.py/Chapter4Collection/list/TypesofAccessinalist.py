# Aeccessing in a list:-  list = [ 10,20,30,40,50]
#1. Indexinng : ex list[2] = 20
#2. Negative :- ex list[-2] = 40
#3. Ranges of indexing: ex  To access items in range syntex list[starting:ending]
#    Starting index is Inclusive, Ending index is Exclusive ex list[1:3] =20 30 (positive index)
#4. Range of negativeindexs:  list[-3:-1]= 20 30 (Negative indexing)  
fruits = ["Apple", "Mango", "Bananna","Cherry"]
print(fruits)

# Indexing in a list
print(fruits[1]) # Mango
print(fruits[-3])# Mango
print(fruits[1:3]) # [ 'Mango', 'Bananna']
print(fruits[-3:-1]) # ['Mango', 'Bananna']