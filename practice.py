from examples import is_palindrome


def sum_ints(lst):
    '''
    INPUT: list
    OUTPUT: int

    The input list contains a mixture of integers, floats and strings. Sum up
    only the ints.
    Hint: Use the isinstance function.
    '''
    total = 0
    for entry in lst:
        if isinstance(entry, int) == True:
            total += entry
    return total


def min_and_max(lst):
    '''
    INPUT: list
    OUTPUT: tuple of two ints/floats

    Given a list of ints and/or floats, return a 2-tuple containing the values
    of the items with the smallest and largest absolute values.

    In the case of an empty list, return None.
    '''
    if lst == []:
        return None
    abs_max = abs(lst[0])
    abs_min = abs(lst[0])

    for entry in lst:
        if abs(entry) > abs(abs_max):
            abs_max = entry
        if abs(entry) < abs(abs_min):
            abs_min = entry

    return (abs_min, abs_max)


def are_palindromes(words):
    '''
    INPUT: list
    OUTPUT: bool

    Given a list of strings, return whether ALL of the elements are
    palindromes.

    Hint: use the is_palindrome function that has been imported at
    the top of this file
    '''
    for word in words:
        if is_palindrome(word) == False:
            return False
    return True


def substring(words, substrings):
    '''
    INPUT: list, list
    OUTPUT: list

    Given two lists of strings, return the list of strings from the second list
    that are a substring of a string in the first list.

    The strings in the substrings list are all 3 characters long.
    '''
    output = []
    for sub in substrings:
        for word in words:
            if sub in word:
                output.append(sub)
    return output
