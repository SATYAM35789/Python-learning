lower = int(input("Enter Lower value:"))
Upper = int(input("Enter Upper value:"))

for num in range(lower,Upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)