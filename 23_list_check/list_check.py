def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    count = 0
    for element in lst:
        if (not isinstance(element, (list))):
            count += 1
    if count >= 1:
        return False
    else:
        return True
