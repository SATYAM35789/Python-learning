# string
name = "satyam"

# Integer 
roll_number = 23

# Floating number
percentage = 95.5

# boolean 
is_student = True

print(name, roll_number, percentage, is_student )

# updating the value
percentage = 93
print(name, roll_number, percentage, is_student)

# checking the type of variable
print(type(name))
print(type(roll_number))
print(type(percentage))
print(type(is_student))

# concanating 
# about your self
# same datatypes then we can use + operator if different then use comma (,)
print("My name is" + name + "and my roll number is " , roll_number)
print("i scord", percentage, "%in my final exam . I am a student is" , is_student)

# print expression
print("My percentage has changed to", percentage -1.0)

# print with seperator 
print(name, roll_number, percentage, is_student ,sep=("-") )
x=1
y=2
z=3
print(x,y,z,sep="->")
