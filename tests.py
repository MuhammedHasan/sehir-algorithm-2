import unittest
import random
from Qs import *


class TestQ2(unittest.TestCase):

    def test_is_sorted(self):
        nums = random.sample(list(enumerate(range(100000))), 10000)
        self.assertFalse(is_sorted(nums))
        self.assertTrue(is_sorted(sorted(nums, key=lambda x: x[1])))

    def test_list_divider(self):
        nums = list(enumerate(range(4)))
        expected = ([(0, 0), (1, 1)], [(2, 2), (3, 3)], 1, 2)
        self.assertEqual(list_divider(nums), expected)

    def test_half_partition_left(self):
        nums = [(0, 1), (1, 2), (2, 4), (3, 6),
                (4, 8), (5, 10), (6, 13), (7, 15)]

        self.assertEqual(half_partition_left(nums, 9), (5, 10))

    def test_half_partition_right(self):
        nums = [(8, 11), (9, 9), (10, 12), (11, 13),
                (12, 15), (13, 17), (14, 20), (15, 25)]

        self.assertEqual(half_partition_right(nums, 15), (12, 15))


if __name__ == '__main__':
    unittest.main()
