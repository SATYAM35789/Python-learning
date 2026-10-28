# Ternary operator: Used simplfy the conditional statements in single line
# syntex:- Variable= "value1" if condition else "value2"
# Question1 :- Write a program to check if number is odd or even using ternary operator
num = int(input("Enter a number :"))

output = "Even" if num%2==0 else "odd"
print("Output is" , output)

# we can also write as
# print("output is" , "Even" if num %2==0 else "odd")
