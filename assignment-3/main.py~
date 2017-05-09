mountain = [[1], [1, 2], [3, 5, 4], [2, 6, 7, 4]]


def bestRoute(mountain):
    t_scores = [mountain[0]]
    for i in range(len(mountain) - 1):
        t_scores.append([0] * len(mountain[i + 1]))
        for j, l in enumerate(mountain[i]):
            for ni, nj in [(i + 1, j), (i + 1, j + 1)]:
                if l + t_scores[i][j] >= t_scores[ni][nj]:
                    t_scores[ni][nj] = l + t_scores[i][j]
    return max(t_scores[-1])


print(bestRoute(mountain))
