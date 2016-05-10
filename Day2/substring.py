from collections import defaultdict


def substring_old(words, substrings):
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


def substring_new(words, substrings):
    '''
    INPUT: list, list
    OUTPUT: list

    Given two lists of strings, return the list of strings from the second list
    that are a substring of a string in the first list.

    The strings in the substrings list are all 3 characters long.
    '''
    words_set = set(words)
    sub_set = set(substrings)
    #output_set = set()

    # for sub in sub_set:
    #     for word in words_set:
    #         if sub in word:
    #             output_set.update(sub)
    # return list(output_set)

    return list({sub for word in words_set for sub in sub_set if sub in word})

    #return '\n'.join(item + ': ' + str(d[item]) for item in d)
