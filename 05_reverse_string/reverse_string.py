def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    set1 = phrase[::-1]
    return set1

print(reverse_string('awesome'))
print(reverse_string('sauce'))