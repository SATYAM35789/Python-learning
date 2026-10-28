'''
Pass by reference and Pass by value 
1 Pass by value ( for immutable objects , strinds,integers,float,tuples)
 1. When passed to a function then copy of a object is created. 
   The change in defination of function will not affect at calling.and assigned to local variable in function. 
 2. If any change is made to inside the function do not affect the original object outside a function. 

2 Pass by reference (Pass mutable objects like lists, dictionary) 
 1.Reference of actual object is passed to the function
 2. Changes inside function will afect the original object. 
 '''
# Pass by value
def addOne(x):
    x=x+1
    print("Inside function:",x)

x=5
addOne(x)
print("Outside function:",x) # Inside function value changed but outside it's remain same.

# Pass by reference
def modifyList(list):
    list.append(4)
    list=[4,5,6]  # By doing this the change not occured outside because here new object created instance of modifying
    print("Insude Function:",list)
list = [1,2,3]
modifyList(list)
print("Outside the function:",list)  # Outside the function effect is happened