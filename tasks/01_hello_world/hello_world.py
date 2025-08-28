# Task 1: Hello World
# Complete the exercises below

# 1. Print "Hello, World!" to the console
# Your code here:
print("Hello, World!")

# 2. Create a variable with your name and print a greeting using that variable
# Your code here:
name = "Oleh"
print(f"Hello, {name}!")

# 3. Create two number variables and print their sum
# Your code here:
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}")

# 4. Print the current date
# Your code here:
from datetime import datetime
print(f"Today is {datetime.now().strftime('%Y-%m-%d')}")

# Real-World Task: Personal Information Card
# This task will help you apply the concepts you've learned to create a practical program.

# 1. Get user input for name, age, city, and a fun fact
# Example:
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
fun_fact = input("Enter a fun fact about yourself: ")

# 2. Calculate the birth year based on the current year (2025) and the age provided
# Example:
current_year = 2025
birth_year = current_year - int(age)

# 3. Format and display all information as a nicely formatted "Personal Info Card"
print("Name: {}".format(name))
print(f"Age: {age}")
print(f"City: {city}")
print(f"Birth Year: {birth_year}")
print(f"Fun Fact: {fun_fact}")

# 4. Include the current date at the bottom of the card
print(f"Created on: {datetime.now().strftime('%B %d, %Y')}")

# Example output:
# ===================================
#         PERSONAL INFO CARD
# ===================================
# Name: John Smith
# Age: 25
# City: New York
# Birth Year: 2000
# Fun Fact: I can solve a Rubik's cube in under 2 minutes
#
# Created on: August 26, 2025
# ==================================

