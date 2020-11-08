import tic_tac_toe


def main():
    board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while True:
        tic_tac_toe.instructions('instructions.txt')
        player2 = tic_tac_toe.opponent_choice()
        player1_marker = tic_tac_toe.marker_choice()
        player2_marker = tic_tac_toe.opponent_marker(player1_marker)
        if player2 == 'player':
            turn_number = 1
            player1_victory_count = 0
            player2_victory_count = 0
            victory = False
            tic_tac_toe.draw_board(board)
            while victory == False:
                (board, player1_board_selection) = tic_tac_toe.select_marker_position(
                    board, player1_marker)
                tic_tac_toe.draw_board(board)
                victory = tic_tac_toe.check_victory(board)
                tie = tic_tac_toe.check_tie(board)
                if victory == True:
                    player1_victory_count += 1
                    print(
                        '''

                            player 1 won {0} victory(ies) out of {1} turn(s).

                            '''.format(player1_victory_count, turn_number)
                    )
                    break
                elif tie == True:
                    print(
                        '''

                            Turn {} was a tie.

                            '''.format(turn_number)
                    )
                    break
                (board, player2_board_selection) = tic_tac_toe.select_marker_position(
                    board, player2_marker)
                tic_tac_toe.draw_board(board)
                victory = tic_tac_toe.check_victory(board)
                tie = tic_tac_toe.check_tie(board)
                if victory == True:
                    player2_victory_count += 1
                    print(
                        '''

                            player 2 won {0} victory(ies) out of {1} turn(s).

                            '''.format(player2_victory_count, turn_number)
                    )
                    break
                elif tie == True:
                    print(
                        '''

                            Turn {} was a tie.

                            '''.format(turn_number)
                    )
                    break

            turn_number += 1
        elif player2 == 'computer':
            print(
                '''

                  AI not implemented yet.
                  Sorry, play against another human.

                  '''
            )
        end = tic_tac_toe.end_game()
        if end == True:
            break
        else:
            board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


if __name__ == '__main__':
    main()
