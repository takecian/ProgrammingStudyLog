# note solved
# N = int(input())

M = 100000

c = [59049, 46656, 7776, 6561, 1296, 729, 216, 81, 36, 9, 6, 1]


cache = {}


def solve(x, l):
    if len(l) == 0:
        return 10000000000

    if x in cache:
        if len(l) in cache[x]:
            return cache[x][len(l)]

    t = l[0]
    if x // t > 0:
        res = []
        for i in range(x // t + 1):
            count = i
            rest = x - (t * i)
            if rest == 0:
                return count

            val = solve(rest, l[1:])
            if rest not in cache:
                cache[rest] = {}
            cache[rest][len(l[1:])] = val
            res.append(count + val)
        return min(res)
    else:
        val = solve(x, l[1:])
        if x not in cache:
            cache[x] = {}
        cache[x][len(l[1:])] = val
        return val


# for i in range(10):
#     val = 9 ** i
#     if val <= M:
#         print(val)
#         c.append(val)
#
# for i in range(10):
#     val = 6 ** i
#     if val <= M:
#         print(val)
#         c.append(val)

# count = 0

result = solve(N, c)
# for i in c:
#     if rest // i > 0:
#         count += rest // i
#         print(str(i) + ', ' + str(rest // i) + ' times, rest = ' + str(rest % i))
#         rest = rest % i
#
#     if rest == 0:
#         break

print(result)
