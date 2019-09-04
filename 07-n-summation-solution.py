# Author - Ayush Mathur
# Write a program to print n number summation.
##################################################################################

n = int(input("Enter the value of n : "))                   # Taking the value of n as input from user
summation=0                                                 # initializing the variable for final summation of values
for x in range(n+1):                                        # loop to traverse through numbers till number n
    summation += x                                          # incrimenting the value of summation with current value of loop
print("The summation of n numbers is : " + str(summation))  # Printing the final value of sum