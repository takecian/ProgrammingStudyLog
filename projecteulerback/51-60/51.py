# https://projecteuler.net/problem=51

import itertools
import functools


def is_prime(n):
    if 2 > n: return False
    if 2 == n: return True
    if n % 2 == 0: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


for digit in range(2, 10):
    li = [0] * digit
    print("digit = " + str(digit) + ", " + str(li))
    for p in range(1, digit):
        for comb in itertools.combinations(list(range(digit)), p):
            v_dig = digit - p
            for raw_val in range(10 ** v_dig):
                val_list = list(map(int, list(str(raw_val).zfill(v_dig))))

                candidates = []
                for i in range(0, 10):
                    test_val_list = list(val_list)
                    test_li = list(li)
                    # print("comb = " + str(comb) + ", li = " +str(test_val_list))
                    if digit - 1 in comb:
                        break
                    for v in range(digit):
                        if v in comb:
                            test_li[v] = i
                        else:
                            test_li[v] = test_val_list[0]
                            del test_val_list[0]
                    # print(test_li)

                    # print("replace = " + str(comb) + ", li = " + str(test_li) + ", vdig = " + str(v_dig) + ", i = " + str(i))
                    target = functools.reduce(lambda x, y: x * 10 + y, test_li)
                    # print(target)
                    if is_prime(target) and len(str(target)) == digit:
                        candidates.append(target)

                if len(candidates) == 8:
                    print("prime = " + str(len(candidates)) + ", comb = " + str(comb) + ", val_list = " + str(val_list) + ", cand = " + str(candidates))
                    exit(0)
