# Write a program that asks a user to input a string and outputs every second letter in reverse order. 
# Author: Magdalena Malik

#input for text
text = input("Please enter a sentence: ")

reversed_text = text[::-1] # reversed given text
every_second_letter = reversed_text[::2] # select every second letter from the reversed text

print(every_second_letter) 