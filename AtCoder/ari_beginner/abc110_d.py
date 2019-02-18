# https://atcoder.jp/contests/abc110/tasks/abc110_d


N, M = map(int, input().split())

def compute_divisors(n):
    dic = {}

    m = n
    while m % 2 == 0:
        dic[2] += 1
        m = m // 2
    r = 3
    while m > 1:
        if r**2 > m:
            ret[m] = 1
            break
        while m%r==0:
            ret[r] += 1
            m = m//r
        r += 2
    return ret

def get_prime_dic(n):
    dic = {}

    i = 2
    while m % 2 == 0:
        ret[2] += 1
        m = m // 2

    while i <= n:
        while n % i == 0:
            n //= i
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        i += 1
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

    d = get_prime_dic(M)
    # print(d)

    ans = 1

    for k, v in d.items():
        ans *= combination(v + N - 1, v)
        ans %= 1000000007


    print(ans)

main()
