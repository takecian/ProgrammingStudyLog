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

### Loop(find value)

* 多重ループになった場合にループを減らせないか
  * 判定式を書き換えてループが減らせないか考える

### DP(動的計画法)

  
### 全組み合わせチェック
* Bit 全探索で解けるか考える
  * O(2**n) なのでできれば避けたい
  