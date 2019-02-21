# https://abc084.contest.atcoder.jp/tasks/abc084_d


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def main():
    p_l = primes(10**5)
    total = [0 for _ in range(10 ** 5 + 1)]
    for i in range(3, 10 ** 5 + 1):
        if i in p_l and (i + 1) // 2 in p_l:
            total[i] = 1 + total[i - 1]
        else:
            total[i] = total[i - 1]

    # print(total[:10])
    Q = int(input())
    lrs = [list(map(int, input().split())) for _ in range(Q)]
    for lr in lrs:
        print(total[lr[1]] - total[lr[0]-1])


main()




