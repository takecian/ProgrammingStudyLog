# https://atcoder.jp/contests/abc106/tasks/abc106_b


def count_div(n):
    return sum([n % i == 0 for i in range(1, n+1)])


N = int(input())
print(sum(count_div(i) == 8 for i in range(1, N + 1, 2)))
