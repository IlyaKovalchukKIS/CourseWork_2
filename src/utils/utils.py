from random import choice

import requests


def load_words_subwords(list_word: str):
    f = requests.get(list_word)
    result = f.json()
    return result


def random_word_in_list(list_word: str):
    return choice(list_word)

