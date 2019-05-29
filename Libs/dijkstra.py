from collections import defaultdict
from heapq import heappop, heappush


class Graph:
    """
    隣接リストによる有向グラフ
    """
    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra:
    """
    ダイクストラ法（二分ヒープ）による最短経路探索
    計算量: O((E+V)logV)
    """
    def __init__(self, graph, start):
        self.g = graph.graph

        # big value
        INF = int(1e15)
        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
        self.dist = defaultdict(lambda: INF)
        self.dist[start] = 0

        # 最短経路でのそのノードの1つ前のノード
        self.prev = defaultdict(lambda: None)

        # startノードを優先度付きキューに入れる、タプル最初の要素が優先度順で並べ替えられる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    # startノードからgoalノードまでの最短距離
    def shortest_distance(self, goal):
        return self.dist[goal]

    # startノードからgoalノードまでの最短経路
    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]
