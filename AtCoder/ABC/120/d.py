# https://atcoder.jp/contests/abc120/tasks/abc120_d

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline

# Union find
class UnionFind():
    #負の値の場合根を表す。絶対値はツリーの高さ
    #正の値は次の要素を返す、根まで続く
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]
        self.size_table = [1 for _  in range(size)]

        # 集合の代表を求める
    def find(self, x):
        while self.table[x] >= 0:
            # 根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x

        # 併合
    def union(self, x, y):
        s1 = self.find(x)  # 根のindex,table[s1]がグラフの高さ
        s2 = self.find(y)
        if s1 != s2:  # 根が異なる場合
            if self.table[s1] != self.table[s2]:  # グラフの高さが異なる場合
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                    self.size_table[s1] += self.size_table[s2]
                else:
                    self.table[s1] = s2
                    self.size_table[s2] += self.size_table[s1]
            else:
                # グラフの長さが同じ場合,どちらを根にしても変わらない
                # その際,グラフが1長くなることを考慮する
                self.table[s1] += -1
                self.table[s2] = s1
                self.size_table[s1] += self.size_table[s2]
        return

    def size(self, x):
        return self.size_table[self.find(x)]


def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges = list(map(lambda l: [i-1 for i in l], bridges))
    # print(bridges)

    fuben = N * (N-1) // 2
    answers = []
    uf = UnionFind(N)
    for j in range(len(bridges)-1, 0, -1):
        br = bridges[j]

        if uf.find(br[0]) == uf.find(br[1]):  # もともと繋がってる
            answers.insert(0, fuben)
        else:  # 新しく繋がる
            b1 = uf.size(br[0])
            b2 = uf.size(br[1])
            fuben = fuben - b1 * b2
            answers.insert(0, fuben)

        uf.union(br[0], br[1])

    # print(answers)

    for a in answers:
        print(a)

        # 最後
    print(N * (N-1) // 2)


if __name__ == '__main__':
    main()

