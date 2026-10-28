'''
Types of Arguments
1.Default arguments
2.Keyword arguments(named arguments)
3.Positional arguments
4.Arbitary arguments(variable-lenght arguments *args and **kwargs)
'''
# Function which takes 2 number as input and returns their sum
def add(n1,n2):
    sum = n1+n2
    return sum

x=2
y=3
print("The sum is", add(x,y))

