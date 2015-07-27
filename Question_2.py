""" Problem 2:
Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c]
and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].
"""

def combine_lists(list1, list2):
    """ Combines the two given lists by interleaving list1 [a1, a2, a3 ...] and list2 [b1, b2, b3 ...] into a new list
    [a1, b1, a2, b2, a3, b3 ...]. The lists are expected to be of equal length.
    """

    tuples = zip(list1, list2)
    interleaved = sum(tuples, ())

    return list(interleaved)
