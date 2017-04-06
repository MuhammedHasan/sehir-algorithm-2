class Grid:

    def __init__(self, grid_list):
        self._grid = grid_list

    def cells(self):
        for i, row in enumerate(self._grid):
            for j, cell in enumerate(row):
                yield (i, j, cell)

    def neighbors(self, i, j):
        for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nc = (i + x, j + y)
            if self.in_grid(nc[0], nc[1]):
                ncell = self._grid[nc[0], nc[1]]
                if ncell == 'X':
                    nnc = (i + 2 * x, j + 2 * y)
                    if self.in_grid(nnc[0], nnc[1]):
                        nncell = self._grid[nnc[0], nnc[1]]
                        if nncell != 'X':
                            yield (nnc[0], nnc[1], 2 * nncell)
                    yield (nc[0], nc[1], ncell)

    def in_grid(self, i, j):
        return len(self._grid) > i > 0 and len(self._grid[0]) > j > 0


class Graph(dict):

    def add_node(self, node):
        self[node] = dict()

    def add_edge(self, node1, node2, w1, w2=0, directed=False):
        [self.add_node(n) for n in [node1, node2] if n not in self]
        self[node1][node2] = w1
        if not directed:
            self[node2][node1] = w2

    def topological_order(self):
        pass

    @staticmethod
    def from_grid(grid_list):
        graph, grid = Graph(), Grid(grid_list)
        for i, j, v in grid.cells():
            for ni, nj, nv in grid.neighbors(i, j):
                graph.add_edge((i, j), (ni, nj), nv, v)
        return graph

    @staticmethod
    def from_negative_graph(grid):
        pass

    def add_check_point(self):
        # think about cost
        pass

    def find_sortest_path(self):
        for n in self.topological_order():
            for nn in self[n]:
                pass
