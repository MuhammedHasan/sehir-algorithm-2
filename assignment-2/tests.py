import unittest
from main import Graph, Grid


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.G = [[0, 'X', 1, 4, 9, 'X'],
                  [7, 7, 4, 'X', 4, 8],
                  [3, 'X', 3, 2, 'X', 4],
                  [10, 2, 5, 'X', 3, 0]]
        self.graph = Graph()

    def test_add_node(self):
        node = (1, 2)
        self.graph.add_node(node)
        self.assertTrue(node in self.graph)

    def test_add_edge(self):
        pass

    def test_topological_order(self):
        pass

    def test_from_grid(self):
        pass

    def test_from_negative_graph(self):
        pass

    def test_add_check_point(self):
        # think about cost
        pass

    def test_find_sortest_path(self):
        pass

if __name__ == '__main__':
    unittest.main()
