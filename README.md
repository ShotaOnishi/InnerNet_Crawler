# InnerNet_Crawler
This is a repository for InnerNetCrawler


Pythonのバージョン確認と, ライブラリのインストール.
Pythonは3系を使ってください.
入っていなけれればbrewして下さいな〜〜
```
pyenv version

=> 3.5.1

pip3 install selenium

pip3 install bottle

pip3 install uuid

pip3 install tldextract  
```

ヘッドレス化するためにPhantomJSを使う.
```
brew install phantomjs
```

prologの利用
```
brew install swi-prolog

swipl
```

起動
```
python3 crawler_server.py

curl -X GET "http://127.0.0.1:8080/get_pages?query=ReactJS+Redux"
```

これでRails側に画像が送られる.(is_favoriteはfalseに設定されています. )
