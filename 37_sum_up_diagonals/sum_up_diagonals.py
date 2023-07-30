def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    import math
    middle = math.trunc(len(matrix) / 2)
    str1 = matrix[0][0] + matrix[len(matrix)-1].pop()
    str2 = matrix[0].pop() + matrix[len(matrix)-1][0]
    if (len(matrix) > 2):
        str3 = matrix[middle][middle]
        str1 = str1+str3
        str2 = str2 + str3
    return (str1+str2)
