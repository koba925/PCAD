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
