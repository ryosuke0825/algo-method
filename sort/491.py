# Q1-8. ごはんを買う
# https://algo-method.com/tasks/491

N, K = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

AB.sort()
ans = 0
remaining = K
for a, b in AB:
    if remaining >= b:
        ans += a*b
        remaining -= b
    else:
        ans += a*remaining
        remaining = 0
    if remaining == 0:
        break
print(ans)
