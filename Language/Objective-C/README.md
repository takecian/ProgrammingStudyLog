<<<<<<< HEAD
# Objective-C

## Overview
* C 言語の Super set
  * C言語はそのまま動く
* Smalltalk の発展した言語

## import はできるだけ実装側で行う

ヘッダファイル側ではクラスの先行宣言を行うと良い
```objc
@class OtherClass

@interface SomeClass : NSObject

@property (nonatomic, strong) OtherClass* *otherClass;
 
@end 
```

実装ファイル側で import する。ビルド時に不要なファイル参照がなくなる。

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

### category

* Category can add new functionality to any class even if its class is built in.

```
@implementation SomeClass (Append)

-(void)tf_doSomethingEx {
    NSLog(@"doSomethingEx is called.");
}

@end
```

#### Class extension
クラスの実装ファイルに追加できる無名カテゴリのこと。隠蔽しておきたい変数の宣言とかに使える。

```
@interface SomeClass ()

@property NSString* firstName;

@end

```
### Protocols
Swift の protocol とほとんど同じ。けど protocol conformance が必須じゃない。

### Nullability

nullability annotation で明示する。明示するだけなので実際にそう動くかは自分でチェックしとかないといけない。
```
-(NSString*)loadStr;
```

* nullable → `?` になる
```
-(nullable NSString*)loadStr;
loadStr() -> String?
```
* nonnull → 無印
```
-(nullable NSString*)loadStr;
loadStr() -> String
```
* 未指定 -> IOU になる
```
-(nullable NSString*)loadStr;
loadStr() -> String!
```
マクロでも指定できる。
NS_ASSUME_NONNULL_BEGIN と NS_ASSUME_NONNULL_END

## Preprocessor
Objective-C のビルドは複数のプロセスからなる。
最初に処理されるのが Preprocessor

マクロは preprocessor で処理される code fragment replacement.
```
#define M_PI 3.1415926535897932384626
```
`#undef M_PI` でマクロを消せる。

### Conditional compilation

`#ifdef`, `#if` `#else`, `#endif`とかでコードをコンパイルするかどうか切り替えられる。

シミュレータでだけ有効なコードとか書ける。

プラットフォームが提供するマクロもある。
* TARGET_OS_IPHONE
* TARGET_OS_IOS
* TARGET_OS_MAC
* TARGET_OS_SIMULATOR

predefined なマクロもある
* DEBUG
* __DATE__
* __TIME__
* __FILE__
* __LINE__

```
#define let __auto_type const
#define var __auto_type
```
このマクロを使うと Objc の変数宣言を Swift っぽくかけたりする。

### Metadata macros
* #warning
* #error
* #paragma


## Naming conventions
命名規則があるのでそれに合わないものはエラーになる。

* `alloc` methods must return a retainable object pointer type.
* `copy` methods must return a retainable object pointer type.
* `mutableCopy` methods must return a retainable object pointer type.
* `new` methods must return a retainable object pointer type. 
* `init` methods must be instance methods and must return an Objective-C pointer type. Additionally, a program is ill-formed if it declares or contains a call to an init method whose return type is neither id nor a pointer to a super-class or sub-class of the declaring class (if the method was declared on a class) or the static receiver type of the call (if it was declared on a protocol).

## autorelesepool

通常は run loop が一回処理が終わったタイミングで autorelease されているオブジェクトを解放する。
けどそれよりもっと早い段階で解放したいケースがある。そんな時に `@autoreleasepool` で囲って、
そのスコープから出たらそのスコープ内で生成した autorelease オブジェクトを解放する。

## Objective-C++

