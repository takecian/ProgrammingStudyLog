# https://atcoder.jp/contests/abc110/tasks/abc110_d


def get_prime_dic(n):
    dic = {}

    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        i += 1

    if n > 1:
        dic[n] = 1
    return dic


# Calculate count of combination
def combination(n, r):
    a = 1
    b = 1
    for i in range(r):
        a *= (n - i)
        b *= (i + 1)
    return a // b


def main():
    N, M = map(int, input().split())
    d = get_prime_dic(M)
    # print(d)

    ans = 1
    for k, v in d.items():
        ans *= combination(v + N - 1, v)
        ans %= 1000000007

    print(ans)


main()
