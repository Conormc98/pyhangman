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
    selection = random.randint(1, len(words) + 1)
    selected_word = words[selection]
    return selected_word