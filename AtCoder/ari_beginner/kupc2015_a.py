# https://atcoder.jp/contests/kupc2015/tasks/kupc2015_a

T = int(input())
S = [input() for _ in range(T)]


def count_tape(s):
    count = 0
    while True:
        kyoto_i = s.find("kyoto")
        tokyo_i = s.find("tokyo")

        if kyoto_i != -1 and tokyo_i != -1:
            if kyoto_i < tokyo_i:
                s = s[kyoto_i + 5:]
                count += 1
            else:
                s = s[tokyo_i + 5:]
                count += 1
        elif kyoto_i != -1:
            s = s[kyoto_i + 5:]
            count += 1
        elif tokyo_i != -1:
            s = s[tokyo_i + 5:]
            count += 1
        else:
            break
    return count


for s in S:
    print(count_tape(s))

