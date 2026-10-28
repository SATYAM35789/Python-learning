#                1          Row = no. of n
#               123         Col= space + digit   Space = n-i  Digit = 2i-1
#              12345        Col= 
#             1234567
n = int(input("Enter n:"))
for i in range(1,n+1): # loop for rows
    # Printing space
    print(" " * (n-i), end="")

    # Printing digits
    for j in range(1, 2*i):
        print(j, end="")
    print()