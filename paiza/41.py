# https://paiza.jp/career/challenges/41/page/problem

from typing import List


def twice_one_digit(number):
    ret = number * 2
    if ret > 9:
        l = list(map(int, list(str(ret))))  # type: List[int]
        return sum(l)
    else:
        return ret


def solve(l):
    odds = list(map(int, l[1:15:2]))
    evens = list(map(int, l[::2]))
    odds_sum = sum(odds)
    evens_sum = sum(map(twice_one_digit, evens))

    val = odds_sum + evens_sum
    x = 10 - val % 10 if val % 10 != 0 else 0
    print(x)


count = int(input())  # number of cards
for i in range(count):
    li = list(input())
    solve(li)

