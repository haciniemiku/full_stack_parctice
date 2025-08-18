"""
Author: Your Name
Date: 2025-08-18
Description:  Python Loops Practice
Tasks:
1. Sum numbers from 1 to 100
2. Print all even numbers from 1 to 100
3. Continuously ask the user to enter numbers until 0 is entered, then display the total sum
"""

# Task 1: Sum numbers from 1 to 100
total_sum=0
for i in range(1,101):
    total_sum+=i
print("Sum of numbers from 1 to 100 is:", total_sum)    

# Task 2: Print all even numbers from 1 to 100
total_sum=0
for i in range(1,101):
    if i%2==0:
        total_sum+=i
print("Even numbers from 1 to 100 are:",total_sum)

# Task 3: Continuously ask the user to enter numbers until 0 is entered, then display the total sum

total_sum = 0  # Reset for the next task
while True:
    user_input=int(input("Enter a number (0 to stop): "))
    if user_input == 0:
        break
    total_sum += user_input
print("Total sum of entered numbers is:", total_sum)
