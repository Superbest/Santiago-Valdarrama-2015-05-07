""" Problem 3:
Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the
Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the
first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
"""

def get_first_100_fibs():
    """ Calculates first 100 Fibonacci numbers: 0, 1, 1, 2, 3 ... .

    Uses a progressive summing algorithm to build up the sequence, starting at the beginning.
    """

    n = 100
    seq = [0, 1]

    while len(seq) < 100:
        seq += [sum(seq[-2:])]

    return seq