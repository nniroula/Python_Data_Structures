def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst1 = [0, False, '', None, []]
    new_lst = []
    for item in lst:
        if item:
            new_lst.append(item)
    return new_lst
print(compact([0, 1, 2, '', [], False, (), None, 'All done']))

