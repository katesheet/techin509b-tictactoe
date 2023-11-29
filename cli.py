# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Game

# Reminder to check all the tests

if __name__ == '__main__':
    # player_num = input('please input player number: ')
    # player_num = int(player_num)
    # game = Game(player_num)
    # game.play_game()
    for i in range(50):
        game = Game(0)
        game.play_game()