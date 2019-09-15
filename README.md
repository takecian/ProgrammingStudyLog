# Programming Study Log

## Contest

* https://projecteuler.net/
* http://atcoder.jp/
* https://paiza.jp/challenges
* https://leetcode.com

### Snippet

[A collection of useful methods](snippet_for_leetcode.py) for competitive programming.

## Knowledge
### Order
|テストケース|Order|メモ|
|:--|:--|:--|
|10^8以上|O(N)でいけるか微妙、O(logN)かO(1)||
|10^5以上|O(N)かO(N log N)|二部探索とか累積和とか考える|
|3000|O(N^2)||
|500|N^3||
|100|N^3||
|50|N^5||
|20|2^N||

1 秒間で処理できる for 文ループの回数は、10^8=100,000,000 回程度

### 桁
* 1000=10^3 は大体 1024=2^10
* log10 2 = 0.301
  * 例：2**50 の10進数での桁数を考える
  * log10 2**50 = 50 * log10 2 = 50 * 0.301 = 15.5 -> 16桁

## Language

* Haskell
* Rust

## コーディング面接で知っておきたい10の知識
参考：https://www.youtube.com/watch?v=r1MXwyiGi_U

1. DFS
1. BFS
1. Parentheses matching
1. Hash table
1. pointer manipulation
1. reversing linked list
  * https://leetcode.com/problems/reverse-linked-list/
1. sort fundamentals
1. recursion
1. custom data structure
1. binary search

## Pattern

問題を解くときの着目点

### Arrays & Strings

####

* 文字列を先頭から走査していく
  * https://leetcode.com/problems/strobogrammatic-number/

#### 回文・辞書式順序
* 文字列を reverse して比較してみる
* 真ん中から左・右に広げていく
* 前方から比較してみる
* 後ろから for 文を回してみる
  * 辞書式順序で最小の文字を作る時は後ろからも見てみる

#### 文字列
* 回転する string の substring → string + string に対して含まれるか調べる 

#### 配列

* Sort したら簡単に解けないか
  * https://leetcode.com/problems/wiggle-sort/
  * https://leetcode.com/problems/array-partition-i/
* Reverse したら簡単に解けないか
* 2つポインタ持たせて不要なループを減らせないか（しゃくとり方）
  * 先頭に２つポインタを持たせてずらしていく
  * 先頭と最後尾からポインタをずらしていくパターン
    * https://leetcode.com/problems/3sum/
* 二分探索すると早くできないか
  * 端っこの処理が難しくなりそうなら番兵的なものを置くと簡潔にできないか
* 累積和(Cumulative sum)を計算して簡単にならないか
  * 前方からの累積和、後方からの累積和を考える
  * 全部の中から各要素をそれぞれ一つ取り除いたものを作る時に、前方&後方からの累積和を各ステップで組み合わせることで実現できる
    * https://leetcode.com/problems/product-of-array-except-self/
* 三角形構造の配列をいじる場合は上位の配列の先頭と最後に要素を追加した配列を２つ作ると計算しやすくなる
  * https://leetcode.com/problems/triangle/
    ```javascript
    [
     [2],
    [3,4]
    ]
    ```
    上位層の値を階層に加える場合は、
    ```buildoutcfg
    [
    [0,2],
    [2,0],
    [3,4]
    ]
    ```
    `[0,2]`, `[2,0]` を作ってそれぞれ足すと簡単に実装できる。
  * 
    

### Linked lists

* head の前に Dummy node を作って`dummy.next = head` を使うと便利
  * `while cursor` みたいな感じで走査していく
* ポインタを２つ用意して異なる速度で動かしてみる
* 再帰と組み合わせて解くパターン
  * https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
* 先頭から走査していって、不要なものを取り除くパターン、next を書き換えるタイミングに注意
  * https://leetcode.com/problems/remove-linked-list-elements/
* リストの同士の計算は数値に変換してしまうと桁上がりを気にしなくて楽、 Dummy node も使う
  * https://leetcode.com/problems/add-two-numbers-ii/

### Stacks & Queues

* 括弧の有効判定に stack を使う
  * https://leetcode.com/problems/valid-parentheses/

### Graph & Tree

* 順列(itertools.permutations)でルートの選択肢を全列挙
* ダイクストラ法
  * 最短経路探索に使う
  * 全部の経路のコストが正
  * heapq(優先度付きque)を使って実装する
* ワーシャルフロイド法
  * 全２点間の経路を探す
* UnionFind で連結判定できないか
  * 辺を追加していくことしかできないので、辺を削除する話があったら reverse して考える
  * 最小全域木はクラスカル法で解く時に UnionFind を使う
* 連結グラフを考える時、それは一本道かスター型のどちらがよさそうか
* DFS
* BFS
* 二部グラフ(bipartite graph)
  * 頂点集合を二つの部分集合に分割した時に各集合内の頂点同士の間には辺がないようにできるグラフのこと
  * 2色で彩色できるか試すことでテストできる(DFSかBFS)
#### ある区間の最小値、最大値をたくさん聞かれる（クエリ）
* セグメント木を考える
  * 要素数 N 個の場合 2N-1 個からなるツリー
  * 上位は下位の２つの要素の和とか差とか最小値とか最大値とかになる
  * 親→子：2倍して +1 or +2
  * 子→親：-1 して2で割る
  
### Grid(格子型)

* グリッドと二次元配列で x y の順番が直感と異なるので注意
* たどり着けるかどうか
  * DFS(depth-first search)
* 最短経路
  * BFS(breath-first search)
* 周辺を走査する時は配列作るといい
```
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    for dy, dx in zip(dxs, dys):
       xxx
```
  * https://leetcode.com/problems/flood-fill/

* 四角形が出てきたら中点をうまく活用できないか考える

### Recursion
* 問題を小さく分割して解く
  * https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
* 取りうるパターンを再帰の中で分岐していく
  * https://leetcode.com/problems/generate-parentheses/
* 条件によって再帰させる範囲を決めていく
  * https://leetcode.com/problems/trim-a-binary-search-tree/

### DP(動的計画法)

#### 最大値、最小値
直接計算すると大きな時間がかかってしまう問題に対し、途中の計算結果をうまく再利用することで計算効率を上げる手法のこと。
最大値(最大和)とか、最小値を計算する時に使うケースが多い。
* ナップサック問題
* 最長共通部分列問題
  * Longest Common Subsequense
* 最長増加部分列
  * LIS : Longest Increasing Subsequense
  * 挿入ソートする時の操作の回数とかもこれ

#### 最大長
直前までの最長＋今の時点の文字（条件が一致するなら）、という考え方で連続する長さの計算ができる。
* https://atcoder.jp/contests/abc141/tasks/abc141_e
* https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

### Sorting & Search
* ソートアルゴリズムは O(n log n)
* 二分探索
* 同点だった時に次は何の要素で並べるか、sort(key=lambda x: (x[0], x[1])) のようにタプルで指定できる
  * https://leetcode.com/problems/reorder-log-files/

### Binary search

* ある特定の値を答える場合に答えになる可能性のある下限と上限が分かるなら2分探索で減らしていく
  * https://atcoder.jp/contests/abc063/tasks/arc075_b
  * https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
  * https://leetcode.com/problems/koko-eating-bananas/
  * https://leetcode.com/problems/minimize-max-distance-to-gas-station/

### Others

#### Hash(dictionary, set)

* 重複を取り除くのに使う
  * https://leetcode.com/problems/letter-tile-possibilities/

* 順序を保持する dictionary もある、OrderedDict
  * https://leetcode.com/problems/lru-cache/


#### 貪欲法
* 何か優先順位をつけて、その順番で処理していく
  * 大きい方(小さい方)から入る分だけ詰めてみる
  * 桁の大きい数字の中で取り除いて一番効果のある数字を取っていく
    * https://leetcode.com/problems/remove-k-digits/

* 優先度順で操作したい＆要素を追加したりする場合は heapq(優先度付きキュー)を使う
  * https://leetcode.com/problems/cut-off-trees-for-golf-event/

#### 全探索
* 全組み合わせを for 文で回す
  * Grid とか 配列とか
  * 多重ループになると厳しいことがある
    * 多重ループになった場合にループを減らせないか
    * 判定式を書き換えてループが減らせないか考える
  * 数が多くなさそうであれば全ループで試す
    * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
* 組み合わせ全探索は Bit 全探索で解けるか考える
  * O(2**n) なのでできれば避けたい

#### 区間スケジューリング問題
* 終端(最後の位置)でソートしてそれを基準に選ぶ
  * 選んだ終端が別の始端になったら次を選ぶ

#### 積、素数
* 素因数分解して考える
* エラトステネスの篩  

#### 置き換え
* 一度の処理で個数がどう変化するかをみてみる

#### XOR
* 扱う数字が大きい場合は2進数にして考える
* n が偶数との時、n XOR (n+1) は常に１になる

#### mod
* 約数列挙することで対象を削れないか考える
* 各桁で分解して余りを加算しても値全体の余りは計算できる

#### Finding majority

* 配列の中の大部分を占める要素を見つける問題
  * 各要素の数を数えていくパターン
    * https://leetcode.com/problems/majority-element/
  * さらに計算量を落とせるアルゴリズムがある
    * Boyer-Moore Majority Vote Algorithm.
      * https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
    * https://leetcode.com/problems/majority-element-ii/

## Tips

1. Clarify input
  * How large
  * Possible input, e.g. only positive integers, floats, zero, negative, None, empty
2. Clarify output
3. Speak ieda
  * How to solve simple problem
  * Entire approach
4. Write code, 'Should I start coding with this idea?'
  * code clean
  * corner case
5. Optimize
  * Time complexity
  * Space complexity

    
## Others

* https://yangshun.github.io/tech-interview-handbook/
* https://www.hiredintech.com/classrooms/interview-strategies/lesson/88https://www.hiredintech.com/classrooms/interview-strategies/lesson/88
