# https://projecteuler.net/problem=27


def get_prime_numbers(v):
    p = []

    for n in range(2, v):

        i = 2
        is_prime = True
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            p.append(n)

    return p


def calc(n, a, b):
    return n**2 + a * n + b


def is_prime(n):
    if n < 2:
        return False


    i = 2

    its_prime = True
    while i * i <= n:
        if n % i == 0:
            its_prime = False
            break
        i += 1

    return its_prime


p = get_prime_numbers(1001)

max_n = 0
max_product = 0

for b in p:
    for a in range(-999,1000):
        n = 0
        while True:
            v = calc(n, a, b)
            if not is_prime(v):
                break
            n += 1

        # print("consecutive :" + str(n) + ", " + str(a) + ", " + str(b))
        if n > max_n:
            max_n = n
            max_product = a * b


print(max_n)
print(max_product)