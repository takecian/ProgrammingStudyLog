def get_subs(l, c, n):
    # print('c = ' + str(c))
    canl = []
    for index, val in enumerate(l):
        if val == c:
            candidate = ''
            for i in range(n):
                if index + i < len(l):
                    candidate += l[index + i]
            canl.append(candidate)
    res = list(set(canl))
    # print(res)
    return res


s = input()
K = int(input())

cand = sorted(list(set(list(s))))
cand.reverse()
# print(cand)


subl = []
while len(subl) < K:
    c = cand.pop()
    n = 1
    while n <= K:
        canl = get_subs(list(s), c, n)
        subl.extend(canl)
        subl = list(set(subl))
        n += 1

subl = sorted(subl)
# print(subl)
print(subl[K-1])
