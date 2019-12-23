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
#                                   word_separator="",
#                                   shuffle_password = True,
#                                   capitalize = True,
#                                   display_passwords = False)
# print(password_list)
#
import random
import secrets
import argparse
import os
import csv

NOUN_LIST_FILE_LOCATION = './1syllablenouns.txt'
VERB_LIST_FILE_LOCATION = './1syllableverbs.txt'
ADVERB_LIST_FILE_LOCATION = './1syllableadverbs.txt'
ADJECTIVE_LIST_FILE_LOCATION = './1syllableadjectives.txt'
COMMON_SYMBOLS = ['!', '@', "£", '$', '%', '^', '&', '*', '(', ')', '+', '=', '<', '>', '/', '?']
CSV_OUTPUT_FILE_LOCATION = './Passwords.csv'

def openfile(fn, access):
    # check file exists and is not empty
    if os.path.isfile(fn):
        result = os.stat(fn)
        if access == 'r':
            if result.st_size < 1:
                print("File {} is empty. Exiting.".format(fn))
                exit(0)
    try:
        fp = open(fn, access)
        return fp
    except:
        print("Could not open file {}, check file exists and you have permission to read or write to it. Exiting.".format(fn))
        exit(0)


def split_file_in_to_list(fn):
    return [line.rstrip('\n') for line in openfile(fn, 'r')]


def get_random_value(word_list, capitalize):
    if capitalize:
        return secrets.choice(word_list).capitalize()
    else:
        return secrets.choice(word_list)


def get_random_number_as_string(number_range):
    return str(random.randint(number_range[0], number_range[1]))


def append_word_list(word_lists, number_of_words, word_list):
    word_lists.append({"number_of_words_to_use": number_of_words, "word_list": word_list})
    return word_lists

def write_csv_file(password_list, output_fn):
    csvfield = ['Password']

    fp = openfile(output_fn, 'w')
    csv_writer = csv.DictWriter(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=csvfield)

    for password in password_list:
        csv_writer.writerow({'Password' : password})

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
                       word_separator="",
                       shuffle_password=True,
                       display_passwords=True,
                       capitalize=True,
                       write_csv=False):

    # word lists I have used come from http://www.ashley-bovan.co.uk/words/partsofspeech.html
    # (https://drive.google.com/file/d/0B5eYVI2s0XztOVdaUnNWQWFZOEU/)
    # but any text file formatted with one word per line will work

    # don't bother loading the word list file if we're not going to use any of it as a component of our passwords.

    word_lists = []
    if number_of_nouns > 0:
        nouns = split_file_in_to_list(NOUN_LIST_FILE_LOCATION)
        word_lists = append_word_list(word_lists, number_of_nouns, nouns)
    if number_of_verbs > 0:
        verbs = split_file_in_to_list(VERB_LIST_FILE_LOCATION)
        word_lists = append_word_list(word_lists, number_of_verbs, verbs)
    if number_of_adverbs > 0:
        adverbs = split_file_in_to_list(ADVERB_LIST_FILE_LOCATION)
        word_lists = append_word_list(word_lists, number_of_adverbs, adverbs)
    if number_of_adjectives > 0:
        adjectives = split_file_in_to_list(ADJECTIVE_LIST_FILE_LOCATION)
        word_lists = append_word_list(word_lists, number_of_adjectives, adjectives)
    if number_of_symbols > 0:
        common_symbols = COMMON_SYMBOLS
        word_lists = append_word_list(word_lists, number_of_symbols, common_symbols)

    password_list = []
    for _ in range(number_of_passwords):
        password_components = []
        # loop through each word list and choose a random word to add to password_components[]
        for w_list in word_lists:
                for _ in range(w_list["number_of_words_to_use"]):
                    password_components.append(get_random_value(w_list["word_list"], capitalize))
        password_components.append(get_random_number_as_string(number_range))

        if shuffle_password:
            random.shuffle(password_components)

        # add completed password to list of passwords
        p = word_separator.join(password_components)
        password_list.append(p)

        if display_passwords:
            print(p)

    if write_csv:
        write_csv_file(password_list, CSV_OUTPUT_FILE_LOCATION)
    return password_list


if __name__ == "__main__":
    # default values when run from the command line
    default_number_of_nouns = 0
    default_number_of_verbs = 0
    default_number_of_adverbs = 1
    default_number_of_adjectives = 1
    default_number_of_symbols = 1
    default_number_range = (0, 99)
    default_word_separator = ""
    default_number_of_passwords = 25
    default_capitalize = True
    default_shuffle_password = False
    default_write_csv = False

    parser = argparse.ArgumentParser()
    parser.add_argument("--nouns",
                        help="number of nouns to use, default is {}".format(default_number_of_nouns),
                        default=default_number_of_nouns, type=int)
    parser.add_argument("--verbs",
                        help="number of verbs to use, default is {}".format(default_number_of_verbs),
                        default=default_number_of_verbs, type=int)
    parser.add_argument("--adverbs",
                        help="number of adverbs to use, default is {}".format(default_number_of_adverbs),
                        default=default_number_of_adverbs, type=int)
    parser.add_argument("--adjectives",
                        help="number of adjectives to use, default is {}".format(default_number_of_adjectives),
                        default=default_number_of_adjectives, type=int)
    parser.add_argument("--symbols",
                        help="number of symbols to use, default is {}".format(default_number_of_symbols),
                        default=default_number_of_symbols, type=int)
    parser.add_argument("--number_lower_range",
                        help="lower range of number to use, default is {}".format(default_number_range[0]),
                        default=default_number_range[0], type=int)
    parser.add_argument("--number_upper_range",
                        help="upper range of number to use, default is {}".format(default_number_range[1]),
                        default=default_number_range[1], type=int)
    parser.add_argument("--number_of_passwords",
                        help="number of passwords to generate, default is {}".format(default_number_of_passwords),
                        default=default_number_of_passwords, type=int)
    parser.add_argument("--word_separator",
                        help="choose a character or string to separate the randomly selected words. The default is '{}'"
                        .format(default_word_separator),
                        default=default_word_separator, type=str)
    parser.add_argument("--shuffle_password",
                        help="shuffle the order in which each password component is used, default is {}"
                        .format(default_shuffle_password),
                        default=default_shuffle_password, action="store_true")
    parser.add_argument("--do_not_capitalize",
                        help="do not capitalize the first letter of each word, default is {}"
                        .format(default_capitalize),
                        default=default_capitalize, action="store_false")
    parser.add_argument("--write_csv",
                        help="Output generated passwords to a CSV file, default is {}"
                        .format(default_write_csv),
                        default=default_write_csv, action="store_true")
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
                       word_separator=args.word_separator, shuffle_password=args.shuffle_password,
                       number_range=(args.number_lower_range, args.number_upper_range),
                       capitalize=args.do_not_capitalize, write_csv=args.write_csv)
