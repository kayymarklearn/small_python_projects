import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

punctuations = [
    ".", ",", "?", "!",      # basic
    ":", ";",                # colon, semicolon
    "-", "–", "—",            # hyphen, en dash, em dash
    "'", "\"",               # apostrophe, quotation mark
    "(", ")",                # parentheses
    "[", "]",                # brackets
    "{", "}",                # braces
    "...",                   # ellipsis
    "/", "\\",               # slash, backslash
    "@", "#", "$", "%",      # symbols
    "&", "*", "^",
    "_", "~", "|", " "
]


nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabets.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
user_word_codes = [nato_alphabet_dict[letter] for letter in user_word if letter not in punctuations]


print(user_word_codes)