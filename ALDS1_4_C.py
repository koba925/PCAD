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
    
    def print(self):
        print(self.size)
        print(self.table)

def test():
    h = HashTable(5); h.print()
    assert(not h.find("A"))
    assert(not h.find("B"))
    assert(not h.find("C"))

    h.insert("A"); h.print()
    assert(h.find("A"))
    assert(not h.find("B"))
    assert(not h.find("C"))

    h.insert("A"); h.print()
    assert(h.find("A"))
    assert(not h.find("B"))
    assert(not h.find("C"))

    h.insert("B"); h.print()
    assert(h.find("A"))
    assert(h.find("B"))
    assert(not h.find("C"))

    h.insert("C"); h.print()
    assert(h.find("A"))
    assert(h.find("B"))
    assert(h.find("C"))

# test()
# exit()

from sys import stdin

def main():
    h = HashTable(100000)
    _ = int(input())
    for l in stdin:
        #print(l)
        cmd, param = l.split()
        if cmd == "insert":
            h.insert(param)
        elif h.find(param):
            print("yes")
        else:
            print("no")
            
main()
