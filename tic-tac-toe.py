board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def instructions(filename):
    '''Print instructions at the beginning of the game

    :param filename: name of file, should be called instructions.txt
    :type filename: str
    '''
    with open(filename, 'r') as f:
        instructions = f.read()
        print(instructions)


def draw_board(board):
    '''Print board and board elements as they are updated
    '''
    print('' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print('' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print('' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def user_choice():
    '''Input wich marker X or O for the game

    :returns user_choise: user input representing board marker X or O
    :rtype user_choice: str
    '''
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
        if user_choice.upper() not in ['X', 'O']:
            print(
                '''

                Sorry I did not understand that. Type your marker again

                ''')
            continue
        else:
            break
    return user_choice.upper()


def opponent_choice():
    '''Choose playing agains another player or the computer

    :returns opponent choice: another player (human) or computer (ai)
    :rtype opponent_choice: str
    '''
    while True:
        try:
            opponent_choice = input(
                '''

                Do you wish to play agains another player
                or against the computer ?
                Please type player or computer:

                ''')
        except ValueError:
            print(
                '''

                Sorry I did not understand that.

                ''')
            continue
        if opponent_choice.lower().replace(' ', '') not in ['computer', 'player']:
            print(
                '''

                Sorry I did not understand that.

                ''')
            continue
        else:
            break
    return opponent_choice.lower().replace(' ', '')


def select_marker_position(board, user_choice):
    '''Select where to place marker with list index

    :param board:
    :type board: list
    :param user_choice: marker choice X or O
    :type user_choice: tr
    :returns board: updated marker list according to index choice
    :rtype board: list
    '''
    while True:
        try:
            index_board_selection = input(
                '''

                Please select the index position for your marker.
                Choose an index between(1 - 9).

                '''
            )
        except ValueError:
            print(
                '''

                  Sorry that is not a digit.
                  Enter a number between(1 - 9)

                  '''
            )
            continue
        if int(index_board_selection) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(
                '''

                  Sorry you either did not enter a digit or
                  entered the wrong number.
                  Enter a number between(1 - 9)

                  '''
            )
        else:
            break
    board[index_board_selection] = user_choice
    return board


def select_mode(opponent_choice):
    '''Determine in what mode the game will be played

    :param opponent_choice: user input for opponent selection
    :type opponent_choice: str
    :returns mode: mode of the game, computer(ai) or player(human)
    :rtype mode: str
    '''
    if opponent_choice == 'computer':
        mode = 'computer'
    elif opponent_choice == 'player'
        mode = 'player'
    return mode
