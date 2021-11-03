# ビット演算
# ビット演算 4-6
# https://algo-method.com/tasks/189

N = int(input())
ans = 1
for _ in range(N):
    ans = ans << 1
print(ans)
