# グリッド操作
dx4 = [0, 0, 1, -1]
dy4 = [1, -1, 0, 0]

for dx, dy in zip(dx4, dy4):
    break


dx8 = [0, 0, 1, -1, 1, -1, 1, -1]
dy8 = [1, -1, 0, 0, 1, 1, -1, -1]

for dx, dy in zip(dx8, dy8):
    break


# big value
INF = int(1e15)


# エラトステネスの篩: n 以下の数字うち、素数のリスト, O(n loglogn)
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):  # 非素数を見つけたいから sqrt(n) まで調べたら良い(ペアが絶対 sqrt(n) 以下
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):  # is_prime[i] は素数、その倍数を False にする
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

print(primes(100))


# ソート済みの配列からの二分探索で Longest Increase Subsequence を作る, O(n logn)
def LIS(L):
    from bisect import bisect
    seq = []
    for i in L:
        pos = bisect(seq,i)
    if len(seq) <= pos:
        seq.append(i)
    else:
        seq[pos] = i
    return len(seq)

# 一つの要素と残りのリストを作る時の読み込み
K, *A = list(map(int, input().split()))


# 素因数分解
def prime_dic(n):
    dic = {}

    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        i += 1

    if n > 1:
        dic[n] = 1
    return dic


# Calculate count of combination
def combination(n, r):
    a = 1
    b = 1
    for i in range(r):
        a *= (n - i)
        b *= (i + 1)
    return a // b


# Union find
class UnionFind():
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]  # 負の値の場合根を表す。絶対値はツリーの高さ 正の値は次の要素を返す、根まで続く
        self.size = [1 for _  in range(size)]

    #集合の代表を求める
    def find(self,x):
        while self.table[x] >= 0:
            #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    #併合
    def union(self,x,y):
        s1 = self.find(x)#根のindex,table[s1]がグラフの高さ
        s2 = self.find(y)
        if s1 != s2:#根が異なる場合
            if self.table[s1] != self.table[s2]:#グラフの高さが異なる場合
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                    self.size[s1] += self.size[s2]
                else:
                    self.table[s1] = s2
                    self.size[s2] += self.size[s1]
            else:
                #グラフの長さが同じ場合,どちらを根にしても変わらない
                #その際,グラフが1長くなることを考慮する
                self.table[s1] += -1
                self.table[s2] = s1
                self.size[s1] += self.size[s2]
        return

    def group_size(self, x):
        return self.size[self.find(x)]


# Bit 全探索
l = []  # linked_list
pattern = 1 << len(l)  # 1 をリストの長さだけ左にシフトする
for i in range(pattern):
    scope = []
    for j in range(len(l)):
        if (i >> j) & 1:
            scope.append(l[j])


# 直積
import itertools
for st, tt in itertools.product([0, 1], ["1", "2"]):
    print(st)
    print(tt)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)



# 拡張ユークリッドの互除法：ax + by = gcd(a, b) となる x, y を返す
def extgcd(a, b):
    # ２つの等式を繰り返し引いていく
    x0, y0 = 1, 0  # a = X * x0 + Y * 0 ← 常にこっちの方が大きい
    x1, y1 = 0, 1  # b = X * 0  + Y * y0

    while b:
        q = a // b
        r = a % b
        x2 = x0 - q * x1
        y2 = y0 - q * y1

        a = b
        b = r
        x0, y0 = x1, y1
        x1, y1 = x2, y2

    return a, x0, y0


print(extgcd(12, 21))
