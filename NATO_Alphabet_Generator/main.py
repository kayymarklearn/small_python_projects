import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}


nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabets.iterrows()}

print("Convert a word to NATO phonetic")

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        user_word_codes = [nato_alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, letters in the alphabets only please.")
        generate_phonetic()
    else:
        print(user_word_codes)

generate_phonetic()
