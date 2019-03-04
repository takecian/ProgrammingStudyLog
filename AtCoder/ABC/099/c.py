# https://atcoder.jp/contests/abc099/tasks/abc099_c

def main():
    max_val = 10**5 + 1
    dp = [i for i in range(max_val)]  # i 円作るのに必要な引き出す回数。初期値は全部１円で引き出した場合の回数

    for i in range(max_val):
        p = 1
        while p < max_val:
            dp[i] = min(dp[i], dp[i - p] + 1)
            p *= 6
        p = 1
        while p < max_val:
            dp[i] = min(dp[i], dp[i - p] + 1)
            p *= 9

    N = int(input())
    print(dp[N])


if __name__ == '__main__':
    main()
