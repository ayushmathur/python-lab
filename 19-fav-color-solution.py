# Author- Ayuah Mathur
""" Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
1. Find out how many students are in the list
2. Change Lisa’s favourite colour
3. Remove 'Jenny' and her favourite colour
4. Sort and print students and their favourite colours alphabetically by name"""
########################################################################################

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print("Total number of students in the list: " + str(len(people)))
people['Lisa']='Red'
print("Lisa's favourite color is now changed to Red\n" + str(people))
del people['Jenny']
print("Entry of Jenny is removed\n" + str(people))
print("Sorted students: ")
for x in sorted(people):
    print(x+":" +people[x])