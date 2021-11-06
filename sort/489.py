# Q1-2. X 番目に小さい数
# https://algo-method.com/tasks/501

N, M = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

A.sort()
for x in X:
    print(A[x])
