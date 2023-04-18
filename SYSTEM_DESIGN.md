# System design study

## Prepare for Your Google Interview: Systems Design

https://www.youtube.com/watch?v=Gg318hR5JY0

20分で最初のソリューションを出す
* Communication
  * understanding problem
  * designing
  * think it loud
  * ask clarify
* scaling data
  * must be scalable
  * how can we tell how the system is working?
  * is there a bottleneck in the design?
  * how do the component together
  * how to shared
* System properties
  * latency
  * throughput
  * storage
* concrete
  * cost of operation
    * read from disk 200MB/s
    * read from memory 2GB/s
    * local area network 1Gbps -> 100MB/s
    * continental network RTT 150ms
 * sharding data
 * replication
 * write ahead logging
 * load distribution 
 * separating data and meta data storage
* trade off and compromise
  * rotating disk?
  * flash drive?
* best practice
  * explain
  * clarify
  * improve
  * practice

### Note
* Requirement の整理
  * 単語で書くより文章で「〜できる」って書いた方が分かりやすい
  * 例：「他のユーザーと友達になれる」「他のユーザーと１対１でチャットができる」
* ロードバランサーの設置、TLS termination の実施
* アプリサーバの水平スケーリング
* DB の master-slave 化
* DB の sharding
* 画像を使うとしたらリサイズするサーバーが必要
  * アップロード時にリサイズするか
    * タスク管理するMessage Queue、リサイズする worker server が必要
  * 画像リクエストされた時にリサイズするか→この場合キャッシュ必須
* 画像な S3 のような Object storage に置いて CDN にアクセスさせる
  * Object storage を HDD にするか SSD にするか
* キャッシュした方がいい場所はないか

## Software Engineering Advice from Building Large-Scale Distributed Systems from Jeff Dean

https://static.googleusercontent.com/media/research.google.com/en//people/jeff/stanford-295-talk.pdf

## Numbers
|Latency Comparison Numbers (~2012)||||
|:--|:--|:--|:--|
|L1 cache reference |                          0.5 ns||||
|Branch mispredict  |                          5   ns||||
|L2 cache reference |                          7   ns   | |                  14x L1 cache|
|Mutex lock/unlock  |                         25   ns||||
|Main memory reference|                      100   ns|            |          20x L2 cache, 200x L1 cache|
|Compress 1K bytes with Zippy|             3,000   ns|        3 us||
|Send 1K bytes over 1 Gbps network|       10,000   ns|       10 us||
|Read 4K randomly from SSD*         |    150,000   ns|      150 us |         ~1GB/sec SSD|
|Read 1 MB sequentially from memory |    250,000   ns|      250 us||
|Round trip within same datacenter  |    500,000   ns|      500 us||
|Read 1 MB sequentially from SSD*   |  1,000,000   ns|    1,000 us|    1 ms,  ~1GB/sec SSD, 4X memory|
|Disk seek                          | 10,000,000   ns|   10,000 us|   10 ms,  20x datacenter roundtrip|
|Read 1 MB sequentially from disk   | 20,000,000   ns|   20,000 us|   20 ms,  80x memory, 20X SSD|
|Send packet CA->Netherlands->CA    |150,000,000   ns|  150,000 us|  150 ms| 

最近のSSD,HDDだと読み込み速度で
* メモリ：20GB/sec とかある
* SSD: 2GB/sec とかある
* HDD: 200MB/sec とかある

* データセンターのネットワークは 100Gbps とか？
  * https://businessnetwork.jp/Detail/tabid/65/artid/6473/Default.aspx
* 1Gbps でサーバー間通信をすると仮定すると 120MB/s

* 4G は 80Mbps -> 10MB/sec とか？
  * 場所とかキャリアで大きく変わりそうだけど計算上楽だから 10MB/sec で考える

## システム設計の進め方

## システムの概要、要件をまとめる
* 誰が使うのか
* どのように使うのか
  * 想定ユーザーは何人くらいか
    * ユーザー認証をするか
  * 保存したいデータは何があるか
    * 読み書きの比率はどのくらいか
    * 秒間何リクエストくらい想定されるか 
  
* 概要から必要なデータ量、パフォーマンスを推測する
  * 保存するデータの１レコードあたりのサイズ
  * どれくらいの容量を捌く必要があるか
    * １レコードあたりのサイズ x 1日あたりのデータ数
    
## ハイレベルでのシステムデザインを作る
* どんなコンポーネントが存在するか
  * クライアント
  * ロードバランサー
  * Web サーバー(API サーバー)
  * DB
  * CDN
  * バッチサーバー
  
## 詳細設計
* コアになるデータベースのスキーマを決める
* データの生成方法など決める（ハッシュ化させるとか）

## スケール検討
* ボトルネックになりそうなところを割り出す
  * ロードバランサーが必要ではないか
  * 水平スケーリングする部分はないか
    * 台数並列に増やす
  * キャッシングした方がいい部分はないか
  * データベースシャーディングは必要か
    * シャーディングするとしたら何で分割するか
      * ユーザー単位、データ（テーブル）単位
        * データ単位だと結合が手間になるのでよく考えること

* データ量が増えるとシステム上困る部分は出てこないか
  * ハッシュを使うとすると衝突はどのくらいで起きるか
    * 起きた時どうするか

## 覚えておきたい
* Base64
  * 64文字（英数と+/=) で表す
  * 64文字だから 64=2**6 から 6bit 分を表すことができる
  * 6bit は半端なので、４文字分(3byte)をまとめて変換していく
  * 3byte(24bit) が 4byte になるので 1.3倍長くはなる

* 秒数
  * 一日86400秒
  * 一ヶ月約250万秒

# 事例

[秒間120万つぶやきを処理、Twitterシステムの“今”](https://atmarkit.itmedia.co.jp/news/201004/19/twitter.html)

## Ref.
* https://www.hiredintech.com
* https://github.com/donnemartin/system-design-primer/blob/master/README-ja.md

