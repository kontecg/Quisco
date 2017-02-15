# -*- coding: utf-8 -*-
"""
Created on Sun, 05 Feb 2017 02:25:53

@author: konte.cg@gmail.com
"""
import random

vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'


dict = []  # list containing all words up to 12 letters from english dictionary.
word_scores = {}  # dictionary containing scores for each word in dict.

with open('eng.dic', 'r') as f:
    # appending all words up to 12 letters in dict.
    for line in f:
        if len(line) <= 12:
            line = line.strip('\n')
            line = line.replace("'", '')
            dict.append(line.upper())
        else:
            continue

for word in dict:
    # adding word as key and its score as value in word_scores dictionary.
    word_scores[word] = len(word) * 2


def valid_word(word, letters, dict):
    """
    Returns True if word is in dict and is entirely
    composed of offered letters. Otherwise, returns False.

    word: string
    letters: list of strings
    dict: list of strings
    """
    test_word = ''
    if word in dict and all(l in letters for l in list(word)):
        for l in word:
            if word.count(l) <= letters.count(l):
                test_word += l
    if test_word == word:
        return True
    else:
        return False


def choose_word(letters, word_scores):
    """
    Iterate through words in word_scores, find the one that gives
    the maximum value score considering available letters, and return it.

    If no word can be made from the available letters, return None.

    letters: list of strings
    wordList: dictionary (string: int)

    returns: string or None
    """
    best_score = 0
    best_word = None
    for word in word_scores:
        if valid_word(word, letters, word_scores):
            # find out how much making that word is worth
            score = word_scores[word]
            # If the score for that word is higher than your best score
            if score > best_score:
                # update your best score, and best word accordingly
                best_score = score
                best_word = word
    return best_word

letters = []  # list of letters to choose from.

num_of_vowels = random.randrange(4, 7)  # deciding number of vowels (between 4 and 6).

for i in range(num_of_vowels):
    # appending vowels in list of available letters.
    v = random.choice(vowels)
    letters.append(v)

while len(letters) < 12:
    # filling up list with consonants.
    c = random.choice(consonants)
    letters.append(c)

random.shuffle(letters)  # shuffle list of available letters.

print('Available letters: ', end=' ')

for i in letters:
    # print each letter.
    print(i, end=' ')
print()

computer_word = choose_word(letters, word_scores)

while True:
    user_word = input("Enter your word: ").upper()
    if valid_word(user_word, letters, dict):
        score = word_scores[user_word]
        if len(user_word) >= len(computer_word):
            print("You won {} points!".format(score + 3))
            break
        else:
            print("You won {} points!".format(score))
            break
    else:
        print("Your word isn't valid. Try again.")
        print()

print("Our word is '{}'.".format(computer_word))
