# https://www.hackerrank.com/challenges/detect-html-tags/problem
import re

n = int(input())

result = []

for _ in range(n):
    line = input()
    matches = re.findall(r'< *(\w+).*?>', line)
    for match in matches:
        result.append(match)
result = sorted(set(result))
print(';'.join(result))
