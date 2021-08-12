# This program counts the vowels in a string.

# Takes user input and counts vowels.
def countVowels():
    data = str(input("Please type a sentence: "))
    vowels = "aeiou"
    for v in vowels:
        print(v, data.lower().count(v))

#Code Execution Begins
if __name__ == "__main__":
    countVowels()
