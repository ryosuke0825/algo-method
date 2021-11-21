# Q2-7. コマの移動 (4)
# https://algo-method.com/tasks/335

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[9_999_999] * N for i in range(N)]
dp[0][-1] = A[0][-1]

for h in range(N):
    for w in reversed(range(N)):
        if h == 0 and w == N-1:
            continue

        # 上のマスから移動
        if h != 0:
            dp[h][w] = min(A[h][w]+dp[h-1][w], dp[h][w])
        # 右のマスから移動
        if w != N-1:
            dp[h][w] = min(A[h][w]+dp[h][w+1], dp[h][w])
print(dp[-1][0])
