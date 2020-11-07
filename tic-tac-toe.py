from instructions import *


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


def opponent_marker(marker_choice):
    if marker_choice == 'X':
        opponent_choice = 'O'
    elif marker_choice == 'O':
        opponent_choice = 'X'
    return opponent_choice


def select_marker_position(board, marker_choice):
    '''Select where to place marker with list index

    :param board:
    :type board: list
    :param marker_choice: marker choice X or O
    :type marker_choice: str
    :returns board: updated marker list according to index choice
    :rtype board: list
    :returns index_board_selection: index of the marker during the turn
    :rtype index_board_selection: int
    '''
    while True:
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


def check_victory(board):
    '''Check if the victory condition is met

    :param board: list of marker elements in the board list
    :type board:s list
    :returns victory: victory condition met or not
    :rtype victory: bool
    '''
    if (board[1] != ' ' and board[2] != ' ' and board[3] != ' ') and (board[1] == board[2] == board[3]):
        victory = True
    elif (board[4] != ' ' and board[5] != ' ' and board[6] != ' ') and (board[4] == board[5] == board[6]):
        victory = True
    elif (board[7] != ' ' and board[8] != ' ' and board[9] != ' ') and (board[7] == board[8] == board[9]):
        victory = True
    elif (board[1] != ' ' and board[4] != ' ' and board[7] != ' ') and (board[1] == board[4] == board[7]):
        victory = True
    elif (board[2] != ' ' and board[5] != ' ' and board[8] != ' ') and (board[2] == board[5] == board[8]):
        victory = True
    elif (board[3] != ' ' and board[6] != ' ' and board[9] != ' ') and (board[3] == board[6] == board[9]):
        victory = True
    elif (board[7] != ' ' and board[5] != ' ' and board[3] != ' ') and (board[7] == board[5] == board[3]):
        victory = True
    elif (board[1] != ' ' and board[5] != ' ' and board[9] != ' ') and (board[1] == board[5] == board[9]):
        victory = True
    else:
        victory = False
    return victory


def check_tie(board):
    '''Check if there is a tie, game ended

    :param board: list of marker elements in the board list
    :type board: list
    :returns check_tie: tie condition met or not
    :rtype check_tie: bool
    '''
    if ' ' not in board:
        tie = True
    else:
        tie = False
    return tie


def main():
    board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    instructions('instructions.txt')
    player2 = opponent_choice()
    player1_marker = marker_choice()
    player2_marker = opponent_marker(player1_marker)
    print(player1_marker)
    print(player2_marker)
    if player2 == 'player':
        turn_number = 0
        while turn_number <= 5:
            print(
                '''

                  Turn number {}

                  '''.format(turn_number + 1)
            )
            (board, index_board_selection) = select_marker_position(
                board, player1_marker)
            draw_board(board)
            print(board)
            if check_victory(board) == True:
                print(
                    '''

                      player 1 won

                      '''
                )
                break
            (board, index_board_selection) = select_marker_position(
                board, player2_marker)
            draw_board(board)
            if check_victory(board) == True:
                print(
                    '''

                      player 2 won

                      '''
                )
                break
            turn_number += 1
    elif player2 == 'computer':
        print('Leave human')


if __name__ == '__main__':
    main()
