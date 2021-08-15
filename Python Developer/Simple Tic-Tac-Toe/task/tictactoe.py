# print grid in console
def print_grid(grid):
    print("-" * 9)
    for i in range(3):
        print('|', end=' ')
        for j in range(3 * i, 3 * i + 3):
            print(grid[j] if grid[j] != '_' else ' ', end=' ')
        print('|')
    print("-" * 9)


# check if someone wins
def win(grid, sign):
    # rows
    for i in range(3):
        if grid[3 * i] == sign and grid[3 * i + 1] == sign and grid[3 * i + 2] == sign:
            return True

    # columns
    for i in range(3):
        if grid[i] == sign and grid[i + 3] == sign and grid[i + 6] == sign:
            return True

    # main diagonal
    if grid[0] == sign and grid[4] == sign and grid[8] == sign:
        return True

    # side diagonal
    if grid[2] == sign and grid[4] == sign and grid[6] == sign:
        return True

    return False


# check if game is over
def game_over(grid):
    if win(grid, 'X'):
        print('X wins')
        return True
    elif win(grid, 'O'):
        print('O wins')
        return True
    elif grid.count('_') == 0:
        print('Draw')
        return True
    return False


symbols = '_' * 9  # start with empty grid
print_grid(symbols)

step = 0

while True:  # game loop
    while True:  # loop for check user input
        coords = input('Enter the coordinates: ')

        try:
            a, b = map(int, coords.split())
        except Exception as e:
            print('You should enter numbers!')
            continue

        if a not in [1, 2, 3] or b not in [1, 2, 3]:
            print('Coordinates should be from 1 to 3!')
            continue

        if symbols[3 * (a - 1) + (b - 1)] != '_':
            print('This cell is occupied! Choose another one!')
            continue

        index = 3 * (a - 1) + (b - 1)

        if step % 2 == 0:
            symbol = 'X'
        else:
            symbol = 'O'
        symbols = symbols[:index] + symbol + symbols[index + 1:]
        step += 1
        print_grid(symbols)
        break

    if game_over(symbols):
        break
