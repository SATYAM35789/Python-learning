colours = ("blue","yellow","red")
print("Tuple :" ,colours)

# Checking if an item exists in tuple
if "blue"in colours:
    print(" blue is the part of tuple.")

# Traverse the tuple
for i in colours:
    print(i)

# adding two tuple
more_colours = ("Black","White")
colours = more_colours + colours
print(colours) 
print(len(colours))

# Unpacking a tuplle
colour1, colour2, colour3, colour4, colour5 = colours
 
print(colour1, colour2, colour3, colour4, colour5)
