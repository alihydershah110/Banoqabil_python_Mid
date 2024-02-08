# -*- coding: utf-8 -*-

Question Number 1
"""

# Arithmetical Operations Program

# Addition
num1_addition = float(input("Enter the first number for addition: "))
num2_addition = float(input("Enter the second number for addition: "))
sum_result = num1_addition + num2_addition

# Division
dividend = float(input("Enter the dividend for division: "))
divisor = float(input("Enter the divisor for division: "))
division_result = dividend / divisor

# Output
print(f"\nSum: {num1_addition} + {num2_addition} = {sum_result}")
print(f"Division: {dividend} / {divisor} = {division_result}")

"""Question no:2"""

# Triangle Area Calculation Program

# Input the length of the base and height of the triangle
base_length = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
triangle_area = 0.5 * base_length * height

# Output
print(f"\nThe area of the triangle is: {triangle_area}")

"""Question No:3"""

# Celsius to Fahrenheit Conversion Program

# Input temperature in Celsius
celsius_temperature = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit_temperature = (celsius_temperature * 9/5) + 32

# Output
print(f"\n{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit")

"""Question No:4"""

# Data Type Demonstration Program

# Integers
number_integer = 19
print(f"The Data Type of {number_integer} is {type(number_integer)}")

# Floats
number_float = 16.5
print(f"The Data Type of {number_float} is {type(number_float)}")

# Strings
your_name = "Your Name"
print(f"The Data Type of {your_name} is {type(your_name)}")

# Booleans
boolean_value = True
print(f"The Data Type of {boolean_value} is {type(boolean_value)}")
