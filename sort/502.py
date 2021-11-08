# Q1-6. 投票結果
# https://algo-method.com/tasks/502

N = int(input())
A = list(map(int, input().split()))

nums = [0]*N
for a in A:
    nums[a] += 1

students = [i for i in range(N)]

students.sort(key=lambda s: nums[s], reverse=True)
for s in students:
    print('{} {}'.format(s, nums[s]))
