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

## Reviewing