#simple calculator:
# 1. function for operation 
# 2. user input
# 3. print result

#functions for operation
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def avg(num1,num2):
    return (num1 * num2)/2  

#user input
print("Select a operation:\n "\
 "1. Additon\n" \
 "2. Subtraction\n" \
 "3. Multiplication\n" \
 "4. Division\n" \
 "5. Avg\n") 

Select = int(input("Select a operation from: 1,2,3,4,5: "))
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

#print the result
if Select == 1:
    print(number1, "+", number2,"= " , \
          add(number1, number2))

elif Select == 2:
    print(number1, "-", number2,"= " , \
          sub(number1, number2))

elif Select == 3:
    print(number1, "*", number2,"= " , \
          multiply(number1, number2))

elif Select == 4:
    print(number1, "/", number2,"= " , \
          divide(number1, number2))

elif Select == 5:
    print("(",number1, "+", number2, ")", "/", "2", "= " , \
          avg(number1, number2))

else:
    print("Invalid operation! Please select again!")