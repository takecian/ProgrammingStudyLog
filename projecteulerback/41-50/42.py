# https://projecteuler.net/problem=42


def conv(c):
    return ord(c) - ord("A") + 1


def is_triangle(n):
    i = 0
    t = 0
    while t < n:
        t = i * (i + 1) // 2
        i += 1

    return n == t


file = open("p042_words.txt", "r")
names = list(file.read().split(","))
file.close()
names = list(map(lambda x: x.replace("\"", ""), names))

total = 0
for n in names:
    v = 0
    for c in n:
        v += conv(c)

    if is_triangle(v):
        print(str(n) + ", value = " + str(v))
        total += 1

print(total)
