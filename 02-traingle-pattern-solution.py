# Author - Ayush Mathur
# Print the pattern
#    1
#   234
#  56789
# 10111213141516
#########################################################

num=1                               # numbers to be printed initiated with 1
rows=4                              # total number of rows to be printed
theta=2                             # range denoter for loop to print numbers
for x in range(rows):               # Loop to print rows
    print(" "*(rows-x-1),end="")    # Printing spaces which is total rows less number of row less 1
    for y in range(1,theta):        # Loop to print numbers two times more than ones in last row
        print(num,end="")           # print current number
        num+=1                      # incrementing number
    print("\r")                     # printing line break
    theta+=2                        # incrementing range for loop two times