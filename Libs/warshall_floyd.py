import collections

Edge = collections.namedtuple("Edge", "start end weight")

def solve_by_warshall_floyd(n, edges):
    """
    ワーシャルフロイド法で最短経路を計算する
    Order = O(N**3)
    :return:
    """
    # big value
    INF = int(1e15)
    d = [[INF] * n for _ in range(n)]

    for i in range(n):
        d[i][i] = 0

    for edge in edges:
        d[edge.start][edge.end] = edge.weight
        # d[edge.end][edge.start] = edge.weight # もし無効グラフならこれもたす

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d

def main():
    N = int(input())
    edges = []
    for _ in range(N):
        s, e, w = map(int, input().split())
        edges.append(Edge(s-1, e-1, w))

    distance = solve_by_warshall_floyd(N, edges)

    print(distance)


if __name__ == '__main__':
    main()
