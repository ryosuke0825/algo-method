# Q2-4. コマの移動 (1)
# https://algo-method.com/tasks/329

N = int(input())

ans = [[0] * N for i in range(N)]

for h in range(N):
    for w in range(N):
        if h != 0 and w == 0:
            ans[h][w] += ans[h-1][w]
        elif h == 0 and w != 0:
            ans[h][w] += ans[h][w-1]
        elif h != 0 and w != 0:
            ans[h][w] += ans[h-1][w]+ans[h][w-1]
        else:
            ans[0][0] = 1

print(ans[-1][-1])
