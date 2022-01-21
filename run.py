# Import the gspread library to use with google sheets api
import gspread
from google.oauth2.service_account import Credentials
import random


# Google api information
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('wordlepy')
LOGINS = SHEET.worksheet('logins')
WORD_LIST = SHEET.worksheet('words')

# constants
DIVIDER = '-' * 30


def get_logins() -> list:

    """
    Gets all the user log in details from the worksheet and
    return a list of dictionaries
    """
    login_data = LOGINS.get_all_records()
    return login_data


get_logins()


def login() -> None:
    """
    Function to take user input (username and password) and compare
    to google sheet data record
    """
    print(DIVIDER)
    username = input('\nEnter username: \n')
    password = input('\nPassword: \n')
    logins = get_logins()
    # list comprehension making a list from an iteration
    # a more succint way to create a list from a for loop
    # Every x is one dictionary in the list i.e. 1 username password pair
    # key value pair
    # We check if not to check if there is no result in the list matching
    # a username then:
    if not [x for x in logins if x['Username'] == username]:
        print('\nNo such user found\n')
        print('\nPlease check and try again.\n')
        login()
    else:
        matched_username = [x for x in logins if x['Username'] == username][0]
    if password == matched_username['Password']:
        print('\nLogin successful\n')
        print(DIVIDER)
        print('\nHow to play:\n'
              'Guess the WORDLE in 6 tries.\n'
              'Each guess must be a valid 5 letter word.'
              ' Hit the enter button to submit.\n'
              'After each guess, you will receive feedback'
              ' to show how close your guess was to the word.\n')
        print(DIVIDER)
    else:
        print('\nLogin failed\n')
        print('\nPassword did not match\n')
        print('\nPlease try again\n')
        login()


login()


def get_word() -> str:
    """
    Pulls all data from the google worksheet, chooses a random integer to
    use in referencing the list of words produced
    """
    values_list = []
    for word in WORD_LIST.col_values(1):
        values_list.append(word.upper())
    random_integer = random.randint(0, 410)
    game_word = values_list[random_integer]
    return game_word, values_list


game_word, values_list = get_word()


def take_user_input():
    """
    Takes a user input of 5 letters only, that is in the list of words in
    the game.
    If user input isnt in the correct format, it prints an error message
    to the user and asks for another input.
    """
    init_user_input = input(
        "\nPlease enter a 5 letter word as your guess:\n").upper()
    # takes user input as a string
    while (not init_user_input.isalpha() or len(init_user_input) != 5):
        # Checks if input is all letters and len = 5
        print(F"\nIncorrect format, please enter a 5 letter word"
              " as your guess\n")
        print(DIVIDER)
        init_user_input = input(
            "\nPlease enter a 5 letter word as your guess:\n")
    while init_user_input.upper() not in values_list:
        # Checks if the word is in the input list as to not waste a turn if
        # the word isn't in the list
        print(F"\nWord is not in word list\n")
        print(DIVIDER)
        init_user_input = input(
            "\nPlease enter a 5 letter word as your guess:\n")
    return init_user_input.upper()
    # returns a string


def check_letters(game_word, input):  # both are strings
    """
    Function to check which letters are in the correct position,
    which letters are in the word and not in the correct position
    """
    correct_position = []
    # list which holds the letters in the correct position
    cor_pos_index = []
    # list which holds the index number of each correctly positioned letter
    in_word = []
    # list which holds the letters in the word but not in the correect position
    in_word_index = []
    # list which holds the index number of each incorrectly positioned letter
    for index, letter in enumerate(game_word):
        # enumerate records how many times weve iterated,
        # index is our iteration number (starts at 0)
        # letter is the current letter in the string game_word
        if letter in input:  # searches the input for the letter
            if letter == input[index]:
                # if the same letter is in the same position
                correct_position.append(letter)
                # save the correct letter in the correct_position list
                cor_pos_index.append(index)
                # save the correct letter index in the cor_pos_index list
            else:  # if not in correct position, but letter is in the word
                in_word.append(letter)  # save the letter in the in_word list
                in_word_index.append(user_input.find(letter[:]))
                # saves the index of the user input
                # correct letter for future use
                # find() takes the letter as a parameter,
                # searches the string input
                # for the letter from left to right (0 index to last index),
                # and returns the index where it is found
    return correct_position, cor_pos_index, in_word, in_word_index  # 4 lists


# Take user input until they win or they reach 6 turns and the gam ends
run = True
i = 1  # counts how many turns the user has had
while run:
    user_input = take_user_input()  # takes the user input
    if user_input.upper() == game_word.upper():
        # converts to upper case to make the comparison easier
        print(DIVIDER)
        print(F"\nCongrats, you win!")
        print(DIVIDER)
        run = False  # loop ends
    elif i == 6:
        # indicates to the user that they have no more turns left
        print(F"\nYou have no more guesses remaining, "
              "the word was:")
        print(game_word.upper())
        print(F"Better luck next time.")
        print(DIVIDER)
        break
    else:
        correct_position, cor_pos_index, in_word, in_word_index \
            = check_letters(game_word, user_input)
        if len(correct_position) == 0 and len(in_word) == 0:
            print(f"\nNone "
                  "of those letters "
                  "appear in the word")
        if len(correct_position) > 0:
            # if there are letters in the correct position
            for index, letter in enumerate(correct_position):
                character_index = cor_pos_index[index]
                # finds the index of the letter in user_input
                # that was in the correct spot
                print(f"\nThe "
                      "letter {0} is in the word "
                      "and is in the correct position "
                      "({1})".format(letter, character_index + 1))
                # The 2 arguments .format takes are letter {0} and
                # character_index + 1 to help the player understand where
                # the correct letter is
        if len(in_word) > 0:
            # if they got a letter in the word but not in correct position
            for index, letter in enumerate(in_word):
                character_index = in_word_index[index]
                # finds the index of the letter in
                # user_input that was in the correct spot
                print(f"\nThe "
                      "letter {0} is in the word "
                      "but not in position "
                      "{1}".format(letter, character_index + 1))
        print("\nPlease try again...")
        i += 1  # used 1/6 of their attempts
        print(f"You have {7 - i} attempts remaining")
        print(DIVIDER)
