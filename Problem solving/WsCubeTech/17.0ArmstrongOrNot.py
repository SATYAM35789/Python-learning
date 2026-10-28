# Armstrong = Sum of each term power of the number of terms. 153 407
num = int(input("Enter a number here:"))
order = len(str(num))
sum=0
temp=num
while temp>0:
    digit= temp%10
    cube = digit**order
    sum = sum + cube
    temp //=10

if sum==num:
    print("Armstrong number")
else:
    print("Not armstrong number")