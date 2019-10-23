def reverse(arr):

    arr_length = len(arr)
    for i in range(arr_length // 2):
        k = arr_length - i - 1
        arr[i], arr[k] = arr[k], arr[i]
    return arr


# test cases
import random
from copy import deepcopy

x = []
for i in range(50):
    x.append(random.randint(0, 9999))

y = x
y.reverse()
assert reverse(x) == y

