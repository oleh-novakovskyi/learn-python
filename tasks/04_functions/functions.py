# Task 4: Functions
# Complete the exercises below

# 1. Create a simple function that takes no parameters and returns a greeting
# Your code here:
# Example:
print("1. Create a simple function that takes no parameters and returns a greeting")
def say_hello():
#     """Return a simple greeting message."""
     return "Hello, world!"
# 
# # Call the function
greeting = say_hello()
print(greeting)

def say_goodbye():
    return "Goodbye, world!"
print(say_goodbye())

# 2. Write a function that takes parameters and returns a calculated value
# Your code here:
# Example:
print("\n2. Create a function that takes no parameters and returns a greeting")
def calculate_area(length, width):
#     """Calculate the area of a rectangle."""
     return length * width
# 
# # Call the function
area = calculate_area(5, 3)
print(f"The area is {area} square units")

def calculate(param1, param2):
    return param1 + param2
param1 = int(input("Enter a number: "))
param2 = int(input("Enter another number: "))
result = calculate(param1, param2)
print(f"{param1} + {param2} = {result}")

# 3. Create a function with default parameter values
# Your code here:
# Example:
print("\n3. Create a function that takes no parameters and returns a greeting")
def make_coffee(type="latte", size="medium", sugar=True):
#     """Prepare a coffee with specified parameters."""
     result = f"Making a {size} {type}"
     if sugar:
         result += " with sugar"
     return result

# Call the function with different combinations
print(make_coffee())  # Uses all defaults
print(make_coffee("espresso", "small", False))  # No defaults

print("\nMy function")
def make_pizza(type="margherita", size="medium", extra_cheese=True):
    result = f"Baking a {size} {type} pizza"
    if extra_cheese:
        result += " with extra cheese"
    return result

print(make_pizza())
print(make_pizza("pepperoni", "large", False))

# 4. Implement a function that uses keyword arguments
# Your code here:
# Example:
print("\n4. Implement a function that uses keyword arguments")
def create_profile(name, age, city="Unknown", hobby="Unknown"):
#     """Create a user profile."""
     return {
         "name": name,
         "age": age,
         "city": city,
         "hobby": hobby
     }

# Call the function with keyword arguments
profile = create_profile(name="Alice", age=30, hobby="Painting")
print(profile)
print("\nMy function")
def create_character(login, race, level=0, weapon="Unknown"):
    return {
        "login": login,
        "race": race,
        "level": level,
        "weapon": weapon
    }
character = create_character(login="Oleh", race='Elf', level=20)
print(character)


# 5. Create a function that returns multiple values
# Your code here:
# Example:
print("\n5. Create a function that returns multiple values")
def get_dimensions():
#     """Return width, height, and depth of an object."""
     width = 10
     height = 20
     depth = 15
     return width, height, depth
# 
# Call the function and unpack the returned values
w, h, d = get_dimensions()
print(f"Width: {w}, Height: {h}, Depth: {d}")

print("\nMy function")
def get_parameters():
    health = 100
    score = 14567
    level = 12
    return health, score, level
health, score, level = get_parameters()
print(f"Health: {health}, Score: {score}, Level: {level}")

# 6. Write a recursive function (e.g., factorial or Fibonacci)
# Your code here:
# Example:
print("\n6. Write a recursive function (e.g., factorial or Fibonacci)")
print("\nFunction factorial")
def factorial(n):
#     """Calculate the factorial of n using recursion."""
     # Base case
     if n == 0 or n == 1:
         return 1
#     # Recursive case
     else:
         return n * factorial(n - 1)
#

result = factorial(5)
print(f"factorial of 5 is {result}")

print("\nFunction fibonacci")
fibonacci = int(input("Enter a number: "))
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

result = fib(fibonacci)
print(f"Fib of {fibonacci} is {result}")

print("\nFunction power")
a = int(input("Enter a number: "))
n = int(input("Enter n number: "))
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)

result = power(a, n)
print(f"{a}^{n} is {result}")

print("\nFunction reverse")
text_reverse = input("Enter number or text: ")
def reverse(text):
    return text[::-1]
print(reverse(text_reverse))


# Real-World Task: Date and Time Utility Library
# This task will help you apply function concepts in a practical context.

# Import the datetime module to work with dates and times
# import datetime

# 1. Function that returns the current date and time in a formatted string
from datetime import datetime, date, timedelta
def get_formatted_time(format_string="%B %d, %Y - %H:%M:%S"):
    now = datetime.now()
    return now.strftime(format_string)

# 2. Function that converts between different time units
def convert_time(value, from_unit="hours", to_unit="minutes"):
    """
    Convert a time value from one unit to another.

    Args:
        value (float): The time value to convert.
        from_unit (str): The unit to convert from. Options: "seconds", "minutes", "hours", "days".
        to_unit (str): The unit to convert to. Options: "seconds", "minutes", "hours", "days".

    Returns:
        float: The converted time value.

    Raises:
        ValueError: If an invalid unit is provided.
    """
    to_seconds = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400
    }

    if from_unit not in to_seconds or to_unit not in to_seconds:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', 'hours', or 'days'.")

    value_in_seconds = value * to_seconds[from_unit]
    return value_in_seconds / to_seconds[to_unit]

# 3. Function with default parameters that formats a date in different styles
def format_date(year, month, day, style="medium"):
    """
    Format a date in different styles.

    Args:
        year (int): The year.
        month (int): The month (1-12).
        day (int): The day of the month.
        style (str): The formatting style. Options: "short", "medium", "long", "iso".
                    Default is "medium".

    Returns:
        str: The formatted date string.

    Examples:
        - Short style: "08/26/25"
        - Medium style: "Aug 26, 2025"
        - Long style: "August 26, 2025"
        - ISO style: "2025-08-26"
    """
    # Your code here:
    d = date(year, month, day)
    if style == "short":
        return d.strftime("%m/%d/%y")
    elif style == "medium":
        return d.strftime("%b %d, %Y")
    elif style == "long":
        return d.strftime("%B %d, %Y")
    elif style == "iso":
        return d.strftime("%Y-%m-%d")
    else:
        raise ValueError("Invalid style. Use 'short', 'medium', 'long', or 'iso'.")

# 4. Function that calculates the time difference between two dates
def calculate_time_difference(date1, date2, unit="days"):
    """
    Calculate the time difference between two dates.
    
    Args:
        date1 (str): The first date in format "YYYY-MM-DD".
        date2 (str): The second date in format "YYYY-MM-DD".
        unit (str): The unit for the result. Options: "days", "hours", "minutes", "seconds".
                   Default is "days".
    
    Returns:
        float: The time difference in the specified unit.
    """
    # Your code here:
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    seconds = (d2 - d1).total_seconds()

    if unit == "days":
        return seconds / 86400
    elif unit == "hours":
        return seconds / 3600
    elif unit == "minutes":
        return seconds / 60
    elif unit == "seconds":
        return seconds
    else:
        raise ValueError("Invalid unit. Use 'days', 'hours', 'minutes', or 'seconds'.")

# 5. Function that returns multiple values about a given date
def get_date_components(date_str):
    """
    Get various components of a given date.
    
    Args:
        date_str (str): The date in format "YYYY-MM-DD".
    
    Returns:
        tuple: A tuple containing:
            - weekday (str): The day of the week (e.g., "Monday").
            - day_of_year (int): The day of the year (1-366).
            - week_number (int): The week number of the year (1-53).
    """
    # Your code here:
    d = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = d.strftime("%A")
    day_of_year = d.timetuple().tm_yday
    week_number = d.isocalendar().week
    return weekday, day_of_year, week_number

# 6. Recursive function that calculates a future date after adding business days
def add_business_days(date_str, days):
    """
    Calculate a future date after adding a specified number of business days (skipping weekends).
    
    Args:
        date_str (str): The starting date in format "YYYY-MM-DD".
        days (int): The number of business days to add.
    
    Returns:
        str: The resulting date in format "YYYY-MM-DD".
    """
    # Your code here:
    # Hint: Use recursion to handle the case of adding one business day at a time
    d = datetime.strptime(date_str, "%Y-%m-%d")
    if days == 0:
        return d.strftime("%Y-%m-%d")
    d += timedelta(days=1)
    if d.weekday() >= 5:
        return add_business_days(d.strftime("%Y-%m-%d"), days)
    else:
        return add_business_days(d.strftime("%Y-%m-%d"), days - 1)

# Test your functions
def test_date_time_library():
    """Test the date and time utility functions."""
    print("Date and Time Utility Library Tests\n")
    
    # Test get_formatted_time
    print("1. Current formatted time:")
    current_time = get_formatted_time()
    print(f"   {current_time}")
    
    # Test convert_time
    print("\n2. Time conversion:")
    minutes = convert_time(2, from_unit="hours", to_unit="minutes")
    print(f"   2 hours = {minutes} minutes")
    
    # Test format_date
    print("\n3. Date formatting:")
    short_date = format_date(2025, 8, 26, style="short")
    medium_date = format_date(2025, 8, 26)  # Default style
    long_date = format_date(2025, 8, 26, style="long")
    print(f"   Short: {short_date}")
    print(f"   Medium: {medium_date}")
    print(f"   Long: {long_date}")
    
    # Test calculate_time_difference
    print("\n4. Time difference:")
    days_diff = calculate_time_difference("2025-12-25", "2025-08-26", unit="days")
    print(f"   Days between Aug 26 and Dec 25, 2025: {days_diff}")
    
    # Test get_date_components
    print("\n5. Date components:")
    weekday, day_of_year, week_num = get_date_components("2025-08-26")
    print(f"   August 26, 2025 is a {weekday}, day {day_of_year} of the year, in week {week_num}")
    
    # Test add_business_days
    print("\n6. Adding business days:")
    future_date = add_business_days("2025-08-26", 10)
    print(f"   10 business days after August 26, 2025: {future_date}")

# Uncomment to run the tests
test_date_time_library()