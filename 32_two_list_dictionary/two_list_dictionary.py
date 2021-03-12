def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    dict1 = {}

    # if len(keys) < len(values):
    #     new_values = values.copy()
    #     for i in range(len(keys)):
    #         if i > len(values):
    #             new_values.append(None)       
    #             for i in range(len(keys)):
    #                 dict1[keys[i]] = values[i]
    #     print(new_values)

    for i in range(len(keys)):
        dict1[keys[i]] = values[i]
    return dict1

    """
     out = {}
    for idx, val in enumerate(keys):
        out[val] = values[idx] if idx < len(values) else None
    return out
    """

print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))
#print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))