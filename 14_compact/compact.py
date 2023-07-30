def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    final_lst = []
    for element in lst:
        if(bool(element)):
            final_lst.append(element)
    return final_lst
        
