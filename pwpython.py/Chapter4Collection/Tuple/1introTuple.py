#  TUPLE :- Used store multiple items in a variable.
#  Syntex: tuple_name=("item1","item2") Ex colours=("blue","black")
# PROPERTIES OF TUPLE:-
# 1.ORDERED :- items are in order
# 2.IMMUTABLE:- values of the tuple cann't be changed
# 3.Anydata type :- int, float, string etc
# 4. Duplicate allowed
# 5. Mix of different datatypes :allowed

# Creating a tuple
colours = ("blue","yellow","red")
print("Tuple :" ,colours)

# Creating a tuple with one item
# fruit = ("apple") HERE the compiler not understand that this is a tuple or string 
# so we use a comma so it can understand 
fruit = ("apple")
print(type(fruit))            # String
fruit = ("apple",)
print("Tuple :" ,fruit)      # Tuple

# Checking type of tuple:
print(type(colours))
print(type,(fruit))

# Check lenght
print(len(colours))

# Another way creating tuple
name = tuple(("Satyam")) # Two bracket 1 for constructor 2 for defining tuple
print("Another way",name)
print(type(name))