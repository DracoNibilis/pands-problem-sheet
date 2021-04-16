# Program that outputs whether or not today is a weekday.
# Author: Magdalena Malik

#list with weekend days
weekendDays = ["Saturday", "Sunday"]

#input for day
givenDay = input("enter a day: ")

#if statement that checking if day is weekday or weekend
if givenDay in weekendDays:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")