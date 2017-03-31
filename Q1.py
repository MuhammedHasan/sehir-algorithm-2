import timeit
import random
import builtins
import matplotlib.pyplot as plt


def partition_list(nums):
    pass


def list_divider(nums):
    mid = int(len(nums) / 2)
    return nums[:mid], nums[mid:]


def half_partition(nums, r_min):
    print(nums)

    if len(nums) == 1:
        return nums[0]

    left_nums, right_nums = list_divider(nums)
    left_max, right_min = max(left_nums), min(right_nums)

    if left_max < right_min and left_max < r_min:
        return half_partition(right_nums, r_min)
    else:
        return half_partition(left_nums, min(r_min, right_min))


numbers = [1, 3, 4, 6, 8, 10, 13, 15, 11, 9, 12, 13, 15, 17, 20, 25]


n1, n2 = list_divider(numbers)

print(half_partition(n1, min(n2)))
print(half_partition(n2, max(n1)))

builtins.__dict__.update(locals())

running_times = list()

for i in range(1000, 10000, 100):
    l = sorted(random.sample(range(10000), i)) + random.sample(range(10000), i)
    running_times.append(timeit.timeit(
        'half_partition(%s, %d)' % (str(l), random.randint(0, 10000)),
        number=100))


plt.plot(running_times)
plt.show()
