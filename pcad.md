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
