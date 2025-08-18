"""
Author: Cao Boyuan
Date: 2025-08-18
Description: Python Functions & Git Practice
Tasks:
1. Functions to calculate average and maximum of a list
2. Refactor simple calculator into functions
3. Upload code to GitHub
"""

#1. Function to calculate average and maximum of a list
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

def calculate_maximum(numbers):
    """Calculate the maximum of a list of numbers."""
    if not numbers:
        return None
    return max(numbers)

# Example usage
if __name__ == "__main__":
    sample_numbers = [10, 20, 30, 40, 50]
    average = calculate_average(sample_numbers)
    maximum = calculate_maximum(sample_numbers)
    
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
#2. Refactor simple calculator into functions
def calculator(num1,num2,operation):
    """Perform basic arithmetic operations."""
    if operation=='add':
        return num1 + num2
    elif operation=='subtract':
        return num1-num2
    elif operation=='multiply':
        return num1 * num2
    elif operation=='divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# Example usage of calculator function
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    operation = 'add'
    
    result = calculator(num1, num2, operation)
    print(f"Result of {operation} between {num1} and {num2}: {result}")

