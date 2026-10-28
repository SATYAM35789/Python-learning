# Accessing items of set
name = {"Sia","Mia","tia"}
print(name)
for x in name:
    print(x)

# Check if an item exist in a set
if "Sia"in name:
    print("sia is in set")

# Add a element in set
name.add("riya")
print(name)

# Add a another sequence in a set
name_list = {"kia","jia"}
name.update(name_list)  # Add the name.list values to the name set
print(name)

# Removing elements froma set
name.remove("tia")
print("tia")

name.discard("tia") # this function will not show an error if the value is  not present in the set
print("tia")

# Join two a sets
print("Now the set:")
s1 = {'a','b','c'}
s2 = {'e','f','a'}
print(s1,s2)

s3 = s1.union(s2) # union():- it returns set in which there is value of both set
print(s3)

# if we want to add the set next to to another update()
s1.update(s2)
print( "Addition of elment from end of another set:",s1)

# Want keep only duplicates while joining
s4= ('a','g','t')
s1.intersection_update(s4)
print("Duplicate element:",s1)

# Want to keep all values except duplicates
s1.symmetric_difference_update(s4)
print("Except duplcates element",s1)

