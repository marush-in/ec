# ec

[![Build Status](https://travis-ci.org/marush-in/ec.svg?branch=master)](https://travis-ci.org/marush-in/ec)

# 開発環境

※ Dockerを立ち上げる

## コマンド一覧

・開発環境の構築
```
./operate init
```

・開発環境を起動する
```
./operate up
```

・開発環境を停止する
```
./operate down
```

・開発環境を再起動する
```
./operate restart
```

・DBを初期化する
```
./operate initdb
```

・アプリケーションのコンテナに入る
```
./operate login
```

・Postgresqlのシェルにログインする
```
./operate postgres
```

・管理ユーザーを作成する
```
./operate createsuperuser
```

・マイグレーションファイルを作成する
```
./operate makemigrations
```

・マイグレーションファイルをDBに適用する
```
./operate migrate
```

・文法を確認する
```
./operate flake8
```

・テストを実行する
```
./operate test
```
