# Q1-5. テストの順位
# https://algo-method.com/tasks/492

N = int(input())
A = list(map(int, input().split()))

AA = sorted(set(A), reverse=True)
rnk = {v: i for i, v in enumerate(AA)}

for p in A:
    print(rnk[p])
