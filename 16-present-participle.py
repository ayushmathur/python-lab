# Author- Ayush Mathur
""" In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A simple set
of heuristic rules can be given as follows:
•If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
•If the verb ends in ie like die, change ie to y and add ing
•For  words consisting of consonant-vowel-consonant like fit , double the final letter before adding ing
•By default just add ing like read
Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
returns its present participle form. Test your function with words such as lie, see, move and hug """
###################################################################################################################

import ???                                       # importing regular expression library
def make_ing_form(string):                      # creating function that takes one input string
    if string[???]=='???' and string[???]=='???':     # if sting is ending with ie
        ans=???.???('???','???',???)         # replace ie in end by ying
        print(???)                              # print final string
    elif string[???]=='???' and string[???]!='???':   # if string ends with e but not ee
        ans=???.???('???','???',???)           # replace e in end by ing
        print(???)                              # print final string
    elif ???.???(r'[???][???][???]$',???):  # if string has consonent vowel consonent fit
        ??? += ???[???]+'ing'              # concatenate string with its last letter and 'ing'
        print(???)                           # print final string
    else:                                       # if none of the condition is matched
        ans=???+'???'                        # concatenate string with 'ing'
        print(???)                              # print final string
strng="hug"                                     # string variable with value as input word
make_ing_form(???)                            # calling the function created above