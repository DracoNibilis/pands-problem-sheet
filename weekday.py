# Program that outputs whether or not today is a weekday.
# Author: Magdalena Malik

weekendDays = ["Saturday", "Sunday"]
givenDay = input("enter a day: ")
if givenDay in weekendDays:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")