#
# pyhangman - 'Hangman' clone developed in python
# CREATED BY CONOR MCCORMICK
# Main script file to run the game
#

import gamemodes

def start_game():
    print('\nWelcome to pyhangman!\n')
    print('What kind of game would you like to play?')
    game_mode = input('0 - Player vs CPU; 1 - Player vs Player\n')
    if (game_mode == "0"):
        gamemodes.player_vs_cpu()
    elif (game_mode == "1"):
        gamemodes.player_vs_player()
    else:
        print('\nInvalid game mode.\n\n\n')
        start_game()

start_game()