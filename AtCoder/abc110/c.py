# https://atcoder.jp/contests/abc110/tasks/abc110_c

S = input()
T = input()


def to_dict(s):
    dic = {}
    for c in list(s):
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

    return sorted(list(dic.values()))


sl = to_dict(S)
tl = to_dict(T)

if to_dict(S) == to_dict(T):
    print("Yes")
else:
    print("No")

