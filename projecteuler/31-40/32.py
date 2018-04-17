# https://projecteuler.net/problem=32

import itertools


def check_pandigital(plicand_set, plier_set, a_set):
    products = []
    for plicand in itertools.permutations(plicand_set):
        p1 = int("".join(list(map(str, plicand))))
        for plier in itertools.permutations(plier_set):
            p2 = int("".join(list(map(str, plier))))
            answer = p1 * p2
            answer_list = list(str(answer))

            if len(answer_list) != len(a_set):
                continue

            if a_set == set(map(int, answer_list)):
                products.append(answer)

    return products


dig = [1, 2, 3, 4, 5, 6, 7, 8, 9]

products = []
for i in range(1, 8):
    for j in range(1, 8 - i):

        for multiplicand_set in itertools.combinations(dig, i):
            answer_set = [item for item in dig if item not in multiplicand_set]
            for multiplier_set in itertools.combinations(answer_set, j):
                answer_set2 = [item for item in answer_set if item not in multiplier_set]
                l = check_pandigital(multiplicand_set, multiplier_set, set(answer_set2))
                if len(l) > 0:
                    products += l


# print(sum(products))
print(sum(set(products)))
