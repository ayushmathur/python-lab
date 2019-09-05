# Author- Ayush Mathur
"""Write a program that contains a function that has one parameter, n, representing an integer greater
than 0. The function should return n! (n factorial). Then write a main function that calls this function with
the values 1 through 20, one at a time, printing the returned results. This is what your output should look
like:
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 3628800 """
#################################################################################################################

def factorial(???):                               # Function to find factorial of any number n
    r=???                                         # initializing a variable of intiger type to store factorial
    if n <= ???:                                  # if number is 0, factorial is 0
        return ???                                # return 0
    else:                                       # if number is grater than 0
        for x in range(???,???):                # initiate loop that traverse through numbers from 1 to input number n
            r = ???                              # each number is multiplied to previous result and stored in same variable for next loop
    return r                                    # return final factorial value

def main():                                     # Main function to find factorial of numbers 0-20
    for x in range(???,???):                       # creating a loop to traverse number from 1 to 20
        print(???+???+???)     # in each loop print number and its factorial returned from factorial function

main(???)                                          # calling main function to start program