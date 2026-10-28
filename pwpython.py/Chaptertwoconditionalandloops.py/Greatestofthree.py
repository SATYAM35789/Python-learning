# Question3:
#Take 3 positive integers input and print the greatest of them. 
# Taking 3 number as input
n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))
n3 = int(input("Enter third number :"))
# checking if n1 is greatest
if n1>n2 and n1>n3:
    print("N1 is the greatest number")
# Checking if n2 is greatest
elif n2>n1 and n2>n3:
    print("n2 is the greatest number")
# Checking if n3 is greatest
else:
    print("n3 is the greatest")

