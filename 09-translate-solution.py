# Author- Ayush Mathur
"""Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between. 
For example, translate("this is fun") should return the string "tothohisosisosfofunon"."""
######################################################################################################################

def translate(inpstr):                              # Creating translate function that accepts a string as input
    alphabets = '''abcdefghijklmnopqrstuvwxyz'''    # Creating a variable with all the alphabets
    no_punct = ""                                   # initiating a variable that will contain string with no punctuations
    for char in inpstr.lower():                     # creating loop to traverse input string
        if char in alphabets:                       # checking if the current character is an alphabet 
            no_punct += char                        # if true append it to the string with no punctuations
    vowels="""aeiou"""                              # creating a string with all the vowels
    FinalStr=''                                     # initiating the final string that will contain translated text
    for r in no_punct:                              # creating a loop to traverse through string with no punctuation
        if r not in vowels:                         # checking if currect character is a consonent 
            FinalStr+=r+"o"+r                       # if its consonent then add it to final string 
                                                    # by doubling it and placing an o in between
        else:
            FinalStr+=r                             # else if it is vowel, add it to final string as is
    return FinalStr                                 # the function will return final translated string

my_str=input("Enter the string to tranlate: ")      # asking user for string to translate
print (translate(my_str))                           # Printing the output of translate function with user entered string as input