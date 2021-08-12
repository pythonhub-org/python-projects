# This is quadratic formula calculator
# ax^2 + bx + c = 0

# Using Math module for square roots
import math

# Takes user input and calculates solution(s)
def quadratic_eq_calculator():
    a = float(input("Enter A Value: "))
    b = float(input("Enter B Value: "))
    c = float(input("Enter C Value: "))
    try: 
        print(f"Quadratic Equation: {a}x^2 + {b}x + {c} = 0")
        print ("Solution 1: ", (-b + math.sqrt(b**2 - 4 * a * c))/ 2 * a)
        print ("Solution 2: ", (-b - math.sqrt(b**2 - 4 * a * c))/ 2 * a)
    except ValueError:
        print ("No solutions.")

# Code Execution begins
if __name__ == "__main__":
    print("This is a quadratic equation calculator")
    print("ax^2 + bx + c = 0")
    quadratic_eq_calculator()