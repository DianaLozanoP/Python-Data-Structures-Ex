def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase= ''
    for letter in phrase:
        if(letter.lower()== to_swap.lower()):
            if(letter.islower()):
                new_phrase += letter.upper()
            elif(letter.isupper()):
                new_phrase += letter.lower()
        else:
            new_phrase += letter

    return new_phrase




