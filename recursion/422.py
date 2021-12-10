# Q4-1. 1 + 2 + … + N (再帰)
# https://algo-method.com/tasks/422

import sys
sys.setrecursionlimit(10 ** 6)


def func(x):
    if x == 0:
        return 0
    return func(x-1)+x


N = int(input())
print(func(N))
