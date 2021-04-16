# Program that asks user to input any positive integer 
# and outputs the successive values of the following calculation.
# The Collatz conjecture.
# Author: Magdalena Malik

#input for positive number
number = int(input("Please enter a positive integer: "))

print(number, end=" ")

# while loop when number is not 1
while number != 1: 
    if number % 2 == 0: # while number is even 
        number = number // 2
        print(number, end=" ")
    else: # while number is odd
        number = number * 3 + 1
        print(number, end=" ")
