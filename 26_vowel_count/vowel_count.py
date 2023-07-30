def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    direc = {}
    countA = 0
    countE = 0
    countI = 0
    countO = 0
    countU = 0
    for letter in phrase:
        if letter.lower() in "a":
            countA += 1
            direc[letter.lower()] = countA
        elif letter.lower() in "e":
            countE += 1
            direc[letter.lower()] = countE
        elif letter.lower() in "i":
            countI += 1
            direc[letter.lower()] = countI
        elif letter.lower() in "o":
            countO += 1
            direc[letter.lower()] = countO
        elif letter.lower() in "u":
            countU += 1
            direc[letter.lower()] = countU

    return direc
