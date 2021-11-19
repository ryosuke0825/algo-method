# Q2-6. コマの移動 (3)
# https://algo-method.com/tasks/334

N = int(input())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)

ans = [[0] * N for i in range(N)]
ans[0][0] = A[0][0]
for h in range(N):
    for w in range(N):
        # 上左端ではないマス
        if h != 0 and w != 0:
            ans[h][w] = A[h][w] + max(ans[h-1][w], ans[h][w-1])
        # 上端のマス
        elif h == 0 and w != 0:
            ans[h][w] = A[h][w] + ans[h][w-1]
        # 左端のマス
        elif h != 0 and w == 0:
            ans[h][w] = A[h][w] + ans[h-1][w]
print(ans[-1][-1])
