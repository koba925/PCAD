#! /usr/local/bin/python3
# coding: utf-8

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

    def print(self):
        print(self.n, self.top, self.last, self.q)

n, q = [int(x) for x in input().split()]

proc = Queue(n)

for i in range(n):
    name, ptime = input().split()
    proc.push((name, int(ptime)))
# proc.print()

time = 0
while not proc.is_empty():
    name, ptime = proc.pop()
    time += min(q, ptime)
    ptime -= min(q, ptime)
    if ptime <= 0:
        print(name, time)
    else:
        proc.push((name, ptime))
    # proc.print()

exit()

q = Queue(3)

q.push(1)
q.print()
q.push(2)
q.print()
print(q.pop())
print(q.pop())
q.push(3)
q.print()
q.push(4)
q.print()
print(q.pop())
print(q.pop())
