# https://atc001.contest.atcoder.jp/tasks/unionfind_a

# Union find
class UnionFind():
    #負の値の場合根を表す。絶対値はツリーの高さ
    #正の値は次の要素を返す、根まで続く
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]

    #集合の代表を求める
    def find(self,x):
        while self.table[x] >= 0:
            #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x

    #併合
    def union(self,x,y):
        s1 = self.find(x)#根のindex,table[s1]がグラフの高さ
        s2 = self.find(y)
        if s1 != s2:#根が異なる場合
            if self.table[s1] != self.table[s2]:#グラフの高さが異なる場合
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                else:
                    self.table[s1] = s2
            else:
                #グラフの長さが同じ場合,どちらを根にしても変わらない
                #その際,グラフが1長くなることを考慮する
                self.table[s1] += -1
                self.table[s2] = s1
        return


def main():
    N, Q = map(int, input().split())

    uf = UnionFind(N)
    for _ in range(Q):
        P, A, B = map(int, input().split())
        if P == 0:
            uf.union(A, B)
        else:
            if uf.find(A) == uf.find(B):
                print("Yes")
            else:
                print("No")

main()