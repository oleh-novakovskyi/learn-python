# Task 6: File I/O
# Complete the exercises below

print("\n1. Create a text file and write content to it")
# Your code here:
# Example:
# Method 1: Open, write, close
file = open("sample.txt", "w")
file.write("Hello, world!\n")
file.write("This is a sample text file.\n")
file.write("By Oleh Novakovskyi!\n")
file.close()
# 
print("File created successfully.")


print("\n2. Read content from a text file")
# Your code here:
# Example:
print("\nMethod 1: Read entire file")
file = open("sample.txt", "r")
content = file.read()
file.close()
# 
print("File content (read):")
print(content)
# 
print("\nMethod 2: Read line by line")
file = open("sample.txt", "r")
lines = file.readlines()
file.close()
# 
print("File content (readlines):")
for i, line in enumerate(lines, 1):
     print(f"Line {i}: {line.strip()}")


print("\n3. Append content to an existing file")
# Your code here:
# Example:
file = open("sample.txt", "a")
file.write("\n-- ### ---\n")
file.write("This line was appended.\n")
file.write("Another appended line.\n")
file.close()
#
print("Content appended to file.")
#
# Read the updated file
file = open("sample.txt", "r")
updated_content = file.read()
file.close()
#
print("Updated file content:")
print(updated_content)


print("\n4. Work with file paths using the os module")
# Your code here:
# Example:
import os
# 
# Get current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")
# 
# Join paths in a platform-independent way
file_path = os.path.join(current_dir, "data", "sample.txt")
print(f"Full file path: {file_path}")
# 
# Check if a file exists
if os.path.exists("sample.txt"):
     print("sample.txt exists")
else:
     print("sample.txt does not exist")
# 
# Get file information
if os.path.exists("sample.txt"):
     size = os.path.getsize("sample.txt")
     print(f"File size: {size} bytes")


print("\n5. Use context managers (with statement) for file operations")
# Your code here:
# Example:
# Writing with context manager
with open("context_sample.txt", "w") as file:
     file.write("Using context manager for file operations.\n")
     file.write("No need to explicitly close the file.\n")
# 
print("File written using context manager.")
# 
# Reading with context manager
with open("context_sample.txt", "r") as file:
    content = file.read()
# 
print("Content from context manager file:")
print(content)


print("\n6. Read and write CSV files")
# Your code here:
# Example:
import csv
# 
# Writing CSV
data = [
     ["Name", "Age", "City", "Status"],
     ["Alice", 30, "New York", "Worker"],
     ["Bob", 25, "Los Angeles", "Student"],
     ["Charlie", 35, "Chicago", ""],
     ["Oleh", 39, "Zhytomyr", "Student"]
 ]
# 
with open("people.csv", "w", newline="") as file:
     writer = csv.writer(file)
     writer.writerows(data)
# 
print("CSV file written successfully.")
# 
# Reading CSV
with open("people.csv", "r") as file:
     reader = csv.reader(file)
     print("CSV file content:")
     for row in reader:
         print(row)
# 
# Using DictReader and DictWriter
dict_data = [
     {"Name": "David", "Age": 28, "City": "Boston"},
     {"Name": "Eve", "Age": 22, "City": "Miami"},
     {"Name": "Frank", "Age": 45, "City": "Seattle"}
 ]
# 
with open("people_dict.csv", "w", newline="") as file:
     fieldnames = ["Name", "Age", "City"]
     writer = csv.DictWriter(file, fieldnames=fieldnames)
     writer.writeheader()
     writer.writerows(dict_data)
#
print("Dict CSV file written successfully.")

import csv

new_people = [
    {"Name": "Ivan", "Age": 29, "City": "Kyiv"},
    {"Name": "Maria", "Age": 31, "City": "Lviv"}
]

with open("people_dict.csv", "a", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerows(new_people)

print("New rows added successfully.")

print("\n7. Work with JSON files")
# Your code here:
# Example:
import json
# 
# Create data structure
person = {
     "name": "Alice",
     "age": 30,
     "city": "New York",
     "languages": ["Python", "JavaScript", "Java"],
     "is_student": False,
     "contact": {
         "email": "alice@example.com",
         "phone": "123-456-7890"
     }
 }
# 
# Write JSON to file
with open("person.json", "w") as file:
     json.dump(person, file, indent=10)

print("JSON file written successfully.")

# Read JSON from file
with open("person.json", "r") as file:
     loaded_person = json.load(file)
#
print("JSON file content:")
print(json.dumps(loaded_person, indent=4))
print(json.dumps(loaded_person, separators=(",", ":")))
# 
# Access specific data
print(f"Name: {loaded_person['name']}")
languages_str = ', '.join(loaded_person['languages'])
print(f"Languages: {languages_str}")
print(f"Languages: {languages_str.split(",")}")
print(f"Email: {loaded_person['contact']['email']}")
print(f"Phone: {loaded_person['contact']['phone']}")


# Real-World Task: Note-Taking Application
# This task will help you apply file I/O concepts in a practical context.

# Import necessary modules
import os
import json
import datetime
import shutil  # For file operations like copying

# Constants
NOTES_DIR = "notes"  # Directory to store notes
INDEX_FILE = os.path.join(NOTES_DIR, "index.json")  # Master index file

# Ensure the notes directory exists
def setup_notes_directory():
    """Create the notes directory if it doesn't exist."""
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)
        print(f"Created notes directory: {NOTES_DIR}")
    
    # Create an empty index file if it doesn't exist
    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "w") as f:
            json.dump([], f)
        print("Created empty index file")

# Function to get a list of all notes from the index
def get_notes_index():
    """Read the master index file and return the list of notes."""
    try:
        with open(INDEX_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is invalid, return an empty list
        return []

# Function to save the notes index
def save_notes_index(notes_index):
    """Save the notes index to the master index file."""
    with open(INDEX_FILE, "w") as f:
        json.dump(notes_index, f, indent=4)

# Function to create a new note
def create_note():
    """Create a new note with title, content, and tags."""
    # Your code here:
    # 1. Get note title, tags, and content from user
    # 2. Create a unique filename based on the title
    # 3. Save the note content to a text file
    # 4. Create metadata (title, date, tags) and save as JSON
    # 5. Update the master index
    title = input("Enter note title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    tags_input = input("Enter tags (comma-separated, optional): ").strip()
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()] if tags_input else []

    content = input("Enter note content: ").strip()

    # Create unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_base = title.replace(" ", "_").lower() + "_" + timestamp
    content_file = os.path.join(NOTES_DIR, filename_base + ".txt")
    meta_file = os.path.join(NOTES_DIR, filename_base + ".json")

    # Save content
    with open(content_file, "w") as f:
        f.write(content)

    # Create metadata
    metadata = {
        "title": title,
        "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tags": tags,
        "filename": filename_base
    }

    # Save metadata
    with open(meta_file, "w") as f:
        json.dump(metadata, f, indent=4)

    # Update index
    notes_index = get_notes_index()
    notes_index.append(metadata)
    save_notes_index(notes_index)

    print(f"Note '{title}' created successfully.")

# Function to view a note
def view_note():
    """Display the content and metadata of a selected note."""
    # Your code here:
    # 1. List all available notes
    # 2. Ask user to select a note
    # 3. Read the note file and metadata
    # 4. Display the note content and metadata
    notes_index = get_notes_index()
    if not notes_index:
        print("No notes available.")
        return

    print("\nAvailable notes:")
    for i, note in enumerate(notes_index):
        print(f"{i + 1}. {note['title']} ({note['created'][:10]})")

    try:
        choice = int(input("Select note number: ")) - 1
        if 0 <= choice < len(notes_index):
            note = notes_index[choice]
            filename_base = note['filename']
            content_file = os.path.join(NOTES_DIR, filename_base + ".txt")

            with open(content_file, "r") as f:
                content = f.read()

            print(f"\nTitle: {note['title']}")
            print(f"Created: {note['created']}")
            print(f"Tags: {', '.join(note['tags'])}")
            print("\nContent:")
            print(content)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")
    except FileNotFoundError:
        print("Note file not found.")

# Function to edit a note
def edit_note():
    """Edit the content or metadata of an existing note."""
    # Your code here:
    # 1. List all available notes
    # 2. Ask user to select a note
    # 3. Read the current note content and metadata
    # 4. Ask what to edit (content, title, or tags)
    # 5. Update the note file and metadata
    # 6. Update the master index if necessary
    notes_index = get_notes_index()
    if not notes_index:
        print("No notes available.")
        return

    print("\nAvailable notes:")
    for i, note in enumerate(notes_index):
        print(f"{i + 1}. {note['title']} ({note['created'][:10]})")

    try:
        choice = int(input("Select note number: ")) - 1
        if 0 <= choice < len(notes_index):
            note = notes_index[choice]
            filename_base = note['filename']
            content_file = os.path.join(NOTES_DIR, filename_base + ".txt")
            meta_file = os.path.join(NOTES_DIR, filename_base + ".json")

            with open(content_file, "r") as f:
                content = f.read()

            print(f"\nCurrent title: {note['title']}")
            new_title = input("New title (enter to keep): ").strip()
            if new_title:
                note['title'] = new_title

            print(f"Current tags: {', '.join(note['tags'])}")
            new_tags_input = input("New tags (comma-separated, enter to keep): ").strip()
            if new_tags_input:
                note['tags'] = [tag.strip() for tag in new_tags_input.split(',') if tag.strip()]

            print(f"Current content: {content}")
            new_content = input("New content (enter to keep): ").strip()
            if new_content:
                content = new_content

            # Save updated content and metadata
            with open(content_file, "w") as f:
                f.write(content)
            with open(meta_file, "w") as f:
                json.dump(note, f, indent=4)

            save_notes_index(notes_index)
            print("Note updated successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")
    except FileNotFoundError:
        print("Note file not found.")

# Function to delete a note
def delete_note():
    """Delete a note and remove it from the index."""
    # Your code here:
    # 1. List all available notes
    # 2. Ask user to select a note
    # 3. Confirm deletion
    # 4. Remove the note file and metadata
    # 5. Update the master index
    notes_index = get_notes_index()
    if not notes_index:
        print("No notes available.")
        return

    print("\nAvailable notes:")
    for i, note in enumerate(notes_index):
        print(f"{i + 1}. {note['title']} ({note['created'][:10]})")

    try:
        choice = int(input("Select note number to delete: ")) - 1
        if 0 <= choice < len(notes_index):
            note = notes_index[choice]
            confirm = input(f"Delete '{note['title']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                filename_base = note['filename']
                content_file = os.path.join(NOTES_DIR, filename_base + ".txt")
                meta_file = os.path.join(NOTES_DIR, filename_base + ".json")

                os.remove(content_file)
                os.remove(meta_file)

                notes_index.pop(choice)
                save_notes_index(notes_index)
                print("Note deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")
    except FileNotFoundError:
        print("Note file not found.")

# Function to list all notes
def list_notes():
    """Display a list of all available notes with their metadata."""
    # Your code here:
    # 1. Read the master index
    # 2. Display each note with its title, creation date, and tags
    # 3. Handle the case when no notes exist
    notes_index = get_notes_index()
    if not notes_index:
        print("No notes available.")
        return

    print("\nAll notes:")
    for note in notes_index:
        print(f"Title: {note['title']}")
        print(f"Date: {note['created'][:10]}")
        print(f"Tags: {', '.join(note['tags'])}")
        print("-" * 40)

# Function to search notes
def search_notes():
    """Search for notes by title or content."""
    # Your code here:
    # 1. Ask for search term
    # 2. Search through note titles and content
    # 3. Display matching notes
    # 4. Handle case when no matches are found
    search_term = input("Enter search term: ").strip().lower()
    if not search_term:
        print("Search term cannot be empty.")
        return

    notes_index = get_notes_index()
    matches = []

    for note in notes_index:
        # Check title and tags
        if (search_term in note['title'].lower() or
                any(search_term in tag.lower() for tag in note['tags'])):
            matches.append(note)
            continue

        # Check content
        filename_base = note['filename']
        content_file = os.path.join(NOTES_DIR, filename_base + ".txt")
        try:
            with open(content_file, "r") as f:
                content = f.read().lower()
            if search_term in content:
                matches.append(note)
        except FileNotFoundError:
            pass

    if not matches:
        print("No notes found matching the search term.")
        return

    print(f"\nMatching notes ({len(matches)}):")
    for note in matches:
        print(f"Title: {note['title']}")
        print(f"Date: {note['created'][:10]}")
        print(f"Tags: {', '.join(note['tags'])}")
        print("-" * 40)

# Function to export a note
def export_note():
    """Export a note to plain text or JSON format."""
    # Your code here:
    # 1. List all available notes
    # 2. Ask user to select a note
    # 3. Ask for export format (text or JSON)
    # 4. Ask for export location
    # 5. Export the note to the specified format and location
    notes_index = get_notes_index()
    if not notes_index:
        print("No notes available.")
        return

    print("\nAvailable notes:")
    for i, note in enumerate(notes_index):
        print(f"{i + 1}. {note['title']} ({note['created'][:10]})")

    try:
        choice = int(input("Select note number: ")) - 1
        if 0 <= choice < len(notes_index):
            note = notes_index[choice]
            filename_base = note['filename']
            content_file = os.path.join(NOTES_DIR, filename_base + ".txt")

            with open(content_file, "r") as f:
                content = f.read()

            export_format = input("Export format (text/json): ").strip().lower()
            export_location = input("Export location (filename, optional): ").strip()

            if not export_location:
                ext = "txt" if export_format == "text" else "json"
                export_location = f"{note['title'].replace(' ', '_')}.{ext}"

            if export_format == "text":
                export_data = f"Title: {note['title']}\nCreated: {note['created']}\nTags: {', '.join(note['tags'])}\n\n{content}"
                with open(export_location, "w") as f:
                    f.write(export_data)
            elif export_format == "json":
                export_data = note.copy()
                export_data["content"] = content
                with open(export_location, "w") as f:
                    json.dump(export_data, f, indent=4)
            else:
                print("Invalid format. Use 'text' or 'json'.")
                return

            print(f"Note exported to {export_location}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")
    except FileNotFoundError:
        print("Note file not found.")

# Display the main menu
def display_menu():
    """Display the main menu options."""
    print("\nNOTE-TAKING APPLICATION")
    print("=======================")
    print("\nMain Menu:")
    print("1. Create a new note")
    print("2. View a note")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. List all notes")
    print("6. Search notes")
    print("7. Export a note")
    print("8. Exit")

# Main function to run the note-taking application
def main():
    """Run the note-taking application."""
    # Ensure the notes directory exists
    setup_notes_directory()
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                create_note()
            elif choice == 2:
                view_note()
            elif choice == 3:
                edit_note()
            elif choice == 4:
                delete_note()
            elif choice == 5:
                list_notes()
            elif choice == 6:
                search_notes()
            elif choice == 7:
                export_note()
            elif choice == 8:
                print("\nThank you for using the Note-Taking Application. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 8.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

# Uncomment the line below to run the note-taking application
if __name__ == "__main__":
     main()