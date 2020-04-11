import generatePasswords
import argparse


if __name__ == "__main__":
    password_generator = generatePasswords.PasswordGenerator()
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
    default_csv_filename = generatePasswords.CSV_OUTPUT_FILE_LOCATION

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
    parser.add_argument("--write_csv_filename",
                        help="choose a path and filename for output csv. The default is '{}'"
                        .format(default_csv_filename),
                        default=default_csv_filename, type=str)
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

    password_generator.generate_passwords(number_of_symbols=args.symbols, number_of_nouns=args.nouns, number_of_adverbs=args.adverbs,
                       number_of_adjectives=args.adjectives, number_of_passwords=args.number_of_passwords,
                       word_separator=args.word_separator, shuffle_password=args.shuffle_password,
                       number_range=(args.number_lower_range, args.number_upper_range),
                       capitalize=args.do_not_capitalize, write_csv=args.write_csv,
                       write_csv_filename=args.write_csv_filename)