# Author- Ayush Mathur
# Write a program to find prime number
############################################################

def is_prime(n):                                            # Creating a function to check if number is prime 
        status = True                                       # initializing boolian variable to store info if number is prime or not
        if n < 2:                                           # if number is less than 2 then it is not a prime
            status = False
        else:
            for i in range(2,n):                            # loop to traverse through numbers till input number
                if n % i == 0:                              # calculatig if input number is totally divisible by current number in loop
                    status = False                          # if it is divisible, then its not a prime. Setting status
        return status                                       # function returns final value of status 
number=input("Enter a number to check if it is Prime: ")    # Asking user to input a number to check if its a prime
if is_prime(int(number)):                                   # calling the function to check if input number is prime
    print(number + " is a prime number")                    # if true, print output accordingly
else:
    print(number + " is NOT a prime number")                # if false, print output accordingly
