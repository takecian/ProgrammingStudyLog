# グリッド操作
dx4 = [0, 0, 1, -1]
dy4 = [1, -1, 0, 0]

for dx, dy in zip(dx4, dy4):
    break


dx8 = [0, 0, 1, -1, 1, -1, 1, -1]
dy8 = [1, -1, 0, 0, 1, 1, -1, -1]

for dx, dy in zip(dx8, dy8):
    break


# big value
INF = int(1e15)


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

print(primes(100))


# ソート済みの配列からの二分探索で Longest Increase Subsequence を作る, O(n logn)
def LIS(L):
    from bisect import bisect
    seq = []
    for i in L:
        pos = bisect(seq,i)
    if len(seq) <= pos:
        seq.append(i)
    else:
        seq[pos] = i
    return len(seq)

# 一つの要素と残りのリストを作る時の読み込み
K, *A = list(map(int, input().split()))


# 素因数分解
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