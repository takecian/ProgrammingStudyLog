# https://projecteuler.net/problem=46

import math


def is_prime(n):
    if 2 > n: return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def update_prime_list(l, n):
    i = l[-1] + 1
    while i < n:
        if is_prime(i):
            l.append(i)
        i += 1

    return l


prime_list = [2, 3, 5]
for i in range(7, 100000, 2):
    print(i)

    if is_prime(i):
        # print(str(i) + " is prime.")
        continue

    prime_list = update_prime_list(prime_list, i)
    # print(prime_list)

    can_compose = False
    for p in prime_list:
        rest = i - p
        if rest <= 0:
            continue

        if rest == 1 or math.sqrt(rest / 2).is_integer():
            print("p = " + str(p) + ", rest = " + str(rest))
            can_compose = True
            break

    if not can_compose:
        print("ng = " + str(i))
        break

