def list_check(lst):
    """Are all items in lst a list?

        >>> sum_floats([1, 2, 3])
        True

        >>> list_check([[1], "nope"])
        False
    """
    type_holder = True
    for items in lst:
        # print(type(items))
        if isinstance(items, list):
            type_holder = False
    return type_holder

sum_floats = [1, 2, 3]
print(list_check(sum_floats))
print(list_check([[1], "nope"]))