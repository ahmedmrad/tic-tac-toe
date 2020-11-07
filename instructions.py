
def instructions(filename):
    '''Print instructions at the beginning of the game

    :param filename: name of file, should be called instructions.txt
    :type filename: str
    '''
    with open(filename, 'r') as f:
        instructions = f.read()
        print(instructions)


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
            opponent = input(
                '''

                Do you wish to play against another player
                or against the computer ?
                Please type player or computer:

                ''')
        except ValueError:
            print(
                '''

                Sorry I did not understand that.

                ''')
            continue
        if opponent.lower().replace(' ', '') not in ['computer', 'player']:
            print(
                '''

                Sorry I did not understand that.

                ''')
            continue
        else:
            break
    return opponent.lower().replace(' ', '')
