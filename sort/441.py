# Q2-3. 挿入ソート
# https://algo-method.com/tasks/441

N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
    pos = i
    while not(pos == 0) and A[pos-1] > A[pos]:
        A[pos], A[pos-1] = A[pos-1], A[pos]
        pos -= 1
    print(' '.join(map(str, A)))
