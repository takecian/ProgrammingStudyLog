# https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_b

paths = [sorted(list(map(int, input().split()))) for _ in range(3)]

# print(paths)

c1 = 0
c2 = 0
c3 = 0
c4 = 0

for p in paths:
    for c in p:
        if c == 1:
            c1 += 1
        elif c == 2:
            c2 += 1
        elif c == 3:
            c3 += 1
        elif c == 4:
            c4 += 1

if [c1,c2,c3,c4].count(2) == 2 and [c1,c2,c3,c4].count(1) == 2:
    print("YES")
else:
    print("NO")
#
# print("{}, {}, {}, {}".format(c1,c2,c3,c4))

