#
# pyhangman - 'Hangman' clone developed in python
# CREATED BY CONOR MCCORMICK
# Script to get the words to use for CPU games
#

import pandas as pd
import random

def get_word():
    wordsFrame = pd.read_csv('words.csv')
    words = wordsFrame["Word"].values
    definitions = wordsFrame["Definitions"].values
    selection = random.randint(1, len(words))
    selected_word = words[selection]
    word_definition = definitions[selection]
    return selected_word, word_definition