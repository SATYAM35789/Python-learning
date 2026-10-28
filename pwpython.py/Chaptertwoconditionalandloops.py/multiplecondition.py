# Multiple conditions using 'and' and 'or'
# Logical operator which help us to combine the result of two conditions 
#Question:1
eng_marks = int(input("Enter the english marks:"))
hindi_marks = int(input("Enter the Hindi marks:"))

# If both marks are more than 80, then print A grade
if hindi_marks > 80 and eng_marks > 80 :
    print("A grade")

# If either of condition is true than print B Grade
elif hindi_marks > 80 or eng_marks > 80 :
    print("B grade")

else: 
    print("C Grade")