# System design study

## システム設計を進め方

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
  
* Various operations time

|Operations|Time|
|:--|:--|
| execute typical instruction |	1/1,000,000,000 sec = 1 nanosec| 
| execute typical instruction |	1 microsec = 1000 nanosec| 
| execute typical instruction |	1 millsec = 1000 microsec| 
| fetch from L1 cache memory | 0.5 nanosec| 
| branch misprediction | 5 nanosec| 
| fetch from L2 cache memory | 7 nanosec| 
| Mutex lock/unlock | 25 nanosec| 
| fetch from main memory | 100 nanosec| 
| send 2K bytes over 1Gbps network | 20,000 nanosec| 
| read 1MB sequentially from memory | 250,000 nanosec| 
| fetch from new disk location (seek) | 8,000,000 nanosec| 
| read 1MB sequentially from disk | 20,000,000 nanosec| 
| send packet US to Europe and back | 150 milliseconds = 150,000,000 nanosec| 



http://norvig.com/21-days.html#answers

## Ref.
* https://www.hiredintech.com
* https://github.com/donnemartin/system-design-primer/blob/master/README-ja.md

