# import sqlite3
import random
import time

# conn = sqlite3.connect('Bank.db')

# cursor = conn.cursor()

# cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS bank_details(
#                username TEXT UNIQUE,
#                password TEXT,
#                account_number TEXT UNIQUE,
#                balance REAL,
#                loan REAL,
#                created_at TEXT)
#                ''')
# conn.commit()


accounts = []


def create_account():
    full_name = input('Enter full name:')
    username = input('Enter username:')
    password = input('Enter password: ')
    account_number = str(random.randint(1000000000, 1999999999))
    balance = float(input('Enter amount here: '))

    account = {
        "full_name": full_name,
        "username": username,
        "password": password,
        "account_number": account_number,
        "balance": balance,
        "loan": 0,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    accounts.append(account)

    print(f"Your Account Number is: {account_number}")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for acc in accounts:
        if acc["username"] == username and acc["password"] == password:
            print(f"Welcome {username}!")
            return acc 

    print("Invalid username")
    return None


def deposit(account):
    amount = float(input('Enter deposit amount here: '))
    if amount <= 2000:
        print('Minimum Deposit is N2,000')
        return
    account['balacne'] += amount
    print(f"Your deposit of {amount} has been completed. Your balacne is now: {account['balance']}")


def withdraw(account):
    amount = float(input('Enter deposit amount here: '))
    if amount > account['balance']:
        print('Your balance is too low for this withdraw')
    elif amount <= 100:
        print('Try a higher amount')
    else:
        account['balance'] -= amount
        print(f"Your withdraw of {amount} was succesful. Your balacne is now: {account['balance']}")

def check_balance(account):
    print(f"Your current balcnce is N{account['balance']}")

def transfer(account):
    pass


def loan(account):
    amount = float(input('Enter deposit amount here: '))
    if amount <= 0:
        print("Invalid loan amount.")
        return

    account["loan"] += amount
    account["balance"] += amount
    print(f"Your loan of N{amount} was successful")
    print(f"Your balance is now N{account['balance']}")

def menu(account):
    while True:
        print("\n Welcome!")
        print("\n MENU")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Account Balance")
        print("5. Apply for Loan")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            deposit(account)
        elif choice == '2':
            withdraw(account)
        elif choice == '3':
            transfer(account)
            pass
        elif choice == '4':
            check_balance(account)
        elif choice == '5':
            loan(account)
        elif choice == '6':
            print("Bye!")
            break
        else:
            print("Select Option 1-8")
    
# print(create_account())


def beginning_menu():
    while True:
        print("\n Welcome")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
            break
        elif choice == '2':
            user = login()
            if user:
                menu(user)
        elif choice == '3':
            print("Bye!")
            break
        else:
            print("Select Option 1-3")

print(beginning_menu())


# link login with menu page
# add to the data base   

# def login():
#     username = input('Enter username:')
#     password = input('Enter password: ')


# def find_account (username, password=None):
#     for acc in accounts:
#         if acc['username'] ==username:
#             return acc

# def find_acct_num(account_number):
#     for acc in accounts:
#         if acc["account_number"] == account_number:
#             return acc



# class account:
#     def __init__(self, username, password, balance=0):
#         self.username = username
#         self.password = password
#         self.balance = balance
#         # self.withdraw = withdraw
#         # self.transfer = transfer
#         # self.check_balance = check_balance
#         # self.loan = loan
#         # self.create_account = create_account
#         # self.create_account = create_account
#         # self.create_account = create_account

#   
#         def create_table():


# create_account() 
# login()
# deposit() 
# withdraw() 
# transfer()
# check_balance()
# apply_loan() 