# ソートされてない配列から LIS を作っていく。LISはソート済みの配列なので二分探索しつつ更新していく O(n logn)
from bisect import bisect_left

def LIS(L):
    seq = []
    for i in L:
        pos = bisect_left(seq, i)
        if len(seq) <= pos:  # 既存の部分列のすべてより大きいなら追加する
            seq.append(i)
        else:  # 既存の部分列の中に含まれるんだったら、自分より大きくて一番小さいものと差し替える
            seq[pos] = i
    return len(seq)

print(LIS([1,3,9,2,4,10,4,2,9]))
