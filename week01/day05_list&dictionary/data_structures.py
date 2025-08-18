"""
Author: Cao Boyuan
Date: 2025-08-18
Description:  Python Lists & Dictionaries Practice
Tasks:
1. Find max and min values in a list
2. Remove duplicates from a list
3. Count character frequency in a string using a dictionary
"""

# Task 1: Find max and min values in a list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_value = max(numbers)
min_value=min(numbers)
print(f'Max value: {max_value}, Min value: {min_value}')

# Task 2: Remove duplicates from a list
unique_numbers=set(numbers)
print(f'Unique numbers: {unique_numbers}')

# Task 3: Count character frequency in a string using a dictionary
text = "hello world"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(f'Character frequency: {frequency}')