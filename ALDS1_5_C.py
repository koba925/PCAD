#! /usr/local/bin/python3
# coding: utf-8

from math import pi, sin, cos

class Point2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, p):
        return Point2D(self.x + p.x, self.y + p.y)

    def sub(self, p):
        return Point2D(self.x - p.x, self.y - p.y)

    def rotate(self, theta):
        return Point2D(self.x * cos(theta) - self.y * sin(theta),
                       self.x * sin(theta) + self.y * cos(theta))

    def scale(self, a):
        return Point2D(self.x * a, self.y * a)

    def __str__(self):
        return "{} {}".format(self.x, self.y)

def koch(p1, p2, level):
    if level == 0:
        return
    l = p2.sub(p1)
    s = p1.add(l.scale(1/3))
    t = p1.add(l.scale(2/3))
    u = s.add(l.scale(1/3).rotate(pi/3))
    koch(p1, s, level - 1)
    koch(s, u, level - 1)
    koch(u, t, level - 1)
    koch(t, p2, level - 1)
    if level == 1:
        print(p1)
        print(s)
        print(u)
        print(t)

def main():
    n = int(input())
    koch(Point2D(0.0, 0.0), Point2D(100.0, 0.0), n)
    print(Point2D(100.0, 0.0))

main()
