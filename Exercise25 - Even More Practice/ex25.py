__author__ = 'phpgeek'

# these line prevent error "SyntaxError of Non-ASCII character"
# -*- coding: utf-8 -*-

'''
We're going to do some more practice involving functions and variables to make sure you
know them well. This exercise should be straightforward for you to type in, break down,
and understand.

However, this exercise is a little different. You won't be running it. Instead you will import it into
Python and run the functions yourself.

First, run this like normal with python ex25.py to fi nd any errors you have made. Once you have
found all the errors you can and fi xed them, you will then want to follow the WYSS section to
complete the exercise.

To use function on this file:
1. import ex25
2. call a function that you want in this file
'''

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(- 1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)