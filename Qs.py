
# Q.1


# Q.2

key = lambda x: x[1]


def is_sorted(nums):
    if len(nums) < 2:
        return True
    for i in range(len(nums) - 1):
        if nums[i][1] > nums[i + 1][1]:
            return False
    return True


def list_divider(nums):
    mid = int(len(nums) / 2)
    left_nums, right_nums = nums[:mid], nums[mid:]
    left_max = max(left_nums, key=key)[1]
    right_min = min(right_nums, key=key)[1]
    return left_nums, right_nums, left_max, right_min


def half_partition_left(nums, r_min):
    if len(nums) == 1:
        return nums[0]

    left_nums, right_nums, left_max, right_min = list_divider(nums)

    if left_max <= min(r_min, right_min) and is_sorted(left_nums):
        return half_partition_left(right_nums, r_min)
    else:
        return half_partition_left(left_nums, min(r_min, right_min))


def half_partition_right(nums, r_max):
    if len(nums) == 1:
        return nums[0]

    left_nums, right_nums, left_max, right_min = list_divider(nums)

    if right_min >= max(left_max, r_max) and is_sorted(right_nums):
        return half_partition_right(left_nums, r_max)
    else:
        return half_partition_right(right_nums, max(left_max, r_max))


def partition_list(nums):

    if type(nums[0]) != tuple:
        nums = list(enumerate(nums))

    if len(nums) < 2 or is_sorted(nums):
        return (None, None)

    left_nums, right_nums, left_max, right_min = list_divider(nums)

    if left_max <= right_min:
        if is_sorted(left_nums):
            return partition_list(right_nums)
        elif is_sorted(right_nums):
            return partition_list(left_nums)
    return half_partition_left(left_nums, right_min)[0], \
        half_partition_right(right_nums, left_max)[0]

    # return half_partition_left(left_nums, right_min),
    # half_partition_right(right_nums, left_max)

# Q.3
import collections import defaultdict


def build_graph(edges):
    graph = defaultdict(list)

    for s, t in edges:
        graph[s].append(t)

    return graph


def visit_nodes(graph, node, visits=None):
    visits = visits or dict()


def number_of_paths(G, start, end):
    graph = build_graph(G)

    for node in graph:


if __name__ == '__main__':

    # import timeit
    # import random
    # import builtins
    # import matplotlib.pyplot as plt

    # numbers = [1, 2, 4, 6, 8, 10, 13, 15, 11, 9, 12, 13, 15, 17, 20, 25]
    # numbers = [1, 2, 4, 6, 8, 10, 13, 15, 11, 15, 17, 20, 25]
    # n1, n2, left_max, right_min = list_divider(list(enumerate(numbers)))
    #
    # print(half_partition_left(n1, right_min))
    # print(half_partition_right(n2, left_max))

    # print(partition_list(numbers))
    #
    # builtins.__dict__.update(locals())
    #
    # running_times = list()
    #
    # for i in range(1000, 10000, 100):
    #     l = list(enumerate(sorted(random.sample(range(10000), i)) +
    #                        random.sample(range(10000), i)))
    #     running_times.append(timeit.timeit(
    #         'half_partition_left(%s, %d)' % (str(l), random.randint(0, 10000)),
    #         number=100))
    #
    #
    # plt.plot(running_times)
    # plt.show()
