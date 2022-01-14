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
    # Every x is one dictionary in the list i.e. 1 username password pair 
    # key value pair
    # We check if not to check if there is no result in the list matching 
    # a username then:
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

get_word()

def take_user_input():
    user_input = input("Please enter a 5 letter word as your guess:\n")
    while (user_input.isalpha() != True or len(user_input) != 5):
        print("Incorrect format, please enter a 5 letter word as your guess")
        user_input = input("Please enter a 5 letter word as your guess:\n")
    while (user_input not in values_list):
        print("Word is not in word list")
        user_input = input("Please enter a 5 letter word as your guess:\n")
    
    return user_input


