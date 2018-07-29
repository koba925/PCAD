#! /usr/local/bin/python3
# coding: utf-8

class Stack():

    def __init__(self):
        self.s = []

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

test_stack()
