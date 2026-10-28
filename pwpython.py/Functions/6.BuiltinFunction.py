'''
sum(), min(),max()
'''
#Q1. Write a python function to calculate the factorial of a number (non -ve integer). The function accepts the number
#    as an argument.
def factorial(n):
    ans = 1
    if n==0:
        ans =1
    else:
        for i in range(1,n+1):
            ans *= i
    return ans

n = int(input("Enter a number:"))
output= factorial(n)
print("The factorial is",output)