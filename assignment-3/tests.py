import unittest
from main import *


class MountainTests(unittest.TestCase):
    def setUp(self):
        self.mountain = [[1], [1, 2], [3, 5, 4], [2, 6, 7, 4]]

    def test_best_route_tables(self):
        scores, prevs = best_route_tables(self.mountain)
        expected_scores = [[1], [2, 3], [5, 8, 7], [7, 14, 15, 11]]
        expected_prevs = {
            (3, 2): (2, 1),
            (3, 3): (2, 2),
            (3, 0): (2, 0),
            (3, 1): (2, 1),
            (2, 1): (1, 1),
            (2, 0): (1, 0),
            (2, 2): (1, 1),
            (1, 0): (0, 0),
            (1, 1): (0, 0)
        }
        self.assertEqual(scores, expected_scores)
        self.assertEqual(prevs, expected_prevs)

    def test_bestRoute(self):
        path, score = bestRoute(self.mountain)
        self.assertEqual(path, [(0, 0), (1, 1), (2, 1), (3, 2)])
        self.assertEqual(score, 15)


class ConferenceTests(unittest.TestCase):
    def setUp(self):
        self.conferences = {
            "Conference 1": [1300, 1559, 300],
            "Conference 2": [1100, 1359, 500],
            "Conference 3": [1600, 1759, 200]
        }

        self.conferences2 = {
            "c 0": [43, 70, 27],
            "c 1": [3, 18, 24],
            "c 2": [65, 99, 45],
            "c 3": [20, 39, 26],
            "c 4": [45, 74, 26],
            "c 5": [10, 28, 20],
            "c 6": [78, 97, 23],
            "c 7": [0, 9, 22]
        }

    def test_bestSelection(self):
        score, bests = bestSelection(self.conferences)
        expected_score = 700
        expected_bests = ['Conference 2', 'Conference 3']
        self.assertEqual(score, expected_score)
        self.assertEqual(bests, expected_bests)

        score, bests = bestSelection(self.conferences2)
        expected_score = 100
        expected_bests = ['c 1', 'c 3', 'c 0', 'c 6']
        self.assertEqual(score, expected_score)
        self.assertEqual(bests, expected_bests)


class PartitionsTests(unittest.TestCase):
    def test_possibleCombinations(self):
        self.assertEqual(possibleCombinations(100), 190569291)


if __name__ == '__main__':
    unittest.main()
