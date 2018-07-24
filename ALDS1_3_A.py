#! /usr/local/bin/python3
# coding: utf-8

sp = 0
stack = [0] * 100

def stack_push(v):
    global sp, stack
    # print("push: sp =", sp, ", v =", v)
    stack[sp] = v
    sp += 1

def stack_pop():
    global sp, stack
    sp -= 1
    # print("pop: sp =", sp, ", v =", stack[sp])
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
