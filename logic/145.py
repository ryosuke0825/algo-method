# 問題 4
# https://algo-method.com/tasks/145

A, B = map(int, input().split())

if (A+B) % 2 == 0:
    print((A+B)//2)
else:
    print(-1)
