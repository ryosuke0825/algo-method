# Q3-6. 部分和問題 (応用 2)
# https://algo-method.com/tasks/352

N, A, B = map(int, input().split())
X = list(map(int, input().split()))

dp = [[False] * A for i in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(A):
        if not dp[i][j]:
            continue

        dp[i+1][j] = True
        dp[i+1][(j+X[i]) % A] = True

if dp[N][B]:
    print('Yes')
else:
    print('No')
