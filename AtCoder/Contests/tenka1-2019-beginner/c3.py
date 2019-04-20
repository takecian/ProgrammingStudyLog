
def main():
    N = int(input())
    S = list(input())
    # print(S)

    right_white = S.count('.')
    left_black = 0

    ans = min(S.count('.'), S.count('#'))
    for i in range(len(S)):
        if S[i] == '#':  # black
            left_black += 1
        else: # white
            right_white -= 1

        ans = min(ans, left_black + right_white)

    print(ans)

if __name__ == '__main__':
    main()
