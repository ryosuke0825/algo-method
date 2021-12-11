# Q4-2. A + (A+1) + … + B (再帰)
# https://algo-method.com/tasks/426

import sys
sys.setrecursionlimit(10 ** 6)


def func(x):
    if x == A:
        return x
    return func(x-1)+x


A, B = map(int, input().split())
print(func(B))
