"""
Author: Cao Boyuan
Date: 2025-08-19
Description: Week 2 -  Lists Practice
"""

# 1. Create a list of numbers from 1 to 10
numbers=[i for i in range(1,11)]
print(f'the first number is {numbers[0]}')
print(f'the last number is {numbers[-1]}')
numbers.append(11)
numbers.insert(11,12)
for i in numbers:
    print(i, end=' ')
print()
print(numbers.pop())
numbers.remove(11)
for i in numbers:
    print(i, end=' ')
