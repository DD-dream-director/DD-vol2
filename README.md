# DD-vol2
ハッカソン事後開発

# Project Name

Dream Director

## Introduction

このプロジェクトではDjangoを使ったウェブアプリケーションを開発します。このアプリケーションではユーザーが...（ここにプロジェクトの詳細を記入してください）

## Installation & Setup

以下の手順で、ローカル環境にプロジェクトをセットアップしてください。

### Virtual Environment作成

Pythonの仮想環境を作成し、アクティブにする。

```
$ python3 -m venv venv
$ source venv/bin/activate
```

### Dependenciesのインストール

プロジェクトの依存関係をインストールします。このソフトウェアは `pip` を使って `requirements.txt` ファイルからインストールします。

```
$ pip install -r requirements.txt
```

### Djangoの設定

Djangoの設定を行います。まず、マイグレーションします。

```
$ python manage.py makemigrations
$ python manage.py migrate
```

次に、Super Userを作成します。

```
$ python manage.py createsuperuser
```

必要な情報（ユーザー名、メールアドレス、パスワード）を入力してください。

### アプリケーションの実行

開発サーバーを起動します。

```
$ python manage.py runserver
```

開発サーバーが起動したら、ブラウザで http://127.0.0.1:8000/ にアクセスしてください。プロジェクトのホームページが表示されます。

## Usage

アプリケーションの使い方や機能についての説明をここに記入してください。
(後でユーザーズガイド作らないとだね)

## Motivation

モチベーションをあげる動画を共有するWebサービスの提供

## Contributing

- pullしてからpushしてください
- コミットは[これ](https://suwaru.tokyo/%E3%80%90%E5%BF%85%E9%A0%88%E3%80%91git%E3%82%B3%E3%83%9F%E3%83%83%E3%83%88%E3%81%AE%E6%9B%B8%E3%81%8D%E6%96%B9%E3%83%BB%E4%BD%9C%E6%B3%95%E3%80%90prefix-emoji%E3%80%91/)を参考にするといい感じになると思います。.commit_templateもこの際作ってみましょう！

## Acknowledgments

DMM.comのメンター様とスマプロハッカソン2023運営の方々、事後開発ですが、必ず作り上げるのでお楽しみに！
  