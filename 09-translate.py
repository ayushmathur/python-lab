# Author- Ayush Mathur
"""Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between. 
For example, translate("this is fun") should return the string "tothohisosisosfofunon"."""
######################################################################################################################

def translate(???):                              # Creating translate function that accepts a string as input
    alphabets = '''???'''    # Creating a variable with all the alphabets
    no_punct = ""                                   # initiating a variable that will contain string with no punctuations
    for char in ???:                     # creating loop to traverse input string
        if char in ???:                       # checking if the current character is an alphabet 
            no_punct += ???                        # if true append it to the string with no punctuations
    vowels="""???"""                              # creating a string with all the vowels
    FinalStr='???'                                     # initiating the final string that will contain translated text
    for r in ???:                              # creating a loop to traverse through string with no punctuation
        if r not in ???:                         # checking if currect character is a consonent 
            FinalStr+=???                       # if its consonent then add it to final string 
                                                    # by doubling it and placing an o in between
        else:
            FinalStr+=???                             # else if it is vowel, add it to final string as is
    return ???                                 # the function will return final translated string

my_str=input("Enter the string to tranlate: ")      # asking user for string to translate
print (???(???))                           # Printing the output of translate function with user entered string as input