#  Given a list in a python and provided the index of the  elements, Write a program to
# swap the two elements in the list. 
# ex.  input list=[23,65,19,90] idx1=0 , idx2=2
#     output: [19,65,23,90]
n= int(input("Enter the size of the list"))
list = []
for i in range(n): # Taking Inputs in list
    num = int(input("Enter the inputs :"))
    list.append(num) 

print("The input you have given in list:", list)
idx1 = int(input("Enter index 1 :"))
idx2 = int(input("Enter index 2 :"))

# swapping values
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print("List after swapping :" , list)
