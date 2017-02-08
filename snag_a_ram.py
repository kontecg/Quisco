# -*- coding: utf-8 -*-
"""
Created on Sun, 05 Feb 2017 02:25:53

@author: konte.cg@gmail.com
"""
import random

dic = []  # list containing all words up to 12 letters from english dictionary.
long_words = []  # list containing words from 8 to 12 letters.

with open('eng.dic', 'r') as f:
    for line in f:
        if len(line) <= 12:
            line = line.strip('\n')
            line = line.replace("'", '')
            dic.append(line.upper())
        else:
            continue

for i in dic:
    if len(i) >= 8:
        long_words.append(i)

word = random.choice(long_words)
shuffle = list(''.join(random.sample(word, len(word))))

while len(shuffle) < 12:
    shuffle.append(chr(random.randrange(65, 91)))

for i in shuffle:
    print(i, end=' ')
print()

user_word = input("Enter your word: ").upper()

if all(l in shuffle for l in list(user_word)):
    if user_word in dic:
        if len(user_word) >= len(word):
            print("You won {} points!".format(len(user_word) * 2 + 3))
        else:
            print("You won {} points!".format(len(user_word) * 2))
    else:
        print("Your word isn't valid. You have 0 points for this game.")
else:
    print("Your word doesn't match with given letters. You have 0 points for this game.")

print("Our word is '{}'".format(word))
