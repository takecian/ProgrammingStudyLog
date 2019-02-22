# https://atcoder.jp/contests/abc114/tasks/abc114_c

N = int(input())


def f(s):
    if len(s) > 0 and int(s) > N:
        return 0

    ans = 1 if all(s.count(c) > 0 for c in '753') else 0

    for c in '753':
        ans += f(s + c)

    return ans


print(f(""))

