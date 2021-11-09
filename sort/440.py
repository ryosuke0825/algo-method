# Q2-2. 選択ソート
# https://algo-method.com/tasks/440

N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    idx = i
    mi = A[i]
    for j in range(i, N):
        if A[j] < mi:
            idx = j
            mi = A[j]
    A[i], A[idx] = A[idx], A[i]
    print(' '.join(map(str, A)))
