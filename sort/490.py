# Q1-4. 差の最小値
# https://algo-method.com/tasks/490

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = 10**10
for i in range(N-K+1):
    if abs(A[i] - A[i+K-1]) < ans:
        ans = abs(A[i] - A[i+K-1])
print(ans)
