# https://paiza.jp/challenges/43/show

import re
import string

inp = list(input())

lowerReg = re.compile(r'^[a-z]+$')


def is_alphabet(s):
    return lowerReg.match(s) is not None


def parse(l):
    res = {}

    mul = 0
    while len(l) > 0:
        c = l.pop(0)
        # print(c)

        if c.isdigit():
            mul = mul * 10 + int(c)
        elif is_alphabet(c):
            mul = 1 if mul == 0 else mul
            if c in res:
                res[c] += mul
            else:
                res[c] = mul
            mul = 0
        elif c == '(':
            child = parse(l)
            mul = 1 if mul == 0 else mul
            child = {x: child[x] * mul for x in child}

            # merge
            for key, val in child.items():
                if key in res:
                    res[key] += val
                else:
                    res[key] = val

            mul = 0
        elif c == ')':
            break

    return res


ans = parse(inp)

for c in list(string.ascii_lowercase):
    if c not in ans:
        ans[c] = 0

for key, val in sorted(ans.items()):
    print(str(key) + ' ' + str(val))
