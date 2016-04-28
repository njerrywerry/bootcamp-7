'''Test suite for super_sum'''
from unittest import TestCase
from day_4.super_sum import super_sum

class SuperSumTestCase(TestCase):
    """TestCase for super_sum"""

    def test_empty_input(self):
        '''Test empty input.'''
        self.assertEqual(super_sum(), 0)

    def test_sum_of_integers(self):
        '''Test sum of integers.'''
        # asserting that super_sum(1, 2, 3) returns 6
        self.assertEqual(super_sum(1, 2, 3), 6)
        self.assertEqual(super_sum(-1, 1), 0)
        self.assertNotEqual(super_sum(10, 11, 12), 4)

    def test_string_input_(self):
        '''Test string input'''
        # asserting that super_sum('string') returns 0
        self.assertEqual(super_sum('njerry', 'mum', 4), 0)


    def test_sum_of_items_in_one_list(self):
        '''Test sum of items in a single list.'''
        # asserting that super_sum([1, 2, 3]) returns 6
        self.assertEqual(super_sum([1, 2, 3]), 6)
