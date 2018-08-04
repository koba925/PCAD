#! /usr/local/bin/python3
# coding: utf-8

from collections import deque

class Stack():

    def __init__(self):
        self.s = deque()

    def size(self):
        return len(self.s)
    
    def top(self):
        return self.s[-1]

    def push(self, x):
        self.s.append(x)
    
    def pop(self):
        return self.s.pop()
    
    def empty(self):
        return len(self.s) == 0

def test_stack():
    stack = Stack()
    assert stack.empty()
    assert stack.size() == 0

    stack.push(10)
    assert not stack.empty()
    assert stack.size() == 1
    assert stack.top() == 10

    stack.push(20)
    assert not stack.empty()
    assert stack.size() == 2
    assert stack.top() == 20

    v = stack.pop()
    assert v == 20
    assert not stack.empty()
    assert stack.size() == 1
    assert stack.top() == 10

    v = stack.pop()
    assert v == 10
    assert stack.empty()
    assert stack.size() == 0
    assert stack.empty()

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

    def print(self):
        print(self.q)

def test_queue():
    queue = Queue()
    # queue.print()
    assert queue.empty()
    assert queue.size() == 0
    
    queue.push(10)
    # queue.print()
    assert not queue.empty()
    assert queue.size() == 1
    assert queue.front() == 10

    queue.push(20)
    # queue.print()
    assert not queue.empty()
    assert queue.size() == 2
    assert queue.front() == 10

    v = queue.pop()
    # queue.print()
    assert v == 10
    assert not queue.empty()
    assert queue.size() == 1
    assert queue.front() == 20

    v = queue.pop()
    # queue.print()
    assert v == 20
    assert queue.empty()
    assert queue.size() == 0
    assert queue.empty()

class Vector():
    def __init__(self):
        self.v = []
    
    def __getitem__(self, i):
        return self.v[i]
    
    def __setitem__(self, i, val):
        self.v[i] = val

    def size(self):
        return len(self.v)
    
    def push_back(self, x):
        self.v.append(x)
    
    def pop_back(self):
        return self.v.pop()
    
    def __iter__(self):
        return iter(self.v)

    # pythonでは対応するものがない？
    # def end(self):
    
    # C++のvectorではイテレータで位置を指定するのでちょっと違う
    def insert(self, p, x):
        self.v.insert(p, x)

    # 同上
    def erase(self, p):
        del self.v[p]

    def clear(self):
        self.v.clear()

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

def test_vector():
    vec = Vector()
    assert vec.size() == 0

    vec.push_back(10)
    assert vec.size() == 1
    assert vec[0] == 10
    
    vec.push_back(20)
    assert vec.size() == 2
    assert vec[0] == 10
    assert vec[1] == 20

    vec.pop_back()
    assert vec.size() == 1
    assert vec[0] == 10

    vec.push_back(20)
    vec.push_back(30)
    for i, n in enumerate(vec):
        assert i * 10 + 10 == n

    vec.insert(0, 0)
    vec.insert(2, 15)
    vec.insert(-1, 25)
    assert vec.v == [0, 10, 15, 20, 25, 30]

    vec.erase(2)
    vec.erase(3)
    assert vec.v == [0, 10, 20, 30]

    vec[-1] = 40
    assert vec.v == [0, 10, 20, 40]

    vec.clear()
    assert vec.size() == 0

def test_list():
    l = List()
    assert l.size() == 0

    l.push_front(10)
    assert l.size() == 1
    assert list(l) == [10]

    l.push_front(20)
    assert l.size() == 2
    assert list(l) == [20, 10]

    l.push_back(30)
    assert l.size() == 3
    assert list(l) == [20, 10, 30]

    l.insert(2, 40)
    assert l.size() == 4
    assert list(l) == [20, 10, 40, 30]

    l.remove(10)
    assert l.size() == 3
    assert list(l) == [20, 40, 30]

    assert l.pop_back() == 30
    assert list(l) == [20, 40]

    assert l.pop_front() == 20
    assert list(l) == [40]

    l.clear()
    assert l.size() == 0

test_stack()
test_queue()
test_vector()
test_list()
