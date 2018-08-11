#! /usr/local/bin/python3
# coding: utf-8

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

    def keys(self, str):
        k = self.key(str)
        return str, k, self.h1(k), self.h2(k)

    def items(self):
        return [x for x in self.table if x]

from sys import stdin

def main():
    h = HashTable()
    _ = int(input())
    for l in stdin:
        #print(l)
        cmd, param = l.split()
        if cmd == "insert":
            h.insert(param)
            # print(h.items())
        elif h.find(param):
            print("yes")
        else:
            print("no")
            
main()
