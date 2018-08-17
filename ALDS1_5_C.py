#! /usr/local/bin/python3
# coding: utf-8

from math import pi, sin, cos

class Point2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point2D(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point2D(self.x - p.x, self.y - p.y)

    def __rmul__(self, a):
        if isinstance(a, float):
            return Point2D(self.x * a, self.y * a)
        else:
            return NotImplemented
    
    def rotate(self, theta):
        return Point2D(self.x * cos(theta) - self.y * sin(theta),
                       self.x * sin(theta) + self.y * cos(theta))

    def __str__(self):
        return "{} {}".format(self.x, self.y)

def koch(p1, p2, level):
    if level == 0:
        return
    l = p2 - p1
    s = p1 + (1/3) * l
    t = p1 + (2/3) * l
    u = s + (1/3) * l.rotate(pi/3)
    koch(p1, s, level - 1)
    print(s)
    koch(s, u, level - 1)
    print(u)
    koch(u, t, level - 1)
    print(t)
    koch(t, p2, level - 1)

def main():
    n = int(input())
    print(Point2D(0.0, 0.0))
    koch(Point2D(0.0, 0.0), Point2D(100.0, 0.0), n)
    print(Point2D(100.0, 0.0))

main()