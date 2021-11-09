# Q2-4. クイックソート
# https://algo-method.com/tasks/442

import sys
sys.setrecursionlimit(10 ** 6)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    X = len(arr)//2
    for i in range(len(arr)):
        if i == X:
            continue
        if arr[i] < arr[X]:
            left.append(arr[i])
        else:
            right.append(arr[i])

    ret = []
    ret.extend(quick_sort(left))
    ret.append(arr[X])
    ret.extend(quick_sort(right))
    return ret


N = int(input())
A = list(map(int, input().split()))

print(' '.join(map(str, quick_sort(A))))
