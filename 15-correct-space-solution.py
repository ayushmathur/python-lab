# Author- Ayush Mathur
"""Define a simple "spelling correction" function correct() that takes a string and sees to it that
1) two or more occurrences of the space character is compressed into one, and
2) inserts an extra space after a period if the period is directly followed by a letter.
e.g. correct("This is very funny and cool.Indeed!") should return "This is very funny and cool. Indeed!" """
################################################################################################################

import re                               # importing regular expression module
def correct(string):                    # creating a function to correct the input string
    dot=re.sub(r'\.','. ',string)       # regular expression to add a space after a dor (.) wherever required
    sq=re.sub(r' +',' ',dot)            # regular expression to remove extra spaces after a single space has occured
    return sq                           # returining final corrected string
   
strng="Do not     go gentle into that    good night.Rage,rage  against  the   dying of light. Goodbye!"
print(correct(strng))                   # printing correct string