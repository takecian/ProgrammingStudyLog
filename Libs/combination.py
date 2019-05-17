# Calculate count of combination
def combination(n, r):
    a = 1
    b = 1
    for i in range(r):
        a *= (n - i)
        b *= (i + 1)
    return a // b

# エラトステネスの篩: n 以下の数字うち、素数のリスト, O(n loglogn)
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):  # 非素数を見つけたいから sqrt(n) まで調べたら良い(ペアが絶対 sqrt(n) 以下
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):  # is_prime[i] は素数、その倍数を False にする
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]