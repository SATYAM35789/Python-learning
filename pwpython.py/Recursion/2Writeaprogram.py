# Write a program to print numbers from n to 1.
def print_nto1(n):
    #Base case
    if n==0:
        return 1
    #print(n)
    print_nto1(n-1)
    print(n)

n = int(input("Enter n:"))
print_nto1(n)