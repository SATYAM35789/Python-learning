# Elif can be used multiple times
# Question:4 Take input percentage of a student and print the grade according to marks
# a. 81-100 very good
# b. 61-80  good 
# c. 41-60 Average
# d. <=40  fail
percentage = float(input("Enter the percenage of student :"))
if percentage >= 81 :
    print("Very Good")
elif percentage >= 61:
    print("good")
elif percentage >= 41 :
    print("average")
else:
    print("Fail")

