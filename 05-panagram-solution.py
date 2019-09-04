# Author- Ayush Mathur
# A pangram is a sentence that contains all the letters of the English alphabet at least once. 
# example: The quick brown fox jumps over the lazy dog.
# Your task here is to write a function to check a sentence to see if it is a pangram or not
#################################################################################################
def pangram(x):     
    """Function to check pangram
     Converting the string into a set and subtracting it from the set of alphabets.
     If it gives a null set i.e. a set of length Zero then its a pangram.
     It returns true if condition matches else returns false."""
    if len(set("abcdefghijklmnopqrstuvwxyz")-set(x.lower()))==0:
        return True
    return False


phrase=input("Enter the phrase to be checked: ")        # Taking input from user
if pangram(phrase):                                     # Calling the above function with input phrase and if check
    print("The phrase is a Pangram")                    # Print results accordingly
else:
    print("The phrase is not a Pangram")