""" Problem 1:
Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.
"""


def sum_with_for_loop(list_to_sum):
    """ Sums numbers using a for loop.
    """
    total = 0

    for i in list_to_sum:
        total += i

    return total


def sum_with_while_loop(list_to_sum):
    """ Sums numbers using a while loop.
    """
    total = 0

    while any(list_to_sum):
        total += list_to_sum.pop()

    return total


def sum_with_recursion(list_to_sum):
    """ Sums numbers using recursion.
    """
    if len(list_to_sum) == 0:
        return 0
    else:
        return list_to_sum.pop() + sum_with_recursion(list_to_sum)
