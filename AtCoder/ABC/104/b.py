# https://atcoder.jp/contests/abc104/tasks/abc104_b


def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        S = S.replace('A', '', 1).replace('C', '', 1)
        if all(c.islower() for c in S):
            print("AC")
            exit()

    print("WA")


if __name__ == '__main__':
    main()


