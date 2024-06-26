import time
import re
import source.datastore as configures
import source.commands as commands

error = False

# this function extracts the name of the file from the filepath
def getFileName(filePath):
    # turning the file path into a raw string
    raw_filePath = repr(filePath)[1:-1]
    # instead of if elsing to select the the of slash in the text, just seperate the text by 2 delimiters 
    pattern = '|'.join(map(re.escape, "\/"))
    # patern = r'\\|/'
    # pattern = r'[\\/]'
    extracted_filepath = re.split(pattern, raw_filePath)[-1]
    return extracted_filepath.split(".")[0]

# this function takes the entire code file and seperates it into different lines of code
def seperateIntoLines(text):
    lines = []
    #lineNumber = 0
    line = ''
    charCount = 0
    # reading each character from the code
    for char in text:   
        # if its a new line the line is added to the lines list
        if char == '\n':
            lines.append(line)
            line = ''
        # if char is equal to the ending character and the character count also the same with the length of the text - 1 indicating the index of the last character, this line is also added
        elif char == text[-1] and charCount == len(text) - 1:
            lines.append(line)
            line = ''
        # otherwise the char is added to the line
        else:
            line += char
        charCount += 1
    return lines

# remove white spaces from the code line
def removeWhitespace(lines):
    for line in range(len(lines)):
        # lstrip will remove all the white spaces in front of the line whether it is tab or whitespace 
        lines[line] = lines[line].lstrip()
    return lines

# taking in file path
# fileInPath = input("Please enter the filepath where your pseudocode is stored: ")
fileInPath = "D:/Code/Python/Pseudocode compiler/text.txt"

# reading the pseudocode text file 
with open(fileInPath, "r") as file:
    read = file.read()

linesW = seperateIntoLines(read)
linesNW = removeWhitespace(linesW)

programObject = []

for index in range(len(linesNW)):
    splitedLine = linesNW[index].split()

    if linesNW[index][:6] == "OUTPUT" or linesNW[index][:5] == "PRINT":
        print("OUTPUT detected")
        programObject.append(commands.OUTPUT(index, index, index, linesW[index]))
        
    elif "=" == splitedLine[1]:
        print("ASSIGN detected")
        programObject.append(commands.ASSIGN(index, index, index, linesW[index]))
        
    programObject[index].run()
