def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    placeholder = ""
    for char in phrase:
        # if to_swap.lower() is True and char.lower() == to_swap:
        if char.lower() == to_swap:
            char = char.swapcase()
        elif char.upper() == to_swap:
            char = char.swapcase()
        placeholder = placeholder + char
    # return phrase
    return placeholder

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))


