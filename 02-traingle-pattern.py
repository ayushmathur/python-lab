# Author - Ayush Mathur
# Print the pattern
#    1
#   234
#  56789
# 10111213141516
#########################################################

num=???                               # numbers to be printed initiated with 1
rows=???                              # total number of rows to be printed
theta=???                             # range denoter for loop to print numbers
for x in range(???):               # Loop to print rows
    print(" "*(???-???-1),end="")    # Printing spaces which is total rows less number of row less 1
    for y in range(1,???):        # Loop to print numbers two times more than ones in last row
        print(???,end="")           # print current number
        num+=???                      # incrementing number
    print("\r")                     # printing line break
    theta+=???                        # incrementing range for loop two times