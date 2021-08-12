# This program copies lines with specified keyword from one file to another.

# Takes user input and copies text to other file.
def copyFile():
    try:
        fileone = input("Enter your first txt file: ")
        filetwo = input("Enter your second txt file: ")
        texttocopy = input("What text are you looking for in your file?")
        firstfile = open(fileone, 'r')
        secondfile = open(filetwo, 'w')
    except FileNotFoundError:
        print("File doesn't exist. ")
    
    # read content from first file
    for line in firstfile:
        if texttocopy in line: 
            secondfile.write(line)  # append content to second file
            print(line)

# code execution starts here
if __name__ == "__main__":
    copyFile()


