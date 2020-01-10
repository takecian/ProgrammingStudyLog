<<<<<<< HEAD
# Objective-C

## Overview
* C 言語の Super set
* Smalltalk の発展した言語

## import はできるだけ実装側で行う

ヘッダファイル側ではクラスの先行宣言を行うと良い
```objc
@class OtherClass

@interface SomeClass : NSObject

@property (nonatomic, strong) OtherClass* *otherClass;
 
@end 
```

実装ファイル側で import する

```objc
#import "OtherClass.h"

@implementation

-(void)someFunc() {
  [self.otherClass doSomething];
}

@end
```

しかし継承するクラスやプロトコルはヘッダファイル側で import するしかない。

## リテラル構文を出来るだけ使う

```
NSString* someString = @"some text";
NSNumber* someNumber = @1;

NSString* dog = animals[1];

NSDictionary* dic = @{ @"age" : @28, @"firstName": @"Chie"}

```

## プリプロセッサマクロではなく型付定数を使おう

`#define DURATION 0.3` みたいなやつのこと。型情報がないのでつらい。

`static const NSTimeInterval kAnimeDuration = 0.3` とすると型の情報が含まれる。グローバルに定義すべきものではない場合は実装ファイル側に書こう。　

共通で利用したい定数の場合は
* ヘッダファイルに `extern` をつけて宣言
* 実装ファイルに定義をする
```objc
extern NSString* const someString;

NSString* const someString = @"text text";
```

## enum

switch 文で使う時は `default` の使用は避ける。後から追加した時に処理が漏れるかもしれない。


# gRPC

https://grpc.io/

protocol buffer でシリアライズ/でシリアライズしたデータをやり取りする仕組みのこと。HTTP2 ベース(heroku だと使えない)

## Objc
Objc で使用する場合は自分で podspec を作ってそこで指定するフォルダに .proto ファイルをおく。
 

=======
# Objective-C Note

* http://google.github.io/styleguide/objcguide.html
* https://raimon49.github.io/2015/03/21/review-nytimes-objective-c-style-guide.html

## クラス定義

* `@interface` を自身のヘッダファイル以外で書くこともできる（カテゴリのこと）

### インスタンス変数

* `@property` をつけるとプロパティの getter/setter を作ってくれる
    * `@systhesis`をつけなければプロパティの実体（インスタンス変数）を `_` 付きの名前で作ってくれる
    * `@systhesis`をつけるとプロパティの実体を紐づけることができる → あまり使わない
>>>>>>> Update objc note

