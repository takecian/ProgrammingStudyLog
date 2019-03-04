# https://abc084.contest.atcoder.jp/tasks/abc084_c

def main():
    N = int(input())
    # C: 所要時間、S: 始発の時間、F: 発射間隔
    CSFs = [list(map(int, input().split())) for _ in range(N-1)]
    C = [CSF[0] for CSF in CSFs]
    S = [CSF[1] for CSF in CSFs]
    F = [CSF[2] for CSF in CSFs]

    for i in range(N):
        total = 0
        for j in range(i, N-1):
            if total < S[j]:
                total = S[j] + C[j]
            elif total % F[j] == 0:
                total += C[j]
            else:
                total += C[j] + (F[j] - total % F[j])
        print(total)


main()


