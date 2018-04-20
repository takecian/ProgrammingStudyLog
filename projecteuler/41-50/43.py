# https://projecteuler.net/problem=43


import itertools
import functools


def three_digit(li, idx):
    return li[idx] * 100 + li[idx + 1] * 10 + li[idx + 2]


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0
c1 = list(itertools.combinations(l,1));

for p1 in c1:
    l1 = list(l)
    d1 = p1[0]

    l1.remove(p1[0])
    # print(p1[0])
    # print("len(l1) = " + str(len(l1)))

    # d2, d3, d4
    c2 = list(itertools.permutations(l1, 3));
    for p2 in c2:
        l2 = list(l1)
        d2, d3, d4 = p2[0], p2[1], p2[2]
        l2.remove(p2[0])
        l2.remove(p2[1])
        l2.remove(p2[2])
        # print("len(l2) = " + str(len(l2)))

        if (d2 * 100 + d3 * 10 + d4) % 2 != 0:
            continue

        c5 = list(itertools.permutations(l2))
        # print(len(c5))
        for p5 in c5:
            d5, d6, d7, d8, d9, d10 = p5[0], p5[1], p5[2], p5[3], p5[4], p5[5]
            # print(str(d5) + ", " + str(d6) + ", " + str(d7) + ", " + str(d8) + ", " + str(d9) + ", " + str(d10))

            # fl = [1, 4, 0, 6, 3, 5, 7, 2, 8, 9]
            fl = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
            # print(fl)
            # print(three_digit(fl, 2))
            # print(three_digit(fl, 3))
            # print(three_digit(fl, 4))
            # print(three_digit(fl, 5))
            # print(three_digit(fl, 6))
            # print(three_digit(fl, 7))

            if three_digit(fl, 2) % 3 != 0:
                # print("not meet 3, " + str(d3) + ", " + str(d4) + ", " + str(d5))
                continue
            if three_digit(fl, 3) % 5 != 0:
                # print("not meet 5, " + str(d2) + ", " + str(d3) + ", " + str(d4))
                continue
            if three_digit(fl, 4) % 7 != 0:
                # print("not meet 7, " + str(d2) + ", " + str(d3) + ", " + str(d4))
                continue
            if three_digit(fl, 5) % 11 != 0:
                # print("not meet 11, " + str(d2) + ", " + str(d3) + ", " + str(d4))
                continue
            if three_digit(fl, 6) % 13 != 0:
                # print("not meet 13, " + str(d2) + ", " + str(d3) + ", " + str(d4))
                continue
            if three_digit(fl, 7) % 17 != 0:
                # print("not meet 17, " + str(d2) + ", " + str(d3) + ", " + str(d4))
                continue

            v = functools.reduce(lambda x, y: x * 10 + y, fl)
            print("sub-string divisible = " + str(v))
            total += v

print(total)
