import sys
from time import time
from random import choice, sample
from operator import itemgetter

from allwords import common_words


def map_inputs(letter, guessing, word):
    if not letter in word:
        return guessing, False
    occurences_ = [i for i,x in enumerate(word) if x == letter]
    for _ in occurences_:
        guessing[_] = letter
    return guessing, True


def get_suitable_word(all_words=common_words) -> str:
    while True:
        _word = choice(common_words()).upper()
        if len(_word) < 4:
            continue
        return _word


def calculate_score(_attempts, _len) -> float:
    score = _len / (_attempts + _len)
    return round(100 * score, 1)


filler = ' __ '
word = get_suitable_word()
guess = [filler for _ in range(len(word))]
nchars = int(0.36 * len(word))
nchars = nchars + 1 if nchars == 1 else nchars
first_chars = sample(word, nchars)

n = 0
breakpoint = False
for l in first_chars:
    if breakpoint:
        break
    for i,k in enumerate(word):
        if l == k:
            guess[i] = l
            n += 1
            if n == 2:
                breakpoint = True

incorrect_letters = set()
t = time()

while True:
    if ''.join(guess).strip() == word:
        total_time = int(time() - t)
        print(f'Correct, the word is "{word}". ')
        score = calculate_score(len(incorrect_letters), len(word))
        time_bonus = 180 - total_time
        print(f'\nGuess({score}) | TimeBonus({time_bonus})')
        break
    if len(incorrect_letters) > 0:
        print('Miss Fired:', incorrect_letters)
    print(''.join(guess))
    in_char = input('Guess next letter:').upper()
    guess, hit = map_inputs(in_char, guess, word)
    if not hit:
        incorrect_letters.add(in_char)
