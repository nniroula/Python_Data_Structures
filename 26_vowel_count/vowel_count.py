def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    new_dict = dict()
    for letters in phrase:
        letters = letters.lower()
        if letters == 'a': 
            new_dict[letters] = phrase.count(letters)
        elif letters == 'e':
             new_dict[letters] = phrase.count(letters)
        elif letters == 'i':
             new_dict[letters] = phrase.count(letters)
        elif letters == 'o':
             new_dict[letters] = phrase.count(letters)
        elif letters == 'u':
             new_dict[letters] = phrase.count(letters)

    return new_dict
print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))