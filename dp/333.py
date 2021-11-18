# Q2-5. コマの移動 (2)
# https://algo-method.com/tasks/333

N = int(input())

S = []
for _ in range(N):
    s = list(input())
    S.append(s)

ans = [[0] * N for i in range(N)]
ans[0][0] = 1

for h in range(N):
    for w in range(N):
        if S[h][w] == '#':
            continue

        if h != 0:
            ans[h][w] += ans[h-1][w]
        if w != 0:
            ans[h][w] += ans[h][w-1]
print(ans[-1][-1])
