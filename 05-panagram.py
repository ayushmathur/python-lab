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
    if len(set("???")-set(x.lower()))==???:
        return ???
    return ???


phrase=input("Enter the phrase to be checked: ")        # Taking input from user
if pangram(???):                                     # Calling the above function with input phrase and if check
    print("???")                    # Print results accordingly
else:
    print("???")