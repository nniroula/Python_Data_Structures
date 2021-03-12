def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # turn into set, find intersection and turn back to set
    set1 = set(l1)
    set2 = set(l2)
    set3 = set1 & set2
    # pop items from set and append them in list
    lst = []
    for item in set3:
        lst.append(item)
    return lst
print(intersection([1, 2, 3], [2, 3, 4]))
print(intersection([1, 2, 3], [3, 4]))
print(intersection([1, 2, 3], [4, 5, 6]))
    