

def display_board():
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]}')


def update_board(position):
    global board
    if not(board[position - 1] in range(1, 10)):
        return False

    board[position - 1] = current_player
    return True


def get_position():
    result = False

    while not result:
        result = check_input(input(f'\nChose your position, {current_player}: '))

    return result


def check_input(user_input):
    try:
        result = int(user_input)
        return result if result in range(1, 10) else False
    except ValueError:
        return False


def check_result():
    wins_numbers = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    result = False

    for a, b, c in wins_numbers:
        result = board[a - 1] == board[b - 1] == board[c - 1]

        if result:
            break

    return result


board = list(range(1, 10))
play = True
current_player = 'X'

print('\nWelcome to Tic-Tac-Toe !!!')

while play:
    position = get_position()
    update_board(position)
    display_board()

    if check_result():
        print(f'\n{current_player} wins, congrats !!!')
        print('Thanks for playing...')
        play = False
        break

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


