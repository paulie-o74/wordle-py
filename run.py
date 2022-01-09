# Import the gspread library to use with google sheets api
import gspread
from google.oauth2.service_account import Credentials
# Imports and starts the colorama function for people accessing on windows devices and autoreset means after every print statement
# the default color of the text printed to the terminal goes back to white
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 

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
    Gets all the user log in details from the worksheet and return a list of lists
    """
    login_data = LOGINS.get_all_records()
    return login_data

def login():
    """
    Function to take user input (username and password) and compare
    to google sheet data record
    """
    print(DIVIDER)
    username = input('\nEnter username: \n')
    password = input('\nPassword: \n')
    logins = get_logins()
    if not [x for x in logins if x['username'] == username]:
        print('\nNo such user found')
        print('\nPlease check and try again.')
        login()
    else:
        matched_username = [x for x in logins if x['username'] == username][0]
    if password == matched_username['password']:
        print('\nLogin successful')
        # main_menu()
    else:
        print('\nLogin failed')
        print('\nPassword did not match.')
        print('\nPlease try again.')
        login()

login()