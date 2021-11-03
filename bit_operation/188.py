# ビット演算
# ビット演算 4-4
# https://algo-method.com/tasks/188

N, M = map(int, input().split())
ans = N

for _ in range(M):
    ans = ans >> 1
print(ans)
