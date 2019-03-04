# https://atcoder.jp/contests/abc108/tasks/abc108_b

x1, y1, x2, y2 = map(int, input().split())

x = x2 - x1  # 1 -> 2へのベクトルを計算する
y = y2 - y1

print("{} {} {} {}".format(x2 - y, y2 + x, x1 - y, y1 + x))

