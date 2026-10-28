'''
1.Key characterstices of Recursive Function:
Recursion:- Call it self to solve the big problem. By answering the sub problem of big problem.
Suntex:- 
def recursive():
   recurse()
recurse()

Example:
2.Base case and Recursive case 
def factorial(n):
   if n==0 :                     Base case(Stoping Condition)
      return 1
    ans = n*factorial(n-1)       Recursive case 
    return ans

3.The call stack and Recursive calls
  Recursive function working in the memory. It helps to track the recusive calls. 
'''
def factorial(n):
    #Base case
    if n==0:
        return 1
    #Recusive case
    ans = n*factorial(n-1)
    return ans
n= int(input("Enter n"))
print(factorial(n))