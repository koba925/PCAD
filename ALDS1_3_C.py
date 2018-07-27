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