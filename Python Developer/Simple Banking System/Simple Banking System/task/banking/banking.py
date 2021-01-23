# Write your code here
from random import randint, seed
import sqlite3

CREATE_CARD_TABLE = 'CREATE TABLE IF NOT EXISTS card ' \
                    '(id INTEGER PRIMARY KEY, "number" TEXT, pin TEXT, balance INTEGER);'
INSERT_CARD = 'INSERT INTO card ("number", pin, balance) VALUES (?, ?, ?);'
GET_ALL_CARDS = 'SELECT * FROM card'
GET_CARD_BY_NUMBER = 'SELECT * FROM card WHERE "number" = ?'
GET_CARD_BY_NUMBER_AND_PIN = 'SELECT * FROM card WHERE "number" = ? AND pin = ?'
DELETE_CARD_BY_NUMBER = 'DELETE FROM card WHERE "number" = ?'


def connect():
    return sqlite3.connect('card.s3db')


def create_table(connection):
    with connection:
        connection.execute(CREATE_CARD_TABLE)


def add_card(connection, number, pin, balance=0):
    with connection:
        connection.execute(INSERT_CARD, (number, pin, balance))


def get_all_cards(connection):
    with connection:
        return connection.execute(GET_ALL_CARDS).fetchall()


def get_card_by_number(connection, number):
    with connection:
        return connection.execute(GET_CARD_BY_NUMBER, (number,)).fetchone()


def get_card_by_number_and_pin(connection, number, pin):
    with connection:
        return connection.execute(GET_CARD_BY_NUMBER_AND_PIN, (number, pin)).fetchone()


def delete_card_by_number(connection, number):
    with connection:
        connection.execute(DELETE_CARD_BY_NUMBER, (number,))


def change_money(connection, card, money):
    with connection:
        id, number, pin, balance = get_card_by_number(connection, card)
        delete_card_by_number(connection, card)
        add_card(connection, number, pin, balance + money)


MENU_PROMPT = """
1. Create an account
2. Log into account
0. Exit
"""

MENU_USER_PROMPT = """
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
"""

MENU_NEW_CARD_PROMPT = """
Your card has been created
Your card number:
{number}
Your card PIN:
{pin}
"""


def is_valid_card(card_number):
    print(card_number)
    return int(card_number[-1]) == luhn_algorithm(card_number[:len(card_number) - 1]) and \
           card_number[0] == '4' and \
           len(card_number) == 16


def luhn_algorithm(part_of_the_card_number):
    # str to list
    check_sum = list(map(int, part_of_the_card_number))
    # multiply every second digit by 2
    check_sum = [check_sum[i] * 2 if i % 2 == 0 else check_sum[i] for i in range(15)]
    # subtract 9 from each element greater than 9
    check_sum = [elem - 9 if elem > 9 else elem for elem in check_sum]
    # return checksum
    return (10 - sum(check_sum) % 10) % 10


def generate_card_number():
    global conn
    while True:
        result = '400000'  # our Bank Identification Number
        result += ''.join([str(randint(0, 9)) for i in range(9)])  # random 9 digits
        result += str(luhn_algorithm(result))  # last correct number

        if not get_card_by_number(conn, result):  # if new card not already exist in database
            break
    return result


def null_balance(connection):
    cards = get_all_cards(connection)
    for card in cards:
        id, number, pin, balance = card
        delete_card_by_number(conn, number)
        add_card(conn, number, pin, 0)


seed()
conn = connect()
create_table(conn)

is_login = False
current_account_number = None
while (user_input := int(input(MENU_USER_PROMPT if is_login else MENU_PROMPT))) != 0:
    if is_login:
        if user_input == 1:
            balance = get_card_by_number(conn, current_account_number)[3]
            print('Balance:', balance)
        elif user_input == 2:
            income = int(input('Enter income:\n'))
            print('Income was added!\n')
            change_money(conn, current_account_number, income)
        elif user_input == 3:
            transfer_card_number = input('Transfer\nEnter card number:\n')
            transfer_card = get_card_by_number(conn, transfer_card_number)
            if not is_valid_card(transfer_card_number):
                print('Probably you made a mistake in the card number. Please try again!')
            elif not transfer_card:
                print('Such a card does not exist.')
            elif transfer_card[1] == current_account_number:
                print("You can't transfer money to the same account!")
            else:
                transfer_money = int(input('Enter how much money you want to transfer:\n'))
                id, number, pin, balance = get_card_by_number(conn, current_account_number)
                if balance < transfer_money or balance == 25000:
                    print('Not enough money!')
                else:
                    change_money(conn, current_account_number, -transfer_money)
                    change_money(conn, transfer_card_number, transfer_money)
                    print('Success!')
        elif user_input == 4:
            delete_card_by_number(conn, current_account_number)
            print('The account has been closed!')
            is_login = False
            current_account_number = None
        elif user_input == 5:
            print('You have successfully logged out!')
            is_login = False
            current_account_number = None
        else:
            print('Invalid input, please try again!')
    else:
        if user_input == 1:
            card_number = generate_card_number()
            card_pin = str(randint(1000, 9999))
            # add new card and pin  in databases
            add_card(conn, card_number, card_pin)
            print(MENU_NEW_CARD_PROMPT.format(number=card_number, pin=card_pin))
        elif user_input == 2:
            card_number = input('Enter your card number:\n').strip()
            card_pin = input('Enter your PIN:\n').strip()
            card = get_card_by_number_and_pin(conn, card_number, card_pin)
            if card:
                print('You have successfully logged in!\n')
                is_login = True
                current_account_number = card_number
            else:
                print('Wrong card number or PIN!')
        else:
            print('Invalid input, please try again!')
print('Bye!')

