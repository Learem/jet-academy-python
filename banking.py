import random
import sqlite3


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


def generate_digit():
    return str(random.randint(0, 9))


def generate_luhn_digit(num):
    digits = [int(char) for char in num[0:15]]
    for i in range(0, 15, 2):
        digits[i] = digits[i] * 2
        if digits[i] > 9:
            digits[i] -= 9
    total = 0
    for item in digits:
        total += item
    return (10 - total % 10) % 10


def generate_card_num():
    new_card_num = "400000"
    for _ in range(9):
        new_card_num += generate_digit()
    return new_card_num + str(generate_luhn_digit(new_card_num))


def generate_pin():
    new_pin = ""
    for _ in range(4):
        new_pin += generate_digit()
    return new_pin


def grant_access(account, code):
    cur.execute(f"SELECT number FROM card WHERE number = {account} AND pin = {code};")
    return cur.fetchone()


def get_balance(account):
    cur.execute(f"SELECT balance FROM card WHERE number = {account};")
    result = cur.fetchone()
    return result[0]


def add_balance(account, amount):
    cur.execute(f"UPDATE card SET balance = balance + {amount} WHERE number = {account};")
    conn.commit()


def sub_balance(account, amount):
    cur.execute(f"SELECT balance FROM card WHERE number = {account};")
    result = cur.fetchone()
    if result[0] < amount:
        return False
    else:
        cur.execute(f"UPDATE card SET balance = balance - {amount} WHERE number = {account};")
        conn.commit()
        return True


def close_account(account):
    cur.execute(f"DELETE FROM card WHERE number = {account};")
    conn.commit()


def is_present_card(account):
    cur.execute(f"SELECT number FROM card WHERE number = {account};")
    return cur.fetchone()


def check_account(account):
    if account == account[0:15] + str(generate_luhn_digit(account)):
        if is_present_card(account):
            return True
        else:
            print("Such a card does not exist.")
            print()
            return False
    else:
        print("Probably you made a mistake in the card number. Please try again!")
        print()
        return False


def account_menu(account):
    while True:
        print("1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        choice_1 = input()
        if choice_1 == "1":
            print()
            print("Balance:", get_balance(account))
            print()
        if choice_1 == "5":
            print()
            print("You have successfully logged out!")
            print()
            return "logout"
        if choice_1 == "2":
            print()
            print("Enter income:")
            income = int(input())
            add_balance(account, income)
            print("Income was added!")
            print()
        if choice_1 == "4":
            print()
            close_account(account)
            print("The account has been closed!")
            print()
            return "close"
        if choice_1 == "3":
            print()
            print("Transfer")
            print("Enter card number:")
            number = input()
            if account == number:
                print("You can't transfer money to the same account!")
                print()
            elif check_account(number):
                print("Enter how much money you want to transfer:")
                income = int(input())
                if sub_balance(account, income):
                    add_balance(number, income)
                    print("Success!")
                    print()
                else:
                    print("Not enough money!")
                    print()
        if choice_1 == "0":
            return "exit"


cur.execute("""
    CREATE TABLE IF NOT EXISTS card (
        id INTEGER,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
    );
""")
conn.commit()
while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    my_choice = input()
    if my_choice == "0":
        print()
        print("Bye!")
        break
    if my_choice == "1":
        print()
        print("Your card has been created")
        new_account = generate_card_num()
        new_PIN = generate_pin()
        cur.execute(f"INSERT INTO card (number, pin) VALUES ('{new_account}', '{new_PIN}');")
        conn.commit()
        print("Your card number:")
        print(new_account)
        print("Your card PIN:")
        print(new_PIN)
        print()
    if my_choice == "2":
        print()
        print("Enter your card number:")
        my_account = input()
        print("Enter your PIN:")
        my_PIN = input()
        if grant_access(my_account, my_PIN):
            print()
            print("You have successfully logged in!")
            print()
            if account_menu(my_account) == "exit":
                print()
                print("Bye!")
                break
        else:
            print()
            print("Wrong card number or PIN!")
            print()
    if my_choice == "999":
        cur.execute("SELECT * FROM card;")
        print(cur.fetchall())
conn.close()
