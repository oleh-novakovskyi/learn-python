# Task 5: Lists and Dictionaries
# Complete the exercises below
from itertools import count

# 1. Create and manipulate lists using various operations
# Your code here:
# Example:
# # Create a list
#fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
# 
# # Access elements
#first_fruit = fruits[0]
#last_fruit = fruits[-1]
# 
# # Slicing
#some_fruits = fruits[1:3]  # Gets elements at index 1 and 2
# 
# # Modify elements
#fruits[0] = "pear"
# 
# # Print results
#print("First fruit:", first_fruit)
#print("Last fruit:", last_fruit)
#print("Some fruits:", some_fruits)
#print("Modified list:", fruits)

print("\n1. Create and manipulate lists using various operations:")
equipment = ['Laptop', 'Tablet', 'Television', 'Headphones', 'Camera']
equipment_other = ['Refrigerator', 'Washing machine', 'Microwave', 'Vacuum cleaner']
print("\nList of equipment:", equipment)

first_equipment = equipment[0]
last_equipment = equipment[-1]
some_equipment = equipment[1:-1]
equipment[0] = "Smartphone"

print("First equipment:", first_equipment)
print("Last equipment", last_equipment)
print("Some equipment", some_equipment)

# 2. Use list methods (append, insert, remove, etc.)
# Your code here:
# Example:
# numbers = [1, 2, 3, 4, 5]
# 
# # Append - add to the end
# numbers.append(6)
# 
# # Insert - add at specific position
# numbers.insert(0, 0)  # Insert 0 at position 0
# 
# # Remove - remove by value
# numbers.remove(3)
# 
# # Pop - remove by index and return the value
# popped_value = numbers.pop(2)
# 
# # Sort and reverse
# unsorted = [3, 1, 4, 1, 5, 9, 2]
# unsorted.sort()
# unsorted.reverse()
# 
# print("Numbers after operations:", numbers)
# print("Popped value:", popped_value)
# print("Sorted and reversed:", unsorted)

print("\n2. Use list methods (append, insert, remove, etc.)")
equipment.append("Smartphone")
print("\nAppend list:", equipment)

equipment.extend(equipment_other)
print("Extend list:", equipment)

equipment.insert(-1,"test")
print("Insert list:", equipment)

equipment.remove("test")
print("Remove list:", equipment)

equipment.sort()
print("Sort list:", equipment)

equipment.reverse()
print("Reverse list:", equipment)

popped_equipment = equipment.pop(4)
print("Pop list:", popped_equipment)
print("New Pop list", equipment)

count_equipment = len(equipment)
print("Count equipment:", count_equipment)

# 3. Implement list comprehensions for concise list creation
# Your code here:
# Example:
# # Create a list of squares from 1 to 10
# squares = [x**2 for x in range(1, 11)]
# 
# # Create a list of even numbers from 1 to 20
# evens = [x for x in range(1, 21) if x % 2 == 0]
# 
# # Create a list of tuples (number, square) for numbers 1 to 5
# number_squares = [(x, x**2) for x in range(1, 6)]
# 
# print("Squares:", squares)
# print("Evens:", evens)
# print("Number-square pairs:", number_squares)

print("\n3. Implement list comprehensions for concise list creation")
new_squares = [x**5 for x in range(1,11)]
print("Squares:", new_squares)

new_evens = [x for x in range(1,21) if x % 2 == 0]
print("Evens:",new_evens)

new_number_squares = [(x, x**5) for x in range(1, 8)]
print("Number-square pairs:", new_number_squares)

# 4. Create and manipulate dictionaries
# Your code here:
# Example:
# # Create a dictionary
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "job": "Engineer"
# }
# 
# # Access values
# name = person["name"]
# 
# # Add or modify values
# person["email"] = "alice@example.com"
# person["age"] = 31
# 
# print("Person:", person)
# print("Name:", name)

print("\n4. Implement list comprehensions for concise list creation")
student = {
    'first_name': 'Oleh',
    'last_name': 'Novakovskyi',
    'age': 39,
    'city': 'Zhytomyr',
    'country': 'UA'
}
print(student)

first_name, last_name, age, city, country = student.values()
print(first_name, last_name, age, city, country)

first_name= student['first_name']
print(first_name)

student['age'] = 40
print(student)

student.pop('country')
print(student)
get_city = student.get('city').upper()
print(get_city)

city = student['city'].lower()
print(city)

student.update({"country": "Ukraine"})
print(student)

student["course"] = 2
print(student)
print(student.keys())

# 5. Access and modify dictionary values
# Your code here:
# Example:
# student = {
#     "name": "Bob",
#     "grades": {
#         "math": 85,
#         "science": 92,
#         "history": 78
#     }
# }
# 
# # Safe access with get (provides default if key doesn't exist)
# english_grade = student["grades"].get("english", "Not taken")
# 
# # Update multiple values at once
# student["grades"].update({"math": 87, "english": 80})
# 
# print("Student:", student)
# print("English grade:", english_grade)
print("\n5. Access and modify dictionary values")
new_student = student.copy()
print(new_student)
new_student["grades"] = {"math": 85, "science": 92, "history": 78}
print(new_student)
new_student["grades"].update({"englesh": 85})
print(new_student)



# 6. Iterate through lists and dictionaries
# Your code here:
# Example:
# colors = ["red", "green", "blue", "yellow"]
# 
# # Iterate through a list
# print("Colors:")
# for color in colors:
#     print(f"- {color}")
# 
# # Iterate with index
# print("\nIndexed colors:")
# for i, color in enumerate(colors):
#     print(f"{i}: {color}")
# 
# # Iterate through a dictionary
# scores = {"Alice": 95, "Bob": 82, "Charlie": 88}
# print("\nScores:")
# for name, score in scores.items():
#     print(f"{name}: {score}")
print("\n6. Access and modify dictionary values")
for value in new_student.values():
    print(f"- {value}")

for i, value in enumerate(new_student):
    print(f"-"
          f"{i}: {value}")

for name, score in new_student["grades"].items():
    print(f"- {name}: {score}")

# 7. Implement nested data structures
# Your code here:
# Example:
# # List of dictionaries
# students = [
#     {"name": "Alice", "age": 22, "major": "Computer Science"},
#     {"name": "Bob", "age": 20, "major": "Engineering"},
#     {"name": "Charlie", "age": 21, "major": "Mathematics"}
# ]
# 
# # Dictionary of lists
# class_roster = {
#     "math101": ["Alice", "Bob", "Eve"],
#     "cs50": ["Alice", "Charlie", "Dave"],
#     "eng200": ["Bob", "Charlie", "Eve"]
# }
# 
# # Accessing nested structures
# first_student_name = students[0]["name"]
# math_students = class_roster["math101"]
# 
# print("First student:", first_student_name)
# print("Math students:", math_students)
# 
# # Finding students in multiple classes
# print("\nStudents in multiple classes:")
# for student in set(class_roster["math101"]) & set(class_roster["cs50"]):
#     print(f"- {student}")

print("\n7. Access and modify dictionary values")

appliances = [
    {"name": "Fridge", "brand": "Samsung", "price": 12000},
    {"name": "Washing Machine", "brand": "LG", "price": 8000},
    {"name": "Vacuum Cleaner", "brand": "Philips", "price": 3000},
    {"name": "Microwave", "brand": "Panasonic", "price": 2500},
    {"name": "TV", "brand": "Sony", "price": 15000}
]

house_rooms = {
    "kitchen": ["Fridge", "Microwave", "TV"],
    "living_room": ["TV", "Vacuum Cleaner"],
    "laundry": ["Washing Machine"],
    "bedroom": ["TV", "Vacuum Cleaner"]
}

first_appliance_name = appliances[0]["name"]
kitchen_appliances = house_rooms["kitchen"]

print("First appliance:", first_appliance_name)
print("Appliances in kitchen:", kitchen_appliances)

print("\nAppliances in both kitchen and living room:")
for item in set(house_rooms["kitchen"]) & set(house_rooms["living_room"]):
    print(f"- {item}")

print("\nAll Sony appliances:")
for appliance in appliances:
    if appliance["brand"] == "Sony":
        print(f"- {appliance['name']} (price: {appliance['price']} UAH)")

# Real-World Task: Contact Management System
# This task will help you apply list and dictionary concepts in a practical context.

# Initialize the contacts list
contacts = []

# Sample contacts for testing
sample_contacts = [
    {
        "name": "John Smith",
        "phone": "555-123-4567",
        "email": "john@example.com",
        "address": "123 Main St",
        "category": "work"
    },
    {
        "name": "Jane Doe",
        "phone": "555-987-6543",
        "email": "jane@example.com",
        "address": "456 Oak Ave",
        "category": "family"
    }
    ,
    {
        "name": "Jane1 Doe1",
        "phone": "555-987-6542",
        "email": "jane2@example.com",
        "address": "455 Oak Ave",
        "category": ""
    }
    ,
    {
        "name": "Jane2 Doe2",
        "phone": "565-987-6542",
        "email": "jane3@example.com",
        "address": "458 Oak Ave",
        "category": ""
    }
]

# You can uncomment this line to start with sample contacts
contacts = sample_contacts.copy()

# Function to display the main menu
def display_menu():
    """Display the main menu options."""
    print("\nCONTACT MANAGEMENT SYSTEM")
    print("=========================")
    print("\nMain Menu:")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. View contacts by category")
    print("7. Sort contacts")
    print("8. Exit")

# Function to add a new contact
def add_contact():
    """Add a new contact to the contacts list."""
    # Your code here:
    # 1. Get contact details from user input
    # 2. Create a dictionary for the new contact
    # 3. Add the dictionary to the contacts list
    # 4. Print confirmation message

    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    category = input("Enter category (family, work, friend, etc.): ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "category": category
    }

    contacts.append(contact)
    print(f"\n Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts():
    """Display all contacts in the list."""
    # Your code here:
    # 1. Check if contacts list is empty
    # 2. If not empty, iterate through the list and display each contact
    # 3. Use enumerate to show contact numbers
    if not contacts:
        print("\nNo contacts available.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact #{i}")
        for key, value in contact.items():
            print(f"{key.capitalize()}: {value}")

# Function to search for a contact by name
def search_contact():
    """Search for a contact by name (partial matches allowed)."""
    # Your code here:
    # 1. Get search term from user
    # 2. Use list comprehension to find matching contacts
    # 3. Display search results
    # Hint: Use the 'in' operator for partial matches
    term = input("Enter name to search: ").lower()
    results = [c for c in contacts if term in c["name"].lower()]

    if results:
        print("\nSearch results:")
        for contact in results:
            print(f"- {contact['name']} ({contact['phone']})")
    else:
        print("\nNo contacts found.")

# Function to update a contact
def update_contact():
    """Update an existing contact's information."""
    # Your code here:
    # 1. Display all contacts with numbers
    # 2. Ask user which contact to update
    # 3. Ask which field to update
    # 4. Get new value and update the contact
    # 5. Print confirmation message
    view_contacts()
    if not contacts:
        return

    try:
        index = int(input("\nEnter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print("\nFields: name, phone, email, address, category")
            field = input("Which field to update? ").lower()

            if field in contact:
                new_value = input(f"Enter new value for {field}: ")
                contact[field] = new_value
                print(f"\nContact updated successfully!")
            else:
                print("\nInvalid field.")
        else:
            print("\nInvalid contact number.")
    except ValueError:
        print("\nPlease enter a valid number.")

# Function to delete a contact
def delete_contact():
    """Delete a contact from the list."""
    # Your code here:
    # 1. Display all contacts with numbers
    # 2. Ask user which contact to delete
    # 3. Remove the contact from the list
    # 4. Print confirmation message
    view_contacts()
    if not contacts:
        return

    try:
        index = int(input("\nEnter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"\nContact '{removed['name']}' deleted successfully!")
        else:
            print("\nInvalid contact number.")
    except ValueError:
        print("\nPlease enter a valid number.")

# Function to view contacts by category
def view_by_category():
    """Group and display contacts by category."""
    # Your code here:
    # 1. Create a dictionary to group contacts by category
    # 2. Iterate through contacts and add to appropriate category
    # 3. Display contacts grouped by category
    # Hint: Use a dictionary where keys are categories and values are lists of contacts
    if not contacts:
        print("\nNo contacts available.")
        return

    grouped = {}
    for c in contacts:
        grouped.setdefault(c["category"], []).append(c)

    for category, group in grouped.items():
        print(f"\nCategory: {category}")
        for contact in group:
            print(f"- {contact['name']} ({contact['phone']})")

# Function to sort contacts
def sort_contacts():
    """Sort contacts by a selected field."""
    # Your code here:
    # 1. Ask user which field to sort by (name, category, etc.)
    # 2. Sort the contacts list using the sorted() function with a key function
    # 3. Display the sorted contacts
    # Hint: Use a lambda function as the key for sorting
    if not contacts:
        print("\nNo contacts available.")
        return

    field = input("Sort by (name, phone, email, address, category): ").lower()
    if field not in contacts[0]:
        print("\nInvalid field.")
        return

    sorted_list = sorted(contacts, key=lambda x: x[field].lower())

    print("\nSorted contacts:")
    for contact in sorted_list:
        print(f"- {contact['name']} ({contact['phone']})")

# Main function to run the contact management system
def main():
    """Run the contact management system."""
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                add_contact()
            elif choice == 2:
                view_contacts()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                update_contact()
            elif choice == 5:
                delete_contact()
            elif choice == 6:
                view_by_category()
            elif choice == 7:
                sort_contacts()
            elif choice == 8:
                print("\nThank you for using the Contact Management System. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 8.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

# Uncomment the line below to run the contact management system
if __name__ == "__main__":
     main()