# Q1-2. お菓子 (1)
# https://algo-method.com/tasks/362

N = int(input())

ans = 0
while N > 0:
    if N % 2 == 0:
        N = N//2
    else:
        N -= 1
    ans += 1
print(ans)
