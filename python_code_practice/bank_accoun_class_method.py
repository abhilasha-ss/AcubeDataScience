import random
import string


class Account:

    existing_accounts = {}

    def __init__(self, name, branch, min_deposit=500):
        self.name = name
        self.branch = branch
        self.balance = min_deposit
        self.account_number = self.generate_account_number()
        self.pin_number = self.generate_pin_number()
        self.transactions = []

    def generate_account_number(self):
        letters = string.ascii_uppercase
        numbers = string.digits
        random_letters = ''.join(random.choices(letters, k=3))
        random_numbers = ''.join(random.choices(numbers, k=3))
        return f'{random_letters}{random_numbers}{random_letters}'

    def generate_pin_number(self):
        numbers = string.digits
        return ''.join(random.choices(numbers, k=4))

    def pin_validation(self):
        pin = input("Enter Pin Number: ")
        if self.pin_number == pin:
            return True
        else:
            print("Incorrect Pin Number")
            return False

    def deposit(self):
        if not self.pin_validation():
            return
        amount = int(input("Enter Amount(Min: 100): "))
        if amount < 100:
            print("Min deposit is 100")
        self.balance += amount
        self.transactions.append(amount)

    def withdraw(self):
        if not self.pin_validation():
            return
        amount = int(input("Enter amount: "))
        if self.balance+amount < 500:
            print("Insufficent Balance")
        self.balance -= amount
        self.transactions.append(-amount)

    def get_balance(self):
        if not self.pin_validation():
            return
        print("Balance = ", self.balance)

    @classmethod
    def get_account(cls):
        account_number = input("Enter Account Number: ")
        if account_number in cls.existing_accounts:
            return cls.existing_accounts[account_number]
        else:
            print("Incorrect Account Number")
            return None

    @classmethod
    def create_new_account(cls):
        name = input("Enter name: ")
        branch = input("Enter branch: ")
        amount = int(input("Enter deposit amount(min:500): "))
        if amount < 500:
            print("Insufficient deposit")
            return
        account = cls(name, branch, amount)
        cls.existing_accounts[account.account_number] = account
        print(f"Account number: {account.account_number}")
        print(f"Pin number: {account.pin_number}")

    @classmethod
    def session(cls):
        SESSION = True
        while SESSION:
            action = int(input(
                "\n\nEnter your choice\n1: Create new account\n2: Withdraw\n"
                "3: Deposit\n4: Check Balance\n5: Exit\n\n"))
            match action:
                case 1:
                    cls.create_new_account()
                case 2:
                    account = cls.get_account()
                    if account:
                        account.withdraw()
                case 3:
                    account = cls.get_account()
                    if account:
                        account.deposit()
                case 4:
                    account = cls.get_account()
                    if account:
                        account.get_balance()
                case 5:
                    SESSION = False
                case _:
                    print("Enter correct choice")


Account.session()
