'''
Print the sum of all positive no till n.
'''
n = int(input(" Enter n:"))
sum = 0
for i in range(1,n+1):
    sum += i
print("Sum of all till n is:",sum)

# Suppose we have another n value we have to print the . Now again write all the code again. 
n1 = int(input(" Enter another n"))
sum1 = 0
for i in range(1,n+1):
    sum1 += i
print("Sum of all till n is:",sum1)

# Block of reuseable code that perform a specific task. 