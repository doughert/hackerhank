# https://www.hackerrank.com/challenges/alien-username/problem

import re

n = int(input())
for _ in range(n):
    name = input()
    if bool(re.match(r'^[_.][0-9]+[a-zA-Z]*_?$', name)):
        print('VALID')
    else:
        print('INVALID')
