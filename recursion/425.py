# Q4-3. フィボナッチ数列 (再帰-1)
# https://algo-method.com/tasks/425

import sys
sys.setrecursionlimit(10 ** 6)


def func(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return func(x-1)+func(x-2)


N = int(input())
print(func(N))
