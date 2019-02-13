#
# pyhangman - 'Hangman' clone developed in python
# CREATED BY CONOR MCCORMICK
# Script to run the games
#

import wordhandler
import os

def player_vs_cpu():
    print('\nPlayer vs CPU game.\n')
    word, definition = wordhandler.get_word()
    init_game(word, definition)

def player_vs_player():
    print('\nPlayer vs Player game.\n')
    word = input("Please choose a word for the other player to guess.\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    init_game(word.lower())

def init_game(word, definition):
    lives = 6
    draw_lives(lives)
    letters_questions = []
    for i in range(len(word)):
        letters_questions.append("?")
    draw_letters(letters_questions, definition)
    letters_answers = list(word)
    guessed_letters = []
    game_loop(lives, letters_questions, letters_answers, guessed_letters,\
    definition)

def game_loop(lives, letters_questions, letters_answers, guessed_letters,\
definition):
    print("\nGuessed Letters:\n")
    print(guessed_letters)
    print("\n")
    guess = input("Guess a letter to find in the word.\n").lower()
    if(len(guess) == 1):
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess not in letters_answers:
                lives -= 1
            else:
                for i in range(len(letters_answers)):
                    if (letters_answers[i] == guess):
                        letters_questions[i] = guess
                        if letters_questions == letters_answers:
                            print("\nYOU WIN!\n")
                            update_log(letters_answers, "WIN")
                            return None
        else:
            print("\nLetter has already been guessed!\n")
    draw_lives(lives)
    draw_letters(letters_questions, definition)
    if (lives < 1):
        print("\nYOU LOSE!\nThe word was:")
        word = ''.join(letters_answers)
        print(word)
        update_log(letters_answers, "LOSS")
        return None
    game_loop(lives, letters_questions, letters_answers, guessed_letters,\
    definition)

def update_log(letters_answers, result):
    word = ''.join(letters_answers)
    log = open('log.txt', 'a')
    to_write_list = [word, " [", result, "] \n"]
    to_write = ''.join(to_write_list)
    log.write(to_write)
    log.close()

def draw_lives(lives):
    clear = os.system('clear')
    print("\n")
    print("----------")
    print("|        |")

    if(lives < 6):
        print("|        O")
    else:
        print("|")

    if(lives == 4):
        print("|        |")
    elif(lives == 3):
        print("|       \|")
    elif(lives < 3):
        print("|       \|/")
    else:
        print("|")

    if (lives == 1):
        print("|       /")
    elif (lives < 1):
        print("|       /\\")
    else:
        print("|")

    print("----------\n")

def draw_letters(letters_questions, definition):
    print("\n")
    print(definition)
    print("\n")
    for i in range(len(letters_questions)):
        if letters_questions[i] == "?":
            print("-", end="")
        else:
            print(letters_questions[i], end="")
    print("\n")