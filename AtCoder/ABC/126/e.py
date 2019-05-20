# https://atcoder.jp/contests/abc126/tasks/abc126_e
import itertools
from collections import Counter
from collections import defaultdict
import bisect


# Union find
class UnionFind():
    def __init__(self,size):
        self.table = [-1 for _ in range(size)]  # 負の値の場合根を表す。正の値は次の要素を返す、根まで続く

    #集合の代表を求める
    def find(self,x):
        while self.table[x] >= 0:
            #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def rewrite(self,x, p):
        while self.table[x] >= 0:
            #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            tmp = x
            x = self.table[x]
            self.table[tmp] = p
        return

    #併合
    def union(self,x,y):
        s1 = self.find(x)#根のindex,table[s1]がグラフの高さ
        s2 = self.find(y)
        if s1 != s2:#根が異なる場合
            if self.table[s1] != self.table[s2]:#グラフの高さが異なる場合
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                    self.rewrite(y, s1)
                else:
                    self.table[s1] = s2
                    self.rewrite(x, s2)
            else:
                #グラフの長さが同じ場合,どちらを根にしても変わらない
                self.table[s2] = s1
                self.rewrite(y, s1)
        return

    def num_group(self):
        # print(self.table)
        return self.table.count(-1)


def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)

    for _ in range(M):
        x, y, z = map(int, input().split())
        uf.union(x - 1, y - 1)
    print(uf.num_group())

if __name__ == '__main__':
    main()
