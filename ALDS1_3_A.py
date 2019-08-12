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
