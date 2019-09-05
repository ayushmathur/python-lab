#Author- Ayush Mathur
"""Define a function overlapping() that takes two lists and returns True 
if they have at least one member in common, False otherwise."""
###############################################################################################

def overlapping(x,y):
    for n in x:             # Iterating first list
        for m in y:         # Iterating second list
            if n == m:      # Comparing the values if they are equal
                return True
    return False

alist=[1,2,3,4,5,6]
blist=[7,8,9,0]
print(overlapping(alist,blist))