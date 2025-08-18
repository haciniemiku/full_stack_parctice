'''
Author:Cao Boyuan
Date:2025-08-18
Descrption:Python Basic Operations & Input/Output Practice
Tasks:
1. Simple Calculator
2. Even/Odd Check
3. Exponentiation (Square & Cube)

'''

#1.Simple Calculator
num1=float(input('Enter first number: '))
num2=float(input('Enter second number: '))
sum=num1 + num2
diff=num1 - num2
prod=num1 * num2
quot=num1/num2 if num2!=0 else 'undefined'
print(f'Sum: {sum}')
print(f'Difference: {diff}')
print(f'Product: {prod}')
print(f'Quotient: {quot}' )



#2.Check if a number is even or odd
num=int(input('Enter an integer: '))
if num%2==0:
    print(f'num {num} is even')
else:
    print(f'num {num} is odd')



#3.Exponentiation
num=float(input('Enter a number to calculate its square and cube: '))
num_square = num ** 2
num_cube = num ** 3
print(f'square of {num} is {num_square}')
print(f'cube of {num} is {num_cube}')
