def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    lst1 = []
    for element in nums:
        if (nums.count(element) > 1):
            if (lst1.count(element) == 0):
                lst1.append(element)
    if (len(lst1) == 1):
        return (lst1[0])
    else:
        return (None)
