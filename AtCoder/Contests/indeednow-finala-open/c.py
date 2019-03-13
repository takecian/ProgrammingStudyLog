# https://indeednow-finala-open.contest.atcoder.jp/tasks/indeednow_2015_finala_c

def main():
    # https://indeednow-finala-open.contest.atcoder.jp/tasks/indeednow_2015_finala_c

    N, M = map(int, input().split())

    dp_tlc = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

    # abcw = [list(map(int, input().split())) for _ in range(N)]
    for _ in range(N):
        a, b, c, w = map(int, input().split())
        dp_tlc[a][b][c] = max(dp_tlc[a][b][c], w)

    # for j in abcw:
    #     dp_tlc[j[0]][j[1]][j[2]] = max(dp_tlc[j[0]][j[1]][j[2]], j[3])
    #     # print("{}, {}, {} = {}".format(j[0],j[1],j[2], dp_tlc[j[0]][j[1]][j[2]]))

    for t in range(101):
        for l in range(101):
            for c in range(101):
                if t >= 1:
                    dp_tlc[t][l][c] = max(dp_tlc[t][l][c], dp_tlc[t - 1][l][c])
                if l >= 1:
                    dp_tlc[t][l][c] = max(dp_tlc[t][l][c], dp_tlc[t][l - 1][c])
                if c >= 1:
                    dp_tlc[t][l][c] = max(dp_tlc[t][l][c], dp_tlc[t][l][c - 1])
                # dp_tlc[t][l][c] = max(dp_tlc[t][l][c], dp_tlc[t-1][l][c], dp_tlc[t][l-1][c], dp_tlc[t][l][c-1])
                # print(dp_tlc[t][l][c])

    for _ in range(M):
        x, y, z = map(int, input().split())
        print(dp_tlc[x][y][z])


if __name__ == "__main__":
    main()

