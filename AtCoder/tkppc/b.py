# https://tkppc.contest.atcoder.jp/tasks/tkppc2015_b

N = int(input())

res = 0
m = -1

for i in range(N):
    temp = int(input())
    if temp > m:
        m = temp
        res = i + 1

print(res)
