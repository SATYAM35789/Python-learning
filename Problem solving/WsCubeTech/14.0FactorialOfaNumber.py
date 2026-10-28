num = int(input("Enter a number:"))
fact = 1

if num<0:
    print("Factorial of 0 does not exist")
if num ==0:
    print("Factorial of zero is",1)
if num>0:
    for i in range(1,num+1):
        fact = fact*i
print("The factorial of a given number is:",fact)
