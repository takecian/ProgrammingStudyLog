# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_c

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# check already can pass
need_prepare = 0
need_change = 0
prepare_margin = 0
for a, b in zip(A, B):
    if a < b:
        need_prepare += b - a
        need_change += 1
    else:
        prepare_margin += a - b

if need_prepare == 0:
    print(0)
    exit(0)

# check impossibility
if prepare_margin < need_prepare:
    print(-1)
    exit(0)

# find
margins = []
for i in range(len(A)):
    margins.append((A[i] - B[i], i))

# print(margins)
margins = sorted(margins, reverse=True)
# print(margins)
# print(need_prepare)

for i in range(len(margins)):
    need_prepare -= margins[i][0]
    need_change += 1
    if need_prepare <= 0:
        break

print(need_change)