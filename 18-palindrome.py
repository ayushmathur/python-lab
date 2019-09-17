# Author- Ayuah Mathur
# Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
# "Go hanga salami I'm a lasagna hog.", "Was it a rat I saw?", 
# "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", 
# "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!". 
# Note that punctuation, capitalization, and spacing are usually ignored.
###################################################################################################

phrase=???("Enter the phrase to be checked: ")
phrase=(''.???(e for e in ??? if ???.isalnum())).???()  # Removing spaces, special characters and lowercase all.
rphrase=???(???)                                    # reversing the string
if list(???) == list(???):                           # Checking if reversed string is same as
    print("Entered phrase is a Palindrome")                 # Original and printing appropriate message
else:
    print("Entered phrase is NOT a Plaindrome")