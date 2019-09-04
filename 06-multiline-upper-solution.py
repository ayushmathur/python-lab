# Author - Ayush Mathur
# Write a program that accepts sequence of lines as input and prints the lines 
# after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# 
# Hello world
# Practice makes perfect
# 
# Then, the output should be:
# 
# HELLO WORLD
# PRACTICE MAKES PERFECT
##################################################################################

lines = []                      # Creating a list of lines
while True:                     # Initiating loop for taking input
    line = input()              # Taking input from user
    if line:                    # Checking if user has entered any string in input
        lines.append(line)      # If true, append to list of lines
    else:                       # If false, break and exit from loop
        break                   # after all lines are entered
text = '\n'.join(lines)         # creating a string variable combining all the lines entered by the user
print(text.upper())             # printing the text in upper case