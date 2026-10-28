# 3. Match case conditional statements :-
# Matching the user input to different statements. 
num1 = int(input("Enter the first Number:"))
num2 = int(input("Enter the second Number:"))
operator = input("Enter operator")
 
match operator :
    case "+":
        print("sum is:", num1 + num2)
    case "-":
        print("diff is:", num1 - num2)
    case "*":
        print("Multiply is:", num1 * num2)
    case "/":
        print("Divide is:", num1 / num2)
    case _ :
        print("Enter a valid operator")

                