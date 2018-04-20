# https://projecteuler.net/problem=41
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?


def is_pandigital(n):
    l = sorted(map(int, list(str(n))))
    # print(l)
    for i in range(0, len(l)):
        if i + 1 != l[i]:
            return False

    return True


def is_prime(n):
    if 2 > n: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10  <----------------------
# 1 + 2 + 3 + 4 + 5 = 15
# 1 + 2 + 3 + 4 + 5 + 6 = 21
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 <-----------
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
#
# for i in range(10**3 + 1, 10**4, 2):
#     # print(i)
#     if is_pandigital(i) and is_prime(i):
#         print("prime pandigital = " + str(i))
#
# for i in range(10 ** 6 + 1, 10**7, 2):
#     # print(i)
#     if is_pandigital(i) and is_prime(i):
#         print("prime pandigital = " + str(i))
#         # break


i = 10**7 - 1

while i > 0:
    # print(i)
    if is_pandigital(i) and is_prime(i):
        print("largest prime pandigital = " + str(i))
        break

    l = list(map(int, list(str(i))))
    # print(l)
    for a in range(len(l)):
        for b in range(a + 1, len(l)):
            if l[a] == l[b]:
                l[b] = l[a] - 1 if l[a] - 1 > 0 else 0
    # print(l)
    ne = 0
    for o in range(len(l)):
        ne = ne * 10 + l[o]

    if i == ne:
        i -= 1
    else:
        i = ne

