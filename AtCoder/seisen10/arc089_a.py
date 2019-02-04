# https://atcoder.jp/contests/abc086/tasks/arc089_a

N = int(input())


def is_reachable(src, dst):
    can_go = True
    dt = dst[0] - src[0]
    dist = abs(dst[1] - src[1]) + abs(dst[2] - src[2])
    if dt < dist:
        can_go = False
    if dt % 2 != dist % 2:
        can_go = False
    return can_go


route = [list(map(int, input().split())) for _ in range(N)]
route.insert(0, [0, 0, 0])

# print(route)

reachable = True

for i in range(N):
    source = route[i]
    destination = route[i + 1]
    if not is_reachable(source, destination):
        reachable = False

if reachable:
    print("Yes")
else:
    print("No")
