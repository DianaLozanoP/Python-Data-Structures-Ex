def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.

    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.

        >>> truncate("Hello World", 6)
        'Hel...'

        >>> truncate("Problem solving is the best!", 10)
        'Problem...'

        >>> truncate("Yo", 100)
        'Yo'

    The smallest legal value of n is 3; if less, return a message:

        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    str1 = "..."
    if (n < 3):
        return "Truncation must be at least 3 characters."
    elif (n == 3):
        return str1
    elif (len(phrase) >= n):
        finalN = n - 3
        str2 = phrase[0:finalN]
        str3 = str2 + str1
        return str3
    else:
        return phrase
