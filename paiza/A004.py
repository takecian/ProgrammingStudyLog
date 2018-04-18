# https://paiza.jp/challenges/20/show
# Note: This code does not pass all test.

l, n, m = input().split(" ")
l = int(l)
n = int(n)
m = int(m)

# print(str(l) + ", " + str(n) + ", " + str(m))


warp = []

for i in range(m):
    ob, op, ip = input().split(" ")
    ob = int(ob) - 1
    ib = ob + 1
    op = int(op)
    ip = int(ip)
    warp.append(((ib, ip), (ob, op)))


# print(warp)

s = (0, l)

while s[1] > 0:
    s = (s[0], s[1] - 1)

    w = list(filter(lambda x: x[0] == s or x[1] == s, warp))
    if len(w) > 0:
        if w[0][0] == s:
            s = w[0][1]
        else:
            s = w[0][0]

    # print(s)

print(s[0] + 1)
