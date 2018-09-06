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

## [PCAD] ALDS1_3_A: Stack

appendとpopでやるのは反則としておこう
どこまでならゆるされるだろうか、と考えて配列とスタックポインタで書いてみた

Pythonで「配列」って言うのは変かな
でも気持ちは配列

```python3
#! /usr/local/bin/python3
# coding: utf-8

sp = 0
stack = [0] * 100

def stack_push(v):
    global sp, stack
    stack[sp] = v
    sp += 1

def stack_pop():
    global sp, stack
    sp -= 1
    return stack[sp]

def stack_op2(op):
    v2 = stack_pop()
    v1 = stack_pop()
    stack_push(op(v1, v2))

def calc(terms):
    for t in terms:
        if t == "+":
            stack_op2(lambda v1, v2: v1 + v2)
        elif t == "-":
            stack_op2(lambda v1, v2: v1 - v2)
        elif t == "*":
            stack_op2(lambda v1, v2: v1 * v2)
        else:
            stack_push(int(t))
    return(stack_pop())

print(calc(input().split()))
```

動いたけど、解説と見比べてみたら`sp`が普通と1ずれてるな
普通は指してるところが最新の値か 言われてみるとそうだな
そのかわり0番目は空けておくのか

```python3
def stack_push(v):
    global sp, stack
    sp += 1
    # print("push: sp =", sp, ", v =", v)
    stack[sp] = v

def stack_pop():
    global sp, stack
    # print("pop: sp =", sp, ", v =", stack[sp])
    sp -= 1
    return stack[sp + 1]
```

お、しかもエラーチェックやってるな
と思ったら擬似コードのほうだけか

ところで`+`とか`-`を関数として使うにはどうしたらいいのかな
`lambda`で書いたけど

## [PCAD] ALDS1_3_B: Queue

キューはどんなふうに実装するのかな
配列をリングにするのか
線形リストを使うか

たぶん配列

そういえば、キューの出し入れって英語で何ていうんだろう
スタックならpushにpopだけど
まあpushとpopにしておくか

うひ100000行まであるのか
またTLEするかな
100000プロセス同時起動とはどんなDOS攻撃
時間差つけて起動したほうがそれっぽい気がするけど
キューの勉強だからってことかな

今回はカッコつけてクラスにしてみました
（クラスの書き方を調べながら）

```python3
class Queue:
    def __init__(self, n):
        self.n = n + 1
        self.q = [0] * self.n
        self.top = 0
        self.last = 0

    def is_empty(self):
        return self.top == self.last

    def push(self, v):
        self.q[self.top] = v
        self.top = (self.top + 1) % self.n

    def pop(self):
        v = self.q[self.last]
        self.last = (self.last + 1) % self.n
        return v

n, q = [int(x) for x in input().split()]

proc = Queue(n)
for i in range(n):
    name, ptime = input().split()
    proc.push((name, int(ptime)))

time = 0
while not proc.is_empty():
    name, ptime = proc.pop()
    time += min(q, ptime)
    ptime -= min(q, ptime)
    if ptime <= 0:
        print(name, time)
    else:
        proc.push((name, ptime))
```

TLEはせず無事ACでした

解説
なるほどhead、tail、enqueue、dequeueか
そしてheadのほうから取り出すのか

今回キューはクラスにしたけどプロセスの名前と時間はクラスにするのも大げさだなと
思ったので単にタプルにしました
Cのstructくらいなら気楽に書くんですけどPythonではどうするのが普通なんですかね

## [PCAD] ALDS1_3_C: Doubly Linked List

リストの実装となるとポインタっぽいからC++で書いたほうがいいのかなーと
思ってましたがやってみたらごく自然に書けました
ただの先入観でした

しかし意外と例外を細かく考える必要があるなあ
この問題だとまだ操作が限られてるけどフルに実装するとまだいくつかのケースがある

```python3
#! /usr/local/bin/python3
# coding: utf-8

class DoublyLinkedNode:

    def __init__(self, x):
        self.prev = None
        self.next = None
        self.value = x

    def print(self):
        print(self.value, end = "")

class DoublyLinkedList:

    def __init__(self, n):
        self.head = None
        self.tail = None

    def insert(self, x):
        node = DoublyLinkedNode(x)
        node.prev = None
        node.next = self.head
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node

    def delete(self, x):
        node = self.head
        while node is not None:
            if node.value == x:
                break
            node = node.next
        else:
            return

        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            node.next.prev = None
        elif node == self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def delete_first(self):
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

    def delete_last(self):
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

    def print(self):
        node = self.head
        while node is not None:
            node.print()
            node = node.next
            if node is not None:
                print(" ", end = "")
        print()

n = int(input())
dll = DoublyLinkedList(n)

for i in range(n):
    line = input().split()
    if line[0] == "insert":
        dll.insert(int(line[1]))
    elif line[0] == "delete":
        dll.delete(int(line[1]))
    elif line[0] == "deleteFirst":
        dll.delete_first()
    elif line[0] == "deleteLast":
        dll.delete_last()

dll.print()
```

で提出してみるとデータ200万個でTLE
最初に全部確保したほうが早かったりするのかな？

いや、ファイル入出力の方を疑うほうが先か
`line = input().split()`の代わりに

```python3
    if i % 2 == 0:
        line = ["insert", str(i)]
    else:
        line = ["delete", str(i - 1)]
```

としてみる

サンプルデータダウンロードしようと思ったら

```console
:
:
insert 695
..... (terminated because of the limitation)
```

なんてなっててびっくり
画面上ではまあ200万行も読み込ませたら大変だししょうがないよねと思ったけど
しかたないので自分でそれっぽく作って試しました

```console
$ time ALDS1_3_C.py < in.txt


real    0m4.613s
user    0m4.575s
sys     0m0.019s
```

そんなに速くもないな
07.45sでTLEにされてるから・・・

元に戻して実行すると

```console
$ time ALDS1_3_C.py < in.txt

real    0m14.741s
user    0m12.575s
sys     0m2.039s
```

うーん
ファイル入出力が5倍くらい早くなれば・・・

調べてたとき、sys.stdinの方がバッファリングの関係で速いとかなんとか
書いてあった気がするなあ

```console
import sys

for l in sys.stdin:
    line = l.split()
```

ってしてみた

```console
$ time ALDS1_3_C.py < in.txt

real    0m3.973s
user    0m3.853s
sys     0m0.034s
```

いや、ファイル読んでないやつより速いのはおかしいだろ
キャッシュに入ったとしても
いや、もとに戻すとやっぱ遅いな

ま、まあいいか
提出してみよう

・・・さっきのは通ったけど最後のテストでTLE
さっきはinsertしてdeleteして、って要素が増えなかったけど
今度は要素が増えていく
メモリ使う分遅くなってるのかな

どうしていいのかわからないので正解出てる人のを参考に直しながら調べてみる
`==`で比較してたのは間違いで`is`で比較する必要があった、というのはいいとして
最後の決め手はメインルーチンを`_main`関数にしたってとこなんだけど
そんなんで速くなるの？
でも`stdin`と`is`と`_main`にしただけでACされた・・・

そういうものとしておこう
Paizaでは一度拒絶されたらリカバリできないから、最初から`stdin`と`_main`を
使うようにしたほうがよさそうだ

というわけで現状のソースはこう
解説は明日読もう

```python3
#! /usr/local/bin/python3
# coding: utf-8

class DoublyLinkedNode:

    def __init__(self, x):
        self.prev = None
        self.next = None
        self.value = x

    def print(self):
        print(self.value, end = "")

class DoublyLinkedList:

    def __init__(self, n):
        self.head = None
        self.tail = None

    def insert(self, x):
        node = DoublyLinkedNode(x)
        node.prev = None
        node.next = self.head
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node

    def delete(self, x):
        node = self.head
        while node is not None:
            if node.value == x:
                break
            node = node.next
        else:
            return

        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.next.prev = None
        elif node is self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def delete_first(self):
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

    def delete_last(self):
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

    def print(self):
        node = self.head
        while node is not None:
            node.print()
            node = node.next
            if node is not None:
                print(" ", end = "")
        print()

def _main():
    n = int(input())
    dll = DoublyLinkedList(n)

    import sys

    for l in sys.stdin:
        line = l.split()
        if line[0] == "insert":
            dll.insert(int(line[1]))
        elif line[0] == "delete":
            dll.delete(int(line[1]))
        elif line[0] == "deleteFirst":
            dll.delete_first()
        elif line[0] == "deleteLast":
            dll.delete_last()

    dll.print()

if __name__ == "__main__":
    _main()
```

## [PCAD] ALDS1_3_C 続き

> 解説は明日読もう

読んで早々、

> また、リストの先頭を指す特別なノードを設置することによって実装を
> 簡略化することができます。
> このノードは「番兵」と呼ばれるもので

あっ

言われてみると！

`head`で先頭、`tail`で末尾を覚えるって代わりに
`nil`というノードを定義して
`nil.next`が先頭を、`nil.prev`が末尾を指すようにするのか

それでうまくいくのか？
・・・いくな
場合分けがキレイになくなってしまう
すばらしい

最初のひとつの追加
先頭に追加
途中に追加
末尾に追加
先頭を削除
途中を削除
末尾を削除
最後のひとつを削除

これくらいの場合について検証が必要
途中に追加、途中を削除、を先に考えてから他のケースが同じように
考えられるかどうかを考える、という順番がよさそう
でも途中で納得したので全部はやってない
`nil`のおかげで双方向リストが輪になってて、どこにも特別なノードが存在しないので
場合分けが必要ないことが直感的にわかる
`nil`も他と同じ輪の構成要素で、たまたまちょっとマークがついてるにすぎないので

とはいうもののそれなりにややこしいので`assert`を使ってテストも書いてみた
テスト部分はジャッジには関係ないけど最終版の全ソース（このままでもAC）

```python3
#! /usr/local/bin/python3
# coding: utf-8

class DoublyLinkedNode:

    def __init__(self, x):
        self.value = x
        self.prev = None
        self.next = None

    def str(self):
        return str(self.value)

class DoublyLinkedList:

    def __init__(self):
        self.nil = DoublyLinkedNode(None)
        self.nil.prev = self.nil.next = self.nil

    def insert(self, x):
        node = DoublyLinkedNode(x)
        node.prev = self.nil
        node.next = self.nil.next
        self.nil.next.prev = node
        self.nil.next = node

    def search(self, x):
        node = self.nil.next
        while node is not self.nil and node.value != x:
            node = node.next
        return node

    def delete_node(self, node):
        # print("delete_node:", node.value, node.prev.value, node.next.value)
        if node is self.nil:
            return
        next = node.next
        node.prev.next = next
        next.prev = node.prev

    def delete(self, x):
        self.delete_node(self.search(x))

    def delete_first(self):
        self.delete_node(self.nil.next)

    def delete_last(self):
        self.delete_node(self.nil.prev)

    def str(self):
        node = self.nil.next
        v = ""
        while node is not self.nil:
            v += node.str()
            node = node.next
            if node is not self.nil:
                v += " "
        return v

    def debug_str(self):
        v = self.nil.next.str() + " "
        v += self.nil.prev.str() + " | "
        v += self.str()
        return v

def test():
    dll = DoublyLinkedList()
    assert dll.debug_str() == "None None | "
    dll.insert(1)
    assert dll.debug_str() == "1 1 | 1"
    dll.insert(2)
    assert dll.debug_str() == "2 1 | 2 1"
    dll.insert(3)
    assert dll.debug_str() == "3 1 | 3 2 1"
    dll.delete(2)
    assert dll.debug_str() == "3 1 | 3 1"
    dll.delete(1)
    assert dll.debug_str() == "3 3 | 3"
    dll.delete(3)
    assert dll.debug_str() == "None None | "
    dll.insert(1)
    assert dll.debug_str() == "1 1 | 1"
    dll.insert(2)
    assert dll.debug_str() == "2 1 | 2 1"
    dll.delete(2)
    assert dll.debug_str() == "1 1 | 1"
    dll.delete(1)
    assert dll.debug_str() == "None None | "
    dll.insert(1)
    assert dll.debug_str() == "1 1 | 1"
    dll.insert(2)
    assert dll.debug_str() == "2 1 | 2 1"
    dll.delete_first()
    assert dll.debug_str() == "1 1 | 1"
    dll.delete_first()
    assert dll.debug_str() == "None None | "
    dll.insert(1)
    assert dll.debug_str() == "1 1 | 1"
    dll.insert(2)
    assert dll.debug_str() == "2 1 | 2 1"
    dll.delete_last()
    assert dll.debug_str() == "2 2 | 2"
    dll.delete_last()
    assert dll.debug_str() == "None None | "

def main():
    n = int(input())
    dll = DoublyLinkedList()
    # print(dll.debug_str())

    from sys import stdin

    for _ in range(n):
        line = stdin.readline().split()
        if line[0] == "insert":
            dll.insert(int(line[1]))
        elif line[0] == "delete":
            dll.delete(int(line[1]))
        elif line[0] == "deleteFirst":
            dll.delete_first()
        elif line[0] == "deleteLast":
            dll.delete_last()
        # print(dll.debug_str())

    print(dll.str())

test()

main()
```

## [PCAD] 標準ライブラリ

ここでちょっと問題はひとやすみ
標準ライブラリでスタック、キュー、ベクタ、リストを使う方法が解説されてます

Pythonではどうなるのかな

### スタック

C++のSTLには`size`、`top`、`push`、`pop`、`empty`といった関数が
含まれている模様
サンプルを見ると、`pop`は削除のみで値を取り出すのは`top`を使えってことかな
何ていうんだっけ
関数は副作用なしで値を返すだけ、副作用はコマンドでコマンドは値を返さない、みたいなの

ググったらPythonチュートリアルで早速紹介されてるようだ
ということは逆に言うとStackクラスみたいなのはないってことだなきっと

> スタックの一番上に要素を追加するには append() を使います。スタックの一番上から要素を取り出すには pop() をインデクスを指定せずに使います。
[5.1.1. リストをスタックとして使う](https://docs.python.jp/3/tutorial/datastructures.html#using-lists-as-stacks)

あれ
考えてみたら`append`って末尾にくっつけるやつだよな
普通のリストだとO(n)になってしまうよな
Pythonでリストって言ってるやつは双方向リストなのかな

・・・
ただの配列だった
そうだったか
確認してなかった

そりゃ末尾に追加だな

わざわざクラスで書くとこうかな

```python3
class Stack():

    def __init__(self):
        self.s = []

    def top(self):
        return self.s[-1]

    def size(self):
        return len(self.s)

    def push(self, x):
        self.s.append(x)

    def pop(self):
        return self.s.pop()

    def empty(self):
        return len(self.s) == 0
```

もう一度調べてみたら双方向キューを実装した`collections.deque`っていうのがある
といってもスタックとして使うだけなら配列で十分

`from collections import deque`して
`self.s = []`を`self.s = deque()`にするだけで動くことは動く

### キュー

キューのクラスは書いたけど`collections.deque`で書き直してみよう
`append`、`appendleft`、`pop`、`popleft`とあって先頭も末尾も
自由にできるけど、左か右か、どっちを先頭とするべきかな

```python3
$ python3
>>> from collections import deque
>>> q = deque([1,2,3])
>>> q
deque([1, 2, 3])
>>> q.popleft()
1
```

`append`と`popleft`を使うのが素直そうな感じ

```python
class Queue():

    def __init__(self):
        self.q = deque()

    def size(self):
        return len(self.q)

    def front(self):
        return self.q[0]

    def push(self, x):
        self.q.append(x)

    def pop(self):
        return self.q.popleft()

    def empty(self):
        return len(self.q) == 0
```

## [PCAD] 標準ライブラリ 続き

### ベクタ

ベクタは単にpythonの配列だったことが判明しましたのでそのまま使います
クラス作る必要はまったくないけど練習で
おかげで`[]`がオーバーロード？できるようになってることを知るなど

```python
class Vector():
    def __init__(self):
        self.v = []

    # []によるアクセス
    def __getitem__(self, i):
        return self.v[i]

    # 同上
    def __setitem__(self, i, val):
        self.v[i] = val

    def size(self):
        return len(self.v)

    def push_back(self, x):
        self.v.append(x)

    def pop_back(self):
        return self.v.pop()

    # beginとendの代わり
    def __iter__(self):
        return iter(self.v)

    # C++のvectorではイテレータで位置を指定するのでちょっと違う
    def insert(self, p, x):
        self.v.insert(p, x)

    # 同上
    def erase(self, p):
        del self.v[p]

    def clear(self):
        self.v.clear()
```

型がちぇっくされないということはこういうこともできるかな

```python
class Foo():
    def __init__(self, a):
        self.a = a

    def __getitem__(self, f):
        return list(map(f, self.a))

a = Foo([1, 2, 3])
print(a[lambda x: x * 2]) # => [2, 4, 6]
```

できた（しない

## [PCAD] 標準ライブラリ 続き2

### リスト

STLで`list`っていったら双方向リストなんだ
まあ配列をリストと呼ぶよりは納得できる

dequeがそのまんまで足りてそう

```python
class List():
    def __init__(self):
        self.l = deque()

    def size(self):
        return len(self.l)

    def __iter__(self):
        return iter(self.l)

    def push_front(self, x):
        self.l.appendleft(x)

    def push_back(self, x):
        self.l.append(x)

    def pop_front(self):
        return self.l.popleft()

    def pop_back(self):
        return self.l.pop()

    def insert(self, i, x):
        self.l.insert(i, x)

    # ない！
    # def erase(self, i):

    # 代わりに、指定した値の要素を消すのならある
    def remove(self, x):
        self.l.remove(x)

    def clear(self):
        self.l.clear()
```

と思ったら`erase`に対応した関数がなかった
双方向リストなら途中の要素を消すのも簡単なはずだけど
`deque`の中をいじれないとどうしようもない？

## [PCAD] 書き直し

標準のデータ構造でALDS1_3_A、ALDS1_3_B、ALDS1_3_Cを書き直しました
すっきり

ALDS1_3_A
(pythonの)リストと`append`、`pop`を使いました

```python
#! /usr/local/bin/python3
# coding: utf-8

def stack_op2(s, op):
    v2 = s.pop()
    v1 = s.pop()
    s.append(op(v1, v2))

def calc(terms):
    s = []
    for t in terms:
        if t == "+":
            stack_op2(s, lambda v1, v2: v1 + v2)
        elif t == "-":
            stack_op2(s, lambda v1, v2: v1 - v2)
        elif t == "*":
            stack_op2(s, lambda v1, v2: v1 * v2)
        else:
            s.append(int(t))
    return s.pop()

print(calc(input().split()))
```

ALDS1_3_B

`deque`で`appendleft`と`pop`を使いました

```python
#! /usr/local/bin/python3
# coding: utf-8

from collections import deque

def main():
    n, q = [int(x) for x in input().split()]

    proc = deque()

    for i in range(n):
        name, ptime = input().split()
        proc.appendleft((name, int(ptime)))

    time = 0
    while proc:
        name, ptime = proc.pop()
        time += min(q, ptime)
        ptime -= min(q, ptime)
        if ptime <= 0:
            print(name, time)
        else:
            proc.appendleft((name, ptime))

main()
```

ALDS1_3_C

`deque`で`appendleft`、`remove`、`pop`、`popleft`を使いました
`remove`は対象がないとExceptionなので無視してやる必要がありました

```python
#! /usr/local/bin/python3
# coding: utf-8

from sys import stdin
from collections import deque

def main():
    n = int(input())
    dll = deque()

    for _ in range(n):
        line = stdin.readline().split()
        if line[0] == "insert":
            dll.appendleft(int(line[1]))
        elif line[0] == "delete":
            try:
                dll.remove(int(line[1]))
            except ValueError:
                None
        elif line[0] == "deleteFirst":
            dll.popleft()
        elif line[0] == "deleteLast":
            dll.pop()

    print((" ".join(map(str, dll))))

main()
```

200万件の実行結果 01.80 s
ってめっちゃ速え！
自前の双方向リストだと 04.98 s
自分で書いちゃだめですね

## [PCAD] ALDS1_3_D

> ※この問題はやや難しいチャレンジ問題です。難しいと感じたら今は飛ばして、実力をつけてから挑戦してみましょう。

どこが難しいんだろう？
水面の高さを覚えておいて、あと面積を足し算していくだけじゃない？
今水たまりの中か外か覚えておいて場合分けは必要かな
そもそもデータ構造らしきものも出てこないし・・・

などと思った私があさはかでした

そもそもデータ構造らしきものが出てこない時点でおかしいと思え

左から見ていくだけでできると思ったんですけどね
考えてみたら右側の岸が確定するまで水面の高さ出ませんね

しばらくがんばって考えましたが、データ構造っぽいものが出てくるやり方は
思いつかなかったのでまずは力技でやってみました

まずは地形まで求めたあと、すべてのx座標(左右)について、一番高いところの高さから
1ずつ下がりつつ、左右に岸のある高さを探して水面を求める、という方式
横方向にループして、高さ方向にループして、また横方向にループするからO(n^3 )かな

あ、面積はマジメに台形の計算とかしてないです
幅1なので深さを単純に足し算すれば面積に

```python
#! /usr/local/bin/python3
# coding: utf-8

from operator import add

def shape_to_slope(ch):
    if ch == "\\":
        return -1
    elif ch == "_":
        return 0
    else:
        return 1

def land(height, h, x, delta):
    while x in range(len(height)):
        if height[x] >= h:
            return True
        x += delta
    return False

def depth_at_x(height, x, max_height, min_height):
    for h in reversed(range(height[x], max_height + 1)):
        if land(height, h, x, -1) and land(height, h, x, 1):
            return h - height[x]
    return 0

def main():
    shape = [ch for ch in input()]
    slope = [shape_to_slope(ch) for ch in shape]

    max_height = min_height = 0
    height = [0]
    for sl in slope:
        height.append(height[-1] + sl)
        max_height = max(height[-1], max_height)
        min_height = min(height[-1], min_height)

    prev_depth = 0
    current_area = 0
    pool_area = []

    for x in range(1, len(height)):
        depth = depth_at_x(height, x, max_height, min_height)
        current_area += depth
        if prev_depth > 0 and depth == 0:
            pool_area.append(current_area)
            current_area = 0
        prev_depth = depth

    print(sum(pool_area))
    print(len(pool_area), *pool_area)

main()
```

はいはいTLETLE
400文字でTLEだけど20,000文字まである
O(n^2 )でもダメかも？

しかしスタックだかキューだかリストだか知らんけど
どうやって使うんだ？

解説見るか・・・
うーん
もうちょっと考えよう

## [PCAD] ALDS1_3_D 続き

さて

> しかしスタックだかキューだかリストだか知らんけど

使うとしたらスタックかなあ
何を積むか
計算量を増やさないようにするには、左から順番に１回見るだけで終わらないといけなさそう

深くなっていく間はなにか積んでおいて、浅くなるときに取り出す感じ？
何を積む？
深さ？x座標？両方？
両方いるような気もするけど、スタックをたとえば深さごとに用意するのでは
計算量が増えてしまう

そうか、深くなるのも浅くなるのも１刻みだから深さは覚えておかなくても？
右へ進みつつ、深くなるときx座標だけをpush、浅くなるときにpopしていくと
スタックの一番上にはいつも同じ深さの左側の底のx座標があるということ？

スタックが空なら水たまりが終わりってことになるな
なんかいけそう

コードはほとんど書き直しか

```python
def main():
    shape = [ch for ch in input()]
    slope = [shape_to_slope(ch) for ch in shape]

    left_x = []
    cur_area = 0
    pool_area = []
    for x, sl in enumerate(slope):
        if sl == -1:
            left_x.append(x)
        elif left_x and sl == 1:
            cur_area += x - left_x.pop()
            if not left_x:
                pool_area.append(cur_area)
                cur_area = 0

    print(sum(pool_area))
    print(len(pool_area), *pool_area)
```

これでいけるかと思ったけどダメ
水たまりの終わりの判定条件がおかしい
スタックが空にならなくても水たまりが終わることがある

## [PCAD] ALDS1_3_D 続きの続き

> スタックが空にならなくても水たまりが終わることがある

浅くなってきてた水たまりが深くなったらいったん水たまりが終わったことに
するけれども、右側の底がもっと高くなったら「飲み込まれる」ような動きがいる

と思って作り込んだのがこれ

```python
def pool_merge(pool_area, left_x, cur_area):
    if not pool_area:
        return cur_area
    while pool_area and (pool_area[-1])[0] > len(left_x):
        cur_area += (pool_area.pop())[1]
    return cur_area

def calc(s):
    shape = [ch for ch in s]
    slope = [shape_to_slope(ch) for ch in shape]

    left_x = []
    cur_area = 0
    pool_area = []
    for x, sl in enumerate(slope):
        if sl == -1:
            if cur_area > 0:
                pool_area.append((len(left_x), cur_area))
                cur_area = 0
            left_x.append(x)
        elif left_x and sl == 1:
            cur_area += x - left_x.pop()
            cur_area = pool_merge(pool_area, left_x, cur_area)
            if not left_x:
                pool_area.append((len(left_x), cur_area))
                cur_area = 0
    if cur_area > 0:
        pool_area.append((len(left_x), cur_area))

    return [p[1] for p in pool_area]

pool_area = calc(input())
print(sum(pool_area))
print(len(pool_area), *pool_area)
```

そろそろ頭が死にそうなんだけれども、まだ漏れがある

はずなんだけどAC
（50番のテストが"--"ってなってるんだけどAC）

ていうかね
自分でまだうまくいかないはずっていうテストケースがうまくいってしまう
意味わからないんですけど
`\///\\\//`はうまくいかないはずなんですよ！
まんなかに山があっても飲み込んでしまうはずなの！
まんなかに山があるとか考慮してないんだから！
水たまり以外のことは忘れてしまうんだから！
なんで成功してるの！

：
：

そうか
実際の標高じゃなくて、スタックの深さでやってるからか
山があるってことはスタックが空になってるってことで
その時点で深さ０ってことになるから金輪際飲み込まれることはないってわけか

いや難しすぎる
漏れがないとかまったく保証できる気がしない
AC取ったし解説読む

## [PCAD] ALDS1_3_D 続きの続きの続き

> AC取ったし解説読む

ざっくり方針は同じかな
データ構造の章に出てるっていうのがヒントになったし

> この問題の解法として、ソートアルゴリズムを応用するなど、いくつかのアルゴリズムが考えられますが

ふーん
どんなんだ
ちょっとぱっとは思いつかないな
「応用」だからただソートするわけじゃないんだろうな

> 各水たまりの面積はもう１つのスタックS2を用いて保存していきます。

ここは同じ作戦だ

> スタックS2には、(その水たまりの最も左の\の位置, その水たまりのその時点での面積)の組を積んでいきます。

自分は「その水たまりの最も左の\の位置」じゃなくてその時点でのスタックの深さを積んでた
\の位置を覚えておいてどう使うのかな

> ここで、新たにできる水たまりの面積は、S2に積まれているjの直前までの水たまりの面積の総和と、新しくできる面積i-jの和になります。

jが・・・
・・・

そうか
左の岸より右にある水たまりが飲み込まれるのか
図を見たら当たり前だった

ソース見る
違うところ以外はかなり似てた（当たり前か

```python
def calc(shape):
    left_x = []
    pool_area = []
    for x, sh in enumerate(shape):
        if sh == "\\":
            left_x.append(x)
        elif left_x and sh == "/":
            lx = left_x.pop()
            area = x - lx
            while pool_area and (pool_area[-1])[0] > lx:
                area += (pool_area.pop())[1]
            pool_area.append((lx, area))
        # print(x, ":", sh, left_x, pool_area)

    return [p[1] for p in pool_area]

pool_area = calc(input())
print(sum(pool_area))
print(len(pool_area), *pool_area)
```

## [PCAD] ALDS1_4_A: Linear Search

ひとつめの数列の中に、ふたつめの数列に含まれる要素がいくつあるかを数える
線形探索って書いてあるからソートはなし？
要素数が10000個とか500個とかだから単純に二重ループでやればいいのかな

お、こんなデータがある
ループの順番に気をつけて

```text
5
1 1 2 2 3
2
1 2
```

それくらいでずいぶん簡単に見えるけど落とし穴はないかな
AC
なかったみたい

```python
#! /usr/local/bin/python3
# coding: utf-8

def count(s, t):
    c = 0
    for x in t:
        for y in s:
            if x == y:
                c += 1
                break
    return c

_ = int(input())
s = [int(x) for x in input().split()]

_ = int(input())
t = [int(x) for x in input().split()]

print(count(s, t))
```

解説を読む
あー番兵ね
番兵を入れると定数倍の高速化が期待できるそうな

とは言っても`for ... in ...`で書いてると番兵が置けないので
カウンタ入れてやってみよう
上のコードだと#9のテストに00.03sかかってます

番兵なしだとこう書くのかな
考えてみたら外側は`for ... in ...`でもいいんだけど

```python
#! /usr/local/bin/python3
# coding: utf-8

def count(n, s, q, t):
    c = 0
    i = 0
    while i < q:
        j = 0
        ti = t[i]
        while j < n:
            if s[j] == ti:
                c += 1
                break
            j += 1
        i += 1
    return c

n = int(input())
s = [int(x) for x in input().split()]

q = int(input())
t = [int(x) for x in input().split()]

print(count(n, s, q, t))
```

これだと00.06s

番兵ありだと

```python
#! /usr/local/bin/python3
# coding: utf-8

def count(n, s, q, t):
    c = 0
    i = 0
    s.append(0)
    while i < q:
        j = 0
        s[n] = t[i]
        ti = t[i]
        while s[j] != ti:
            j += 1
        if j < n:
            c += 1
        i += 1
    return c

n = int(input())
s = [int(x) for x in input().split()]

q = int(input())
t = [int(x) for x in input().split()]

print(count(n, s, q, t))
```

00.05s

速くなったと言えば速くなったけど誤差の範囲かもしれない
もうちょっと速くなってもいい気がしたけど
なんにせよpythonでは普通に`for ... in ...`で書こう

## [PCAD] ALDS1_4_B: Binary Search

今度は二分探索
ふたつに分けながら探すっていうことだけ覚えてる
1足したり引いたり終了の判定したりあたりの細かいことは書きながら考える

番兵は・・・いないよね？

```python
#! /usr/local/bin/python3
# coding: utf-8

def search(S, y):
    left = 0; right = len(S) - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == y:
            return True
        if S[mid] < y:
            left = mid + 1
        else:
            right = mid - 1
    return False

def count(S, T):
    c = 0
    for y in T:
        if search(S, y):
            c += 1
    return c

_ = int(input())
S = [int(x) for x in input().split()]

_ = int(input())
T = [int(y) for y in input().split()]

print(count(S, T))
```

AC

解説を見る

1足したり引いたり終了の判定したりあたりの細かいことが違うな
いや、rightが右端「の次」を指してるってことを考えると意味は同じか
（自分は右端を指しているつもりで書いた）
右端の次を指すって考えたほうが筋がよさそうな気はする
微妙に足し算も減るし

```python3
def search(S, y):
    left = 0; right = len(S)
    while left < right:
        mid = (left + right) // 2
        if S[mid] == y:
            return True
        if S[mid] < y:
            left = mid + 1
        else:
            right = mid
    return False
```

## [PCAD] ALDS1_4_C: Dictionary

「簡易的な」辞書って書いてあるけど、ただ配列にいれるだけじゃダメなんだろうね
100,000個で2secって書いてあるし
問題の並びや前にあった解説から空気を読んで配列に入れてハッシュ法でやることにする

4文字の組み合わせで長さが12までだから木を作ってもいいような気もするけど
配列で順序キープしながらだと間に合わないかな

さてハッシュ法と言えばハッシュ関数を使って要素の場所を探す、くらいしか
覚えてないわけだが

* ハッシュ用の関数ってどうするものなんだろう 自分で作るのか？
* テーブルの大きさはどれくらいがいいんだろう？
* ハッシュ値が重なったときはどうするんだっけ

まあやってみよう

ハッシュ関数はmd5を流用してみた
サイズは適当
重なってもいいようにリストで持つ

```python
#! /usr/local/bin/python3
# coding: utf-8

from hashlib import md5

class HashTable():

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, s):
        h = 1
        for c in s:
            h = (h * 9997 + ord(c)) % self.size
        return h

    def insert(self, s):
        e = self.table[self.hash(s)]
        if s not in self.table[self.hash(s)]:
            e.append(s)

    def find(self, s):
        return s in self.table[self.hash(s)]

from sys import stdin

def main():
    h = HashTable(1000000)
    _ = int(input())
    for l in stdin:
        cmd, param = l.split()
        if cmd == "insert":
            h.insert(param)
        elif h.find(param):
            print("yes")
        else:
            print("no")

main()
```

ACだけど04.98sですが何か
サイズを1000000にしたら遅くなった 05.23 s
サイズを10000にしても遅かった 05.28 s

md5に時間がかかるのかなあ
自分で書いてみよう
適当

```python
    def hash(self, s):
        h = 1
        for c in s:
            h = (h * 9997 + ord(c)) % self.size
        return h
```

04.99 s
うーん
2secっていうのはC++用の時間？

もう解説でいいや
どれどれ

ふーんダブルハッシュを用いたオープンアドレス法、か
ハッシュ関数はそんなに凝った感じじゃないな
そんなにバラけなくてもいいってことかな

A,C,G,Tを1,2,3,4に変換してるのって意味あるんだっけ
そのままコード使ってもいい気がするけど
あ、1〜4だからハッシュを求めるとき5をかけてるわけか なるほど
文字列が短い順にキレイに埋まっていきそう
1〜4に変換するより26文字対応にしようかな

```python
class HashTable():

    M = 1046527

    def __init__(self):
        self.table = [False] * HashTable.M

    def h1(self, k):
        return k % HashTable.M

    def h2(self, k):
        return 1 + (k % (HashTable.M - 1))

    CHAR_BEGIN = ord("A") - 1
    CHAR_CYCLE = ord("C") - ord("A") + 1

    def key(self, s):
        k = 0; p = 1
        for c in s:
            k += (ord(c) - HashTable.CHAR_BEGIN) * p
            p *= HashTable.CHAR_CYCLE
        return k

    def find(self, s):
        k = self.key(s)
        h = self.h1(k)
        d = self.h2(k)
        while True:
            if self.table[h] == s:
                return True
            elif not self.table[h]:
                return False
            h = (h + d) % HashTable.M

    def insert(self, s):
        k = self.key(s)
        h = self.h1(k)
        d = self.h2(k)
        while True:
            if self.table[h] == s:
                return
            elif not self.table[h]:
                self.table[h] = s
                return
            h = (h + d) % HashTable.M
```

05.17s

すみません遅くなりました

C++の`for (i = 0; ; i++)`を翻訳しようとして気づいたんだけど
`range`で終わりのない数列を指定する方法ってない？
他の関数があるんだろうか
こういうのでいいんだけど

```python
def iota(start):
    i = start
    while True:
        yield i
        i += 1
```

結局使ってないわけですが

ところでいま世の中で言う「ハッシュ」は別にここで出てくるハッシュ法とは
関係ないそうですね
てっきりアルゴリズムからついた名前かと思ってました

## [PCAD] 標準ライブラリによる検索

### イテレータ

イテレータってforとかで使ってるくらいで素では使ったことないな
たぶん普通は素で使うことはないんだろう

C++と見比べてみると

C++ではend()と比較して、PythonではStopIteration例外を補足する
これは前も見た

サンプルの`print()`をできるだけ直訳するとこんな感じだろうか

```python
def print_it(v):
    it = iter(v)
    while True:
        try:
            print(next(it), end="")
        except StopIteration:
            break
    print()
```

あと、Pythonではイテレータの指す場所の値を更新することはできないのかな
イミュータブルっぽく使えってことだと理解しておく

しかしサンプルをpython化しようとするとこんな

```python
it = iter(v)
v2 = []
next(it)
v2.append(3)
v2.append(next(it) + 1)
v2.append(next(it))
v2.append(next(it))
```

とかこんな

```python
it = iter(v)
v3 = []
for i, x in enumerate(v):
    if i == 0:
        v3.append(3)
    elif i == 1:
        v3.append(x + 1)
    else:
        v3.append(x)
```

でちょっとブサイクな気もする

### 二分探索

pythonでは[bisect](https://docs.python.org/3.6/library/bisect.html)というライブラリが使えそう
二分探索とはいうものの、値をみつけるというよりもソートされた状態を
保ったまま新しい要素を挿入するための場所を探すというのが目的な模様
これを使えば高速な挿入ソートができるというわけかな

C++ではイテレータを返すけどPythonでは単にリストのインデックスを返すので
使い方はこんな感じ

```python
A = [1, 1, 2, 2, 2, 4, 5, 5, 6, 8, 8, 8, 10, 15]
pos = bisect.bisect_left(A, 3)
print("A[%s] = %d" % (pos, A[pos]))
pos = bisect.bisect_left(A, 2)
print("A[%s] = %d" % (pos, A[pos]))
```

普通に値を見つけたいときの使い方も書いてあった
[8.6.1. Searching Sorted Lists](https://docs.python.org/3.6/library/bisect.html#searching-sorted-lists)

ALDS1_4_Bの`search`がこうなる

```python
def search(S, y):
    pos = bisect_left(S, y)
    return S[pos] == y
```

\#10 が 00.09s秒
元のソースだと00.25sだから速くなってる

## [PCAD] ALDS1_4_D: Allocation

> この問題はやや難しいチャレンジ問題です。

出た
思考★★☆、実装★★☆だから水たまりの問題より少し実装が難しいということか

ぱっと見難しい最適化の問題かと思ったけど、ベルトコンベアーとトラックという
制限がついてるからなんとかなるのかな

* 荷物は出てきた順に積まなければならない
* いったん荷物を積んで出発したトラックにあとで荷物を載せ直すことはできない

てことでしょう
といってもいいアイデアがあるわけではない

まず心配なのは出てきた順に常にめいっぱい積めばいいかどうか
あとになってあそこであえて次のトラックに積んでおけば・・・みたいなことが
あるようだと面倒

・・・これはたぶん大丈夫だな
目いっぱいでいこう

で次は
nもkも100000まであるから計算量
なんどもやり直すわけにはいかない気がするけど・・・

Pは少なくとも一番重い荷物よりは大きいし、
少なくとも荷物の総重量÷トラックの台数よりも大きいとは言える
でもあとはやってみないとわからない気がするな・・・
一発でわかるようなやり方があるだろうか・・・

そんなやりかたは思いつかないので
Pを増やしながら試してみよう

```python
from math import floor
from sys import stdin

def allocate(n, k, w, P):
    n_truck = 1
    load = 0
    for wt in w:
        if load + wt > P:
            n_truck += 1
            if n_truck > k:
                return False
            load = 0
        load += wt
    return True

def main():
    n, k = [int(x) for x in stdin.readline().split()]
    w = [int(x) for x in stdin]
    P = max(max(w), floor(sum(w) / k))

    while not allocate(n, k, w, P):
            P += 1
    print(P)

main()
```

予想どおりTLE

うーんなんだろうなあ
検索アルゴリズム入ってないし
使うとしたら二分探索だろうなあ・・・

あ、二分探索すればいいのか
そういうことか？

Pの最大は何に取ればいいかな？
絶対確実に詰めるPは？
総重量そのものを使ったら贅沢すぎるかな？

まずやってみよう
修正は`main()`だけ

```python
def main():
    n, k = [int(x) for x in stdin.readline().split()]
    w = [int(x) for x in stdin]
    min_P = max(max(w), floor(sum(w) / k))
    max_P = sum(w)

    while min_P < max_P:
        mid_P = (min_P + max_P) // 2
        if allocate(n, k, w, mid_P):
            max_P = mid_P
        else:
            min_P = mid_P + 1

    print(min_P)
```

あっさりAC
二分探索すげー

解説は想定通り
二分探索で1足したりするところがやっぱり違う
この間やった二分探索と同じ書き方にしたんだけど
ケースバイケースなのかなあ？

そしてソース
最小と最大が0と100000*100000ってそこまでお大尽だったか
毎回半分になるんだから誤差の範囲？

手頃なところで試してみたところ
上のソースでは21回、0と100000*100000で34回
誤差と言えば誤差かな

## [PCAD] ALDS1_5_A: Exhaustive Search

章が「再帰・分割統治法」でセクションが「全探索」なんだけど
n重ループみたいな単純な全探索じゃないといけないんだろうか
普通に書くと再帰になってしまいそう
再帰を使って全部試せば全探索？

・・・絵からして再帰でよさそうだな

```python
def can_make_sum(A, m):
    if m == 0:
        return True
    elif m < 0 or not A:
        return False
    else:
        return (can_make_sum(A[1:], m - A[0]) or
                can_make_sum(A[1:], m))

def solve():
    n = int(input())
    A = [int(x) for x in input().split()]
    q = int(input())
    M = [int(x) for x in input().split()]

    for m in M:
        print("yes" if can_make_sum(A, m) else "no")

solve()
```

あらTLE
\#10で41.99s

配列がコピーになってるからかな？

``` python
def can_make_sum(A, k, m):
    if m == 0:
        return True
    elif m < 0 or k == len(A):
        return False
    else:
        return (can_make_sum(A, k + 1, m - A[k]) or
                can_make_sum(A, k + 1, m))
```

やっぱり41.99s
42秒制限なのか

適当なデータ使ってローカルで時間を測ってみる
さっきの

```text
time ALDS1_5_A.py  < in.txt
no
no
:
real    0m6.349s
user    0m6.312s
sys     0m0.020s
```

今回の

```text
time ALDS1_5_A.py  < in.txt
no
no
:
real    0m5.879s
user    0m5.857s
sys     0m0.015s
```

速くなった
でもまだTLE

あと何が速くなるかな
`A`を渡すことをやめてみるか
速くなるのか？

```python
def solve():

    def can_make_sum(k, m):
        if m == 0:
            return True
        elif m < 0 or k == n:
            return False
        else:
            return (can_make_sum(k + 1, m - A[k]) or
                    can_make_sum(k + 1, m))

    n = int(input())
    A = [int(x) for x in input().split()]
    _ = int(input())
    M = [int(x) for x in input().split()]

    for m in M:
        print("yes" if can_make_sum(0, m) else "no")
```

なった

```text
real    0m4.824s
user    0m4.805s
sys     0m0.014s
```

でもTLE
劇的に速くならないとだめかなー
ちょっと反則してみよ

```python
from itertools import combinations

def solve():

    def can_make_sum(m):
        for l in range(len(A)):
            for c in combinations(A, l):
                if sum(c) == m:
                    return True
        return False

    _ = int(input())
    A = [int(x) for x in input().split()]
    _ = int(input())
    M = [int(x) for x in input().split()]

    for m in M:
        print("yes" if can_make_sum(m) else "no")

solve()
```

速くなった

```text
real    0m3.383s
user    0m3.322s
sys     0m0.026s
```

でもTLE

枝刈り？すれば速くなりそうな気もするけど「全探索」だしなあ
メモ化した

```python
def solve():
    def can_make_sum(k, m):
        def cmi(k, m):
            if m == 0:
                return True
            elif m < 0 or k == n:
                return False
            else:
                return (can_make_sum(k + 1, m - A[k]) or
                        can_make_sum(k + 1, m))

        if (k, m) not in cache:
            cache[(k, m)] = cmi(k, m)
        return cache[(k, m)]

    cache = {}
    n = int(input())
    A = [int(x) for x in input().split()]
    _ = int(input())
    M = [int(x) for x in input().split()]

    for m in M:
        print("yes" if can_make_sum(0, m) else "no")

solve()
```

さて

```text
real    0m0.112s
user    0m0.085s
sys     0m0.014s
```

一瞬
メモ化すげー
というのは知ってたけどいいのかこれで
まあ全探索はしてるし

今度は余裕でAC
メモリはどうなの
さっきのが5624KB
メモ化して9252KB
4MB程度なのか
それくらいならいいのかな

解説・サンプルコードは素直な再帰だった
他の人はどうやってんのと思ってSolutionsを見てみたら
ビット演算を使った劇的に速いアルゴリズムがあった
なんでこれで？と思うような超短いコードだったけどよく考えたら確かに
なるほど勉強になるなー

ところでAOJならこうやってAC出るまでちょっとずつ改善していけばいいけど
Paizaだと一回失敗したらリカバリできないからなあ
そこがつらい

## [PCAD] ALDS1_5_C:Koch Curve

まずは自力で２次元ベクトルのクラスを作ってみる
正三角形の頂点を求めるのには三角関数でいいのかな？

add, sub, scaleを演算子のオーバーロードで書いてみるテスト
この問題が解ける最低限で

```python
from math import pi, sin, cos

class Point2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point2D(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point2D(self.x - p.x, self.y - p.y)

    def __rmul__(self, a):
        if isinstance(a, float):
            return Point2D(self.x * a, self.y * a)
        else:
            return NotImplemented

    def rotate(self, theta):
        return Point2D(self.x * cos(theta) - self.y * sin(theta),
                       self.x * sin(theta) + self.y * cos(theta))

    def __str__(self):
        return "{} {}".format(self.x, self.y)

def koch(p1, p2, level):
    if level == 0:
        return
    l = p2 - p1
    s = p1 + (1/3) * l
    t = p1 + (2/3) * l
    u = s + (1/3) * l.rotate(pi/3)
    koch(p1, s, level - 1)
    print(s)
    koch(s, u, level - 1)
    print(u)
    koch(u, t, level - 1)
    print(t)
    koch(t, p2, level - 1)

def main():
    n = int(input())
    print(Point2D(0.0, 0.0))
    koch(Point2D(0.0, 0.0), Point2D(100.0, 0.0), n)
    print(Point2D(100.0, 0.0))

main()
```

おｋ

ていうかきっとライブラリがあるだろう
・・・numpyてやつ使わないとそれっぽくない？
複素数でも使うか

```python
from math import pi
from cmath import rect

def print_xy(z):
    print(z.real, z.imag)

def koch(p1, p2, level):
    if level == 0:
        return
    l = p2 - p1
    s = p1 + (1/3) * l
    t = p1 + (2/3) * l
    u = s + (1/3) * l * rect(1, pi/3)
    koch(p1, s, level - 1)
    print_xy(s)
    koch(s, u, level - 1)
    print_xy(u)
    koch(u, t, level - 1)
    print_xy(t)
    koch(t, p2, level - 1)

def main():
    n = int(input())
    print_xy(0+0j)
    koch(0+0j, 100+0j, n)
    print_xy(100+0j)

main()
```

## [PCAD] ALDS1_5_B: Merge Sort

擬似コードをそのまま書けばほとんど終わりだけどあえてイテレータで書いてみた
こういう書き方で合ってるんだろうか
若干無理してる感あるような気も

```python
#! /usr/local/bin/python3
# coding: utf-8

from math import inf

c = 0

def merge(A, left, mid, right):
    global c

    L = A[left:mid]; L.append(inf)
    R = A[mid:right]; R.append(inf)
    i = iter(L); l = next(i)
    j = iter(R); r = next(j)
    for k in range(left, right):
        c += 1
        if l < r:
            A[k] = l
            l = next(i)
        else:
            A[k] = r
            r = next(j)

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

def main():
    n = int(input())
    S = [int(x) for x in input().split()]
    merge_sort(S, 0, n)
    print(*S)
    print(c)

main()
```

比較回数はグローバル変数にしてしまったけどなにかかっこいい書き方ないかな

## [PCAD] ALDS1_6_B: Partition

今回も擬似コード翻訳すれば終わりなんだけどなんかややこしい
ノートに絵を書いてみるまでピンとこなかった
（解説見れば書いてあるんだけど）

```python
#! /usr/local/bin/python3
# coding: utf-8

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1

def bracketify(A, i, q):
    return "[" + str(A[i]) + "]" if i == q else str(A[i])

def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    q = partition(A, 0, n - 1)
    print(*[bracketify(A, i, q) for i in range(n)])

main()
```

イテレータで書き換えてみようかと思ったけど
要素の入れ替えとか最後の要素を見るとか無理な気がしてきたので放置
新しいリストにappendしていくのだとマージになってしまうし

## [PCAD] ALDS1_6_C: Quick Sort

前回の結果を使ってQuick Sort
Stableかどうかも判定するんだけどアレだな
バブルソートじゃTLEだろうからマージソート使うんだな

配列の値から数字を取り出すところは`merge_sort`や`quick_sort`に
関数を渡すのかなと思ったけどそこまですることもあるまいということで直書き

```python
from sys import stdin
from math import inf

def merge(A, left, mid, right):
    L = A[left:mid]; L.append(("", inf))
    R = A[mid:right]; R.append(("", inf))
    i = iter(L); l = next(i)
    j = iter(R); r = next(j)
    for k in range(left, right):
        if l[1] <= r[1]:
            A[k] = l
            l = next(i)
        else:
            A[k] = r
            r = next(j)

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def main():
    n = int(stdin.readline())
    A = []
    for l in stdin:
        suit, num = l.split()
        A.append((suit, int(num)))
    B = A[:]
    quick_sort(A, 0, n - 1)
    merge_sort(B, 0, n)
    print("Stable" if A == B else "Not stable")
    [print(*a) for a in A]

main()
```

おｋ
ところでたまたま結果が同じだったっていうのもStableのうちなのかな？
ちょっと違う気もする

あとここ、リスト閉包で書けないものかな
split()を2回書いてもよければ書けなくもないけどそれはそれでうれしくない

```python
    for l in stdin:
        suit, num = l.split()
        A.append((suit, int(num)))
```

## ひとやすみ: vscode入門

PythonのコードはVisual Studio Codeで書いてます
インストールして特に何も調べずに使ってたので便利な機能を見逃して人生を損してるかもしれない
ということでとりあえず@ITの記事をざっと確認してみました

[Visual Studio Codeの使い方、基本の「キ」 - ＠IT](http://www.atmarkit.co.jp/ait/articles/1507/10/news028.html)

* クイックオープン: Cmd+P、コマンドパレット: Shift+Cmd+P
  * ?: ヘルプ
  * >: コマンド実行
  * #: シンボルへ移動
* パスを通す: コマンドパレット+"Shell Command: Install 'code' command in PATH"
* ウェルカムページ: [ヘルプ]-[ようこそ]
* プレビューエディタ: エクスプローラでシングルクリック
* マルチルートワークスペース: [ファイル]-[ワークスペースにフォルダーを追加]
* 統合ターミナル: Ctrl+Shift+@
* カーソルの左側を削除: Cmd+Delete
* カーソル行を削除: Shift+Cmd+K
* カーソル行の上に改行: Shift+Cmd+Ener
* カーソル位置に改行: Ctrl+O
* カーソル行の下に改行: Cmd+Enter
* ユーザー設定／ワークスペース設定: [Code]-[基本設定]-[設定] Cmd-,
* ショートカット設定: [Code]-[基本設定]-[キーボード ショートカット] Cmd-K Cmd-S

[Visual Studio CodeでGitを利用する - ＠IT](http://www.atmarkit.co.jp/ait/articles/1507/21/news017.html)

* リモートリポジトリの設定はコマンドラインで
  * `git remote add origin https://github.com/koba925/PCAD.git`
  * `git push -u origin master`
* ブランチの切り替えはステータスバーで
  * 新規ブランチも作成可能

[Visual Studio Codeの使い勝手をよくするツール - ＠IT](http://www.atmarkit.co.jp/ait/articles/1509/08/news019.html)

* タスク: コマンドパレットで"task"
* SEARCHバー
  * プロジェクト内で検索
  * Match Case, Whole Match, Regular Expression, その他
* スニペット
  * 作成: [Code]-[基本設定]-[ユーザースニペット]

[Visual Studio Codeの設定「虎の巻」：Python編](http://www.atmarkit.co.jp/ait/articles/1711/24/news034.html)

* Intellisense
* 実行: Python: Run Python File in Terminal → Cmd+Rを割り当ててみた
* デバッグ実行
  * F11(ステップ実行)はMacOSによりデスクトップ表示になっているので変更しておく
* linter
  * pep8をEnableしてみた
  * "python.linting.pep8Enabled": true,
  * "python.linting.pylintEnabled": false
* フォーマッタ
  * "python.formatting.provider": "autopep8"
* オートフォーマット
  * 有効にしてみた
  * "editor.formatOnSave": true,
  * "editor.formatOnType": true
* Jupyter
  * 面白そうだけどまた今度

[VS CodeでPythonするために必要なこと - ＠IT](http://www.atmarkit.co.jp/ait/articles/1805/22/news043.html)

* 仮想環境（よくわかっていない）

[VS CodeでPythonプログラムを快適コーディング！ - ＠IT](http://www.atmarkit.co.jp/ait/articles/1805/29/news031.html)

* けっこうカブってる

[VS CodeでPythonコードのデバッグも楽々！！ - ＠IT](http://www.atmarkit.co.jp/ait/articles/1806/05/news023.html)

* デバッグの構成
  * "stopOnEntry": true
* デバッグコンソール
  * ウォッチ式

[あると便利？　VS Codeで使えるPython関連の拡張機能 - ＠IT](http://www.atmarkit.co.jp/ait/articles/1806/19/news026.html)

* 行末の空白文字を除去（標準の機能）
  * "files.trimTrailingWhitespace": true

## [PCAD] ALDS1_6_A: Counting Sort

いわゆるバケツソート
原理は知ってた

解説はA,Bが1オリジンになってますが
なんかA[0]とかB[0]が使われてないのが気持ち悪いので
0番目から詰めました

```python
def counting_sort(A, k):
    B = [0] * len(A)
    C = [0] * k

    for a in A:
        C[a] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for a in reversed(A):
        B[C[a] - 1] = a
        C[a] -= 1

    return B

def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    print(*counting_sort(A, 10001))

main()
```

最後、Bを作るところはなんで後ろから見てるんだと思いましたが
（実際`reversed`しなくてもソートは成功するし）
そうしないとStableにならないんですね
なるほど

Cをいったん累積にしてからやるのはこれで効率いいのかな
なんか頭いいことしてるような気はするんだけど
普通にやってもいいような気も

ところでpep8でフォーマットするようにしたので実際のソースは
関数と関数の間が２行空くようになりました
どうも間延びしてるように見えて好きになれませんね
慣れの問題かもしれませんが

## [PCAD] ALDS1_5_D: The Number of Inversions

チャレンジ問題

数列AでA[i]>A[j]かつi<jとなるi,jの組の個数を求める
バブルソートの交換回数に等しいんだけどそれだとTLEになるそうな
さてどう考えるのかな

・・・
・・・

わからん！

ソートの章にあるんだからなにかソートするんだろう
普通にソートしてその結果を使うのか、
ソート自体の方法を応用して数えるのか

ソートアルゴリズムはどれを使うんだろう
マージソートかクイックソートかバケツソートか
結果だけ使うならどれでもよさそうだ
O(n^2 )のソートではないんだろうな
nの上限が200000で、バケツソートのときと同じになってるのが気になるけど、
値の上限が10^9 だから少なくともそのままでは使えない

ソートした数列と元の数列を比較したらなにかわかるかと思ったけど
どうもあうまくいかない

・・・

なにはともあれ一度バブルソートでTLEをくらってみるか

```python
def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def count_inversion(A):
    cnt = 0
    for i in range(len(A)):
        for j in reversed(range(i + 1, len(A))):
            if A[j] < A[j - 1]:
                swap(A, j, j - 1)
                cnt += 1
    return cnt

def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    print(count_inversion(A))

main()
```

rangeで1ずつ減らす数列を作ろうとするとわかりづらくなるので
rangeでは増える数列を作っておいてreversedしてみた

そして予定通りTLE
データ数は100000

このソースがなにか参考になるか
どこか変えたらオーダ下がるかな

内側のループでは、ひとつずつ見なくてもそれまでの
結果を使えば速くなるような気もする

あるいは挿入ソート的なやりかただけど二分探索してみるとか
でも挿入するのにO(n)かかるとあんまり変わらないかもしれない

それともぜんぜん違うやり方が必要なのか

## [PCAD] ALDS1_5_D: The Number of Inversions (続き)

> あるいは挿入ソート的なやりかただけど二分探索してみるとか
> でも挿入するのにO(n)かかるとあんまり変わらないかもしれない

やってみた

```python
from bisect import bisect_left

def count_inversion(A):
    cnt = 0
    for i in reversed(range(len(A) - 1)):
        j = bisect_left(A, A[i], i + 1, len(A))
        cnt += j - i - 1
        tmp = A[i]
        del A[i]
        A.insert(j - 1, tmp)
    return cnt

def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    print(count_inversion(A))

main()
```

データ数100000はクリアできたけど200000でTLE
しかもbisect使って
挿入は組み込みだからO(n)ほどの影響を受けなかったのかもしれない
でもこのアプローチはこれくらいまでかなあ

やっぱり挿入ソートベースじゃダメなのか

> それともぜんぜん違うやり方が必要なのか

## [PCAD] ALDS1_5_D: The Number of Inversions (続きの続き)

> やっぱり挿入ソートベースじゃダメなのか

じゃあマージソートかクイックソートかバケツソートか

バケツソートは値が10^9あるからありそうにない
なにか別の値に置き換えるっていう技があるかもしれないけど

バブルソートや挿入ソートと見比べてみると、クイックソートのほうが
その場で入れ替えていく分似てるところがあるような気がする
違うのは、バブルソートや挿入ソートが隣同士で入れ替えているのに対し
クイックソートは離れた要素を入れ替えていること

離れた要素を入れ替えるときは要素間の距離を足せばいいかな？
swapで足せばすぐ試せる

・・・

ダメだった
離れた要素を入れ替えるときは、間に挟まれた要素も結果に影響を与えるのに
そこが考慮できてないし影響を判断するやり方も思いつかない

マージソートかなあ
あんまりできる気はしてないけど

そもそも何を数えればいいのやら
右と左が入れ替わる回数かなあ
違う
入れ替えの距離の合計かなあ
違う

このあたりはコンピュータ使わずひたすらノートに数字を並べたり
入れ替えたりしてるわけですが
対応する数字の間に線を引いていると何やら交点の数が気になってきました
交点の数と、反転数っておんなじなんじゃ？
うんおんなじ
これは考えてみると当然

ソート前の列とソート済みの列を並べて、対応する数字の間に線を引いて、
交点の数を調べれば反転数が求まる
問題は、交点の数を求める方法がわからないってことなわけだが

でもマージソートの各段階で交点の数を求めて、それを合計してやると
全体の反転数になるっぽい
なぜ合計でうまくいくのかはよくわからない

そして、交点の数は、右側の数を取り出すときに左側に残ってる数の数を
足していけばよさそうだってのもわかる

紙の上でいくつか試す
数学的じゃない帰納法によってうまくいきそうな気がしてきたので書いてみる
結局イテレータがじゃまになってきたので素のインデックスを使う
あとはinvという変数に交点の数を累積してるだけ

```python
from math import inf

inv = 0

def merge(A, left, mid, right):
    global inv

    L = A[left:mid]
    L.append(inf)
    R = A[mid:right]
    R.append(inf)
    i = j = 0
    for k in range(left, right):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            inv += len(L) - 1 - i
            A[k] = R[j]
            j += 1

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    merge_sort(A, 0, n)
    print(inv)

main()
```

なんか合わない合わないと思ったらLとRに要素付け足してるの忘れてたりとか
あったけどAC
考え方は合ってたらしい

でも証明してくださいとか言われると困るなー
証明とはいかなくても感覚的にこれは合ってるというところまでも行ってないので
これで漏れなく重複なく数えられてるのかと言うと

このやり方で離れた要素の入れ替えを数えられるなら
クイックソートでも同じ作戦が使えないかな？

ダメか
間に挟まってる数が本来の入れ替えに含まれる場合と含まれない場合があるみたい
それをいちいちチェックするとやっぱりオーダが変わってしまいそう
という観点で見ると、マージソートだと間に挟まってる数が必ず入れ替えに
なる数になっている
というのはあるな
少し確からしさが増した

これくらいで解説を読もう
たぶんマージソートを使うところは合ってると思うので
あとは感覚的に納得できるかどうか

・・・

自分で考えたこと以上の説明はなかった
残念

これがPAIZAの問題だったら完敗
精進せねば

## [PCAD] ALDS1_6_D: Minimum Cost Sort

ALDS1_5_Dが思考★★★、実装★★☆だったのに対し、今度は思考★★★★☆、実装★★☆
思考の星が１個半多い
これはダメかもしれんね

荷物を重さの順にソートするんだけど、要素の交換のときに重さに応じた
コストがかかり、トータルのコストが最小になるようにソートするというもの

* コストは交換する要素間の距離には依存しないので、離れた要素を入れ替えたほうがお得
* 要素数は1000までなのでオーダはそんなに気にしなくてもいいのかもしれない
* 最小値しかもとめられてないので、もしかすると実際のソートの手順は必須ではない

思いつくのはそれくらい
必須ではないと言っても、実際には手順まで求めないとダメな気もする

クイックソートにしてもマージソートにしても、どれを交換するかは
アルゴリズム任せになっているので、交換する要素をどれにするかって
いうのを決めるのは未知の世界

こういう入れ替え方でソートできますけど、こういう入れ替え方でも
できますよ、っていうのはどう考えるのか
普通にソートしてみてからその結果に持っていけるように交換順序を考える、
でいいのかな
そうやったとしてもこれが最小です、って言うのはちょっと難しそうな
オーダあんまり気にしなくても、と言ったって総当たりってわけには
行かないだろうし

紙とペンでやってみた限り、重いものから順に正しい位置へ
入れていくようにするのがいい結果に繋がりそうだ
二つの荷物を入れ替えると両方ちょうどいい場所に来るっていう
ケースは優先的に入れ替えたほうがいいのかな
最初からそうなってれば放置しててもそうなるけど、入れ替えてる
途中でたまたまそういう配置になるっていうこともありそうな

コスト最小が回数最小であるとも限らないし
極端な話、入れ替えてどちらも正しい位置にこないような移動が
最適じゃないとも言い切れない

さてどうしたものか

## [PCAD] ALDS1_6_D: Minimum Cost Sort (続き)

ちょっと時間がない

> 普通にソートしてみてからその結果に持っていけるように交換順序を考える

と

> 重いものから順に正しい位置へ

で１次近似しよう
サンプルデータふたつはこれでも正しい値が出るはず
データがよくない気もするけど

ソートとサーチは素直にライブラリ関数を使った
O(n^2 )

```python
def swap(w, i, j):
    tmp = w[i]
    w[i] = w[j]
    w[j] = tmp

def min_weight(w):
    ws = sorted(w)
    weight = 0
    for i in reversed(range(len(w))):
        j = w.index(ws[i])
        if i != j:
            weight += w[i] + w[j]
            swap(w, i, j)
    return weight

def main():
    n = int(input())
    w = [int(x) for x in input().split()]
    print(min_weight(w))

main()
```

はい3つめのデータでWA
テストデータだとこれが48

```text
4
10 7 8 9
```

上のプログラムだと51
10↔9、9↔8、8↔7という手順

48はどういう手順かな
7↔8、7↔9、7↔10でいいのか
うーん大きな数から正しい位置に、という戦略がそもそもダメってことか

## [PCAD] ALDS1_6_D: Minimum Cost Sort (続きの続き)

総当たりくらいしか思いつかないので総当たりを書いてみた

コストがそれまでの最小コストを上回るか、ソートが成功するまで
あらゆる手を試します
最初の最小コストはそこそこの値をセットしておかないと大変なことになるので
昨日のアルゴリズムで算出した値を使う

```python
from itertools import product
from math import inf
from sys import setrecursionlimit

setrecursionlimit(10000)

ws = []
min_weight = inf

def swap(w, i, j):
    tmp = w[i]
    w[i] = w[j]
    w[j] = tmp


def try_next(w, total, hand):
    global min_weight

    if total > min_weight:
        return

    if w == ws:
        min_weight = min(total, min_weight)
        return

    for i, j in product(range(len(w)), range(len(w))):
        if i >= j:
            continue
        wnew = w[:]
        swap(wnew, i, j)
        hnew = hand[:]
        hnew.append((i, j))
        try_next(wnew, total + w[i] + w[j], hnew)

    return

def first_try(w):
    global ws

    weight = 0
    for i in reversed(range(len(w))):
        j = w.index(ws[i])
        if i != j:
            weight += w[i] + w[j]
            swap(w, i, j)
    return weight

def main():
    global ws, min_weight

    n = int(input())
    w = [int(x) for x in input().split()]
    ws = sorted(w)

    min_weight = first_try(w[:])
    try_next(w, 0, [])
    print(min_weight)

main()
```

今日は6番目のテストまで成功して7番目でTLE
データ数は8個

デバッグのためにそれまでどう入れ替えたか記憶させてたり
安直にリストをコピーしてたりするけど
それくらいの改善では焼け石に水もいいところなのでやらない

## [PCAD] ALDS1_7_A: Rooted Trees

> 難しいと感じたら今は飛ばして、実力をつけてから挑戦してみましょう。

ではお言葉に甘えて
でもこの本でこの先にこの問題が解けるようななにかが出てくるのかなあ？

ふむ
木を作るだけでよさそうだ

でもサンプルデータを見てみるとなんか違和感がある
なんだろう

根から親→子の順に書いてあるんだけど、子の実体が出てくる前に
親が子を知っているからかな
普通だと子が出てきてから子のためのメモリを確保してポインタを
記録すると思うんだけど
こういう場合はどうするのがいいんだろう

出題者の意図はわからないけど、要素数がわかった時点で配列を確保してしまって
あとは添字でポイントするのが楽そうだ
ポイント先も数字で0からn-1って書いてあるし
そうすると入力行に書いてある節点番号が冗長じゃないかな？
いや、順番に出てくるとは書いてないから必要か

あと、親ノードの番号を持つことにする？
この問題としてはそのほうが楽だけど、根から探せないこともなさそう
でも持たせよう
楽しよう

```python
class Node():
    def __init__(self, parent=-1, child=[]):
        self.parent = parent
        self.child = child

def node_depth(u, id):
    if u[id].parent == -1:
        return 0
    else:
        return node_depth(u, u[id].parent) + 1

def node_type(u, id):
    if u[id].parent == -1:
        return "root"
    elif u[id].child == []:
        return "leaf"
    else:
        return "internal node"

def main():
    n = int(input())
    u = [Node() for _ in range(n)]

    for _ in range(n):
        id, _, *child = (int(x) for x in input().split())
        u[id].child = child
        for c in child:
            u[c].parent = id

    for id in range(n):
        print("node {}: parent = {}, depth = {}, {}, {}".
              format(id, u[id].parent,
                     node_depth(u, id), node_type(u, id),
                     u[id].child))

main()
```

ノードを配列で持って添字でポイントする方針だと、`parent`が
直接親ノードを指すわけじゃないから`depth`が`Node`クラス内に
書けないとかあってクラスっぽく書けなくて、構造体と配列、みたいな
感じになった
`Tree`クラスと`Node`クラスを使って・・・ってやろうとするとどうも
うまく書けなくて開き直るまでにけっこう手間取った

解説ではどうなってるだろうか
うん構造からぜんぜん違う
左子右兄弟表現、ってすごい名前だな
leftが長子でright
`car`と`cdr`に似てなくもない

配列を使って添字でポイントするってのは同じだった

書くのは明日やってみよう

## [PCAD] ALDS1_7_A: Rooted Trees (続き)

左子右兄弟表現で
意外と変えずに済んだところも多いかな

```python
class Node():
    NIL = -1

    def __init__(self, parent=NIL, left=NIL, right=NIL, depth=-1):
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth

def read_nodes(T):
    for _ in range(len(T)):
        id, _, *child = [int(x) for x in input().split()]
        for i, c in enumerate(child):
            if i == 0:
                T[id].left = c
            else:
                T[l].right = c
            l = c
            T[c].parent = id

def calc_depth(T):

    def rec(r, p):
        nonlocal T

        T[r].depth = p
        if T[r].right != Node.NIL:
            rec(T[r].right, p)
        if T[r].left != Node.NIL:
            rec(T[r].left, p + 1)

    rec([u.parent for u in T].index(-1), 0)

def node_type(T, id):
    if T[id].parent == Node.NIL:
        return "root"
    elif T[id].left == Node.NIL:
        return "leaf"
    else:
        return "internal node"

def child(T, id):
    c = []
    i = T[id].left
    while i != Node.NIL:
        c.append(i)
        i = T[i].right
    return c

def print_nodes(T):
    for id in range(len(T)):
        print("node {}: parent = {}, depth = {}, {}, {}".
              format(id, T[id].parent, T[id].depth,
                     node_type(T, id), child(T, id)))

def main():
    n = int(input())
    T = [Node() for _ in range(n)]

    read_nodes(T)
    calc_depth(T)
    print_nodes(T)

main()
```

今日はAOJのサイトが使えないみたいなので手元にあったデータだけで
テストしました

## [PCAD] ALDS1_7_B: Binary Tree

今度は二分木
どっちかというと左子右兄弟表現とやらよりこっちのほうがシンプルで
先に出てきそうな気がしますがどうなんでしょう

同じようなことを書くのですいすい書けます

```python
from sys import stdin

class Node():
    NIL = -1

    def __init__(self, p=NIL, l=NIL, r=NIL, d=-1, h=-1):
        self.p = p
        self.l = l
        self.r = r
        self.d = d
        self.h = h

    def __repr__(self):
        return "Node({}, {}, {}, {})".format(self.p, self.l, self.r, self.d)

def root_of(T):
    return [u.p for u in T].index(Node.NIL)

def sibling_of(T, id):
    p = T[T[id].p]
    return p.r if p.l == id else p.l

def degree_of(T, id):
    l = 0 if T[id].l == Node.NIL else 1
    r = 0 if T[id].r == Node.NIL else 1
    return l + r

def calc_depth(T):

    def rec(id, depth):
        nonlocal T

        T[id].d = depth
        if T[id].l != Node.NIL:
            rec(T[id].l, depth + 1)
        if T[id].r != Node.NIL:
            rec(T[id].r, depth + 1)

    rec(root_of(T), 0)

def calc_height(T):

    def rec(id):
        nonlocal T

        l = 0 if T[id].l == Node.NIL else rec(T[id].l) + 1
        r = 0 if T[id].r == Node.NIL else rec(T[id].r) + 1
        T[id].h = max(l, r)
        return T[id].h

    rec(root_of(T))

def type_of(T, id):
    if T[id].p == Node.NIL:
        return "root"
    elif T[id].l == Node.NIL and T[id].r == Node.NIL:
        return "leaf"
    else:
        return "internal node"

def read_nodes(T):
    for line in stdin:
        id, l, r = [int(x) for x in line.split()]
        T[id].l = l
        if l != Node.NIL:
            T[l].p = id
        T[id].r = r
        if r != Node.NIL:
            T[r].p = id

def print_nodes(T):
    for id in range(len(T)):
        print("node {}: ".format(id), end="")
        print("parent = {}, ".format(T[id].p), end="")
        print("sibling = {}, ".format(sibling_of(T, id)), end="")
        print("degree = {}, ".format(degree_of(T, id)), end="")
        print("depth = {}, ".format(T[id].d), end="")
        print("height = {}, ".format(T[id].h), end="")
        print(type_of(T, id))

def main():
    n = int(stdin.readline())
    T = [Node() for _ in range(n)]

    read_nodes(T)
    calc_depth(T)
    calc_height(T)
    print_nodes(T)

main()
```

とそんなふうに考えていた時期が俺にもありました
`read_nodes`で`T`の最後の要素だけなんか意味のわからない値が入って
だいぶ困りました

何も考えずに`T[l].p = id`とか`T[r].p = id`とかやってたせいでした
`l`や`r`が-1のとき、配列の末尾にアクセスしてることに気づいてませんでした
Out of rangeとかでエラーにならないの？とか思ってしまいました
あーなりませんね

`sibling_of`のところ、解説のソースよりも少し単純になってます
これでは不足かなあ？
親の左か右かは確実に自分のはず

## [PCAD] ALDS1_7_C: Tree Walk

今度は二分木を作ったあと、Preorder、Inorder、Postorderで
巡回してみるっていう問題

読み込むところは完全に流用でいいと思うけどあえて１から書き直す
不要な部分もあるし

一度書いたらすぐにもう一度書いてみるっていう勉強法があるらしくて
なんかよさそうな気がするんだけどなかなか実際やってみるとなると
先へ進みたい気持ちが強くてできないのでこういうときだけでも

ノードに親を覚えさせておく必要はあんまりないんだけど
根を探すときに使うので覚えさせておく
探さないと根がわからない、っていうのは普通なのかな
根があってそこにノードを追加していく、っていうのが普通かと思ってたけど

```python
from sys import stdin

class Node():
    NIL = -1

    def __init__(self):
        self.parent = Node.NIL
        self.left = Node.NIL
        self.right = Node.NIL

def read_nodes(T):
    for line in stdin:
        id, left, right = [int(x) for x in line.split()]
        T[id].left = left
        if left != Node.NIL:
            T[left].parent = id
        T[id].right = right
        if right != Node.NIL:
            T[right].parent = id

def root_of(T):
    return [u.parent for u in T].index(Node.NIL)

def walk_preorder(T):

    def rec(id):
        nonlocal T

        if id == Node.NIL:
            return
        print("", id, end="")
        rec(T[id].left)
        rec(T[id].right)

    print("Preorder")
    rec(root_of(T))
    print()

def walk_inorder(T):

    def rec(id):
        nonlocal T

        if id == Node.NIL:
            return
        rec(T[id].left)
        print("", id, end="")
        rec(T[id].right)

    print("Inorder")
    rec(root_of(T))
    print()

def walk_postorder(T):

    def rec(id):
        nonlocal T

        if id == Node.NIL:
            return
        rec(T[id].left)
        rec(T[id].right)
        print("", id, end="")

    print("Postorder")
    rec(root_of(T))
    print()

def main():
    n = int(stdin.readline())
    T = [Node() for _ in range(n)]

    read_nodes(T)
    walk_preorder(T)
    walk_inorder(T)
    walk_postorder(T)

main()
```

`walk_preorder`、`walk_inorder`、`walk_postorder`と
そっくりな関数を３つ書いてしまったので、まとめられる書き方がないか気になる
`rec`をまるごと渡す、だとほとんど変わらないし・・・

## [PCAD] ALDS1_7_D: Reconstruction of the Tree

チャレンジ問題
二分木をpreorderで巡回した結果とinorderので巡回した結果を入力として受け取り、
その二分木をpostorderで巡回したときの結果を出力せよ、というもの
見るからにパズルチックで問題のとおりにコード書けば解けるってものではなさそう

どこから手を付けていいかもわからない
なにかやり方があって一発で求められるのか、
いろいろ可能性があって探索していくのか

preorderとinorderだけで木が一意に決まるものなのか
一意には決まらないけどpostorderの結果はひとつしかないとか
（あまりありそうな気はしないけど）

節点の数が100以下ってことは探索、しかもけっこうオーダの高い探索なのかな？

さっぱりわからんのでn=1から木を具体的に書いてみる
こういうのは紙だな

n=1のときは木は1通り
n=2のときは4通り
n=3のときは36通り(12個めまで書いて挫折
総当たりはとんでもないことになりそうだ
ありうる木の可能性はこうなると思う

```text
def sort_of_trees(n):
    s = 1
    for k in range(n):
        s *= (n - k) * (2 * k - (k - 1))
    return s

for n in range(1, 10):
    print(n, ":", sort_of_trees(n))

1 : 1
2 : 4
3 : 36
4 : 576
5 : 14400
6 : 518400
7 : 25401600
8 : 1625702400
9 : 131681894400
```

preorderが条件に合う木の中でinorderも条件に合うものを探す、とかじゃないと無理

全部のpreordeを満たす木を造って調べる？
どうやって全種類作ればいい？

preorderの最初の要素を根にして
そのあとpreorderの順に全部左へ追加していくとpreorderを満たす木になるので
そのあとpreorderを崩さないようにちょっとずつ変形しながら
inorderを満たす木を探す、みたいなやり方かなー
うまく全部調べられるやり方あるかなあ

preorderを満たす木は何通りあるんだろう
こっちは式は立てられなかったけど数えてみると

n=1 : 1通り
n=2 : 2通り
n=3 : 5通り
n=4 : 14通り
n=5 : 41通り(たぶん)

でやっぱり大変なことになりそう
規則性は見えてないんだけど3倍して1をひくと次の答えになるのは偶然かなあ

ということはもっと狙いを絞ってつくらないといけないのか
わかりやすいところではinorderの最初の要素が左端に来るとかあるので
なにかやれそうではある
具体的にはわからない

これはスルーか

## [PCAD] ALDS1_8_A: Binary Search Tree I

二分探索木に要素を挿入します
コードは問題に書いてあるものに従います

親を覚えるようにしてるってことはどこかで使う予定ってことだろうなあ
挿入・検索では使わなさそうだから削除で使うかな？

```python
from sys import stdin

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, z):

        y = None
        x = self.root

        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def print_inorder(self):
        def rec(node):
            if not node:
                return
            else:
                rec(node.left)
                print("", node.key, end="")
                rec(node.right)

        rec(self.root)
        print()

    def print_preorder(self):

        def rec(node):
            if not node:
                return
            else:
                print("", node.key, end="")
                rec(node.left)
                rec(node.right)

        rec(self.root)
        print()

class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def main():
    _ = int(stdin.readline())
    T = Tree()

    for line in stdin:
        cmd, *args = line.split()
        if cmd == "insert":
            T.insert(Node(int(args[0])))
        elif cmd == "print":
            T.print_inorder()
            T.print_preorder()

main()
```

再帰でやるんじゃないんだな
ソートされたデータを500000も与えられたら再帰じゃ耐えられないか

ACいただきました

命令の数は500000を超えない、って書いてあるのに
ｍ=500001のテストがあるっていうのはどういうことかな
printも命令だよね

## [PCAD] ALDS1_8_A: Binary Search Tree I (続き)

挿入のとき、最初の要素だけ特別扱いしてるのが気になった
番兵使えないかな？

```python
from sys import maxsize

class Tree():
    def __init__(self):
        self.root = Node(maxsize)

    def insert(self, z):

        x = self.root

        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if z.key < y.key:
            y.left = z
        else:
            y.right = z

    def print_inorder(self):

        :

        rec(self.root.left)
        print()

    def print_preorder(self):

        :

        rec(self.root.left)
        print()
```

できてる模様
最初にひとつ、キーを最大にしたノードを置いておいて、
そのノードの左からが本来の木という形

少しだけ短くなった
`self.root.left`から見始めるのがあまり美しくないので
`self.root`はなにかちがう名前にして
`self.root.left`を`self.root`という名前にするといいかもしれない

ついでに

> 再帰でやるんじゃないんだな

そこだけ半端に再帰でやってみた
もとのソースからの差異

```python
    def insert(self, z):

        def rec(node):
            nonlocal z

            if node is None:
                return z
            elif z.key < node.key:
                return Node(node.key,
                            rec(node.left),
                            node.right)
            else:
                return Node(node.key,
                            node.left,
                            rec(node.right))

        self.root = rec(self.root)

class Node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
```

このやりかたでいちいち結果を`self.root`に覚えてるのは一貫性がないかな
`Node`に`parent`を覚えさせるところは手を抜いた
引数にして渡すだけでできると思うけど

> ソートされたデータを500000も与えられたら再帰じゃ耐えられないか

ソートはされてなかったけど当然TLE

## [PCAD] ALDS1_8_A: Binary Search Tree I (続きの続き)

もっとがんばって関数型っぽい雰囲気を目指すとどうなるのか
といっても入出力ありで関数型っぽく書くっていうのがどういうことなのか
よくわかっていなかったりする
Scheme手習いとかでは値しか出力するものがなかったからなあ

とりあえず入出力はできるだけ狭い範囲に閉じ込めた
命令を順次処理しながら木を作っていくところで`reduce`を使ったのは
どうなんだろう
若干無理をしてる気がしないでもないけど

```python
from sys import stdin
from functools import reduce

class Node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def insert(tree, z):
    if tree is None:
        return z
    elif z.key < tree.key:
        return Node(tree.key,
                    insert(tree.left, z),
                    tree.right)
    else:
        return Node(tree.key,
                    tree.left,
                    insert(tree.right, z))

def flatten_inorder(tree):
    if tree is None:
        return []
    else:
        return flatten_inorder(tree.left) + \
            [tree.key] + \
            flatten_inorder(tree.right)

def flatten_preorder(tree):
    if tree is None:
        return []
    else:
        return [tree.key] + \
            flatten_preorder(tree.left) + \
            flatten_preorder(tree.right)

def process_command(tree, command):
    if command[0] == "insert":
        return insert(tree, Node(int(command[1])))
    elif command[0] == "print":
        print("", *flatten_inorder(tree))
        print("", *flatten_preorder(tree))
        return tree

def main():
    _ = int(stdin.readline())

    reduce(process_command,
           [line.split() for line in stdin],
           None)

main()
```

とうぜんデータ数が多いとTLEです

## [PCAD] ALDS1_8_B: Binary Search Tree II

前回のプログラムにfind命令を追加します
どれに追加しようかな

まあ普通に作ったやつから
差分のみ

```python
class Tree():

    :

    def find(self, key):
        x = self.root
        while x != None:
            if key == x.key:
                return True
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return False

def main():
    _ = int(stdin.readline())
    T = Tree()

    for line in stdin:
        cmd, *args = line.split()
        if cmd == "insert":
            T.insert(Node(int(args[0])))
        elif cmd == "find":
            print("yes" if T.find(int(args[0])) else "no")
        elif cmd == "print":
            T.print_inorder()
            T.print_preorder()
```

関数型をめざしたやつベースで
同じく差分のみ

```python
def find(tree, key):
    if tree is None:
        return False
    elif key < tree.key:
        return find(tree.left, key)
    elif key == tree.key:
        return True
    else:
        return find(tree.right, key)

def process_command(tree, command):
    if command[0] == "insert":
        return insert(tree, Node(int(command[1])))
    elif command[0] == "find":
        print("yes" if find(tree, int(command[1])) else "no")
        return tree
    elif command[0] == "print":
        print("", *flatten_inorder(tree))
        print("", *flatten_preorder(tree))
        return tree
```

ゲーム作るときなんかは状態をreduceしながら進めるのかな、とふと思った
