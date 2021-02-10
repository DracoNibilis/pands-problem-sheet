# Program that asks user to input any positive integer 
# and outputs the successive values of the following calculation.
# The Collatz conjecture.
# Author: Magdalena Malik

number = int(input("Please enter a positive integer: "))

print(number, end=" ")

while number != 1: 
    if number % 2 == 0:
        number = number // 2
        print(number, end=" ")
    else:
        number = number * 3 + 1
        print(number, end=" ")
