# Author- Ayush Mathur
# Write a program to accept empno,employee name, Salary,Designation
# write the details into a file empdata.dat in following format
# empno:empname:salary:designation
#####################################################################################

fh = open("empdata.dat","a")                                # create/open empdata.dat file in append mode
consent='y'                                                 # create a variable to store user's choice with default as yes
while consent=='y':                                         # create a loop which will 
    eno=int(input("Enter the employee no: "))               # Take input of employee data accordingly
    ename=input("Enter the employee name: ")
    esal=int(input("Enter the employee salary: "))
    edesig=input("Enter the employee designation: ")
    fh.write(str(eno)+":"+ename+":"+str(esal)+":"+edesig)   # write the accpeted data above in the file in given format
    fh.write("\n")                                          # append a new line character in the end
    consent=input("Do you want to continue? (y/n): ")       # Ask user if they want to continue and change value of variable declared at start
fh.close()                                                  # Close the file