#! /usr/local/bin/python3
# coding: utf-8

from math import pi
from cmath import rect

def print_xy(z):
    print(z.real, z.imag)

def koch(p1, p2, level):
    if level == 0:
        return
    l = p2 - p1
    s = p1 + (1/3) * l
    t = p1 + (2/3) * l
    u = s + (1/3) * l * rect(1, pi/3)
    koch(p1, s, level - 1)
    print_xy(s)
    koch(s, u, level - 1)
    print_xy(u)
    koch(u, t, level - 1)
    print_xy(t)
    koch(t, p2, level - 1)

def main():
    n = int(input())
    print_xy(0+0j)
    koch(0+0j, 100+0j, n)
    print_xy(100+0j)

main()