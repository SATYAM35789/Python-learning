num1 = int(input("Enter num1:"))

if num1==1:
    print("It is not a prime number")
if num1 >1:
    for i in range(2,num1):
        if num1%i==0:
            print("It is not a prime number.")
            break
    else:
        print("It is prime number.")
