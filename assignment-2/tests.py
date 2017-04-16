import unittest
from main import Graph, Grid, PriorityQueue


class PriorityQueueTestCase(unittest.TestCase):

    def setUp(self):
        self.pq = PriorityQueue([(1, 'a'), (4, 'd'), (3, 'c'), (5, 'b')])

    def test_init(self):
        self.assertEqual(PriorityQueue(), [])
        self.assertEqual(self.pq, [(1, 'a'), (4, 'd'), (3, 'c'), (5, 'b')])

    def test_pop(self):
        self.assertEqual(self.pq.pop(), (1, 'a'))
        self.assertEqual(self.pq.pop(), (3, 'c'))

    def test_peek(self):
        self.assertEqual(self.pq.peek(), (1, 'a'))

    def test_insert(self):
        self.pq.insert((0, 'x'))
        self.assertEqual(self.pq.peek(), (0, 'x'))

    def test_decrease_key(self):
        self.pq.decrease_key((6, 'a'))
        self.assertEqual(self.pq, [(3, 'c'), (4, 'd'), (6, 'a'), (5, 'b')])


class GridTestCase(unittest.TestCase):

    def setUp(self):
        self.G = [[0, 'X', 1,  4,  9, 'X'],
                  [7,  7,  4, 'X', 4,  8],
                  [3, 'X', 3,  2, 'X', 4],
                  [10, 2,  5, 'X', 3,  0]]
        self.grid = Grid(self.G)

    def test_cells(self):
        size = len(self.G) * len(self.G[0])
        self.assertEqual(len(list(self.grid.cells())), size)

    def test_neighbors(self):
        self.assertEqual(set(self.grid.neighbors(0, 0)),
                         set([(0, 2, 2), (1, 0, 7)]))

        self.assertEqual(set(self.grid.neighbors(1, 1)),
                         set([(1, 2, 4), (3, 1, 4), (1, 0, 7)]))


class GraphTestCase(unittest.TestCase):

    def setUp(self):
        self.G = [[0, 'X', 1,  4,  9, 'X'],
                  [7,  7,  4, 'X', 4,  8],
                  [3, 'X', 3,  2, 'X', 4],
                  [10, 2,  5, 'X', 3,  0]]

        self.G_neg = [[0, 'X', 5, -3,  6, 'X'],
                      [6, -4,  5, 'X', 3, -8],
                      [4, 'X', 3, -7, 'X', 5],
                      [10, 2, -2, 'X', 6,  0]]

        self.graph = Graph.from_grid(self.G)
        self.graph_neg = Graph.from_negative_graph(self.G_neg)

    def test_add_node(self):
        node = (1, 2)
        self.graph.add_node(node)
        self.assertTrue(node in self.graph)

    def test_add_edge(self):
        self.graph.add_edge((1, 1), (2, 2), 1, 2)
        self.assertEqual(self.graph[1, 1][2, 2], 1)

    def test_topological_order(self):
        pass

    def test_from_grid(self):
        self.assertEqual(self.graph[1, 2][2, 2], 3)
        self.assertEqual(self.graph[2, 2][1, 2], 4)
        self.assertEqual(self.graph[1, 2][1, 4], 8)
        self.assertEqual(self.graph[1, 4][1, 2], 8)

    def test_find_sortest_path(self):
        to_node = len(self.G) - 1, len(self.G[0]) - 1
        from_node = (0, 0)
        dist, path = self.graph.find_sortest_path(from_node, to_node)
        self.assertEqual(dist, 18)
        self.assertEqual(path,
                         [(0, 0), (0, 2), (0, 3), (2, 3), (2, 5), (3, 5)])

    def test_from_negative_graph(self):
        neg_graph = Graph.from_negative_graph(self.G)
        self.assertEqual(neg_graph[1, 2][2, 2], 3)

    def test_find_sortest_path_for_neg(self):
        to_node = len(self.G) - 1, len(self.G[0]) - 1
        from_node = (0, 0)
        dist, path = self.graph_neg.find_sortest_path_for_neg(
            from_node, to_node)
        self.assertEqual(dist, 3)
        self.assertEqual(path,
                         [(0, 0), (0, 2), (0, 3), (2, 3), (2, 5), (3, 5)])

    def test_add_check_point(self):
        # think about cost
        pass


if __name__ == '__main__':
    unittest.main()
