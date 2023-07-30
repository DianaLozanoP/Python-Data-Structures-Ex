def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = phrase.split()
    str4 = ""
    for word in lst:
        str1 = word[0].upper()
        str2 = word[1:].lower()
        str3 = str1+str2
        str4 = str4 + " " + str3
    return (str4.strip())
