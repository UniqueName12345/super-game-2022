# This is still in development!

import time
import random

# This function checks if the player's choice beats the computer's choice
def verify_choice(p_choice, c_choice):
    if p_choice == "r" and c_choice == "s":
        return True
    elif p_choice == "r" and c_choice == "l":
        return True
    elif p_choice == "p" and c_choice == "r":
        return True
    elif p_choice == "s" and c_choice == "paper":
        return True
    elif p_choice == "s" and c_choice == "l":
        return True
    else:
        return False

# This function prints a statement and then waits a certain amount of time
def print_statement(statement, time_to_sleep):
    print(statement)
    time.sleep(time_to_sleep)


    # This is the list of options
def play():
    # This is the player's choice
    full_options = ["rock", "paper", "scissors", "lizard", "food"]
    options = ["r", "p", "s", "l", "f"]
    # This is the computer's choice
    p_choice = input("Choose your weapon: ")
    # This loop makes sure the player's choice is valid
    c_choice = random.choice(options)
    while p_choice not in options:
        print("Please choose a valid weapon.")
        p_choice = input("Choose your weapon: ")
    # This prints the player's choice
    print_statement(f"You chose {full_options[options.index(p_choice)]}", 1)
    # This prints the computer's choice
    print_statement(
        f"The computer chose {full_options[options.index(c_choice)]}", 1
    )

    # This checks if the player's choice beats the computer's choice
    if verify_choice(p_choice, c_choice):
        # This prints if the player wins
        print_statement("You win!", 1)
    else:
        # This prints if the player loses
        print_statement("You lose!", 1)

# This prints the game's name
print_statement("This program will play a game of rock, paper, scissors, lizard.", 1)

# This asks the player if they want to play
play_game = input("Do you want to play? (y/n)")

# This checks if the player wants to play
if play_game == "y":
    # This prints if the player wants to play
    print("Let's play!")
    # This starts the game
    play()
else:
    # This prints if the player doesn't want to play
    print("Ok, maybe next time!")
    # This exits the program
    exit()
