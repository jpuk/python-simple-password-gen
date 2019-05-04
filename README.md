> Simple Python script to generate password combinations with nouns, verbs, adverbs, adjectives, numbers and symbols.
>
> It can be run as a module from within your own script or as a standalone program.
>
> When run from the command line you can adjust the default values listed after  if __name__ == "__main__": in the
> Python source code or by provide optional values to override the defaults.
>
> usage: generatePasswords.py [-h] [--nouns NOUNS] [--verbs VERBS]
>                             [--adverbs ADVERBS] [--adjectives ADJECTIVES]
>                            [--symbols SYMBOLS]
>                            [--numberLowerRange NUMBERLOWERRANGE]
>                            [--numberUpperRange NUMBERUPPERRANGE]
>                             [--numberOfPasswords NUMBEROFPASSWORDS]
>                             [--shufflePassword] [--displayDefaults]
> 
> optional arguments:
>   -h, --help            show this help message and exit
>   --nouns NOUNS         number of nouns to use, default is 1
>   --verbs VERBS         number of verbs to use, default is 1
>   --adverbs ADVERBS     number of adverbs to use, default is 1
>   --adjectives ADJECTIVES
>                         number of adjectives to use, default is 1
>   --symbols SYMBOLS     number of symbols to use, default is 1
>   --numberLowerRange NUMBERLOWERRANGE
>                         lower range of number to use, default is 0
>   --numberUpperRange NUMBERUPPERRANGE
>                         upper range of number to use, default is 99
>   --numberOfPasswords NUMBEROFPASSWORDS
>                         number of passwords to generate, default is 25
>   --shufflePassword     shuffle the order in which each password component is
>                         used, default is false
>   --displayDefaults     Displays default values and exits
>
>
> Alternatively generatePasswords can be used as a module from within your own script and will return a list of
> passwords.
> Example:
> from generatePasswords import generate_passwords
> password_list = generate_password(numberOfNouns = 1,
>                                   numberOfVerbs = 1,
>                                   numberOfAdverbs = 1,
>                                   numberOfAdjectives = 1,
>                                   numberOfSymbols = 1,
>                                   numberRange = (0, 99),
>                                   numberOfPasswords = 25,
>                                   shufflePassword = True,
>                                   displayPasswords = False)
>
