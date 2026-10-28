''' 
File i/o in python 
Python can be used to perform operations on a file. (Read and write)
Types of all files:
1. Text files: .txt, .docx, .log etc ( Data store in character form)
2. Binary Files :- .mp4, .mov, .png, .jpeg etc. ( Data may store in video, audio form)
Note:- All the data in text file or Binary file stored in memory in Bits (0 and 1)
Ram : Random acces memory . Which is fast in our system. When the code run the variable created of the program is 
Ram . But Ram is volatile. Volatile : data erazed when system close. Permanantly not stored.
To store the data permanantly we use files handling. (SSD,)

Opertion
1. Opening a file
We have to open a file before reading or writing. Parameter may in "" or '' quates
f = open("file_name","mode")   file name = simple.txt  mode= r readmode
 default case of mode is r (read mode)

'r' = open for reading (default)
'w' = Open for writing, truncating the file first (pahle jo bhi kilha hoga wo delete ho jayega)
'x' = Create a new file and open it for writing
'a' = Open for writing, jo bhi likha hoga uske aage se likh dega. 
'b'= binary mode (open)
't' = text mode(default) want to open text file. 
'+' = open a disk file for updating (reading and file )

Note:- If file not present then it automatically create the file. Go to stckover flow website for modes understanding 
'''
f = open("demo.txt","r")  
''' if not present in the same file than pass complete path'''
data = f.read()
print(data)
print(type(data))
f.close()