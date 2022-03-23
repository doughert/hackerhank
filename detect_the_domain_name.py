# https://www.hackerrank.com/challenges/detect-the-domain-name/problem
import re

n = int(input())

result = []

for _ in range(n):
    line = input()
    matches = re.findall(r'(?:https?://)(?:www.|ww2.)?([a-z0-9-]+(?:\.[a-z0-9-]+)+)', line)
    for match in matches:
        result.append(match)
result = sorted(set(result))
print(';'.join(result))
