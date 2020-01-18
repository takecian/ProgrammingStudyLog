# Readability

## Naming
* Put the most important word at last
* property is none
* function is verb

## Comments
* Add if property/function name is not enough
* comments for property starts with none
* comments for function starts with verb
* Comments must Includes
  * What it does/What it is
  * Limitations
* Work around

## State
* stateless の方が readability は高いのか
  * ものによる
  * 複雑な再帰処理などの場合は stateless でも分かりにくいことがある
* どうやって readability をあげるか
### Orthogonal(直交)
  * ２つのプロパティにがあった時に、一方に関係することなくもう一方を変更できること
  * Orthogonal: authorName and layoutVisibility
  * Non-orthogonal: authorId and authorName
* non orthoggonal は避けたい
  * 状態の不一致が起こり得る
* どうやってnon orthoggonalを取り除くか
  * 一方を getter と差し替える（もう一方から導出する
  * 構造体か何かにカプセル化する
### state desiggn strategies
* Use immutable object
* Use Idempotency
  * Idempotency is the result of multiple operations are the same as single operation. 
* Acyclic を作って状態遷移をわかりやすくする

## Procedure
### Readable procedure is
* Consistent with name
* Easy to write documentation
* few error cases or limitation

### Responsibility must be clear
* Split if it's hard to summarize
  * Try to summarize what the procedure does 
* Split if it has both return value and side-effect
### Make flow clear
* Do definition based programming
* Focus on normal cases

Hard to summarize = Typical bad signal

### Strategry
* Split procedure by command and query
  * Command: Procedure to modify receiver or parameters 
  * Query:  Procedure to return without any modification

* Don't modify the receiver/parameters with returning a "main" result
  * Acceptable to return a "sub" result with modification
  * Main result: conversion/calculation result, a new instance, ...
  * Sub result: error type, metadata of modification (stored size), ...
    * (Documentation is mandatory)

## Flow is good?
* Try to write short summary

### Definition based programming
* Extracting may make the code less readable
  * nnecessary state
  * Unnecessary strong coupling (will explain at the next session)

### Avoid early return

* Basically early returns leads unclear
  * Easy to find
    * The main flow and purpose of a procedure Relation of error condition and handling logic
  * Ok if condition not met

### Split
* Split by object, non condition
  * Easy to refactor

### Summary
* Check whether it's easy to write a short summary
* Procedure responsibility:
  * Split if required
  * Don't modify returning main result
* Procedure Flow:
  * Apply definition based programing, early return, split by object

## Depedency
* 依存性にも種類がある
  * XX Coupling という名前がついてるっぽい 
### 避けた方がいい 
* Content coupling
  * 呼び出し方に制限がある
    * prepare() -> execute() -> teardown() と呼ばないといけないとか
  * mutable なオブジェクトを共有するとか
* Common coupling
  * global 変数にアクセスする
* Control coupling
  * 処理途中のデータをメンバ変数に保持する
    * 返り値として受け渡しするようにする
  * Switches logic by passing flag "what to do"
    * summarize が難しい → つまり何やってるかわかりにくい

### まぁいい
* Stamp coupling
  * 処理をする時に構造体丸ごと渡す（一部のフィールドしか使わないのに）
* Data coupling
   *処理をする時に必要なフィールドだけ渡す 
* Message coupling
  * 引数なしでメソッド呼び出すこと

* なっぜ不要な依存がバグを生むのか
  * リークするかも
  * 状態の不一致を引きこおす  

### まとめ
* 依存の方向は１方向のみにする
* シンプルに
* 依存はクラス図に見えるようにする

## Reviewing

### Objective

Keep code clean, readable

* Most important
  * readability
* Nice to have
  * Logic correctness
  * Author's responsibility

### How to create PR
* Tell intention with commit structure
  * logical change, syntax change should be separated
  * option of axis
* Keep PR small
* Describe scope of PR
  * main purpose
  * Future plan
  * Out of scope

### How to address code review
* Think why reviewer asked/misunderstood
  * Typical signal that code is unclear 
* Understand reviewer's suggestion
  * Don't just paste attached code in a review comment
    * Think what is the key idea
    * Consider to rename
    * Confirm it's logically correct: exceptions, race conditions ...
* Consider to address a comment to other parts 
  * Find similar code and address it
* Don't make reviewers repeat
  * Coding style and conventions 
  * Authoring: word choice, grammar 
  * Language/platform idiom 
  * Conditional branch structure 
  * Testing
### How to review
#### Principles
Don't be too kind, but be kind a little

#### Reaction
* GOOD:
   - Review soon
   - Redirect to other reviewer
   - "I cannot review", "I'll be late"...
* NOT SO GOOD:
   - Simply ignore
* WORST:
   - Reply "I'll review" without review

#### problematic PR
* Too large or hard to read:
  * Ask to split

* Totally wrong on purpose, assumption, or structure:
  * Ask to make skeleton classes or have casual chat

#### Don't guess author's situation
* Reviewers should not care about deadline
  * Let them explain if they want to merge soon Need to file issue tickets, and add TODO at least
  * Exception: Major/critical issues on a release branch or hotfix

#### What should be commented
* Styles, conventions, idioms, ... (CI can review instead) 
* Tests
* All in this presentation series
* Principles, authoring, structure, dependency Any issues you found
  * Describe what it is rather than how it is used
  
  
  
  
  
  
  