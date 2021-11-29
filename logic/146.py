# 問題 5
# https://algo-method.com/tasks/146

A, B = map(int, input().split())

if (A+B) % 2 == 0 and A >= B:
    print((A+B)//2)
else:
    print(-1)
