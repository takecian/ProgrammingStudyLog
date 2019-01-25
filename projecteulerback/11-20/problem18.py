# https://projecteuler.net/problem=18


def get_large_sum(t, h, s, i):
    if s + i >= len(tree): return 0

    h += 1
    left = t[s + i] + get_large_sum(t, h, s + h, i)
    right = t[s + i] + get_large_sum(t, h, s + h, i + 1)
    return left if left > right else right

data = []

for i in range(15):
    d = input().split()
    data.append(d)

data = sum(data, [])
tree = list(map(int, data))
print(tree)

m = get_large_sum(tree, 0, 0, 0)
print(m)
