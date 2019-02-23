# https://beta.atcoder.jp/contests/agc029/tasks/agc029_a


def main():
    S = list(input())
    count = 0
    w_offset = 0
    for i in range(len(S)):
        if S[i] == "W":
            count += i - w_offset
            w_offset += 1

    print(count)


if __name__ == '__main__':
    main()
