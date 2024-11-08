# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 7 
x += 3
# TODO: Multiply y by 2 using the *= operator
y = 2 
y *= 2
# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y 
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 10
b = 5

if a > b :
    print("a is greater than b")
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
modulus = b%2

if modulus == 0:
    print("b is even")
else:
    print("b is odd")
# TODO: Create a condition that checks if c is less than or equal to a
a = 10
c = 4
print(c<=a)
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
a=10
b=5
c=4
final_condition = (a>b) or (modulus==0) and (c<=a)
# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("What is your test score between 0-100"))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score>59 :
    print ("D")
elif score >69:
    print("C")
elif score > 79:
    print("B")
elif score >89 :
    print("A")
else:
    print ("F")




# TODO: Print the grade for the given score
print(score)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1=int(input("Put in a number"))
num2=int(input("Put in a different number"))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation=input("Insert a operation sign (+, -, *, /)")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+": 
    result=num1 + num2
elif operation == "-":
    result=num1 - num2
elif operation == "*":
    result=num1 * num2
elif operation == "/":
    if num2 == 0 and operation == "/":
        print("This not acceptable")
    else:
        result=num1 / num2
# TODO: Handle the case of division by zero   
else:
    print ("Condition is not met ")
# TODO: Print the result of the operation
if num2 !=0:
    print(result)
