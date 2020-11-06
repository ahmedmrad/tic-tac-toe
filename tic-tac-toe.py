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
    print('         ')
    print('' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print('' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print('' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('         ')


def marker_choice():
    '''Input wich marker X or O for the game

    :raise ValueError: ValueError if x,o X or O is not entered
    :returns marker_choice: user input representing board marker X or O
    :rtype marker_choice: str
    '''
    while True:
        try:
            marker_choice = input(
                '''

                Please choose your marker X or O:

                ''')
        except ValueError:
            print(
                '''

                Sorry I did not understand that. Type your marker again

                ''')
            continue
        if marker_choice.upper() not in ['X', 'O']:
            print(
                '''

                Sorry I did not understand that. Type your marker again

                ''')
            continue
        else:
            break
    return marker_choice.upper()


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


def select_marker_position(board, marker_choice):
    '''Select where to place marker with list index

    :param board:
    :type board: list
    :param user_choice: marker choice X or O
    :type user_choice: tr
    :returns board: updated marker list according to index choice
    :rtype board: list
    :returns index_board_selection: index of the marker during the turn
    :rtype index_board_selection: int
    '''
    while ' ' in board:
        try:
            index_board_selection = int(input(
                '''

                Please select the index position for your marker.
                Choose an index between(1 - 9).

                '''
            ))
        except ValueError:
            print(
                '''

                  Sorry that is not a digit.
                  Enter a number between(1 - 9)

                  '''
            )
            continue
        if index_board_selection not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(
                '''

                  Sorry you either did not enter a digit or
                  entered the wrong number.
                  Enter a number between(1 - 9)

                  '''
            )
            continue
        elif board[index_board_selection] != ' ':
            print(
                '''
                  This index is ticked
                  please choose another one.

                '''
            )
            continue
        else:
            board[index_board_selection] = marker_choice
        return board, index_board_selection
    else:
        print('Board full')


def select_mode(opponent_choice):
    '''Determine in what mode the game will be played

    :param opponent_choice: user input for opponent selection
    :type opponent_choice: str
    :returns mode: mode of the game, computer(ai) or player(human)
    :rtype mode: str
    '''
    if opponent_choice == 'computer':
        mode = 'computer'
    elif opponent_choice == 'player':
        mode = 'player'
    return mode


def check_victory(board):
    '''Check if the victory condition is met

    :param board: list of marker elements in the board list
    :type board:s list
    :returns check_victory: victory condition met or not
    :rtype check_victory: bool
    '''
    if (board[1] == board[2] == board[3]) == True:
        check_victory = True
    elif (board[4] == board[5] == board[6]) == True:
        check_victory = True
    elif (board[7] == board[8] == board[9]) == True:
        check_victory = True
    elif (board[1] == board[4] == board[7]) == True:
        check_victory = True
    elif (board[2] == board[5] == board[8]) == True:
        check_victory = True
    elif (board[3] == board[6] == board[9]) == True:
        check_victory = True
    elif (board[7] == board[5] == board[3]) == True:
        check_victory = True
    elif (board[1] == board[5] == board[9]) == True:
        check_victory = True
    else:
        check_victory = False
    return check_victory


def check_tie(board):
    '''Check if there is a tie, game ended

    :param board: list of marker elements in the board list
    :type board: list
    :returns check_tie: tie condition met or not
    :rtype check_tie: bool
    '''
    if ' ' not in board:
        check_tie = True
    else:
        check_tie = False
    return check_tie
