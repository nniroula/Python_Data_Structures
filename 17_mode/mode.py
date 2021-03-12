def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_count = [] #holds the count of repetition of numbers
    for num in nums:
        num_count.append(nums.count(num))
    highest = num_count[0]
    for i in range(len(num_count)):
        if highest < num_count[i]:
            highest = num_count[i]
    index = num_count.index(highest)
    return nums[index]
print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))
