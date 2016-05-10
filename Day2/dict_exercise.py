def dict_to_str(d):
    '''
    INPUT: dict
    OUTPUT: str

    Return a str containing each key and value in dict d. Keys and values are
    separated by a colon and a space. Each key-value pair is separated by a new
    line.

    For example:
    a: 1
    b: 2

    For nice pythonic code, use iteritems!

    Note: it's possible to do this in 1 line using list comprehensions and the
    join method.
    '''
    #l = []
    #for item in d:
    #    l.append(item + ': ' + str(d[item]))
    #return '\n'.join(l)
    return '\n'.join(item + ': ' + str(d[item]) for item in d)


def dict_to_str_sorted(d):
    '''
    INPUT: dict
    OUTPUT: str

    Return a str containing each key and value in dict d. Keys and values are
    separated by a colon and a space. Each key-value pair is sorted in ascending order by key.
    This is sorted version of dict_to_str().

    Note: This one is also doable in one line!
    '''
    l = []
    for item in sorted(d):
        l.append(item + ': ' + str(d[item]))
    return '\n'.join(l)


def dict_difference(d1, d2):
    '''
    INPUT: dict, dict
    OUTPUT: dict

    Combine the two dictionaries, d1 and d2 as follows. The keys are the union of the keys
    from each dictionary. If the keys are in both dictionaries then the values should be the
    absolute value of the difference between the two values. If a value is only in one dictionary, the
    value should be the absolute value of that value.
    '''
    for item1 in d1:
        if item1 in d2:
            d2[item1] = abs(d2[item1] - d1[item1])
        else:
            d2[item1] = abs(d1[item1])
    for item in d2:
        if d2[item] < 0:
            d2[item] = abs(d2[item])
    return d2
