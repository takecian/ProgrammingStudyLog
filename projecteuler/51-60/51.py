# https://projecteuler.net/problem=51

import itertools
import functools


def is_prime(n):
    if 2 > n: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


for digit in range(2, 5):
    li = [0] * digit
    print("digit = " + str(digit) + ", " + str(li))
    for p in range(1, digit):
        for comb in itertools.combinations(list(range(digit)), p):
            for i in range(1, 10):
                test_li = list(li)
                for v in comb:
                    test_li[v] = i
                v_dig = digit - p
                for i in range(10**v_dig):

                print("replace = " + str(comb) + ", li = " + str(test_li) + ", vdig = " + str(v_dig))


# for i in range(56003, 100000):
#     # i = 56003
#     dig = len(str(i))
#
#     for p in range(1, dig):
#         for comb in itertools.combinations(list(range(dig)), p):
#             # print("replace = " + str(comb))
#             int_li = list(map(int, list(str(i))))
#             candidate = 0
#             prime_num = 0
#             for r in range(10):
#                 temp_int_li = list(int_li)
#                 for v in comb:
#                     temp_int_li[v] = r
#                 candidate = functools.reduce(lambda x, y: x * 10 + y, temp_int_li)
#                 if len(str(i)) != len(str(candidate)):
#                     continue
#                 if is_prime(candidate):
#                     # print("candidate is prime = " + str(candidate))
#                     prime_num += 1
#                 # else:
#                 #     print("candidate = " + str(candidate))
#                 if prime_num == 8:
#                     print("find! = " + str(i))
#                     exit(0)
