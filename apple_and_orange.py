#!/bin/python3

import math
import os
import random
import re
import sys


def count_apples_and_oranges(house_start_position, house_end_position, apple_tree_position, orange_tree_position, apples_distances, oranges_distances):
    apple_count = 0
    orange_count = 0

    for distance in apples_distances:
        if house_start_position <= (distance + apple_tree_position) <= house_end_position:
            apple_count += 1

    for distance in oranges_distances:
        if house_start_position <= (distance + orange_tree_position) <= house_end_position:
            orange_count += 1

    print(f'{apple_count}\n{orange_count}')


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    count_apples_and_oranges(s, t, a, b, apples, oranges)
