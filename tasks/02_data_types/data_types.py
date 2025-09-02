# Task 2: Data Types
# Complete the exercises below

# 1. Create variables with the following data types
# Your code here:
# Integer
# my_integer = 42
my_favorite_number = 73

# Float
# my_float = 3.14
bond_id = 0.07
# String
# my_string = "Hello Python"
fun_fact = "Trust me, I'm an engineer"
# Boolean
# my_boolean = True
bool = False
# Print all variables with their types
# print("Integer:", my_integer)
print("Int:", my_favorite_number)
# print("Float:", my_float)
print("Float", bond_id)
# print("String:", my_string)
print("String", fun_fact)
# print("Boolean:", my_boolean)
print("Boolean", bool)

print("\nType conversion examples:")
# 2. Demonstrate type conversion between different data types
# Your code here:
# Example: Convert string to integer
# num_string = "42"
num_str = "37"
res_str = type(num_str)
# num_integer = int(num_string)
num_int =int(num_str)
res_int = type(num_int)
# print(f"'{num_string}' converted to integer: {num_integer}")
print(f"String '{res_str}'-'{num_int}' is num '{res_int}'-'{num_int}'")


print("\nString operations:")
# 3. Perform string operations (concatenation, slicing, methods)
# Your code here:
# Example: String concatenation
# first_name = "Python"
# last_name = "Learner"
# full_name = first_name + " " + last_name
# print(f"Concatenated string: {full_name}")

first_part = "it's a feature, "
second_part = "not a bug."
full_phrase = first_part + second_part
print(f"Concatenated string: '{full_phrase}'")
print("Slicing:", full_phrase[-4:-1]) #bug
print("Slicing:", full_phrase[7:14]) #feature
print("Uppercase: ", full_phrase.upper())
print("Lowercase: ", full_phrase.lower())
print("Capitalized: ", full_phrase.capitalize())
print("Title: ", full_phrase.title())
print("Replace: ", full_phrase.replace(" ", "_"))

print("\nArithmetic operations:")
# 4. Use arithmetic operators with numbers
# Your code here:
# Example: Addition, subtraction, multiplication, division
# a = 10
# b = 3
# print(f"{a} + {b} = {a + b}")
a = 3
b = 5
c = 15
print(f"{a} + {b} = {a + b}")
print(f"{c} - {b} = {c - b}")
print(f"{a} * {b} = {a * b}")
print(f"{c} / {b} = {c / b}")
print(f"{c} // {b} = {c // b}")
print(f"{b} % {a} = {b % a}")
print(f"{b} ** {a} = {b ** a}")

print("\nComparison results:")
# 5. Demonstrate the use of comparison operators
# Your code here:
# Example: Equal to, greater than
x = 5
y = 10
print(f"{x} == {y}: {x == y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")


# Real-World Task: Temperature Converter
# This task will help you apply data types, type conversion, arithmetic operations, 
# and comparison operators in a practical context.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def compare_temperature(celsius):
    if celsius < 0:
        print("This temperature is below freezing point.")
    elif 20 <= celsius <= 25:
        print("This temperature is room temperature.")
    elif celsius >= 100:
        print("This temperature is the boiling point of water or above.")
    else:
        print("This temperature is in a different range.")

def display_menu():
    print("\nTEMPERATURE CONVERTER")
    print("\nSelect conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

display_menu()

try:
    choice = int(input("\nEnter your choice (1-6): "))

    if choice < 1 or choice > 6:
        print("Invalid choice. Please enter a number between 1 and 6.")
    else:
        temperature = input("Enter temperature: ")
        try:
            temperature = float(temperature)

            if choice == 1:
                result = celsius_to_fahrenheit(temperature)
                print(f"\nRESULT:\n{temperature:.2f}°C = {result:.2f}°F")
                compare_temperature(temperature)

            elif choice == 2:
                result = fahrenheit_to_celsius(temperature)
                print(f"\nRESULT:\n{temperature:.2f}°F = {result:.2f}°C")
                compare_temperature(result)

            elif choice == 3:
                result = celsius_to_kelvin(temperature)
                print(f"\nRESULT:\n{temperature:.2f}°C = {result:.2f}K")
                compare_temperature(temperature)

            elif choice == 4:
                result = kelvin_to_celsius(temperature)
                print(f"\nRESULT:\n{temperature:.2f}K = {result:.2f}°C")
                compare_temperature(result)

            elif choice == 5:
                result = fahrenheit_to_kelvin(temperature)
                print(f"\nRESULT:\n{temperature:.2f}°F = {result:.2f}K")
                celsius_tmp = fahrenheit_to_celsius(temperature)
                compare_temperature(celsius_tmp)

            elif choice == 6:
                result = kelvin_to_fahrenheit(temperature)
                print(f"\nRESULT:\n{temperature:.2f}K = {result:.2f}°F")
                celsius_tmp = kelvin_to_celsius(temperature)
                compare_temperature(celsius_tmp)

        except ValueError:
            print("Invalid temperature. Please enter a number.")

except ValueError:
    print("Invalid choice. Please enter a number between 1 and 6.")