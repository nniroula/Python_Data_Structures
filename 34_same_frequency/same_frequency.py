def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    
    num1 = str(num1)
    num2 = str(num2)

    count1 = 0
    count2 = 0
    for number in num1:
        if number:
            count1 = count1 + 1
    for numbs in num2:
        if numbs:
            count2 = count2 + 1
    # print(count1)
    # print(count2)
    if count1 == count2:
        return True
    else:
        return False

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))