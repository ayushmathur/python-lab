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

import re                                       # importing regular expression library
def make_ing_form(string):                      # creating function that takes one input string
    if string[-2]=='i' and string[-1]=='e':     # if sting is ending with ie
        ans=re.sub('ie$','ying',string)         # replace ie in end by ying
        print(ans)                              # print final string
    elif string[-1]=='e' and string[-2]!='e':   # if string ends with e but not ee
        ans=re.sub('e$','ing',string)           # replace e in end by ing
        print(ans)                              # print final string
    elif re.match(r'[^aeiou][aeiou][^aeiou]$',string):  # if string has consonent vowel consonent fit
        string += string[-1]+'ing'              # concatenate string with its last letter and 'ing'
        print(string)                           # print final string
    else:                                       # if none of the condition is matched
        ans=string+'ing'                        # concatenate string with 'ing'
        print(ans)                              # print final string
strng="hug"                                     # string variable with value as input word
make_ing_form(strng)                            # calling the function created above