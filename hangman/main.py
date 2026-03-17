import random
from hang_words import word_list
from hang_arts import stages, logo

random_word = random.choice(word_list)
print(logo)
lives = 6
placeholder = []
user_guesses = []

for letter in random_word:
    placeholder.append("_")


game_on = True
while game_on:
    word_to_guess = ""
    for i in placeholder:
        word_to_guess += i

    print(f"Word to guess: {word_to_guess}")

    user_guess = str(input("Guess a letter: ")).lower()
    if len(user_guess) != 1:
        print("You may enter a single letter.")
    elif user_guess.isdigit():
        print("You may enter only members of the alphabets.")
    else:
        if user_guess in user_guesses:
            print("You have already guessed that letter.")
        elif user_guess not in random_word:
            print(f"You guessed {user_guess}, that's not in the word. You lose a live")
            lives -= 1
            print(stages[lives])
            print(f"You have {lives} lives left")
        else:
            user_guesses.append(user_guess)
            for i in range(len(random_word)):
                if random_word[i] == user_guess:
                    placeholder[i] = user_guess
            print(stages[lives])
        user_guesses.append((user_guess))

    if lives == 0:
        print(stages[lives])
        game_on = False
        print("You lost!")
        print(f"The word is: {random_word}")
        print("Game Over")
    elif "_" not in placeholder:
        print("You won!")
        print(f"The word is: {random_word}")
        print("Game Over!")
        game_on = False
