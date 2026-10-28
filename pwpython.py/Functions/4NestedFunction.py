#Nested function
def outerFunction():
    x=1 # Variable in the outer function
    def innerFunction():
        y=2 #Variable in the inner function
        result = x+y
        return result
    return innerFunction() # it returns output of the innerfunction

output = outerFunction()
print(output)