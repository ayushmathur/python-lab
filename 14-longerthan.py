# Author- Ayush Mathur
"""Write a function filter_long_words() that takes a list of words and an integer n 
and returns the list of words that are longer than n"""
################################################################################################

def filter_long_words(???,???):                     # creating required funtion with two parameters, a list and an intiger number
    longerwords=[???]                                  # creating an empty list to store final list of desired words
    for x in ???:                                 # traversing the list of words in a for loop
        if len(x) ??? ???:                              # checking if current word meets the requirement
            longerwords.???(???)                   # if it does, save it to final list
    return ???                              # return final list of words with length longer than required number

given=['hello','i','am','robot','somuchfunitis']    # creating a list of words to check
print(???(???,???))                   # calling above function with a list and a number as parameter and printing results