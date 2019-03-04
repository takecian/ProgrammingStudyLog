# https://atcoder.jp/contests/abc116/tasks/abc116_b

s = int(input())
c = {}

c[s] = 1

prev = s
i = 2
while True:
    prev = int(prev/2) if prev % 2 == 0 else 3 * prev + 1
    if prev in c:
        print(i)
        exit()
    # print(prev)
    c[prev] = i
    i += 1



