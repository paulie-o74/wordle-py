# Import the gspread library to use with google sheets api
import gspread
from google.oauth2.service_account import Credentials
# Imports and starts the colorama function for people accessing on windows devices and autoreset means after every print statement
# the default color of the text printed to the terminal goes back to white
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 
import random
from typing import Optional

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
    Gets all the user log in details from the worksheet and return a list of dictionaries
    """
    login_data = LOGINS.get_all_records()
    return login_data

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
    # Every x is one dictionary in the list i.e. 1 username password pair key value pair
    # We check if not to check if there is no result in the list matching a username then:
    if not [x for x in logins if x['Username'] == username]: 
        print('\nNo such user found')
        print('\nPlease check and try again.')
        login()
    else:
        matched_username = [x for x in logins if x['Username'] == username][0]
    if password == matched_username['Password']:
        print('\nLogin successful')
        # main_menu() need to start the main app here 
    else:
        print('\nLogin failed')
        print('\nPassword did not match.')
        print('\nPlease try again.\n')
        # login()

# login()


def get_word() -> str:
    """ 
    Pulls all data from the google worksheet, chooses a random integer to 
    use in referencing the list of words produced
    """
    values_list = WORD_LIST.col_values(1)
    random_integer = random.randint(1, 411)
    game_word = values_list[random_integer].upper()
    return game_word


def play() -> None:
    def colored_alphabet(hits: set[str], misses: set[str]) -> str:
        """ 
        Returns a string of letters of alphabet, color coded by hit, miss or unknown
        """
        def color_and_char(ascii_code: int) -> str:
            char = chr(ascii_code)
            color = Fore.GREEN if char in hits \
                else Fore.RED if char in misses \
                else Fore.LIGHTBLACK_EX
            return color and char
        return ''.join(color_and_char(ascii_code) for ascii_code in range(ord('A'), ord('Z') + 1))

    def get_valid_answer() -> str:
        answer: str | None = None
        while not answer:
            prompt = colored_alphabet(hits, misses) + Fore.LIGHTWHITE_EX + ' --> ' + Fore.WHITE
            response = input(prompt)
            if len(response) != 5:
                print(Fore.WHITE + f'Your answer must have 5 letters')
            elif response not in values_list:
                print(Fore.WHITE + 'Not in word list')
            else:
                answer = response
        return answer


    word = get_word() ##maybe this needs to be outside after the get_word()
    print(word)
    answer: Optional[str] = None ##Optional denotes that it is some type [str] or None (before the user has inputted their guess)
    hits: set[str] = set()
    misses: set[str] = set()

    while answer != word:
        answer = get_valid_answer()
        show_output_pattern()