"""
Author:Cao Boyuan
Date:2025-08-18
Description:Monday- python variables & data types practice
content:
1.BMI calculator
2.Temperature conversion
3.variable type demonstration
"""

# 1. BMI Calculator
height_m=float(input("please input your height in meters:"    ))
weight_kg=float(input("please input your weight in kilograms:"))
bmi=weight_kg/(height_m**2)
print(f"your BMI is:{bmi:.2f}")

#2.temperature_conversion
temp_celsius=float(input("please input the temperature in Celsius:"))
temp_fahrenheit=(temp_celsius*1.8)+32
print(f"the temperature in Fahrenheit is:{temp_fahrenheit:.2f}")

#3. variable type demonstration
print(type(height_m))  # float
print(type(weight_kg))  # float
print(type(bmi))       # float
print(type(temp_celsius))  # float
print(type(temp_fahrenheit))  # float
print(type("Hello, World!"))  # str