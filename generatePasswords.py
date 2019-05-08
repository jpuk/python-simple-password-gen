#!/usr/bin/env python3
"""
Module Docstring
"""
__author__ = "John Porter"
__version__ = "0.1.1"
__license__ = "MIT License"
# MIT License
#
# Copyright (c) 2019 John Porter
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#################################################################################

# Python script to generate simple password combinations
#
# It can be run as either a module from within your own script or as a standalone program on the command line.
#
# When running from the command line you can adjust the default values in this file after "if _name__ == "__main__":"
# to provide defaults options that are applied if you do not provide any command line arguments.
#
# To see a full list of command line options run python ./generatePassword.py --help
#
# When used as a module from within your own script generate_passwords(...) will return a list of
# passwords.
# All values provided to generate_passwords() are optional and if none are provided it will default to the values
# predefined in the generatePasswords() function.
#
# Example with options provided to generate_passwords():
#
# from generatePasswords import generate_passwords
# password_list = generate_passwords(number_of_nouns = 1,
#                                   number_of_verbs = 1,
#                                   number_of_adverbs = 1,
#                                   number_of_adjectives = 1,
#                                   number_of_symbols = 1,
#                                   number_range = (0, 99),
#                                   number_of_passwords = 25,
#                                   shuffle_password = True,
#                                   display_passwords = False)
# print(password_list)
#
import random
import secrets
import argparse
import os


def openfile(fn):
    # check file exists and is not empty
    if os.path.isfile(fn):
        result = os.stat(fn)
        if result.st_size < 1:
            print("File {} is empty. Exiting.".format(fn))
            exit(0)
    try:
        fp = open(fn, 'r')
        return fp
    except:
        print("Could not open file {}, check file exists and you have permission to read it. Exiting.".format(fn))
        exit(0)


def get_random_value(word_list):
    return secrets.choice(word_list).capitalize()

# enter a value for the number of words or symbols from each category from which the password will be formed
# enter a lower and upper range for the number components of the password
# enter number of passwords to generate
# choose to shuffle the password components or leave them in the order generated

# the default option values in this function definition are overridden when run from the command line.
def generate_passwords(number_of_nouns=0,
                       number_of_verbs=0,
                       number_of_adverbs=1,
                       number_of_adjectives=1,
                       number_of_symbols=1,
                       number_range=(0, 99),
                       number_of_passwords=25,
                       shuffle_password=True,
                       display_passwords=True):
    separator = ""
    password_list = []
    # word lists I have used come from http://www.ashley-bovan.co.uk/words/partsofspeech.html
    # (https://drive.google.com/file/d/0B5eYVI2s0XztOVdaUnNWQWFZOEU/)
    # but any text file formatted with one word per line will work
    nouns = [line.rstrip('\n') for line in openfile('./1syllablenouns.txt')]
    verbs = [line.rstrip('\n') for line in openfile('./1syllableverbs.txt')]
    adverbs = [line.rstrip('\n') for line in openfile('./1syllableadverbs.txt')]
    adjectives = [line.rstrip('\n') for line in openfile('./1syllableadjectives.txt')]
    common_symbols = ['!', '@', "£", '$', '%', '^', '&', '*', '(', ')', '+', '=', '<', '>', '/', '?']
    word_lists = [(number_of_nouns, nouns), (number_of_verbs, verbs), (number_of_adverbs, adverbs),
                  (number_of_adjectives, adjectives), (number_of_symbols, common_symbols)]

    for _ in range(number_of_passwords):
        password_components = []
        # loop through each word list and choose a random word to add to password_components[]
        for w_list in word_lists:
            if w_list[0] > 0:
                for _ in range(w_list[0]):
                    password_components.append(get_random_value(w_list[1]))
        password_components.append(str(random.randint(number_range[0], number_range[1])))

        if shuffle_password:
            random.shuffle(password_components)

        # add completed password to list of passwords
        password_list.append(separator.join(password_components))

        if display_passwords:
            print(separator.join(password_components))

    return password_list


if __name__ == "__main__":
    # default values when run from the command line
    number_of_nouns = 0
    number_of_verbs = 0
    number_of_adverbs = 1
    number_of_adjectives = 1
    number_of_symbols = 1
    number_range = (0, 99)
    number_of_passwords = 25
    shuffle_password = False

    parser = argparse.ArgumentParser()
    parser.add_argument("--nouns",
                        help="number of nouns to use, default is {}".format(number_of_nouns),
                        default=number_of_nouns, type=int)
    parser.add_argument("--verbs",
                        help="number of verbs to use, default is {}".format(number_of_verbs),
                        default=number_of_verbs, type=int)
    parser.add_argument("--adverbs",
                        help="number of adverbs to use, default is {}".format(number_of_adverbs),
                        default=number_of_adverbs, type=int)
    parser.add_argument("--adjectives",
                        help="number of adjectives to use, default is {}".format(number_of_adjectives),
                        default=number_of_adjectives, type=int)
    parser.add_argument("--symbols",
                        help="number of symbols to use, default is {}".format(number_of_symbols),
                        default=number_of_symbols, type=int)
    parser.add_argument("--number_lower_range",
                        help="lower range of number to use, default is {}".format(number_range[0]),
                        default=number_range[0], type=int)
    parser.add_argument("--number_upper_range",
                        help="upper range of number to use, default is {}".format(number_range[1]),
                        default=number_range[1], type=int)
    parser.add_argument("--number_of_passwords",
                        help="number of passwords to generate, default is {}".format(number_of_passwords),
                        default=number_of_passwords, type=int)
    parser.add_argument("--shuffle_password",
                        help="shuffle the order in which each password component is used, default is {}".format(shuffle_password),
                        default=shuffle_password, action="store_true")
    parser.add_argument("--display_defaults",
                        help="Displays default values and exits",
                        default=False, action="store_true")
    args = parser.parse_args()

    print("Simple password generator by John Porter (c) 2019")
 
    if args.display_defaults:
        print("Default values are set as follows;\n{}".format(args))
        exit(0)

    if args.number_of_passwords > 1:
        print("Generating {} passwords...".format(args.number_of_passwords))
    else:
        print("Generating password...")

    generate_passwords(number_of_symbols=args.symbols, number_of_nouns=args.nouns, number_of_adverbs=args.adverbs,
                       number_of_adjectives=args.adjectives, number_of_passwords=args.number_of_passwords,
                       shuffle_password=args.shuffle_password,
                       number_range=(args.number_lower_range, args.number_upper_range)
                       )
