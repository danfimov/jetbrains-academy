# Write your code here
from random import randint


def generate_card_number():
    global accounts
    keys = accounts.keys()
    while True:
        result = '400000'
        for i in range(9):
            result += str(randint(0, 9))
        check_sum = list(map(int, result))
        check_sum = [check_sum[i] * 2 if i % 2 == 0 else check_sum[i] for i in range(15)]
        check_sum = [elem - 9 if elem > 9 else elem for elem in check_sum]
        result += str((10 - sum(check_sum) % 10))

        if not (result in keys):
            break
    return result


accounts = dict()
balance = dict()
is_login = False
current_account = None
while True:
    if is_login:
        option = int(input('1. Balance\n2. Log out\n0. Exit\n'))
        if option == 1:
            print('Balance:', balance[current_account])
        elif option == 2:
            print('You have successfully logged out!')
            is_login = False

    else:
        option = int(input("1. Create an account\n2. Log into account\n0. Exit\n"))
        if option == 1:
            print('Your card has been created')
            print('Your card number:')
            card_number = generate_card_number()
            print(card_number)
            print('Your card PIN:')
            card_pin = str(randint(1000, 9999))
            print(card_pin)
            accounts[card_number] = card_pin
        elif option == 2:
            print('Enter your card number:')
            card_number = input()
            print('Enter your PIN:')
            card_pin = input()
            if card_number in accounts.keys() and accounts[card_number] == card_pin:
                print('\nYou have successfully logged in!\n')
                is_login = True
                current_account = card_number
            else:
                print('Wrong card number or PIN!')

    if option == 0:
        print('Bye!')
        break
