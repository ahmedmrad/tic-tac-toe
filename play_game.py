from tic_tac_toe import *
from instructions import *


def end_game():
    while True:
        try:
            end = input(
                '''

                Do you want to quit ? Y/N:

                '''
            )
        except ValueError:
            print(
                '''

                  Sorry, if you want to quit type Y.
                  If you want to keep playing type N.

                  '''
            )
            continue
        if end.replace(' ', '').upper() not in ['Y', 'N', 'YES', 'NO']:
            print(
                '''

                  Sorry, if you want to quit type Y.
                  If you want to keep playing type N.

                  '''
            )
        else:
            if end.replace(' ', '').upper() in ['Y', 'YES']:
                end = True
            elif end.replace(' ', '').upper() in ['N', 'NO']:
                end = False
        return end


def main():
    board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while True:
        instructions('instructions.txt')
        player2 = opponent_choice()
        player1_marker = marker_choice()
        player2_marker = opponent_marker(player1_marker)
        if player2 == 'player':
            turn_number = 1
            player1_victory_count = 0
            player2_victory_count = 0
            victory = False
            while victory == False:
                (board, index_board_selection) = select_marker_position(
                    board, player1_marker)
                draw_board(board)
                print(board)
                victory = check_victory(board)
                if victory == True:
                    player1_victory_count += 1
                    print(
                        '''

                        player 1 won {0} victory(ies) out of {1} turn(s).

                        '''.format(player1_victory_count, turn_number)
                    )
                    break
                (board, index_board_selection) = select_marker_position(
                    board, player2_marker)
                draw_board(board)
                victory = check_victory(board)
                if victory == True:
                    player2_victory_count += 1
                    print(
                        '''

                        player 2 won {0} victory(ies) out of {1} turn(s).

                        '''.format(player2_victory_count, turn_number)
                    )
                    break
            turn_number += 1
        elif player2 == 'computer':
            print('Leave human')
        end = end_game()
        if end == True:
            break
        else:
            board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


if __name__ == '__main__':
    main()
