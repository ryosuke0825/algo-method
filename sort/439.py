# Q2-1. バブルソート
# https://algo-method.com/tasks/439

N = int(input())
A = list(map(int, input().split()))

flg = True
while flg:
    flg = False
    for i in range(N-1):
        if A[i] > A[i+1]:
            tmp = A[i+1]
            A[i+1] = A[i]
            A[i] = tmp
            flg = True
    if flg:
        print(' '.join(map(str, A)))
