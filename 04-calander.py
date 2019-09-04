# Author - Ayush Mathur
# Write a program that asks the user how many days are in a particular month, and what 
# day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that month.
# For example, here is the output for a 30 day month that begins on day 4 (Thursday):
# S  M  T  W  T  F  S
#             1  2  3
# 4  5  6  7  8  9  10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30
#################################################################################################
dy = int(input('Enter the days in the month: '))
sdy = int(input('Enter the first day : '))
#Controller to track characters used in the column. 
#It is initialized to amount used by cursor before it prints the first date
ctr = ???
print('S  M  T  W  T  F  S') #Print days header
print(???, end=???)   #Print spaces to the place where first date is printed
for dt in range(???,???):           #Loop to print dates 1-9
    print(???,end=???)        #print date and 2 spaces
    ctr+=???                  #increment the controller
    if ctr >= ???:                  #Check if workspace is exhausted and go to next line
        print("\n")
        ctr=???                     #Reset controller
for dt in range(???,???):       #Loop to print dates 10 onwards
    print(???,end=???)         #print date and 1 space
    ctr+=???                         #Rest of loop is same as last one
    if ctr >= ???:
        print("\n")
        ctr=???
print("\n")