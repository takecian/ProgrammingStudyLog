# Programming Study Log

## Contest

* https://projecteuler.net/
* http://atcoder.jp/
* https://paiza.jp/challenges
* https://leetcode.com

### Snippet

[A collection of useful methods](snippet_for_leetcode.py) for competitive programming.

## Knowledge

|テストケース|Order|メモ|
|:--|:--|:--|
|10^8以上|O(N)でいけるか微妙、O(logN)かO(1)||
|10^6以上|O(N)かO(N log N)|二部探索とか考える|
|3000|O(N^2)||
|500|N^3||
|100|N^3||
|50|N^5||
|20|2^N||

1 秒間で処理できる for 文ループの回数は、10^8=100,000,000 回程度

## Language

* Haskell

## Pattern

問題を解くときの着目点

### グラフ

* 順列(itertools.permutations)でルートの選択肢を全列挙
* ダイクストラ
* UnionFind で連結判定できないか

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

### 最大値、最小値

#### DP(動的計画法)
直接計算すると大きな時間がかかってしまう問題に対し、途中の計算結果をうまく再利用することで計算効率を上げる手法のこと。
最大値(最大和)とか、最小値を計算する時に使うケースが多い。
* ナップサック問題
* 最長共通部分列問題
  * Longest Common Subsequense
* 最長増加部分列
  * LIS : Longest Increasing Subsequense
  * 挿入ソートする時の操作の回数とかもこれ

### 回文・辞書式順序
* 文字列を reverse して比較してみる
* 前方から比較してみる
* 後ろから for 文を回してみる
  * 辞書式順序で最小の文字を作る時は後ろからも見てみる

### 配列

* Sort したら簡単に解けないか
* Reverse したら簡単に解けないか
* 2つポインタ持たせて不要なループを減らせないか
  * 先頭に２つポインタを持たせてずらしていく
  * 先頭と最後尾からポインタをずらしていく
* 二分探索すると早くできないか
  * 端っこの処理が難しくなりそうなら番兵的なものを置くと簡潔にできないか

### 貪欲法
何か優先順位をつけて、その順番で処理していく
* 大きい方(小さい方)から入る分だけ詰めてみる

### 全探索
* for 文で回す
  * 多重ループになると厳しいことがある
    * 多重ループになった場合にループを減らせないか
    * 判定式を書き換えてループが減らせないか考える
* Bit 全探索で解けるか考える
  * O(2**n) なのでできれば避けたい
* DFS
* BFS

### 区間スケジューリング問題
* 終端(最後の位置)でソートしてそれを基準に選ぶ
  * 選んだ終端が別の始端になったら次を選ぶ

### Linkedlist
* head の前に Dummy node を作って `dummy.next = head` を使うと便利
  * `while cursor` みたいな感じで走査していく
  
### 積、素数
* 素因数分解して考える
* エラトステネスの篩  

### 置き換え
* 一度の処理で個数がどう変化するかをみてみる
