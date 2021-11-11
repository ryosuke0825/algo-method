# Q2-8. ヒープソート
# https://algo-method.com/tasks/524


def heapify(N, A, i):
    c = 2*i+1
    if c >= N:
        return

    if c+1 < N and A[c+1] > A[c]:
        c += 1
    if A[c] <= A[i]:
        return
    A[i], A[c] = A[c], A[i]
    heapify(N, A, c)


N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N-1, -1, -1):
    heapify(N, A, i)

for i in range(N-1, 0, -1):
    A[0], A[i] = A[i], A[0]
    heapify(i, A, 0)
    if i == M:
        print(*A)
print(*A)
