def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)

    """
    import math
    if operation == "add":
        i = a+b
        if make_int == True:
            x = math.trunc(i)
            return (message + " " + str(x))
        else:
            return (message + " " + str(i))
    elif operation == "subtract":
        j = a - b
        if make_int == True:
            y = math.trunc(j)
            return (message + " " + str(y))
        else:
            return (message + " " + str(j))
    elif operation == "multiply":
        f = a*b
        if make_int == True:
            z = math.trunc(f)
            return (message + " "+str(z))
        else:
            return (message + " " + str(f))
    elif operation == "divide":
        g = a/b
        if make_int == True:
            r = math.trunc(g)
            return (message + " " + str(r))
        else:

            return (message + " " + str(g))
