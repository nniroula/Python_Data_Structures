def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict1 = {}
    for char in phrase:
        # dict1[char] = dict1.get(char, 0) + 1
        dict1[char] = dict1.get(char, 0) + 1
    return dict1
print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))