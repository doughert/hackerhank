# https://www.hackerrank.com/challenges/find-substring/problem

import re

n = int(input())
sentence = ''
for _ in range(n):
    sentence += input() + ' '
q = int(input())
for _ in range(q):
    s = input()
    print(len(re.findall(rf'\w{s}\w', sentence)))
