from string import punctuation


def invalid_words(wordlist, document_filename):
    '''
    INPUT: list, str
    OUTPUT: int

    Given a list of all the valid words and a document filename, return a list
    of words from the document that are not valid words.
    '''
    with open(document_filename) as doc:

        wordset = set(wordlist)

        result = []
        for line in doc:
            words = line.strip().split()
            for word in words:
                if word.lower().strip(punctuation) not in wordset:
                    result.append(word)
        return result


def common_characters(s, num):
    '''
    INPUT: str, int
    OUTPUT: list of chars

    Return the list of characters which appear in the string s more than num
    times.
    '''
    new_s = set(s)
    result = []
    for char in new_s:
        if s.count(char) > num:
            if char not in result:
                result.append(char)
    return result


def sum_to_zero(lst):
    '''
    INPUT: list of ints
    OUTPUT: tuple of two ints

    Return a tuple of two values from the input list that sum to zero.
    If none exist, return None.
    '''
    lst_set = set(lst)

    for item1 in lst_set:
        if -item1 in lst_set:
            return (item1, -item1)

    return None

    #for i, item1 in enumerate(lst):
    #    for item2 in lst[i + 1:]:
    #        if item1 + item2 == 0:
    #            return item1, item2
