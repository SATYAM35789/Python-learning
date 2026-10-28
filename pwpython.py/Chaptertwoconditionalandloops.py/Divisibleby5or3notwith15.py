# Take positive integer input and tell if it is divisible by 3 or 5 but not with 15
num = int(input("Enter the no. :"))

# Checking whether it is divisible by 15 
if num%15==0:
    print("The number is divisibe by 15")
else:
    # Checking the no. is divisible by 3 or 5 
    if num%3==0 or num%5==0:
        print("The no is  divisible by 3 or 5 but not divisible by 15 ")
    else: 
        print("The number is not divisible by 3 ,5 ")

