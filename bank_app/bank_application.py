import random
import time
import sqlite3
import hashlib
import re
from getpass import getpass


conn = sqlite3.connect('Bank_details.db')
# conn1 = sqlite3.connect('transactions.db')

cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS bank_details(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name TEXT,
               username TEXT UNIQUE,
               password TEXT,
               account_number TEXT UNIQUE,
               initial_deposit INTEGER,
               balance REAL,
               created_at TEXT)
               ''')
conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_number TEXT,
        type TEXT,
        amount REAL,
        date TEXT
    )
''')
conn.commit()


lower = ['qwertyuiopasdfghjklzxcvbnm']
upper = ['QWERTYUIOPASDFGHJKLZXCVBNM']
symbol = ['~!@#$%^&*(),.']
number = ['1234567890']
def create_account():
    while True:
        full_name = str(input("Enter full name here: "))
        if  len(full_name) < 4:
            print("Full name too short")
            continue
        elif len(full_name) > 255:
            print("Full name too long")
            continue
        break
    while True:
        username = input("Enter username: ")
        if len(username) < 3:
            print("Minimum characters is 3")
            continue
        elif len(username) > 20:
            print("Maximum characters is 20")
            continue
        break
    while True:
        password = getpass("Enter password: ")
        if len(password) < 8 or len(password) > 30:
            print("Password must be between 8 and 30 characters long.")
            continue
        if not re.search(r"[A-Z]", password):
            print("Password must contain at least one uppercase letter.")
            continue
        if not re.search(r"[a-z]", password):
            print("Password must contain at least one lowercase letter.")
            continue
        if not re.search(r"\d", password):
            print("Password must contain at least one number.")
            continue
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # special char
            print("Password must contain at least one special character (!@#$%^&* etc.).")
            continue

        confirm = getpass("Confirm password: ")
        if password != confirm:
            print("Passwords do not match.")
            continue

        print("Password is strong and confirmed!")
        break
    # hashed_password = hashlib.sha256(password.encode()).hexdigest()

    account_number = str(random.randint(1000000000, 1999999999))
    initial_deposit = int(input("Enter deposit here: "))
    balance = print(f'Your balance is now {initial_deposit}')
    created_at = time.strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute('''
        INSERT INTO bank_details (full_name, username, password, account_number, initial_deposit, balance, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)''', (full_name, username, password, account_number, initial_deposit, balance, created_at))
    except sqlite3.IntegrityError:
        print("Username Already Exists")
    else:
        conn.commit()
        print("Your account has been created")
    
    time.sleep(1.5)
    print(login())
    # conn.commit()
    # print(f"Done {account_number}")

def login():
    print("-----LOGIN-----")
    while True:
        username = input("Enter username: ")
        if not username:
            print("Username cannot be empty")
            continue
        break
    while True:
        password = input("Enter password: ")
        if not password:
            print("Enter correct password")
            continue
        break

    cursor.execute('''
    SELECT * FROM bank_details where username = ? and password = ?''', (username, password))
    user = cursor.fetchone()
    while True:
        if user is None:
            print("Invalid username or password")
            return
        print("Login Successful")
        time.sleep(1.5)
        print(menu())

def deposit():
    account_number = input("Enter account number: ")
    cursor.execute(("SELECT * FROM bank_details WHERE account_number = ?"), (account_number,))
    user = cursor.fetchone()
    if user is None:
        print("Invalid usernmae")
        return
    amount = float(input("Enter Deposit Amount: "))

    old_balance = user[6] if user[6] is not None else 0.0
    new_balance = old_balance + amount

    cursor.execute("UPDATE bank_details SET balance = ? WHERE account_number = ?", (new_balance, account_number))

    cursor.execute('''
    INSERT INTO transactions (account_number, type, amount, date) VALUES (?, ?, ?, ?)''', (account_number, "Deposit", amount, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

    # print(f"deposit: {amount} and new_balance: {new_balance}")
    # user = cursor.fetchone()
    # while True:
    #     if user is None:
    #         print("Invalid ")
    #         return
    #     print("Successful")
    # # print(deposit())

def withdrawal():
    account_number = input("Enter account number: ")
    cursor.execute("SELECT * FROM bank_details WHERE account_number = ?", (account_number,))
    user = cursor.fetchone()
    if user is None:
        print("Invalid account")
        return
    amount = float(input("Enter amount"))
    old_balance = user[6] if user[6] is None else 0.0
    new_balance = old_balance - amount
    cursor.execute("UPDATE bank_details SET balance = ? WHERE account_number = ?", (new_balance, account_number))
    conn.commit()

    print(f"Withdrawal of {amount} has been completed, balance now: {new_balance}")
    user = cursor.fetchone
    while True:
        if user is None:
            print("Invalid")
            return
        print("Successful")
        break

def transactions():
    account_number = input("Enter your account number: ")
    cursor.execute("SELECT * FROM transactions WHERE account_number = ?", (account_number,))
    records = cursor.fetchall()

    if not records:
        print("No transactions")

    print("\n=== Transaction History ===")
    for txn in records:
        print(f"Type: {txn[2]} | Amount: ₦{txn[3]} | Date: {txn[4]}")    
    
    # print(transactions(account_number))

def transfer():
    sender = input("Enter your account number: ")
    cursor.execute("SELECT * FROM bank_details WHERE account_number = ?", (sender,))
    user = cursor.fetchone()
    if user is None:
        print("Incorrect account number")
        return
    
    time.sleep(1.5)
    receiver = input("Enter receiver account number: ")
    cursor.execute("SELECT * FROM bank_details WHERE account_number = ?", (receiver,))
    user = cursor.fetchone()
    if user is None:
        print("Incorrect account number")
        return
    
    amount = float(input("Enter amount"))

    sender_balance = user[6] if user[6] is not None else 0.0
    receiver_balance= user[6] if user[6] is not None else 0.0

    if amount > sender_balance:
        time.sleep(1.5)
        print("Insufficient balance")
        return
    new_sender_balance = sender_balance - amount
    new_receiver_balance = receiver_balance + amount

    cursor.execute("UPDATE bank_details SET balance = ? WHERE account_number = ?", (new_sender_balance, sender))
    cursor.execute("UPDATE  bank_details SET balance = ? WHERE account_number = ?", (new_receiver_balance, receiver))

    cursor.execute('''INSERT INTO transactions (account_number, type, amount, date) VALUES (?, ?, ?, ?)''', (receiver, "Transfer Received", amount, time.strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()

    time.sleep(2.5)

    print(f"Transfer of ₦{amount} to {receiver} successful!")
    print(f"Your new balance: ₦{new_sender_balance}")

    # print(transfer())



def menu():
    while True:
        print("-----MENU-----")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Transaction History") 
        print("4. Transfer")

        choice = (input("Enter Option: "))

        if choice == '1':
            time.sleep(1.5)
            print(deposit())
        elif choice == '2':
            time.sleep(1.5)
            print(withdrawal())
        elif choice == '3':
            time.sleep(1.5)
            print(transactions())
        elif choice == '4':
            time.sleep(1.5)
            print(transfer())
        else:
            print("Enter valid option")


# print(menu())

def main_menu():
    print("-----MAIN MENU-----")
    print("WELCOME TO MelvTheBank")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter option 1-3: ")

    if choice =='1':
        time.sleep(1.5)
        print(create_account())
    elif choice == '2':
        time.sleep(1.5)
        print(login())
    elif choice == '3':
        time.sleep(1.5)
        print("Goodbye")
    else:
        time.sleep(1.5)
        print("Invalid Option")

print(main_menu())




# 6. Transfer Validation
# Recipient Account Number:
# - Ensure that the account number is numeric and exists in the database.
# - Ensure that the recipient account number is not the same as the logged-in user's account number (prevent self-transfers).

# Transfer Amount:
# - Ensure the amount is a positive number.
# - Check that the amount does not exceed the sender’s balance.
# - Reject non-numeric or negative values or blank values.

# (1, 'Melvyn', 'Melv', 'Melv', '1706633298', 111, None, '2025-10-28 14-43-13')
# (2, '111', '111', '111', '1027834228', 111, None, '2025-10-28 15-03-56')
# (3, '333', '333', '333', '1025676130', 333, None, '2025-10-28 15-12-40')


# print(create_account())
# print(login())







# import sqlite3

# conn = sqlite3.connect('Bank_details.db')
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM bank_details")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# conn.close()


             