# note solved
#  https://agc024.contest.atcoder.jp/tasks/agc024_b

N = int(input())

p = []

for i in range(N):
    p.append(int(input()))


top = 0
last = 0
for i, v in enumerate(p):
    if v > len(p)//2:
        c = len(p) - i + 1
        if c > last:
            last = c
    if v <= len(p)//2:
        c = v
        if c > top:
            top = c

# mae = p[:len(p)//2]
# usi = p[len(p)//2:]


# mi = min(list(filter(lambda x: x > len(p)//2, mae)))
# ma = max(list(filter(lambda x: x <= len(p)//2, usi)))

print(top)
print(last)

