# https://abc096.contest.atcoder.jp/tasks/abc096_b

A, B, C = map(int, input().split())

K = int(input())

# print(K)

l = sorted([A, B, C])
m = l[-1]
rest = l[:-1:]

# print(m)
# print(rest)

total = m * 2 ** K + sum(rest)
print(total)
