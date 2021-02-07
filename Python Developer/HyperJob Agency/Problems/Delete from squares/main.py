# squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}

user_input = int(input())
try:
    print(squares[user_input])
    del squares[user_input]
except Exception:
    print('There is no such key')
print(squares)