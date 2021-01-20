#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = """Kyle Thomas, with the use of:
             https://regex101.com/
             https://docs.python.org/3/library/re.html
             """

import re


def make_regex(word):
    "Creates a regex pattern based on the test_word input"
    word_regex = r'^'
    for char in word:
        if char == ' ':
            word_regex += r'\w'
        else:
            word_regex += char
    word_regex += r'$'
    return word_regex


def find_matches(word_list, word, pattern):
    "Searches word_list for possible matches"
    matches = []
    for item in word_list:
        if len(item) == len(word) and re.search(pattern, item):
            matches.append(item)
    if len(matches) == 0:
        print('Could not find a word that matches your input.')
    else:
        for match in matches:
            print(match)


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        'Please enter a word to solve.\n' +
        'Use spaces to signify unknown letters: ').lower()

    find_matches(words, test_word, make_regex(test_word))


if __name__ == '__main__':
    main()
