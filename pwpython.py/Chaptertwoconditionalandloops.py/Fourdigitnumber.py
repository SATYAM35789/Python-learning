# Take positive integer input and tell if it is a four digit number or not.
# 1000<= number <=9999
# Question2 :- 
number = int(input("Enter the number:"))
if number>=1000 and number<= 9999:
    print("It is four digit number")
else:
    print("Not a four digit number")