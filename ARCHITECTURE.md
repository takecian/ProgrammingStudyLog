# iOS App architecture

https://medium.com/ios-os-x-development/ios-architecture-patterns-ecba4c38de52

* Common strategy is to divide concerns such as UI, business logic, model(Persistence)

## MVC
Model-View-Controller
* Traditional
* In iOS, View and Controller is the same, ViewController
  * Difficult to separete view code and controller code.

### responsibilities
|Component|Role|
|:--|:--|
|View|画面を描画する|
|Controller|入力を受け付ける、Modelを操作する|
|Model|ドメインロジック、表示ロジックを持つ|

## MVP
Model-View-Presenter
* Completedly separated compared to to MVC
  * treats the view controller as the View

### responsibilities
|Component|Role|
|:--|:--|
|View|Presenterからの指示によって描画する。入力をPresenterに伝える|
|Presenter|表示ロジックを受け持つ、Modelを操作して状態を変更する|
|Model|Presenterからのみアクセスされる、ドメインロジックのみ持つ|

## MVVM
Model-View-ViewModel
* Completedly separated compared to to MVC
  * treats the view controller as the View
* ViewModel is basically UIKit independent View representation
* Bindings between View and ViewModel
  * binding が MVVM と MVP の違い

画面遷移のために Coordinator が追加され、MVVM-C で実装するケースも。
https://hackernoon.com/how-to-use-mvvm-coordinators-and-rxswift-7364370b7b95

### responsibilities
|Component|Role|
|:--|:--|
|View|画面を描画する|
|ViewModel|入力を受け付ける、Modelを操作して状態を変更する|
|Model|ViewModelから受ける。ドメインロジックのみ|

## Flux/Redux

処理の流れが１方向になっているアーキテクチャ。

### Redux - responsibilities
Action が disptach されて、Reducer のなかで state が更新されて、Viewに通知される。View は State に従って画面表を行う。

Reducer は input だけで output が決まる純粋関数なのでテストがしやすい。
Store が reducer と state を保持して、Actionが発行されると reducer で処理を行って state を更新する。

|Component|Role|
|:--|:--|
|Action|ビジネスロジックの変更や状態変化を伝える|
|State|アプリの状態|
|Reducer| Action と State を受け取って新しい State を生成する|
|View| State に従って画面を描画する|

## Clean architecture

https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html

GUI以外の部分も役割に合わせて分割したシステムアーキテクチャ。MV-X のGUIアーキテクチャと組み合わせて使うことができる。 

例：MVVM + Clean architecture, UI 部分を MVVM で構築して、Model 部分を UsecaseやEntityに分割して実装する。

### responsibilities
|Component|Role|
|:--|:--|
|UI、DataStore|フレームワークと言われる部分、プラットフォーム依存|
|Interface adapter|UseCaseとフレームワークの部分を仲介する、Presenter(UI)やGateway(DataStore)がある|
|UseCase|ビジネスロジックを表現する|
|Entity|単純な構造のモデル|

## VIPER

Clean architecture の派生。画面遷移が考慮され Router が追加されているイメージ。

### responsibilities
|Component|Role|
|:--|:--|
|View|画面表示と入力受付|
|Interactor|データ操作、Entityを使ってビジネスロジックを表現する|
|Presenter|どんな要素を表示するかのプレゼンテーションロジックを表現する、UIKitなどプラットフォームに依存しない|
|Entity|単純な構造のモデル|
|Router|画面遷移|



