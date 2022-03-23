# https://www.hackerrank.com/challenges/detect-html-links/problem

import re

n = int(input())

for _ in range(n):
    line = input()
    matches = re.findall(r'<a href=\"(.*?)\".*?>(?:<.*?>)*(.*?)<', line)
    if bool(matches):
        for match in matches:
            print(f'{match[0].strip()},{match[1].strip()}')
