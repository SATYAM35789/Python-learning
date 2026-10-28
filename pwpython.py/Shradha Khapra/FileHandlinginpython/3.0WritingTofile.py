'''
Two way to write in the file:
1. 'w' mode: Overwrite the entire file.
   f = open("demo.txt",'w')
   f.write(This is new line) overwrite 
2. 'a' mode: Append - add at the end
    f.open("demo.txt",'a')
    f.write("This is new line") adds to the end
'''
f = open("demo.txt",'w')
f.write("I wanty to learn Javascript. 123") #overwrite- Purna delete, aB JO PASS HOGA WO LIKH jayega. 
f.close()