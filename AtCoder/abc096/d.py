# https://abc096.contest.atcoder.jp/tasks/abc096_d


def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


N = int(input())


l = []

n = 2
while len(l) < N:
    if is_prime(n) and n % 5 == 1:
        l.append(n)
    n += 1

print(' '.join(map(str, l)))
