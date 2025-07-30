# 基本イメージとしてgolangを使用
FROM golang:alpine as builder

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係のコピーとダウンロード
COPY go.mod ./
RUN go mod download

# ソースコードをコピー
COPY . .

# 実行可能ファイルをビルド
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

# 実行ステージ
FROM alpine:latest  
WORKDIR /root/
COPY --from=builder /app/main .
CMD ["./main"]
