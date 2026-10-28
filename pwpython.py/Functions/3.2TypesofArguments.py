# Keyword arguments or named arguments
def add(n1,n2):
    print("n1",n1)
    print("n2",n2)
    sum = n1+n2
    return sum

print("The sum is", add(n2=2,n1=8))