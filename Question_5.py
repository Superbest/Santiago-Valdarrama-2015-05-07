""" Problem 5:
Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order)
such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.
"""

import itertools
import Question_2  # Turns out the list interleave function is handy for this problem

def all_possibilities_that_sum_to_100():
    """ By brute-force, finds out what placements of +/-/nothing between the numbers 1, 2 ... 9 such that the sum is 100
    can be made. Given that there are 9 numbers, we have 8 slots where one of three signs (including no-sign) can be
    placed - this comes out to 3^8 or 6561 possibilities, each of which will have to be verified by summing. This is not
    an intractable number, so I will simply try all of them.
    """

    all_sign_sequences = map(list, itertools.product([' +', ' -', ''], repeat=8))  # The extra space is a clever trick to split into terms without losing the sign

    def sign_sequence_to_expression(seq):
        signs = ['+'] + list(seq)
        digits = map(str, range(1, len(seq) + 2))
        expression = ''.join(Question_2.combine_lists(signs, digits))

        return expression

    all_expressions = map(sign_sequence_to_expression, all_sign_sequences)

    def evaluate_expression(e):
        # First split into terms (using the extra space we inserted)
        terms = e.split(' ')

        # Parse the sign for each term
        signed_terms = list(map(int, terms))

        total = sum(signed_terms)
        return total

    correct_possibilities = [u for u in all_expressions if evaluate_expression(u) == 100]
    return correct_possibilities