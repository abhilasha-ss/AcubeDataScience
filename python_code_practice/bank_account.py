'''
attributes

Account
name
balance
account number: automatic (ABC123BC)
branch
pin_number (4 digit number) - automatic
trasactions


methods
getters
setters
validate all the getters and setters
deposit and withdrawal methods

details
Create new account
    Name 
    Branch
    Min deposit
Deposit
    Input - account number
    Input - amount
    Output  -  Message with account holder name and money deposited
Withdrwal
    Input - account number
    Input - amount
    Input - pin number  
check balance
    Input - account number
    Input - pin number  
'''

import random
import string


existing_accounts = {}


class Account:
    '''
    This class represents a bank account
    '''

    def __init__(self, name, branch, min_deposit=500):
        self.name = name
        self.branch = branch
        self.balance = min_deposit
        self.account_number = self.generate_account_number()
        self.pin_number = self.generate_pin_number()
        self.transactions = []

    def generate_account_number(self):
        '''
        This method generates a random account number
        '''
        letters = string.ascii_uppercase
        numbers = string.digits
        random_letters = ''.join(random.choices(letters, k=3))
        random_numbers = ''.join(random.choices(numbers, k=3))
        return f'{random_letters}{random_numbers}{random_letters}'

    def generate_pin_number(self):
        '''
        This method generates a random pin number
        '''
        numbers = string.digits
        return ''.join(random.choices(numbers, k=4))

    def pin_validation(self, pin):
        '''
        pin
        '''
        if self.pin_number == pin:
            return True
        else:
            return False

    def deposit(self):
        '''
        Deposit
        '''
        amount = int(input("Enter Amount(Min: 100): "))
        if amount < 100:
            raise ValueError("Min deposit is 100")
        self.balance += amount
        self.transactions.append(amount)

    def withdraw(self):
        '''
        Withdraw
        '''
        pin_number = get_pin_number()
        if not self.pin_validation(pin_number):
            raise ValueError("Incorrect pin")
        
        amount = int(input("Enter amount: "))
        if self.balance+amount < 500:
            raise ValueError("Insufficent Balance")

        self.balance -= amount
        self.transactions.append(-amount)

    def get_balance(self):
        '''
        Check balance
        '''
        return self.balance


def get_account():
    '''
    Retrive account
    '''
    account_number = input("Enter Account Number: ")
    if account_number in existing_accounts:
        return existing_accounts[account_number]
    else:
        print("Incorrect Account Number")
        return None


def get_pin_number():
    '''
    get
    '''
    return int(input("Enter Pin Number: "))


def create_new_account():
    '''
    Created new account
    '''
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    amount = int(input("Enter deposit amount(min:500): "))
    if amount < 500:
        print("Insufficient deposit")
        return
    account = Account(name, branch, amount)
    existing_accounts[account.account_number] = account
    print(f"Account number: {account.account_number}")
    print(f"Pin number: {account.pin_number}")


def withdraw():
    '''
    Withdraw amount
    '''
    account = get_account()
    if not account:
        return
    try:
        account.withdraw()
    except ValueError:
        return


def deposit():
    '''
    Deposit amount
    '''
    account = get_account()
    if not account:
        return

    try:
        account.deposit()
    except ValueError:
        return


def check_balance():
    '''
    Check Balance
    '''
    account = get_account()
    if not account:
        return
    print(account.get_balance())


SESSION = True
while SESSION:
    action = int(input(
        "\n\nEnter your choice\n1: Create new account\n2: Withdraw\n"
        "3: Deposit\n"
        "4: Check Balance\n5: Exit\n\n"))
    match action:
        case 1:
            create_new_account()
        case 2:
            withdraw()
        case 3:
            deposit()
        case 4:
            check_balance()
        case 5:
            SESSION = False
        case _:
            print("Enter correct choice")
