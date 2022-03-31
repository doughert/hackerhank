# https://www.hackerrank.com/challenges/split-number/problem

import re

for _ in range(int(input())):
    match = re.match(r'^(\d{1,3})[ -](\d{1,3})[ -](\d{4,10})$', input())
    print(f'CountryCode={match.group(1)},LocalAreaCode={match.group(2)},Number={match.group(3)}')
