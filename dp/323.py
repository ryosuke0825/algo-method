# Q1-6. すごろく
# https://algo-method.com/tasks/323

N, M = map(int, input().split())
D = list(map(int, input().split()))

dp = [False]*(N+1)
dp[0] = True

# 0マス目から行けるマスをTrueにする
for d in (D):
    if d <= N:
        dp[d] = True

# 2マス目から順番に進むことができるかチェック
for i in range(2, N+1):
    # 既に進むことができる場合はスキップ
    if dp[i]:
        continue

    for d in D:
        if i-d >= 0 and i-d <= N:
            if dp[i-d]:
                dp[i] = True
                break

if dp[-1]:
    print('Yes')
else:
    print('No')
