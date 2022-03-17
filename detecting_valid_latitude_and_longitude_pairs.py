# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem

import re

n = int(input())
for i in range(n):
    coordinate = input()
    if re.match(r'^\([+-]?(90(\.[0]+)?|[1-8]\d(\.\d+)?|[1-9](\.\d+)?), [+-]?(180(\.[0]+)?|1[0-7]\d(\.\d+)?|[1-9]\d(\.\d+)?|[1-9](\.\d+)?)\)$', coordinate):
        print('Valid')
    else:
        print('Invalid')
