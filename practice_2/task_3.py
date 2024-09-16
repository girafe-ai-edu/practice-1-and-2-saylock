# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2
"""

weight = input("your weight in kg: ")
height = input("your height in m: ")

# code here

BMI = float(weight) / float(height) ** 2  # adding "float" to w & h to make them float numbers because the input always returns the string

print(f"your Body Mass Index is {round(BMI, 2)}")  # using f-string to format message (same thing as (str(variable) + "message"))

if BMI <= 20:
    print("you have to eat more fastfood")  # just adding some contex to faceless numbers (aka BMI)

elif 20 < BMI <= 25:
    print("way to go, man!")

else:
    print("you should not wear tight jeans")
