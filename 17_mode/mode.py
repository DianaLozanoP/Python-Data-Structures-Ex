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
    directory1 = {}
    for element in nums:
        directory1[element] = nums.count(element)
    max_value = max(directory1.values())
    for key in directory1.keys():
        if (directory1[key] == max_value):
            return(key)


# mode([1, 2, 1])
# mode([2,3,3,3, 2, 3, 2])



