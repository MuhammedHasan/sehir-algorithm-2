import heapq


class PriorityQueue(list):

    def __init__(self, inlist=None):
        super(PriorityQueue, self).__init__(inlist or [])
        heapq.heapify(self)

    def insert(self, item):
        heapq.heappush(self, item)

    def peek(self):
        return self[0]

    def pop(self):
        return heapq.heappop(self)

    def decrease_key(self, item):
        for i, v in enumerate(self):
            if v[1] == item[1]:
                self[i] = item
                break
        heapq.heapify(self)


class Grid:

    def __init__(self, grid_list):
        self._grid = grid_list

    def cells(self):
        for i, row in enumerate(self._grid):
            for j, cell in enumerate(row):
                yield (i, j, cell)

    def neighbors(self, i, j, directions="all"):
        if directions == 'all':
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        elif directions == 'right-down':
            directions = [(0, 1), (1, 0)]
        else:
            raise ValueError('Directions are not valid')
        for x, y in directions:
            nc = (i + x, j + y)
            if self.in_grid(nc[0], nc[1]):
                ncell = self._grid[nc[0]][nc[1]]
                if ncell == 'X':
                    nnc = (i + 2 * x, j + 2 * y)
                    if self.in_grid(nnc[0], nnc[1]):
                        nncell = self._grid[nnc[0]][nnc[1]]
                        if nncell != 'X':
                            yield (nnc[0], nnc[1], 2 * nncell)
                    continue
                yield (nc[0], nc[1], ncell)

    def in_grid(self, i, j):
        return self.size[0] > i >= 0 and self.size[1] > j >= 0

    @property
    def size(self):
        return (len(self._grid), len(self._grid[0]))


class Graph(dict):

    def add_node(self, node):
        self[node] = dict()

    def add_edge(self, node1, node2, w1, w2=0, directed=False):
        [self.add_node(n) for n in [node1, node2] if n not in self]
        self[node1][node2] = w1

    @staticmethod
    def from_grid(grid_list, directions='all'):
        graph, grid = Graph(), Grid(grid_list)
        graph._size = grid.size
        for i, j, v in grid.cells():
            if v is not 'X':
                for ni, nj, nv in grid.neighbors(i, j, directions):
                    graph.add_edge((i, j), (ni, nj), nv, v)
        return graph

    def init_prev_dists(self, node):
        prev = dict()
        dists = {n: float('inf') for n in self}
        dists[node] = 0
        return prev, dists

    def dijkstra(self, node):
        prev, dists = self.init_prev_dists(node)
        pq = PriorityQueue([(w, n) for n, w in dists.items()])

        while pq:
            (dist, n) = pq.pop()
            for nn, nw in self[n].items():
                if dists[nn] > dist + nw:
                    dists[nn] = dist + nw
                    pq.decrease_key((dists[nn], nn))
                    prev[nn] = n
        return dists, prev

    def prev_to_path(self, prev, node):
        paths = [node]
        while paths[-1] in prev:
            paths.append(prev[paths[-1]])
        return paths

    def find_sortest_path(self, from_node, to_node):
        dists, prev = self.dijkstra(from_node)
        paths = self.prev_to_path(prev, to_node)
        return dists[to_node], list(reversed(paths))

    def topological_order(self):
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                if (i, j) in self:
                    yield (i, j)

    def find_sortest_path_for_neg(self, from_node, to_node):
        prev, dists = self.init_prev_dists(from_node)

        for n in self.topological_order():
            for nn, nw in self[n].items():
                if dists[nn] > dists[n] + nw:
                    dists[nn] = dists[n] + nw
                    prev[nn] = n

        paths = self.prev_to_path(prev, to_node)
        return dists[to_node], list(reversed(paths))

    @staticmethod
    def from_negative_graph(grid_list):
        return Graph.from_grid(grid_list, directions='right-down')

    def add_check_point(self):
        # think about cost
        pass
