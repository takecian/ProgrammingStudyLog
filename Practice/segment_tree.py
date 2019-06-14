import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class SegmentTree:
    def __init__(self, li):
        length = len(li)
        self.low_line_size = 1
        while self.low_line_size < length:
            self.low_line_size *= 2

        seg_tree_size = self.low_line_size * 2 - 1
        self.seg_tree = [0] * seg_tree_size  # 使われないスペースもあるので答えに影響のない値を入れる

        # 最初の要素を下段に入れる、下段は tree_size - 1 から始まる
        for i in range(length):
            self.seg_tree[self.low_line_size - 1 + i] = li[i]
        # 上段の要素を計算していく、下から２段目の右から計算する
        for i in range(self.low_line_size - 2, -1, -1):
            self.seg_tree[i] = min(self.seg_tree[i * 2 + 1], self.seg_tree[i * 2 + 2])
        print(self.seg_tree)

    def update(self, index, val):
        '''
        :param index: index of value changed
        :param val: new value
        :return:
        '''

        tree_index = index + self.low_line_size - 1
        self.seg_tree[tree_index] = val

        while tree_index > 0:
            tree_index = (tree_index - 1) // 2
            self.seg_tree[tree_index] = min(self.seg_tree[tree_index * 2 + 1], self.seg_tree[tree_index * 2 + 2])
        print(self.seg_tree)

    def query(self, a, b, k=0, l=0, r=-1):
        if r < 0:
            r = self.low_line_size

        # クエリの区間外 → 答えに影響のない値を返す
        if r <= a or b <= l:
            return 10**10

        # クエリの範囲内 -> 答えの計算に使うので値を返す
        if a <= l and r <= b:
            return self.seg_tree[k]

        # クエリの範囲にあるが完全に含まれてるわけじゃないのでさらに分割していく
        vl = self.query(a, b, k * 2 + 1, l, (l+r) // 2)  # １階層下の左側を調べる
        vr = self.query(a, b, k * 2 + 2, (l+r) // 2, r)  # １階層下の右側を調べる
        return min(vl, vr)


def main():
    n = list(map(int, input().split()))
    st = SegmentTree(n)

    print(st.query(0, 3))
    st.update(1, -1)
    print(st.query(0, 3))
    print(st.query(1, 2))
    print(st.query(2, 3))


if __name__ == '__main__':
    main()
