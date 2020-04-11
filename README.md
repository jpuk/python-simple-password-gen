Simple Python script to generate password combinations with nouns, verbs, adverbs, adjectives, numbers and symbols.

 It can be run as a module from within your own script or as a standalone program.

 Before running from the command line you can adjust the default values listed after
 

    if __name__ == "__main__":

  You can adjust the default values to suit your needs

   
 
    # default values  
    number_of_nouns = 0 
    number_of_verbs = 0  
    number_of_adverbs = 1  
    number_of_adjectives = 1 
    number_of_symbols = 1  
    number_range = (0, 99) 
    number_of_passwords = 25 
    shuffle_password = False

Or choose them from the command line
  

     usage: generatePasswords.py  
     optional arguments:
        optional arguments:
          -h, --help            show this help message and exit
          --nouns NOUNS         number of nouns to use, default is 0
          --verbs VERBS         number of verbs to use, default is 0
          --adverbs ADVERBS     number of adverbs to use, default is 1
          --adjectives ADJECTIVES
                                number of adjectives to use, default is 1
          --symbols SYMBOLS     number of symbols to use, default is 1
          --number_lower_range NUMBER_LOWER_RANGE
                                lower range of number to use, default is 0
          --number_upper_range NUMBER_UPPER_RANGE
                                upper range of number to use, default is 99
          --number_of_passwords NUMBER_OF_PASSWORDS
                                number of passwords to generate, default is 25
          --shuffle_password    shuffle the order in which each password component is
                                used, default is False
          --display_defaults    Displays default values and exits
    

   
 Alternatively generatePasswords can be used as a module from within your own script and will return a list of passwords.
 
 All values are optional and will default to values predefined in the generatePasswords() function if none are provided.
 
 Example with options provided:
 

    import generatePasswords
    
    password_generator = generatePasswords.PasswordGenerator()

    password_generator.generate_passwords(numberOfNouns = 1,
                                   number_of_verbs = 1,
                                   number_of_adverbs = 1,
                                   number_of_adectives = 1,
                                   number_of_symbols = 1,
                                   number_range = (0, 99),
                                   number_of_passwords = 25,
                                   shuffle_password = True,
                                   display_passwords = False)
    
    print(password_generator.password_list)

The one syllable word lists included in the git are from from Ashley Bovan's  excellent "Parts of speech" word collection available from [here](http://www.ashley-bovan.co.uk/words/partsofspeech.html) where lists of words with more syllables are also available.
 
