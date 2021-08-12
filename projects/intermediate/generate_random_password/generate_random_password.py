# This program generates a random password.
import random
import argparse



def generatePassword(passwordlength):
    passstring = ""
    i=0
    while i < passwordlength:
        character = random.choice(["letter","number","specialchar"])
        if character == "letter":
            randomletter = random.choice("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
            passstring = passstring + randomletter
        elif character == "specialchar":
            randomcharacter = random.choice("!@#$%&*")
            passstring = passstring + str(randomcharacter)
        else:
            randomnumber = random.randint(0,9)
            passstring = passstring + str(randomnumber)
        i+=1
    print(passstring) 

def getUserInput():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-passwordlength', type = int, help='Description for foo argument')
    args = parser.parse_args()
    return args.passwordlength

if __name__ == "__main__": 
    passwordlength =  getUserInput()
    generatePassword(passwordlength)
