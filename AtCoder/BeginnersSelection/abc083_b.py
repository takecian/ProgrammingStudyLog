# https://abs.contest.atcoder.jp/tasks/abc083_b

n, a, b = map(int, input().split())
#
# print(n)
# print(b)

total = 0
for i in range(1, n + 1):
    v = sum(map(int, list(str(i))))
    if a <= v <= b:
        # print("match = " + str(i))
        total += i

print(total)