"""
Author: Cao Boyuan
Date: 2025-08-18
Description: Week 2 -  Functions Practice
"""

def cacualte_average(numbers):
    return sum(numbers)/len(numbers)

def find_max(numbers):
    return max(numbers)

numbers = [10, 20, 30, 40, 50]
print("Average:", cacualte_average(numbers))
print("Max:", find_max(numbers))