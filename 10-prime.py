# Author- Ayush Mathur
# Write a program to find prime number
############################################################

def is_prime(n):                                            # Creating a function to check if number is prime 
        status = ???                                       # initializing boolian variable to denote result. The number is prime by default
        if n < ???:                                           # if number is less than 2 then it is not a prime
            status = ???
        else:
            for i in range(???,???):                            # loop to traverse through numbers till input number
                if n ??? i == ???:                              # calculatig if input number is totally divisible by current number in loop
                    status = ???                          # if it is divisible, then its not a prime. Setting status
        return ???                                       # function returns final value of status 
number=input("Enter a number to check if it is Prime: ")    # Asking user to input a number to check if its a prime
if is_prime(int(???)):                                   # calling the function to check if input number is prime
    print(number + " is ??? a prime number")                    # if true, print output accordingly
else:
    print(number + " is ??? a prime number")                # if false, print output accordingly