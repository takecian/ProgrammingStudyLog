# https://projecteuler.net/problem=35


def is_prime(n):
    if n < 2: return False

    i = 2
    its_prime = True

    while i * i <= n:
        if n % i == 0:
            its_prime = False
            break
        i += 1

    return its_prime


count = 4 # 2, 3, 5, 7 are 1-digit primes
for i in range(10, 1000000):
    if not is_prime(i):
        continue

    l = list(str(i))
    r = l[1:] + l[:1]

    # print(r)
    # print(l)

    circular_prime = True
    while l != r:
        v = int("".join(r))
        # print(v)
        if not is_prime(v):
            circular_prime = False
            break

        r = r[1:] + r[:1]

    if circular_prime:
        count += 1
        # print(str(i) + " is circular prime.")

print(count)
