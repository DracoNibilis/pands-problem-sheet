# A program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Magdalena Malik

num = float(input("Please enter a positive number: "))

def sqrt(num, error=0.1):
    guess = num
    diff = 99999999
    while diff > error:
        newGuess = guess - ((guess**2 - num) / (2*guess))
        diff = newGuess - guess
        if diff < 0:
            diff *= -1 
        
        guess = newGuess
    return guess

print("The square root of {} is approx. {}.".format(num, round(sqrt(num),1)))