# Q1-1. 数字の列
# https://algo-method.com/tasks/302

N, X, Y = map(int, input().split())

for _ in range(N-2):
    tmp = (X+Y) % 100
    X, Y = Y, tmp
print(Y)
