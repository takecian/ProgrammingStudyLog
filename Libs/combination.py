# Calculate count of combination
def combination(n, r):
    a = 1
    b = 1
    for i in range(r):
        a *= (n - i)
        b *= (i + 1)
    return a // b


def cmb(n, r):
    if n - r < r:  # 計算量が少ない方でやる
        r = n - r

    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]  # 分子
    denominator = [k + 1 for k in range(r)]  # 分母

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
                print(numerator)
                print(denominator)
                print('')

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


print(cmb(12, 6))