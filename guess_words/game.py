import sys
from random import choice, sample
from operator import itemgetter

from allwords import common_words

filler = ' __ '
word: str = choice(common_words()).upper()
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

guessed_letters = set()


def map_inputs(letter, guessing, word=word):
    if not letter in word:
        return guessing
    occurences_ = [i for i,x in enumerate(word) if x == letter]
    for _ in occurences_:
        guessing[_] = letter
    return guessing


while True:
    if ''.join(guess).strip() == word:
        print('Correct')
        break
    print('Letters Guessed:', guessed_letters)
    print(''.join(guess))
    in_char = input('Guess next letter:').upper()
    guessed_letters.add(in_char)
    guess = map_inputs(in_char, guess)
