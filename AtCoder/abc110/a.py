# https://atcoder.jp/contests/abc110/tasks/abc110_a

l = list(map(int, input().split()))
l.sort()
print(10 * l[2] + l[1] + l[0])
