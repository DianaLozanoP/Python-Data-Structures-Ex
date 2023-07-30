def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    first = phrase[0].upper()
    last = phrase[1:]
    final_str = first + last
    return final_str
