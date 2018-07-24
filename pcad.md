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

## [PCAD] ALDS1_1_D、ALDS1_1_A

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

## [PCAD] ALDS1_2_C

### ALDS1_2_C: Stable Sort

問題だけ読んで、正解にしてから解説を読む、ってやったんですが
安定性の判断ってとこでけっこう悩みました
まず全部、値でグループを作ってから判定することにしました
C++だとどんなライブラリになるんだろうか、
今どきライブラリにもないってことはないだろう、などと思いつつ

```python3
#! /usr/local/bin/python3
# coding: utf-8

def swap(c, i, j):
    t = c[i]
    c[i] = c[j]
    c[j] = t

def bubble_sort(cs, f):
    c = cs[:]
    for i in range(len(c) - 1):
        for j in range(len(c) - 1, i, -1):
            if f(c[j - 1]) > f(c[j]):
                swap(c, j - 1, j)
            # print(i, j, c)
    return c

def selection_sort(cs, f):
    c = cs[:]
    for i in range(len(c)):
        minj = i
        for j in range(i, len(c)):
            if f(c[j]) < f(c[minj]):
                minj = j
        swap(c, i, minj)
        # print(c)
    return c

def to_group(c):
    b = {}
    for i in c:
        if not(i[1] in b):
            b[i[1]] = [i]
        else:
            b[i[1]] = b[i[1]] + [i]
    return b

def is_stable(c, s):
    bc = to_group(c)
    bs = to_group(s(c, lambda x: x[1]))
    # print(bc)
    # print(bs)
    for k in bc:
        if bc[k] != bs[k]:
            return "Not stable"
    return "Stable"

n = int(input())
c = input().split()

print(" ".join(bubble_sort(c, lambda x: x[1])))
print(is_stable(c, bubble_sort))

print(" ".join(selection_sort(c, lambda x: x[1])))
print(is_stable(c, selection_sort))
```

Stableかどうかの判定はどうやら動いてます

`range`が半開区間なのは理にかなってると思うんですが、減らしていきたいときは
あんまり直感的じゃないっていうか何度も間違えました

ひとつずつソートを実装して動かしてみてよしOK、と思って提出したらWAで
どうなってるのかと思って調べてたんですけど
本に載ってる擬似コードと微妙にループ回数が違う！とかいろいろやったあげく
`c`を使いまわしてたので最初のバブルソートでcがソートされて
その後は全部ソート済みの`c`をソートしてるということが発覚しました
まず複製作ってからからソートして返すってして通したんですけど
普通はどう書くものですかね

ていうかループ回数、おかしくない？と思ったら正誤表出てました
擬似コードはともかく、本物のコードの方も間違ってるのはマズくないですか
たまたまSegmentation Faultとか出なかった？

さて解説を見てみます
is_stableの部分

> ソートの結果が安定かどうかを調べるには、Nの値が小さいので、次のようなカードの組に対する順番を愚直に調べるO(N^4)のアルゴリズムを適用することができます。

それは考えもしなかったなあ
まずは愚直に、って考えるようにしてるつもりでしたが
N^4となると愚直すぎたか
ディクショナリの中でN^2分くらいがんばってくれてるかもしれないけど

しかし今日の衝撃はそこではなかった
バブルソートのStable判定のコード

```c++
cout << "Stable" << endl;
```

O(1)だった
まじすか
そして選択ソートのStable判定はバブルソートの結果との比較で出すという

そういうのもありなのね

## [PCAD] ALDS1_2_D: Shell Sort

ソート自体は擬似コードが書いてあるので移すだけ
挿入ソートだと遠く離れた要素を入れ替えたくてもひとつずつずらしていくので
入れ替えの数が増えてしまいますがシェルソートでは間隔を空けて入れ替えるので
入れ替えが少なくて住むという寸法
自分で考えるのは入れ替える間隔の配列

```python3
#! /usr/local/bin/python3
# coding: utf-8

def insertion_sort(A, g):
    global cnt
    for i in range(g, len(A)):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v

def shell_sort(A):
    global cnt, G
    for g in G:
        insertion_sort(A, g)

n = int(input())

G = [1, 2]
for i in range(2, 100):
    g = G[i - 1] + G[i - 2]
    G.append(g)
G = list(filter(lambda x: x<=n, G))
G.reverse()

cnt = 0
A = []
for i in range(n):
    A = A + [int(input())]

shell_sort(A)

print(len(G))
print(" ".join([str(i) for i in G]))
print(cnt)
[print(i) for i in A]
```

データ数100万でTLE
ていうか長すぎて通信切れたかサーバ応答なくなったかと思ったよ
42.00sかかったって
ていうか

> Time Limit : 6 sec

って出てるからこの基準だとデータ数10万でもうだめなはずなんだけど
22.33sかかってるのにAC
どういうこと
まあいいけど

数列Gがよくないのかな
なんとなくフィボナッチ数列かなーと思って使ったけど
g_n+1 = 3g_n + 1 がいいらしい
もっと離れてていいんだな

```python3
G = [1]
for i in range(1, 100):
    g = 3 * G[i - 1] + 1
    if g > n:
        break
    G.append(g)
G.reverse()
```

でもやっぱりデータ数100万だと42.00sでTLE
42秒がリミットで切られてるのかな
データ量10倍で時間2倍ってことはないだろうし
でも10万でも21.93sかかっててほとんど違いがない
あんまり影響ないのか？

データ数10万で比べてみる

フィボナッチ版実行結果

```python3
$ time (ALDS1_2_D.py < in.txt > out.txt)
real    0m36.617s
user    0m34.522s
sys     0m1.926s
$ head out.txt
24
75025 46368 28657 17711 10946 6765 4181 2584 1597 987 610 377 233 144 89 55 34 21 13 8 5 3 2 1
2746144
0
1
```

3g_n + 1版

```python3
$ time (ALDS1_2_D.py < in.txt > out.txt)
real    0m36.650s
user    0m34.620s
sys     0m1.863s
[PCAD][master *%]$ head out.txt
11
88573 29524 9841 3280 1093 364 121 40 13 4 1
2951754
0
1
```

思った以上に差がなかった
いや、よくみたらフィボナッチ版の方が入れ替え回数すくないやん
どういうこと

まあ10万まで合ってるんだしいいか・・・
Web Board見てみたらRubyやPythonだとTLEになるって言ってる人がいる
自分だけじゃないのか

## [PCAD] イディオムさんたち

昨日ほかの人の回答を見たりしてよく使うパターンをいくつも発見したので
軽くここでまとめ

### 入力

1行をひとつの文字列として読み取る

```python3
>>> input()
aaa bbb ccc
'aaa bbb ccc'
```

1行でひとつの数字を読み取る
ふたつ数字があるとエラー

```python3
>>> int(input())
123
123
>>> int(input())
123 456
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '123 456'
```

1行にいくつかの文字列があるとき
split()で分割

```python3
>>> input().split()
aaa bbb ccc
['aaa', 'bbb', 'ccc']
```

1行にいくつかの数字があるとき
`map`かリスト閉包を使う

```python3
>>> list(map(int, input().split()))
123 456 789
[123, 456, 789]
>>> [int(x) for x in input().split()]
123 456 789
[123, 456, 789]
```

1行に複数のパラメータが指定されているとき

```python3
>>> s1, s2, s3 = input().split()
aaa bbb ccc
>>> s1
'aaa'
>>> s2
'bbb'
>>> s3
'ccc'
```

要素の個数＋指定した数だけの数、という行

```python3
>>> cnt, *nums = [int(x) for x in input().split()]
5 1 2 3 4 5
>>> cnt
5
>>> nums
[1, 2, 3, 4, 5]
```

複数行

```python3
>>> arr = [int(x) for x in sys.stdin]
1
2
3
4 #ここでCtrl+Dを押している
>>> arr
[1, 2, 3, 4]
```

### 出力

文字列の配列をスペース区切りで出力する
`join`でもいいですがアンパック `*arr`を使ったほうが楽
配列の要素をひとつずつカンマで区切った形となって処理されます

```python3
>>> arr = ["aaa", "bbb", "ccc"]
>>> print(" ".join(arr))
aaa bbb ccc
>>> print(*arr)
aaa bbb ccc
```

数値の配列でも同様
ただし`join`は文字列型しか受け取らないのでリスト閉包なり`map`なりで
文字列にしてやる必要があります
アンパック使うほうが楽ですね

```python3
>>> arr = [1, 2, 3, 4, 5]
>>> print(" ".join([str(x) for x in arr]))
1 2 3 4 5
>>> print(" ".join(map(str, arr)))
1 2 3 4 5
>>> print(*arr)
1 2 3 4 5
```

配列を複数行に出力
アンパック＋セパレータ指定でいけます

```python3
>>> [print(x) for x in arr]
1
2
3
4
5
>>> print(*arr, sep="\n")
1
2
3
4
5
```

### フィルタ

フィルタと組み合わせると1行でかなり書けますね

```python3
>>> list(filter(lambda x: x > 3, [2, 4, 6]))
[4, 6]
>>> [x for x in [2, 4, 6] if x > 3]
[4, 6]
```

### 配列の要素

配列の第3要素から第4要素 `arr[2:4]`
配列の先頭の2要素 `arr[:2]`
配列の最後の要素 `arr[-1]`
配列の最後の2要素 `arr[-2:]`
配列の複製 `arr[:]`

### グローバル変数

グローバル変数を関数の中で使う
プログラミングコンテストの題材ぐらいだとついついグローバルにしてしまいます

```python3
v = 0

def some_func():
    global v
    print(v)
```
