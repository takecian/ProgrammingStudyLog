# https://beta.atcoder.jp/contests/abc095/tasks/abc095_b


def inp(): return map(int, input().split())


n, x = inp()

most_cheap = 1001
all_one_cost = 0

for i in range(n):
    cost = int(input())
    if cost < most_cheap:
        most_cheap = cost
    all_one_cost += cost


rest_x = x - all_one_cost
if rest_x > 0:
    print(str(n + rest_x // most_cheap))
else:
    print(str(n))
