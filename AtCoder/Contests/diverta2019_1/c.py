#
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    inside = 0

    top_B = 0
    tail_A = 0
    both = 0
    for _ in range(N):
        s = input()
        inside += s.count('AB')
        if s[0] == 'B' and s[-1] == 'A':
            both += 1
        else:
            if s[0] == 'B':
                top_B += 1
            elif s[-1] == 'A':
                tail_A += 1
    # print('inside = {}, top b = {}, tail a = {}, both = {}'.format(inside, top_B, tail_A, both))
    ans = inside

    if both > 1:
        ans += (both - 1)
        both = 1

    if both > 0:
        if tail_A == 0:
            tail_A += 1
            both -= 1
        if top_B == 0 and both > 0:
            top_B += 1
            both -= 1

    while both > 0 and top_B > 0 and tail_A > 0:
        ans += 2
        both -= 1
        tail_A -= 1
        top_B -= 1

        if both > 0:
            if tail_A == 0:
                tail_A += 1
                both -= 1
        if both > 0:
            if top_B == 0:
                top_B += 1
                both -= 1

    ans += min(top_B, tail_A)

    print(ans)


if __name__ == '__main__':
    main()
