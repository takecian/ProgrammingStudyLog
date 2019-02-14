# https://atcoder.jp/contests/abc116/tasks/abc116_c

N = int(input())
h = list(map(int, input().split()))

count = 0

while max(h) > 0:
    is_pouring = False
    for i in range(N):
        if h[i] > 0:
            h[i] -= 1
            if not is_pouring:
                count += 1
                is_pouring = True
        else:  # 0
            is_pouring = False
    # print(h)

print(count)
