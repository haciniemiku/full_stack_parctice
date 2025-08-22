"""
Author: Cao Boyuan
Date: 2025-08-19
Description: Week 2 - Dictionaries Practice
"""

students={
    'laocao':33,
    'xiaosun':77,
    'daxiong':99,
    'xiaoshi':23
}

print(students)
students['laocao']=100
del students['daxiong']
print(students)

for student,score in students.items():
    print(f'{student} has a score of {score}')