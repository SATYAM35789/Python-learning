''' Given a string and a number N, we need to mirror the charaters from N-th position up to length of the string 
    in a alphabatical order. In mirror operation , we change 'a'to 'z', 'b'to 'y' andso on. 
    Input: N= paradox
    Output: paizwlc
    Zip() fun
    L1 = ["a","b","c"]  we want to made a list1 items to be as Keys. 
    L2 = [1,2,3]         we want to made a list2 items to be as Values. 
    dict= dict(zip(l1,l2)) 
          dict is constructor
'''
input_string = input("Enter a string")
n= int(input("Enter n :"))

# Craeting a dictionary for mirror opertaion
alphabets = "abcdefghijklmnopqrstubwxyz"
reverse_alphabets = alphabets[::-1]   # -1 means right to left moving
dict1= dict(zip(alphabets,reverse_alphabets))

#  Finding the part of string on which we will do mirror opertion
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

# Finding the mirror string
mirror = ""
for i in range(0,len(suffix)):
    mirror= mirror + dict1[suffix[i]]  # Suffix[i] is an alphabets

# Creating the final string 
res = prefix + mirror
print("The result is", res)
