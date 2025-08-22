"""
Author: Cao Boyuan
Date: 2025-08-19
Description: Week 2 -  Sets Practice
"""

numbers={1,1,4,5,1,4}
age={1,2,3,4,5,6,7,}
print(numbers)
numbers.add(6)
numbers.add((19,19))
print(numbers)
numbers.remove((19,19))
print(numbers)
a=numbers&age
b=numbers|age
print(a,b)