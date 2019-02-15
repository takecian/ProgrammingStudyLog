# https://indeednow-finala-open.contest.atcoder.jp/tasks/indeednow_2015_finala_a

n = int(input())
a = list(map(int, input().split()))

a.sort()

min_v = 2000
max_v = 0


for i in range(len(a)//2):
    s = a[i] + a[-i-1]
    min_v = min(min_v, s)
    max_v = max(max_v, s)

print(max_v - min_v)


