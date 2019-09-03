#Q.1. Write a program that asks the user how many days are in a particular month, and what 
#day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that month.
#For example, here is the output for a 30 day month that begins on day 4 (Thursday):
#S  M  T  W  T  F  S
#            1  2  3
#4  5  6  7  8  9  10
#11 12 13 14 15 16 17
#18 19 20 21 22 23 24
#25 26 27 28 29 30
#################################################################################################
dy = int(input('Enter the days in the month: '))
sdy = int(input('Enter the first day : '))
#Buffer to track characters used in the column. 
#It is initialized to amount used by cursor before it prints the first date
ctr = ((sdy)*3) 
print('S  M  T  W  T  F  S') #Print days header
print(" "*sdy*3, end="")   #Print spaces to the place where first date is printed
for dt in range(1,10):           #Loop to print dates 1-9
    print(dt,end="  ")        #print date and 2 spaces
    ctr+=3
    if ctr >= 19:                  #Check if workspace is exhausted and go to next line
        print("\n")
        ctr=0
for dt in range(10,dy+1):       #Loop to print dates 10 onwards
    print(dt,end=" ")         #print date and 1 space
    ctr+=3                         #Rest of loop is same as last one
    if ctr >= 19:
        print("\n")
        ctr=0
print("\n")