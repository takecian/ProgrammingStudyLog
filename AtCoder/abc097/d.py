def is_sorted(l):
    for i in range(len(l)):
        if l[i] != i + 1:
            return False
    return True


def can_go(start, goal, sw, d):
    if d > M: return False
    if start == goal: return True

    for s in sw:
        if s[0] == start:
            if can_go(s[1], goal, sw, d + 1):
                return True
        elif s[1] == start:
            if can_go(s[0], goal, sw, d + 1):
                return True
    return False


def try_s(l, sw):
    maps = swap_map(sw)
    count = 0
    for idx, c in enumerate(l):
        if idx == c:
            count += 1
            continue
        if can_go(idx, c, sw, 0):
            # print(str(c) + ' can go home')
            count += 1
    print(count)


def swap_map(sw):
    maps = {}
    for i in range(M):
        for s in sw:
            if s[0] == i:
                if i not in maps:
                    maps[i] = [s[1]]
                else:
                    maps[i].append(s[1])
            if s[1] == i:
                if i not in maps:
                    maps[i] = [s[0]]
                else:
                    maps[i].append(s[0])
    for m in maps:
        for r in m:

    return maps


N, M = map(int, input().split())
p = list(map(int, input().split()))

swaps = []
for i in range(M):
    x, y = map(int, input().split())
    swaps.append((x-1, y-1))


p = list(map(lambda x: x - 1, p))
# print(p)
# print(swaps)


if is_sorted(p):
    print(len(p))
else:
    print()
    # try_s(p, swaps)
