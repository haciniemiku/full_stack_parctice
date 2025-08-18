"""
Author: Cao Boyuan
Date: 2025-08-18
Description:  Python Conditional Statements Practice
Tasks:
1. Check if an integer is positive or negative
2. Determine whether a year is a leap year
3. Find the maximum of three numbers
"""

# Task 1: Check if an integer is positive or negative

num=int(input("Enter an integer: "))
if num > 0:
    print(f"{num} is a positive integer.")
elif num < 0:
    print(f"{num} is a negative integer.")
else:
    print("The integer is zero.")

# Task 2: Determine whether a year is a leap year
year = int(input("Enter a year: "))
if (year%4 ==0 and year%100!=0) or (year %400 ==0 ):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Task 3: Find the maximum of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
maxium = a  # Assume a is the maximum initially
if b > maxium:
    maxium = b
if c > maxium:
    maxium = c
print(f"The maximum of {a}, {b}, and {c} is {maxium}.")