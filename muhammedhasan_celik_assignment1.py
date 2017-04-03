from collections import defaultdict

# Q.1


def bag_switch(outcomes):

    fb = set(['B', 'Y', 'G'])
    sb = set(['W', 'R', 'O'])

    if outcomes[0] in sb:
        return 0

    n, step = 0, 1

    try:
        while not outcomes[n + step] in sb:
            step *= 2
    except:
        step /= 2

    while True:
        try:
            if outcomes[n] in sb and outcomes[n - 1] in fb:
                return n
            n += step if outcomes[n] in fb else -step
        except:
            n -= step
        if step == 0:
            return
        step /= 2


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


# Q.3

def number_of_paths(G, start, end):

    if type(G) != defaultdict:
        graph = defaultdict(list)
        for s, t in G:
            graph[s].append(t)
        G = graph

    if start == end:
        return 1

    return sum(number_of_paths(G, node, end) for node in G[start])
