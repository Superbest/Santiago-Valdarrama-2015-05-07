import random
import Question_1
import Question_2
import Question_3
import Question_4
import Question_5
from unittest import TestCase

class Test_Question_1(TestCase):
    def test_sum_with_for_loop(self):
        u = [random.randint(0,100) for i in range(10)]

        self.assertEqual(sum(u), Question_1.sum_with_for_loop(u))

    def test_sum_with_while_loop(self):
        u = [random.randint(0,100) for i in range(10)]

        self.assertEqual(sum(u), Question_1.sum_with_while_loop(u))

    def test_sum_with_recursion(self):
        u = [random.randint(0,100) for i in range(10)]

        self.assertEqual(sum(u), Question_1.sum_with_recursion(u))


class Test_Question_2(TestCase):
    def test_combine_lists(self):
        u = ['a', 'b', 'c']
        v = ['1', '2', '3']

        w = ['a', '1', 'b', '2', 'c', '3']

        self.assertListEqual(w, Question_2.combine_lists(u, v))


class Test_Question_3(TestCase):
    def test_running_time(self):
        """ Makes sure the function completes in a reasonable amount of time.

        Common mistakes with calculating the Fibonacci sequence (such as naive recursion) cause a very noticable drop in
        performance.
        """
        from multiprocessing import Process

        p = Process(target=Question_3.get_first_100_fibs)
        p.start()

        p.join(3)  # Imposes a maximum running time of 3 seconds on the function
        finished_on_time = not p.is_alive()
        p.terminate()

        self.assertTrue(finished_on_time, "Execution timed out.")

    def test_fib_number_F_10(self):
        fibs = Question_3.get_first_100_fibs()

        self.assertEqual(34, fibs[9])

    def test_fib_number_F_100(self):
        fibs = Question_3.get_first_100_fibs()

        # 100th Fibonacci is this according to http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibCalcX.html
        self.assertEqual(218922995834555169026, fibs[-1])


class Test_Question_4(TestCase):
    def test_already_rearranged(self):
        u = [5, 4, 3, 2, 1]
        v = Question_4.rearrange_integers(u)
        w = 54321

        self.assertEqual(v, w)

    def test_single_number(self):
        u = [1]
        v = Question_4.rearrange_integers(u)
        w = 1

        self.assertEqual(v, w)

    def test_simple_case(self):
        u = [1, 2, 3, 4, 5]
        v = Question_4.rearrange_integers(u)
        w = 54321

        self.assertEqual(v, w)

    def test_problem_example(self):
        u = [50, 2, 1, 9]
        v = Question_4.rearrange_integers(u)
        w = 95021

        self.assertEqual(v, w)

    def test_lexical_comparison_bug(self):
        u = [5, 50, 56]
        v = Question_4.rearrange_integers(u)
        w = 56550

        self.assertEqual(v, w)

    def test_zero_padding_bug(self):
        u = [420, 42, 423]
        v = Question_4.rearrange_integers(u)
        w = 42423420

        self.assertEqual(v, w)


class Test_Question_5(TestCase):
    def test_with_example_sequence(self):
        u = Question_5.all_possibilities_that_sum_to_100()

        self.assertIn('+1 +2 +34 -5 +67 -8 +9', u)

    def test_with_santiagos_solutions(self):
        """ These solutions were given by Santiago at https://blog.svpino.com/2015/05/08/solution-to-problem-5-and-some-other-thoughts-about-this-type-of-questions
        """

        u = [
            '+1 +2 +3 -4 +5 +6 +78 +9',
            '+1 +2 +34 -5 +67 -8 +9',
            '+1 +23 -4 +5 +6 +78 -9',
            '+1 +23 -4 +56 +7 +8 +9',
            '+12 +3 +4 +5 -6 -7 +89',
            '+12 +3 -4 +5 +67 +8 +9',
            '+12 -3 -4 +5 -6 +7 +89',
            '+123 +4 -5 +67 -89',
            '+123 +45 -67 +8 -9',
            '+123 -4 -5 -6 -7 +8 -9',
            '+123 -45 -67 +89'
        ]

        v = Question_5.all_possibilities_that_sum_to_100()

        self.assertSetEqual(set(u), set(v))
