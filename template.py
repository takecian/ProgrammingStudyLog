
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


# エラトステネスの篩
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
