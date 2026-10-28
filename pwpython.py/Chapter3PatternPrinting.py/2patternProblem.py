#    1234  For n=4
#    1234   Row = n   Column = n 
#    1234   What to print : number are being printed from 1 to n 
#    1234    
#  Using nested loop, outer for col, inner for row
n = int(input("Enter no :"))
for i in range(n): # Loop for rows
    for j in range(1,n+1): # loop for column
        print(j , end="")
    print() # for next row to print in next row