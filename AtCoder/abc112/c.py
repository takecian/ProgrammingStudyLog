# https://atcoder.jp/contests/abc112/tasks/abc112_c

N = int(input())

p_l = [list(map(int, input().split())) for _ in range(N)]
p_l.sort(key=lambda x: -x[2])  # h = 0 は使えない

temp_p = p_l[0]

for x in range(101):  # X
    for y in range(101):  # Y
        # 仮の中心
        h = temp_p[2] + abs(temp_p[1] - y) + abs(temp_p[0] - x)

        if all(max(h - abs(p[1] - y) - abs(p[0] - x), 0) == p[2] for p in p_l[1:]):
            print("{} {} {}".format(x, y, h))
            exit()
