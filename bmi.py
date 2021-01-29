# Program that will calculates somebody's Body Mass Index
# Author: Magdalena Malik

# input height in centimetres and weight in kilograms
height = int(input("Enter weight: "))
weight = int(input("Enter height: "))

# converting height in centimeters into height in meterers
height_m = height / 100

# counting BMI
bmi = weight / height_m**2

#printing result
print("BMI is: {}.".format(bmi))