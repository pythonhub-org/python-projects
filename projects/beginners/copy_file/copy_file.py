# This program copies text from one file to another.

# Takes user input and copies text to other file.
def copyFile():
    try:
        fileone = input("Enter your first txt file: ")
        filetwo = input("Enter your second txt file: ")
        firstfile = open(fileone, 'r')
        secondfile = open(filetwo, 'a')        
    except FileNotFoundError:
        print("File doesn't exist. ")
    
    # read content from first file
    for line in firstfile:
        secondfile.write(line)  # append content to second file

# code execution starts here
if __name__ == "__main__":
    copyFile()
