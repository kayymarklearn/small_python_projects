from hang_arts import logo, stages
from hang_words import word_list
import random

print(logo)

chosen_word = random.choice(word_list)                 # The random word chosen.

user_guess = [''] * len(chosen_word)                 # Will store user input till we get the full word

print(chosen_word)

i = 0                                                           # Keep track of characters

lives = 6                                                       # The number of lives.

placeholder = ""                                                # A place holder for the letters typed by the user.

display = ""                                                    # Used to authenticate user input

game_over = False                                               # Keep track of game state.

for letter in chosen_word:                                      # Initially populate the place holder with underscores.
    placeholder += "_"


print(f"Word to guess: {placeholder}")

while not game_over:
    guess = input("Guess a letter: ")

    # Check if user input is part of the chosen_word.

    for character in chosen_word:
        if guess == character:
            display += character
            user_guess[i] = character
        else:
            display += "_"
        i += 1

    print(user_guess)
    result = "".join(user_guess)
    if result == chosen_word:                                   # Ends game if user gets full word
        game_over = True

print(placeholder)
print(f"Display: {display}")
print(user_guess)
