# Q1-3. コイン問題
# https://algo-method.com/tasks/360

X = int(input())
A = list(map(int, input().split()))

ans = 0

# 50円
if A[0] >= X//50:
    ans += X//50
    X -= (X//50)*50
else:
    ans += A[0]
    X -= A[0]*50

# 10円
if A[1] >= X//10:
    ans += X//10
    X -= (X//10)*10
else:
    ans += A[1]
    X -= A[1]*10

# 5円
if A[2] >= X//5:
    ans += X//5
    X -= (X//5)*5
else:
    ans += A[2]
    X -= A[2]*5

# 1円
ans += X

print(ans)
