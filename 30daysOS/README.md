# 30日OS自作入門

## Setup

Mac Catalina

アセンブラ(nasm)も64bit 対応じゃないと動作しないので注意。

```
brew install qemu
brew install nasm
```

## Run OS

```
cd day1/helloos0
make run
```

## CPU

### 16bit レジスタ
|レジスタ名|意味|
|:--|:--|
|AX|accumulator|
|CX|counter|
|DX|data|
|BX|base|
|SP|stack pointer|
|BP|base pointer|
|SI|source index|
|DI|destination index|

32bit レジスタはこれらの名前の prefix に `E` をつけたものがある。
例：`EAX`, `ECX`

## 参考

https://github.com/tatsumack/30nichideosjisaku