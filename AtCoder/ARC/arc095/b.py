count = int(input())
li = list(map(int, input().split()))

sli = sorted(li)

pair_a = sli[len(sli) - 1]
pair_b = 0

diff = 10**9
for j in range(0, len(sli) - 1):
    h = pair_a / 2
    if abs(h - sli[j]) < diff:
        diff = abs(h - sli[j])
        pair_b = sli[j]

print(str(pair_a) + " " + str(pair_b))
