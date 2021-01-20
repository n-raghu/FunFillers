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

incorrect_letters = set()


def map_inputs(letter, guessing, word=word):
    if not letter in word:
        return guessing, False
    occurences_ = [i for i,x in enumerate(word) if x == letter]
    for _ in occurences_:
        guessing[_] = letter
    return guessing, True


while True:
    if ''.join(guess).strip() == word:
        print(f'Correct, the word is {word}')
        break
    if len(incorrect_letters) > 0:
        print('Miss Fired:', incorrect_letters)
    print(''.join(guess))
    in_char = input('Guess next letter:').upper()
    guess, hit = map_inputs(in_char, guess)
    if not hit:
        incorrect_letters.add(in_char)
