def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    str1 = phrase.title() # This is a built in python function .title()
    return str1
print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))