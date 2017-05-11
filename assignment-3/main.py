import copy
import collections
import bisect


def best_route_tables(mountain):
    scores = copy.deepcopy(mountain)
    prevs = dict()
    for i in range(len(scores) - 1):
        for j, l in enumerate(scores[i]):
            for ni, nj in [(i + 1, j), (i + 1, j + 1)]:
                if l + mountain[ni][nj] >= scores[ni][nj]:
                    scores[ni][nj] = l + mountain[ni][nj]
                    prevs[ni, nj] = (i, j)
    return scores, prevs


def bestRoute(mountain):
    scores, prevs = best_route_tables(mountain)
    best_index, best_score = max(enumerate(scores[-1]), key=lambda x: x[1])
    best_coor = (len(scores) - 1, best_index)
    path = [best_coor]
    while best_coor in prevs:
        path.append(prevs[best_coor])
        best_coor = prevs[best_coor]
    route = list(reversed(path))
    print('Route:', route)
    print('Score:', best_score)
    return route, best_score


def previous_intervals(G):
    starts = [i[0] for i in G]
    ends = [i[1] for i in G]
    return [bisect.bisect_left(ends, starts[i]) for i in range(len(G))]


def path_from_tables(G, table, prevs):
    i = len(G) - 1
    while i >= 0:
        if table[prevs[i]] + G[i][2] > table[i]:
            yield G[i]
            i = prevs[i] - 1
        else:
            i -= 1


def weighted_interval_scheduling(G):
    G.sort(lambda x, y: x[1] - y[1])
    prevs = previous_intervals(G)

    table = [0] * (len(G) + 1)
    table[1] = G[0][2]

    for i in range(1, len(G)):
        table[i + 1] = max(G[i][2] + table[prevs[i]], table[i])

    return table[len(G)], list(path_from_tables(G, table, prevs))[::-1]


def bestSelection(conferences):
    conferences = [v + [k] for k, v in conferences.items()]
    score, bests = weighted_interval_scheduling(conferences)
    bests = [i[-1] for i in bests]
    print("Selected conferences:", bests)
    print("Total number of participants:", score)
    return score, bests


def possibleCombinations(n):
    table = collections.defaultdict(dict)
    table[0][0] = 1
    table[1][1] = 1
    for i in range(1, n + 1):
        c = 0
        for j in range(1, i + 1):
            c += table[i - j][min(i - j, j)]
            table[i][j] = c
    return table[n][n] - 1
