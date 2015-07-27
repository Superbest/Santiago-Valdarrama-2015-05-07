""" Problem 4:
Write a function that given a list of non negative integers, arranges them such that they form the largest possible
number. For example, given [50, 2, 1, 9], the largest formed number is 95021.
"""


def rearrange_integers(list_to_rearrange):
    """ Rearranges the list of non-negative integers so that they spell out the largest possible number.

    Algorithm:
    The key metric is to move "high-value" numbers (those with high digits) to the front and "low-value" numbers to the
    back. Clearly, 99999... is the best number for putting to the beginning, and 100000.... is the second best number
    for putting in the end (the best number is 0).

    Thus the "value" of an n-digit number relates to where it falls on the interval between the (10^n)-1 and 10^(n-1).
    We can then define a metric for an n-digit number x as x/(10^n -1). This metric is comparable across numbers of
    different lengths, and so it can be used as a sorting criterion.

    As a demonstration of the length independence, consider [55, 5]. The metric for 55 is 55/99 and the metric for 5 is
    5/9. Using long division, both can be seen to converge to 0.555... The careful observer will also note that 55/99 is
    mathematically equivalent to 5/9 (both numerator and denominator are divisible by 11). This implies that 55 and 5
    have equal priority for being moved to the front - as expected, since [55, 5] and [5, 55] are equivalent results.
    """

    def metric(x):
        n = len(str(x))
        q = 10 ** n - 1
        m = x / q
        return m

    result = sorted(list_to_rearrange, key=metric, reverse=True)

    largest_number = int(''.join(map(str, result)))
    return largest_number