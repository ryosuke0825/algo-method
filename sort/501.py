# Q1-1. 中央値
# https://algo-method.com/tasks/501

N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 0
if N % 2 == 0:
    ans = (A[N//2]+A[N//2-1])/2
else:
    ans = A[(N-1)//2]
print(ans)
