import random
import time
import sqlite3
import hashlib
import re
from getpass import getpass


conn = sqlite3.connect('Bank_detai.db')

cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS bank_details(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name TEXT,
               username TEXT UNIQUE,
               hashed_password TEXT,
               account_number TEXT,
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


def create_account():
    while True:
        full_name = str(input("Enter full name here: "))
        if  len(full_name) < 4 or len(full_name) > 255:
            print("Full name must be between 4 and 255 characters.")
            continue
        if not re.search(r"[A-Za-z\s]+", full_name):
            print("Full name must contain only letters")       
            continue
        break
    while True:
        username = input("Enter username: ")
        if len(username) < 3 or len(username) > 20:
            print("Username must be between 3 and 20 characters.")
            continue
        if not re.fullmatch(r"\w+", username):
                print("Username can only contain letters, numbers, and underscores (_).")
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
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    account_number = str(random.randint(10000000, 19999999))
    print(account_number)
    initial_deposit = int(input("Enter deposit here: "))
    balance = print(f'Your balance is now N{initial_deposit}')
    balance = initial_deposit
    created_at = time.strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute('''
        INSERT INTO bank_details (full_name, username, hashed_password, account_number, initial_deposit, balance, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)''', (full_name, username, hashed_password, account_number, initial_deposit, balance, created_at))
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
    print("\n-----LOGIN-----")
    while True:
        username = input("Enter username: ")
        if not username:
            print("Username cannot be empty")
            continue
        break
    while True:
        password = getpass("Enter password: ")
        if not password:
            print("Enter correct password")
            continue
        break
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('''
    SELECT * FROM bank_details where username = ? and hashed_password = ?''', (username, hashed_password))
    user = cursor.fetchone()
    while True:
        if user:
            print(f"Welcome {username}")
            time.sleep(1.1)
            menu(user)
            break
        else:
            print("Invalid username or password")
        time.sleep(1)
        login()

def deposit(user):
    account_number = user[4]
    cursor.execute(("SELECT * FROM bank_details WHERE account_number = ?"), (account_number,))
    user = cursor.fetchone()
    if not user:
        print("Invalid usernmae")
        return
    amount = float(input("Enter Deposit Amount: "))
    while True:
        if amount <= 0:
            print("Enter valid amount")
        elif amount < 2000:
            print("Minimum deposit is N2,000")
            continue
        break
    old_balance = user[6] if user[6] is not None else 0.0
    new_balance = old_balance + amount

    cursor.execute("UPDATE bank_details SET balance = ? WHERE account_number = ?", (new_balance, account_number))
    conn.commit()

    cursor.execute('''
    INSERT INTO transactions (account_number, type, amount, date) VALUES (?, ?, ?, ?)''', (account_number, "Deposit", amount, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    
    time.sleep(1)


    print(f"Your deposit of {amount} was successful, balance now {new_balance}")
    time.sleep(1.5)
    menu(user)

def withdrawal(user):
    account_number = user[4]
    cursor.execute("SELECT * FROM bank_details WHERE account_number = ?", (account_number,))
    user = cursor.fetchone()

    if not user:
        print("Invalid account number.")
        return

    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid withdrawal amount.")
        return

    cursor.execute("SELECT balance FROM bank_details WHERE account_number = ?", (account_number,))
    result = cursor.fetchone()
    old_balance = result[0] if result and result[0] is not None else 0.0

    if amount > old_balance:
        print("Insufficient funds.")
        return

    new_balance = old_balance - amount

    cursor.execute("UPDATE bank_details SET balance = ? WHERE account_number = ?", (new_balance, account_number))
    conn.commit()

    cursor.execute('''INSERT INTO transactions (account_number, type, amount, date) VALUES (?, ?, ?, ?)''', (account_number, "Withdrawal", amount, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

    time.sleep(1.5)

    print(f"Withdrawal of ₦{amount} successful. New balance: ₦{new_balance}")

    time.sleep(1.5)
    menu(user)

def transactions(user):
    account_number = user[4]
    cursor.execute("SELECT * FROM transactions WHERE account_number = ?", (account_number,))
    records = cursor.fetchall()

    if not records:
        print("No transactions")

    print("\n-----Transaction History-----")
    for Transfer in records:
        time.sleep(1.5)
        print(f"Type: {Transfer[2]} | Amount: N{Transfer[3]} | Date: {Transfer[4]}")

    time.sleep(1)
    menu(user)
  
def transfer(user):
    sender = user[4]
    cursor.execute("SELECT * FROM bank_details WHERE account_number = ?", (sender,))
    sender_acc = cursor.fetchone()

    if not sender_acc:
        print("account not found.")
        return
    receiver = input("Enter receiver's account number: ")
    cursor.execute("SELECT * FROM bank_details WHERE account_number = ?", (receiver,))
    receiver_acc = cursor.fetchone()

    if not receiver_acc:
        print("Receiver account not found")
        return
    if sender == receiver:
        print("Cannot transfer to yourself")
        return

    amount = float(input("Enter transfer amount: "))
    sender_balance = sender_acc[6] if sender_acc[6] is not None else 0.0

    cursor.execute("SELECT balance FROM bank_details WHERE account_number = ?", (sender,))
    sender_balance = cursor.fetchone()[0]

    if amount > sender_balance:
        time.sleep(1)
        print("Insufficient funds.")
        return

    new_sender_balance = sender_balance - amount
    new_receiver_balance = (receiver_acc[6]) + amount

    cursor.execute("UPDATE bank_details SET balance = ? WHERE account_number = ?", (new_sender_balance, sender))
    cursor.execute("UPDATE bank_details SET balance = ? WHERE account_number = ?", (new_receiver_balance, receiver))
    conn.commit()

    cursor.execute('''INSERT INTO transactions (account_number, type, amount, date) VALUES (?, ?, ?, ?)''', (sender, "Transfer Sent", amount, time.strftime("%Y-%m-%d %H:%M:%S")))
    cursor.execute('''INSERT INTO transactions (account_number, type, amount, date) VALUES (?, ?, ?, ?)''', (receiver, "Transfer Received", amount, time.strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()

    time.sleep(1)
    print(f"Transfer of N{amount} to {receiver} successful. New balance: N{new_sender_balance}")

    time.sleep(1.5)
    menu(user)

def menu(user):
    while True:
        time.sleep(1)
        print("\n-----MENU-----")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Transaction History") 
        print("4. Transfer")
        print("5. Exit")

        choice = input("Enter Option: ")

        if choice == '1':
            time.sleep(1.5)
            deposit(user)
        elif choice == '2':
            time.sleep(1.5)
            withdrawal(user)
        elif choice == '3':
            time.sleep(1.5)
            transactions(user)
        elif choice == '4':
            time.sleep(1.5)
            transfer(user)
        elif choice == '5':
            time.sleep(1.5)
            break
        else:
            print("Enter valid option")

def main_menu():
    while True:
        time.sleep(1)
        print("\n-----MAIN MENU-----")
        print("WELCOME TO MelvTheBank")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter option 1-3: ")

        if choice =='1':
            time.sleep(1.5)
            create_account()
        elif choice == '2':
            time.sleep(1.5)
            login()
        elif choice == '3':
            time.sleep(1.5)
            print("Goodbye")
            break
        else:
            time.sleep(1.5)
            print("Invalid Option")
        


main_menu()


# (1, 'fred', 'fred', '701a30c567addeffb1f43e519c92cd0098f1694bee5c3225d019bac03dc1de96', '14030609', 500000, 547000.0, '2025-10-30 12:05:10')
# (2, 'frank', 'frank', '701a30c567addeffb1f43e519c92cd0098f1694bee5c3225d019bac03dc1de96', '15238209', 500000, 10470000.0, '2025-10-30 12:06:40')
# (3, 'oladeji femi', 'femi123', '701a30c567addeffb1f43e519c92cd0098f1694bee5c3225d019bac03dc1de96', '11143858', 1000000, 1238200.0, '2025-10-30 12:50:27')
# (4, 'Mayungbo', 'MelvTheGoat', '701a30c567addeffb1f43e519c92cd0098f1694bee5c3225d019bac03dc1de96', '15117192', 700000, 1170000.0, '2025-11-03 10:53:41')

# import sqlite3

# conn = sqlite3.connect('Bank_detai.db')
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM bank_details")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# conn.close()
