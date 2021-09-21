import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    """while loop will run until data entered by user is valid, and keep asking user to reenter if needed"""
    while True:
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
        """print(sales_data)
        validate_data(sales_data)"""
        """will need below 'return True' and 'False under 'except valueError' for the if statement
        and as part of 'while' loop"""
        if validate_data(sales_data):
            print('Data is valid!')
            break
    return sales_data

"""to validate user input - use print(values) below to check"""
def validate_data(values):
    """
    inside the try, converts all string values into integers.
    raises ValueError, if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """
    """print(values)"""

    """use below to check validation, try entering just 3 values to test. 
    Note 'e' is python shorthand for 'error'"""
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_sales_worksheet(data):
    """
    update sales worksheet, add new row with the list data provided
    """
    print('updating sales worksheet...\n')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Sales worksheet updated successfully.\n')

def update_surplus_worksheet(data):
    """
    update surplus worksheet, add new row with the list data provided
    """
    print('updating surplus worksheet...\n')
    surplus_worksheet = SHEET.worksheet('surplus')
    surplus_worksheet.append_row(data)
    print('Surplus worksheet updated successfully.\n')

"""refactoring code: i.e. combining above two update sales and surplus worksheets"""
def update_worksheet(data, worksheet):
    """
    receives a list of integerw to be inseeted into a worksheet.
    update the relevant worksheet with the data provided
    """
    print(f'updating {worksheet}...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet updated successfully\n')


def calculate_surplus_data(sales_row):
    """
    compare sales with stock and calculate the surplus for each item type.
    surplus is defined as the sales figure subtracted from the stock:
    -positive surplus indicates waste
    -negative surplus indicate extra made when stock was sold out
    """
    print('calculating surplus data...\n')
    """to calculate surplus, need last line from stock worksheet.  will use gspread 'get_all_values'() """
    stock = SHEET.worksheet('stock').get_all_values()
    """can use 'pprint' method, so data is easier to read when printed to terminal.
    Note: need to import pprint at top of file 
    pprint(stock) see phone """

    """need to get only last line of stock list, so use slice method i.e. [-1]. can also use .len() method """
    stock_row = stock[-1]
    """to print out values of two rows 
    print(f'stock_row: {stock_row}')
    print(f'sales row: {sales_row}')"""

    """zip() is used to iterate through 2 separate lists at same time """
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    """ print to test  print(surplus_data)"""
    return surplus_data

def main():
    """need to wrap all program functions within one function main() Note: function can only
    be 'called' after it is 'defined' """

    """ need to call get_sales_data() function... then check using python3 run.py ... 
    and enter random data"""
    data = get_sales_data()
    """below print when run will confirm that entered data is still a string (see phone) 
    print(data)"""
    sales_data = [int(num) for num in data]
    """need to call u-s-wksht... """
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    """ to test...  print(new_surplus_data)
    update_surplus_worksheet(new_surplus_data)"""
    update_worksheet(new_surplus_data, "surplus")

"""welcome statement will display before using input prompt """
print('Welcome to Love Sandwiches Data Automation')
main()
