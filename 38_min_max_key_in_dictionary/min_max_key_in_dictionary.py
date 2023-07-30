def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    lst1 = list(d.keys())
    sorted_lst = sorted(lst1)
    val1 = sorted_lst[0]
    val2 = sorted_lst[len(lst1)-1]
    if (type(val1) == int):
        dupple1 = f'({val1}, {val2})'
        dupple2 = eval(dupple1)
    else:
        dupple1 = f"('{val1}', '{val2}')"
        dupple2 = eval(dupple1)
    return (dupple2)
