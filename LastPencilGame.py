import sys


class GameVariables:
    """For setting and using game variables."""
    def __init__(self):
        self.number_of_pencils = 0
        self.john_human = 'John'
        self.jack_bot = 'Jack'


# to instantiate an instance of the GameVariables class
gv = GameVariables()


def number_of_pencils():
    """To set the number of pencils to start with. Only a positive numeric is accepted. Appropriate prompts are given if
    required."""
    try:
        gv.number_of_pencils = int(input('How many pencils would you like to use: '))
    except ValueError:
        print("The number of pencils should be numeric")
        number_of_pencils()

    if gv.number_of_pencils < 1:
        print("The number of pencils should be positive")
        number_of_pencils()

    choose_starter()


def choose_starter():
    """To set which player John(human) or Jack(bot) will go first."""

    starter = input(f'Who will be the first (John, Jack): ')

    # deals with case where input != John or Jack
    while starter not in ['Jack', 'John']:
        print(f'Choose between John and Jack')
        choose_starter()

    if starter == 'John':
        john_human_game_play()
    elif starter == 'Jack':
        jack_bot_game_play()


def john_human_game_play():
    """Prompts the user for input (number of pencils to take: 1 - 3). Prompts are given to address any incorrect
    input. User input is deducted from number_of_pencils. If no pencils are left after turn is taken then Jack(bot) is
    declared the winner. If there are pencil(s) left after turn is taken then jack_bot_game_play is called and the game
    continues."""

    # Prints a graphical representation of the number_of_pencils left
    print('|' * gv.number_of_pencils)

    number_of_pencils_to_be_taken_by_john = input("John's turn! ")

    if number_of_pencils_to_be_taken_by_john not in ['1', '2', '3']:
        print("Possible values: '1', '2' or '3'")
        john_human_game_play()

    elif int(number_of_pencils_to_be_taken_by_john) > gv.number_of_pencils:
        print('Too many pencils were taken.')
        john_human_game_play()

    else:
        gv.number_of_pencils -= int(number_of_pencils_to_be_taken_by_john)

        if gv.number_of_pencils < 1:
            # print(number_of_pencils_to_be_taken_by_john)
            print('Jack won!')
            sys.exit()
        else:
            # print(number_of_pencils_to_be_taken_by_john)
            jack_bot_game_play()


def jack_bot_game_play():
    """Algorithm for jack_bot to follow the winning strategy if in number_of_pencils left. If after taking turn no
    pencils are left then John(human) is declared the winner. If there are pencils left john_human_gameplay function
    is called. Game continues."""

    # Prints a graphical representation of the number_of_pencils left
    print('|' * gv.number_of_pencils)

    print("Jack's turn:")

    # Checks for and follows winning strategy if in number_of_pencils left.
    if gv.number_of_pencils % 4 == 0:
        gv.number_of_pencils -= 3
        print('3')
    elif gv.number_of_pencils % 4 == 3:
        gv.number_of_pencils -= 2
        print('2')
    elif gv.number_of_pencils % 4 == 2:
        gv.number_of_pencils -= 1
        print('1')
    else:
        # For case when there is no winning strategy for jack_bot in current position. One pencil is taken in case only
        # one pencil is left.
        gv.number_of_pencils -= 1
        print('1')

    # John is declared winner if no pencils left after jack_bot turn to remove pencil(s) is taken.
    if gv.number_of_pencils < 1:
        print('John won!')
        sys.exit()

    # Send game play back to john_human_game_play if there are pencils left.
    else:
        john_human_game_play()


if __name__ == "__main__":
    number_of_pencils()