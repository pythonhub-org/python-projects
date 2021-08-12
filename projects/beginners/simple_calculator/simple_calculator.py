# This is a calculator program
# This program does +, -, *, / operations

# This function takes user inputs and calculates final answer accordingly. 
def calculator(number1, number2, operation):
    value = 0
    if operation == "+":
        value = (number1 + number2)
    elif operation == "-":
        value = (number1 - number2)
    elif operation == "*":
        value = (number1 * number2)
    elif operation == "/":
        value = (number1/number2)
    else:
        print("Invalid Input")
    
    return value

# Code Execution begins here
if __name__ == "__main__":

    print("This program does +, -, *, / operations")
    number1 = float(input("Enter your first number:"))
    number2 = float(input("Enter your second number:"))
    operation = input("Enter a operation you want to do(+,-,*,/,): ")

    value = calculator(number1, number2, operation)
    print(number1, operation, number2, " = ", value)