# Task 3: Control Flow
# Complete the exercises below

# 1. Create an if-else statement to check if a number is positive, negative, or zero
# print("Number checker:")
# number = 0  # Try changing this value
# Your code here:
print('\n1. Create an if-else statement to check if a number is positive, negative, or zero')
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 2. Write a program that determines if a year is a leap year
# print("\nLeap year checker:")
# Your code here:
print('\n2. Write a program that determines if a year is a leap year')
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# 3. Create a for loop to iterate through a list of items. Print each item
# print("\nFor loop example:")
# Your code here:
print('\n3. Create a for loop to iterate through a list of items. Print each item')
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print("List of fruits: ", fruit)


# 4. Use a while loop to implement a simple guessing game
print('\n4. Use a while loop to implement a simple guessing game')
print("While loop example:")
# Your code here:
# Example:
import random
secret_number = random.randint(1, 10)
guess = 0
attempts = 0

print("I'm thinking of a number between 1 and 10.")
while guess != secret_number and attempts < 3:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")

if attempts == 3 and guess != secret_number:
    print("You lose!")
else:
    print("You win!")


# 5. Implement a nested loop structure
print('\n5. Implement a nested loop structure')
print("Nested loop example:")
# Your code here:
# Example:
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print(end="\n")

# Real-World Task: Adventure Game
# This task will help you apply conditional statements, loops, and logical operators
# in a practical and fun context.

# Game variables
player_health = 100
player_score = 0
game_running = True

# Function to display the game title and instructions
def display_intro():
     print("\nADVENTURE GAME: FOREST MYSTERY")
     print("\nYou find yourself at the edge of a mysterious forest.")
     print("Your goal is to explore the forest and find the hidden treasure.")
     print("Be careful with your choices, as they will affect your health and score.")

# Function to display player status
def display_status():
     print(f"\nHealth: {player_health}  Score: {player_score}")

# Function for the starting scenario
def forest_entrance():
    global player_score

    display_status()
    print("\nWhat would you like to do?")
    print("1. Enter the forest")
    print("2. Walk around the perimeter")
    print("3. Turn back and go home")

    choice = input("\nYour choice: ")

    if choice == "1":
        # Enter the forest - go to next scenario
        print("\nYou bravely step into the mysterious forest...")
        return "forest_path"

    elif choice == "2":
        # Walk around - different outcome
        print("\nAs you walk around the perimeter, you find a map!")
        player_score += 5
        return "forest_entrance"

    elif choice == "3":
        # Go home - end game
        print("\nYou decided to play it safe and go home. Adventure over!")
        return "game_over"

    else:
        print("\nInvalid choice. Please try again.")
        return "forest_entrance"

# Add more scenario functions here
import random

def forest_path():
    global player_health
    print("\nYou are now inside the forest. It's dark and mysterious...")
    display_status()
    print("\nWhat would you like to do?")
    print("1. Go deeper into the forest")
    print("2. Explore a side path")
    print("3. Go back to the entrance")
    print("4. Search for food")

    choice = input("\nYour choice: ")

    if choice == "1":
        print("\nYou walk deeper into the forest...")
        return "encounter_animal"
    elif choice == "2":
        print("\nYou discover a narrow path leading away...")
        return "find_treasure"
    elif choice == "3":
        print("\nYou carefully walk back to the forest entrance.")
        return "forest_entrance"
    elif choice == "4":
        if random.random() < 0.5:
            hp_change = find_food()
            player_health += hp_change
            if player_health > 100:
                player_health = 100
        else:
            print("\nYou searched for food but couldn't find anything this time.")
        return "forest_path"
    else:
        print("\nInvalid choice. Please try again.")
        return "forest_path"



def encounter_animal():
    global player_health, player_score

    print("\nA wild wolf appears in front of you!")
    display_status()
    print("\nWhat will you do?")
    print("1. Run away")
    print("2. Fight the wolf")
    print("3. Try to calm it down")

    choice = input("\nYour choice: ")

    if choice == "1":
        print("\nYou manage to escape, but you get scratched.")
        player_health -= 10
        return "forest_path"

    elif choice == "2":
        if random.random() < 0.5:
            print("\nYou fought bravely and scared the wolf away!")
            player_score += 10
        else:
            print("\nThe wolf bit you before running off...")
            player_health -= 20
        return "forest_path"

    elif choice == "3":
        if random.random() < 0.3:
            print("\nSurprisingly, the wolf calms down and leaves you alone.")
            player_score += 5
        else:
            print("\nYour attempt failed. The wolf attacked you!")
            player_health -= 15
        return "forest_path"

    else:
        print("\nInvalid choice. Please try again.")
        return "encounter_animal"

def find_treasure():
    global player_score

    print("\nYou carefully search around the hidden path...")
    display_status()

    if random.random() < 0.3:
        print("\nCongratulations! You found the hidden treasure!")
        player_score += 50
        return "win"
    else:
        print("\nYou didn’t find anything this time. Keep searching!")
        return "forest_path"

def find_food():
    food = random.choice(["berries", "mushrooms", "root"])
    if food == "berries":
        hp = 10
        print("You found some berries and restored +10 HP!")
        return hp
    elif food == "mushrooms":
        if random.random() < 0.5:
            print("Delicious mushrooms! You restored +15 HP!")
            return 15
        else:
            print("Poisonous mushrooms! You lost -10 HP!")
            return -10
    else:
        print("You found a healing root and restored +20 HP!")
        return 20

# Function to check if the game is over
def check_game_over():
     global player_health, game_running
     if player_health <= 0:
         print("\nYour health has reached zero. Game over!")
         game_running = False
         return True
     return False

# Function to ask if the player wants to play again
def play_again():
     response = input("\nWould you like to play again? (yes/no): ")
     return response.lower() in ["yes", "y"]

# Main game loop
def main_game():
     global player_health, player_score, game_running

     # Reset game variables
     player_health = 100
     player_score = 0
     game_running = True
     current_scenario = "forest_entrance"

     display_intro()

     # Game loop
     while game_running:
         # Handle different scenarios based on current_scenario variable
         if current_scenario == "forest_entrance":
             current_scenario = forest_entrance()
         elif current_scenario == "forest_path":
             current_scenario = forest_path()
         elif current_scenario == "encounter_animal":
             current_scenario = encounter_animal()
         elif current_scenario == "find_treasure":
             current_scenario = find_treasure()
         elif current_scenario == "game_over" or current_scenario == "win":
             break

         # Check if game should end
         if check_game_over():
             break

     # Display final score
     print(f"\nFinal score: {player_score}")

     # Ask to play again
     if play_again():
         main_game()
     else:
         print("\nThanks for playing!")

# Start the game
if __name__ == "__main__":
     main_game()