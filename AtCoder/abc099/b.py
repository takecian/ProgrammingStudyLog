a, b = map(int, input().split())


def get_height(n):
    return n * (n + 1) // 2


h = get_height(b - a)

print(h - b)


