# 『プログラミングコンテスト攻略のためのアルゴリズムとデータ構造』

## [PCAD]『プログラミングコンテスト攻略のためのアルゴリズムとデータ構造』

PaizaでS取れなかったのがちょっと尾を引いており、突然ですが
そっちの勉強をすることにしました

このままたくさん問題を解いていくだけでも少しずつ力はついていくだろうし
運が良ければS取れるかもしれないんですが
それだと運がよかっただけかどうかわからないのでちゃんと勉強してみようと
それにアルゴリズムやデータ構造は本で読んだだけの知識が多くて
実際に書いてみるのもいいかなと思いまして

ただ、Paizaのスキルチェックは解説とか模範解答とかないようなので勉強するには
若干効率がよろしくない感じ
ちょうどAmazonで安くなっていたのでこれを買いました

プログラミングコンテスト系の本はあと2冊くらいよさげなのがありましたが
この本が一番簡単そう
オンラインで判定してくれるというのがいいかなと
ちょっと書いて動かして判定してもらえるっていうシステムはなかなか楽しい

この本のコードはC++で書いてあるのでC++でやろうと思います
たいていの問題はPython3でも書けると思うんですがポインタが出てきたりすると
読み替えが多くなりそうなので

[AIZU ONLINE JUDGE](http://judge.u-aizu.ac.jp)

ここ、ユーザ登録画面がhttpなんだけどいいのか・・・？というのは置いといて
とりあえず"Getting Started - X Cubic"をやってみる

Paizaと違ってブラウザ上で書いて動かせるわけではないので
ローカルで書いてコンパイルして実行する
少々面倒だ
忘れてるし

C++だから、えーと拡張子は.cppにして
コンパイルはg++か
おっとa.outができてしまった

などなどしつつ初提出

ついでにPythonもやってみる

```python
#! /usr/local/bin/python3
# coding: utf-8

print(int(input()) ** 3)
```

## [PCAD] 環境

[Git入門（VSCode Git の使い方）](https://celtislab.net/archives/20180418/git-vscode/)

## [PCAD]

### ALDS1_1_D: Maximum Profit

相場を見ていつ買っていつ売ると最大の利益が得られるかって問題
こういうのはちゃんと問題を読み取れるかがキモかもしれない

C++で書こうと思ってたけどpythonで書けるところはpythonにしようかな
楽だし

```python3
#! /usr/local/bin/python3
# coding: utf-8

n = int(input())

min_r = int(input())
max_margin = -1000000001

for i in range(n - 1):
    r = int(input())
    max_margin = max(r - min_r, max_margin)
    min_r = min(r, min_r)

print(max_margin)
```

ところでこの手の問題、データの前にたいていデータの個数が書いてあるのがどうも
気になります
冗長なので
データの個数が書いてあってデータが並んでると、つい整合性が取れてるかどうか
チェックしたくなったり
しないんだったらファイルの終わりまで読めばいいじゃない？

と思って最後まで読むように書いてみた
こうかな
`n`は読み捨て

```python3
#! /usr/local/bin/python3
# coding: utf-8

import sys

n = int(input())

min_r = int(input())
max_margin = -1000000001

for l in sys.stdin:
    r = int(l)
    max_margin = max(r - min_r, max_margin)
    min_r = min(r, min_r)

print(max_margin)
```

sys.stdinてのを使うんだな
`import sys`がいるとか、ターミナルから直接値を入れるとEOF入れなきゃとかでめんどい
あきらめて普通に書くことにする

### ALDS1_1_A: Insertion Sort

挿入ソート

Pythonで関数に配列を渡すと中身書き換えられるんだっけ？
（よくわからなくなっている）

```python3
#! /usr/local/bin/python3
# coding: utf-8

def insertion_sort(a):
    for i in range(1, len(a)):
        print(" ".join(map(str, a)))
        w = a[i]
        j = i - 1
        while j >= 0 and w < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = w

n = int(input())
a = [int(i) for i in input().split()]
insertion_sort(a)
print(" ".join(map(str, a)))
```

大丈夫だった

コード書いて保存して、ターミナルで実行権限つけて実行して、
Webサイトから入力データをコピペする、っていうのが地味に面倒
このへんはPaizaの方が楽だな

"Link to β version of AOJ 2.0"って書いてあるからもしかしたらそっちでは楽？
と思ったけど入力例で実行してくれるような機能はなさそう 残念
でも結果が見やすいからこっち使おうかな
