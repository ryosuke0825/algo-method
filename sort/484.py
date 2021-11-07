# Q1-3. 総和の最大値
# https://algo-method.com/tasks/484

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
print(sum(A[:K]))
