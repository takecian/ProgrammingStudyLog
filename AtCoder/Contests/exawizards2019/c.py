
import itertools
import collections
import bisect


def main():
    N, Q = map(int, input().split())
    S = list(input())
    T = []
    D = []
    for _ in range(Q):
        t, d = input().split()
        T.append(t)
        D.append(d)

    def is_l_out(start):
        pointer = start
        for i in range(Q):
            if S[pointer] == T[i]:
                if D[i] == 'L':
                    pointer -= 1
                    if pointer < 0:
                        return True
                else:  # R
                    pointer += 1
                    if pointer >= N:
                        pointer = N -1
        return False

    def is_r_out(start):
        pointer = start
        for i in range(Q):
            if S[pointer] == T[i]:
                if D[i] == 'L':
                    pointer -= 1
                    if pointer < 0:
                        pointer = 0
                else:  # R
                    pointer += 1
                    if pointer >= N:
                        return True
        return False

    left = 0
    right = N - 1
    l_candidate = -1
    while left <= right:
        mid = (left + right) // 2
        l_out = is_l_out(mid)
        if l_out:
            # print("l out = {}".format(mid))
            l_candidate = mid
        if l_out:
            left = mid + 1
        else:
            right = mid - 1

    left = 0
    right = N - 1
    r_candidate = N
    while left <= right:
        mid = (left + right) // 2
        # print(mid)
        r_out = is_r_out(mid)
        if r_out:
            # print("r out = {}".format(mid))
            r_candidate = mid
        if r_out:
            right = mid - 1
        else:
            left = mid + 1

    if l_candidate == -1 and r_candidate == N:  # どっちも消えない
        print(N)
    elif l_candidate == -1:  # 左は消えない
        print(r_candidate)
    elif r_candidate == N: # 右は消えない
        print(N - (l_candidate + 1))
    else:
        print(r_candidate - (l_candidate + 1))


if __name__ == '__main__':
    main()
