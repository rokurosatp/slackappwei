# 開発のガイドライン

というか情報の寄せ集めです（Wikiにそのうち移行？）

## 参照用リンク

この辺りを参考にしました

* [django Document](https://docs.djangoproject.com/en/1.11/intro/)
* [Message Buttons With NodeJs](https://api.slack.com/tutorials/intro-to-message-buttons)

## Djangoプロジェクトの作り方
---

細かいことは[ここ](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)を参照

### プロジェクトの作成

プロジェクトのディレクトリ作成がツールで自動的に行われるのでプロジェクトのフォルダを作らずそのホルダーに移動

以下のコマンドを実行

    django-admin startproject <プロジェクト名>

フォルダがいろいろと作成されるので取りあえずプロジェクトフォルダに移動

    cd <プロジェクト名>

まず、開発サーバーの動作確認

    python3 manage.py runserver

URLが出るのでそれをクリックするとページが表示される。

### appの作成

動作確認が終わったらプロジェクトにappsを追加する。(プロジェクトがシステム全体でappは一機能に該当するらしい)

    python3 manage.py startapps <app名>

プロジェクトのフォルダに加えてapp名のフォルダができる

### appを編集して単一ページを追加する

作成するには以下の作業が必要になる(プロジェクト名は`project`, app名は`app`とする)

* viewの作成 - 表示するページの設計
* `project.app.urls`の編集 - URLと作成したビューの結び付け
* `project.urls`の編集 - URLとappsの結び付け

### Viewの作成

`project/app/views.py`

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world. You're at the app's index.")

### アプリケーションのUrl設定

`project/app/urls.py`

    from django.conf.urls import url

    from . import views

    urlpatterns = [
        url(r'^$', views.index, name='index'),
    ]

### プロジェクトのUrl設定

`project/urls.py`

    from django.conf.urls import include, url
    from django.contrib import admin

    urlpatterns = [
        url(r'^app/', include('app.urls')),
        url(r'^admin/', admin.site.urls),
    ]

`python3 manage.py runserver`を実行したUrlがhttp://127.0.0.1:8000の場合.

http://127.0.0.1:8000/appをブラウザで開くと以下の表示が出る

    Hello World, You're at the app's index


## Slackの設定

### アプリケーション管理画面への移動方法

1. [APIのページに移動](https://api.slack.com/) (チーム上のアプリ管理画面から飛ぶ場合は`build`を選択)
2. `Your Apps`をクリック