# Q2-5. 乱択クイックソート
# https://algo-method.com/tasks/443

import random
import sys
sys.setrecursionlimit(10 ** 6)


def quick_sort(arr):
    if len(arr) == 0:
        return arr

    left = []
    right = []
    m = []

    X = random.randrange(len(arr))

    for i in range(len(arr)):
        if arr[i] < arr[X]:
            left.append(arr[i])
        elif arr[i] > arr[X]:
            right.append(arr[i])
        else:
            m.append(arr[i])

    return quick_sort(left)+m+quick_sort(right)


N = int(input())
A = list(map(int, input().split()))

print(*quick_sort(A))
