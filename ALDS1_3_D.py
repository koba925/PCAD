#! /usr/local/bin/python3
# coding: utf-8

from operator import add

def shape_to_slope(ch):
    if ch == "\\":
        return -1
    elif ch == "_":
        return 0
    else:
        return 1

def land(height, h, x, delta):
    while x in range(len(height)):
        if height[x] >= h:
            return True
        x += delta
    return False

def depth_at_x(height, x, max_height, min_height):
    for h in reversed(range(height[x], max_height + 1)):
        if land(height, h, x, -1) and land(height, h, x, 1):
            return h - height[x]
    return 0

def main():
    shape = [ch for ch in input()]
    slope = [shape_to_slope(ch) for ch in shape]

    max_height = min_height = 0
    height = [0]
    for sl in slope:
        height.append(height[-1] + sl)
        max_height = max(height[-1], max_height)
        min_height = min(height[-1], min_height)

    prev_depth = 0
    current_area = 0
    pool_area = []
 
    for x in range(1, len(height)):
        depth = depth_at_x(height, x, max_height, min_height)
        current_area += depth
        if prev_depth > 0 and depth == 0:
            pool_area.append(current_area)
            current_area = 0
        prev_depth = depth
    
    print(sum(pool_area))
    print(len(pool_area), *pool_area)

main()