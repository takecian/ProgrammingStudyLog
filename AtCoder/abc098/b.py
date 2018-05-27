N = int(input())
S = input()


def create_map(s):
    m = {}
    for c in s:
        if c in m:
            m[c] += 1
        else:
            m[c] = 1
    return m


def common(m1, m2):
    c = 0
    # print(m1)
    # print(m2)
    for key in m1.keys():
        if key in m2:
            c += 1
    # print('commmon = ' + str(c))
    return c


m = 0
for i in range(1, len(S)):
    # print(S[:i])
    # print(S[i:])
    m1 = create_map(S[:i])
    m2 = create_map(S[i:])
    com = common(m1, m2)
    if com > m:
        m = com

print(m)