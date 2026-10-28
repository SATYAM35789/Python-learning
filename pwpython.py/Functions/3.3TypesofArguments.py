# Default arguments
def add(n1=0,n2=0): # Default values
    print("n1",n1)
    print("n2",n2)
    sum = n1+n2
    return sum

print("The sum is", add())