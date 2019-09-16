# Author- Ayuah Mathur
# Write another program to read contents from the file empdata.dat
# If designation is 
# a)	Manager- then add bonus=2000 in the salary and display on the screen
# b)	Analyst- then add bonus=1500 in the salary
# c)	otherwise add bonus=1000 in the salary
#######################################################################################

with open("empdata.dat") as fh:                     # Open thr data file in default mode
    for line in fh:                                 # create a for loop to traverse all the lines in data file
        line=line.rstrip()                          # remove all trailing new line characters or extra spaces in current line
        spli=line.split(":")                        # create a list of data in the line seperated by ':'
        if spli[3].lower()=='manager':              # check if the designation field is 'manager' in lower case
            bonus=int(spli[2])+2000                 # if true, add 2000 in salary feild and save it in a seperate variable
        elif spli[3].lower()=='analyst':            # check if the designation field is 'analyst' in lower case
            bonus=int(spli[2])+1500                 # if true, add 1500 in salary feild and save it in a seperate variable
        else:                                       # else if none of the above is true
            bonus=int(spli[2])+1000                 # add 1000 in salary feild and save it in a seperate variable
        print("The bonus added salary for employee "+spli[1]+" is ",bonus)  # print the new salary 