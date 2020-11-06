board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def instructions(filename):
    with open(filename, 'r') as f:
        instructions = f.read()
        print(instructions)


def draw_board(board):
    print('' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print('' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print('' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def user_choice():
    while True:
        try:
        user_choice = input(
                            '''

                            Please choose your marker X or O:

                            ''')
    except ValueError:
        print(
              '''

              Sorry I did not understand that. Type your marker again

              ''')
        continue
    if user_choice not in ['X', 'O']:

    pass


def opponent_choice():
    pass


def select_marker_position():
    pass


def update_board():
    pass
