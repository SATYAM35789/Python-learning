# Without using third variable
x = int(input("Enter the x:"))
y = int(input("Enter the y:"))
x,y = y,x
print("The value of x is",x)
print("The value of x is",y)