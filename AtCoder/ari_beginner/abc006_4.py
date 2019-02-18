# https://atcoder.jp/contests/abc006/tasks/abc006_4

def main():

    N = int(input())
    C = [int(input()) for _ in range(N)]


    from bisect import bisect
    big_val = 10**5
    dp = [big_val] * (N+1)
    dp[0] = 0

    for c in C:
        pos = bisect(dp, c)
        # print("pos = {}, c = {}".format(pos, c))
        dp[pos] = c

    # print(dp)
    for i in range(N+1):
        if dp[i] == big_val:
            print(N - i + 1)
            exit()

    print(0)

main()



