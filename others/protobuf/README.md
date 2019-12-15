# protocol buffer study

## Setup

```
brew install protobuf
brew install swift-protobuf
```

## Compile

```
protoc --swift_out=./ addressbook.proto
protoc --objc_out=./ addressbook.proto
protoc --python_out=./ addressbook.proto
```
