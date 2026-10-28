'''
Reading  a file :- 
data= f.read() // reads entire file
data = f.readline()  reads one line at a time
'''
f = open("demo.txt", "r")
'''data = f.read(5)
print(data) 
note if once read the file than imaginary pinter(cursor) at the end we have nothing to read next to see this remove the 
comment from above code 
'''


line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()