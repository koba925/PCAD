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
