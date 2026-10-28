#    1                   rows = n 
#    12                  columm= row no. (i)
#    123                 what to print = column num (j)
#    1234
n = int(input("Enter number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()