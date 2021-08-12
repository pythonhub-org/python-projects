# This is Fibonacci Number generator progream in Python.
import argparse

def fibonacci_sequence(number):
    numberone = 0
    numbertwo = 1
    i=0
    while i < number:
        numberthree = numberone + numbertwo
        numberone = numbertwo
        numbertwo = numberthree
        i+=1
    print("Fibonacci Number:", numberthree)

def getUserInput():
    parser = argparse.ArgumentParser(description='Fibonacci Sequence')
    parser.add_argument('-n', '--number', type = int, help='Number')
    args = parser.parse_args()
    return args.number

if __name__ == "__main__": 
    number =  getUserInput()
    number = number-1
    if number == 0:
        print("0")
        exit()
    elif number == 1:
        print("1")
        exit()
    fibonacci_sequence(number)
    
