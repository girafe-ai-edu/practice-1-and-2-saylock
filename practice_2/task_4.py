# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
number = input("please input a 4-digit number: ") # asking a user for a 4-digits number, number is a string

sum_ = 0  # creating variable sum_ ["_" is needed because just "sum" is already existing in python as a function]

for digit in number:  # creating variable "digit" for putting in it all digits in order they are appearing in number
    sum_ += int(digit)  # adding each digit to "sum_"

print(f"the sum of the digits in your number is: {sum_}")
