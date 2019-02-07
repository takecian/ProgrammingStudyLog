# Programming Study Log

## Contest

* https://projecteuler.net/
* http://atcoder.jp/
* https://paiza.jp/challenges
* https://leetcode.com

### Snippet

[A collection of useful methods](./snippet.py) for competitive programming.

### Knowledge

1 秒間で処理できる for 文ループの回数は、10^8=100,000,000 回程度

## Language

* Haskell

## Pattern

問題を解くときの着目点

### List

* Sort したら簡単に解けないか
* Reverse したら簡単に解けないか
* 2つポインタ持たせて不要なループを減らせないか
  * 先頭に２つポインタを持たせてずらしていく
  * 先頭と最後尾からポインタをずらしていく

### Grid

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

### DP(動的計画法)
直接計算すると大きな時間がかかってしまう問題に対し、途中の計算結果をうまく再利用することで計算効率を上げる手法のこと。
* ナップサック問題

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

### 回文・辞書式順序
* 文字列を reverse してみる  

### グラフ
* 順列でルートの選択肢を全列挙
