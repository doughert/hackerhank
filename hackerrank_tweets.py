# https://www.hackerrank.com/challenges/hackerrank-tweets/problem

import re

n = int(input())
r = 0
for _ in range(n):
    tweet = input()
    r += len(re.findall(r'(?i)hackerrank', tweet))
print(r)