#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    m_dict = {}
    with open(filename, 'r') as fp:
        data = ' '.join(fp.read().split()).replace('!', '').replace('.', '') \
            .replace(',', '').replace('-', '').replace('?', '').replace(';', '') \
            .replace('`', '').replace(':', '').replace('_', '').replace('"', '') \
            .replace("'", '').replace('(', '').replace(')', '')
        data = data.split(' ')

        # ? How to iterate and get index same time in for loop ? Going with while for now
        while len(data) >= 2:
            if data[0] in m_dict:
                tmp_list = m_dict.get(data[0])
                tmp_list.append(data[1])
            else:
                m_dict[data[0]] = [data[1]]

            # Remove 1st element to always work in the beginning of the list
            data.pop(0)

    return m_dict


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    line, text = '', ''

    # Iterating 200 time to pick up random keys and values
    for count in range(0, 200):
        key = random.choice(list(mimic_dict.keys()))
        val = mimic_dict.get(key)
        line += ('{} {} '.format(key, random.choice(val)))

        # print 70 columns per line
        if len(line) > 70:
            text += line + '\n'
            line = ''

    print(text)
    return True


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
