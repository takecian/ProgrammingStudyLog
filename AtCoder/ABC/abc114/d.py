# https://atcoder.jp/contests/abc114/tasks/abc114_d

N = int(input())


def get_primes_dic(v):
    m = {}
    i = 2

    while i <= v:
        while v % i == 0:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
            v //= i

        i += 1

    return m


prime_dict = {}

for i in range(1, N+1):
    d = get_primes_dic(i)

    for k, v in d.items():
        if k in prime_dict:
            prime_dict[k] += v
        else:
            prime_dict[k] = v

    # print(d)

print(prime_dict)


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


prime_list = []

for i in range(99):
    if is_prime(i):
        prime_list.append(i)


for i in range(len(prime_list)-2):
    for j in range(i+1, len(prime_list)-1):
        for k in range(j+1, len(prime_list)):
            i_c = prime_dict[i] if i in prime_dict else 0
            j_c = prime_dict[j] if j in prime_dict else 0
            k_c = prime_dict[k] if k in prime_dict else 0
            if