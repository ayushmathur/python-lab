# Author- Ayush Mathur
# Write a program to accept empno,employee name, Salary,Designation
# write the details into a file empdata.dat in following format
# empno:empname:salary:designation
#####################################################################################

consent='y'
while consent=='y':
    eno=???(???("Enter the employee no: "))                       # Take input of employee data accordingly
    ename=???("Enter the employee name: ")
    esal=???(???("Enter the employee salary: "))
    edesig=???("Enter the employee designation: ")
    ??? ???("empdata.dat","???") as fh:                             # create/open empdata.dat file in append mode
        fh.???(???(???) ??? "???" ??? ??? ??? "???" ??? ???(???) ??? "???" ??? ???)       # write the accpeted data above in the file in given format
        fh.???("???")                                              # append a new line character in the end
    consent=input("Do you want to continue? (y/n): ")