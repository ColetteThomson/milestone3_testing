import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('spreadsheet1')

# next 3 lines used to check API is working:
# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)

def get_sales_data():
    """
    get sales figures input from the user
    """
    print('Please enter sales data from the last market.')
    print('Data should be six numbers, separated by commas.')
    print('Example: 10, 20, 30, 40, 50, 60\n')

    data_str = input('Enter your data here: ')
    """ to check this is working...
    print(f"The data provided is {data_str}")
    """
    """do this after 'calling get_sales_data() function section.
    use to split entered data string into comma separated value, then print to check """
    sales_data = data_str.split(",")
    """print(sales_data)"""
    validate_data(sales_data)

"""to validate user input - use print(values) below to check"""
def validate_data(values):
    """
    inside the try, converts all string values into integers.
    raises ValueError, if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """
    """print(values)  """

    """use below to check validation, try entering just 3 values to test. 
    Note 'e' is python shorthand for 'error'"""
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


    """ need to call get_sales_data() function... then check using python3 run.py ... 
    and enter random data"""
get_sales_data()



