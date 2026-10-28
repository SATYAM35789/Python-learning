#Writing a function for calculating sum from 1 to n:
n= int(input("Enter n:"))
def sumOnetoN(n):
    sum=0
    for i in range(1,n+1):
        sum += i
    return sum

output= sumOnetoN(n);
print("Sum of all number till n is:",output)

