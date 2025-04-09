# Working with files and Strings: Text shaping
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2

# Library imports
import os

# We are asking the user to enter the name of the text document they will use.
# If the user does not enter a name for a text document, we use the "Lorem ipsum.txt" document.
# If the user does not enter a file extension, we add the ".txt" extension to the end of the file name.

userInput = input("Please enter the filename of the text to be formatted\nor Press ENTER to use 'Lorem ipsum.txt':").strip()
if userInput == "":
    userInput = "Lorem ipsum.txt"
if not userInput.endswith(".txt"):
    userInput += ".txt"

# We are asking the user to enter the name or number of the pattern they wish to use.
# If the user enters an incorrect name or number,we repeatedly ask using a While loop until the correct input is provided.

patterns = ["pacman", "circle", "heart", "torus"]
while True:
    print("You can choose between these patterns:\n 0: pacman\n 1: circle\n 2: heart\n 3: torus")
    patternChoice = input("Enter the pattern number or name you want to use: ").strip()

    if patternChoice.isdigit() and 0 <= int(patternChoice) < len(patterns):
        patternChoice = int(patternChoice)
        break
    elif patternChoice.lower() in patterns:
        patternChoice = patterns.index(patternChoice.lower())
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 3 or a pattern name.")

patternFile = f"{patterns[patternChoice]}.txt"

# We are reading the pattern file
with open(patternFile, 'r') as file:
        pattern = file.read()

# Reading and formatting the text file
with open(userInput, 'r') as file:
    textIndex = 0
    formattedText = ""
    for line in pattern.split('\n'):
        for char in line:
            if char in [' ', '\n']:
                formattedText += char
            else:
                text_char = file.read(1)
                while text_char in ['\n', '\r']:
                    text_char = file.read(1)
                if not text_char:
                    file.seek(0)
                    text_char = file.read(1)
                formattedText += text_char
                textIndex = (textIndex + 1) % len(text_char)
        formattedText += '\n'

# Printing the formatted text and saving it to a new file
print(formattedText)
outputFilename = f"{os.path.splitext(userInput)[0]}_{patterns[patternChoice]}.txt"
with open(outputFilename, 'w') as file:
    file.write(formattedText)
print(f"Formatted text written to {outputFilename}")

