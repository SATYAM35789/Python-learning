# For converting characters to uppercase
str1 = "new york"
str2 = str1.upper()  # this will change the original string str1 and return to str2
print(str2)

# For converting characters to lowercase
str3 = str2.lower()
print(str3)

# for capitalizing the first character of my string
str4 = str3.capitalize()
print(str4)

#for stripping/ removing any trailling white spaces 
str5 = "  new york  "
print(str5.strip())

#replace(): replaces the oldstring with new substring, count no of times.
# syntex: string.replace(oid_substring , new_substring, count)
# If count is not given -> all occurance of old substrinf are replace, jaha jaha bhi oldstring waha waha  newstring aa jayega

str6 = " Hello world, what a beautiful world this is"
print(str6.replace("world","Earth"))
print(str6.replace("world","Earth",1))

# split() :- used to split the string into a list of substring
# syntex: string.split(sep,maxsplit) by default sep = space , maxsplit = kitani bar split karna hai , by default: no limit
# parameters of split() are optional. 
str7 = "apple bananna mango"
list = str7.split()
print(list)

list = str7.split(",",3)
print(list)


