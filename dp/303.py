# Q1-2. マスの移動 (1)
# https://algo-method.com/tasks/303

N = int(input())
A = list(map(int, input().split()))

# 各マスへ辿り着くための最短秒数
ans = [0]*N

# 1マス目は初期位置なので0秒
ans[0] = 0

# 2マス目は1マス目から1マス進むでしかたどり着けない
ans[1] = A[1]

# 3マス目以降を求める
for i in range(2, N):
    # iマス目まで進む最短は1マス進むか、2マス進むか
    ans[i] = min(ans[i-1]+A[i], ans[i-2]+A[i]*2)

# Nマス目の値がなるべくはやくたどりつく時の秒数
print(ans[N-1])
