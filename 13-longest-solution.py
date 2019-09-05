# Author- Ayush Mathur
"""Write a function find_longest_word() that takes a list of words and returns the 
length of the longest one."""
###############################################################################################
def find_longest_word(x):                           # creating the function to find longest word
    length=0                                        # initiatlizing intiger variable to store max length
    for n in x:                                     # creating a loop to traverse through list of words passed as input
        if length < len(n):                         # if the variable soring max length has value smaller than lenght of
                                                    # current word of list in loop, 
            length=len(n)                           # then update max length as length of current word
    return length                                   # return final value of max length

given=['hello','i','am','robot','somuchfunitis']    # creating a list of words
print(find_longest_word(given))                     # passing list as parameter to above function and printing max length