# https://www.hackerrank.com/challenges/detect-the-email-addresses/problem
import re

n = int(input())

result = []

for _ in range(n):
    line = input()
    matches = re.findall(r'\w+(?:\.\w+)?@\w+(?:\.\w+)+', line)
    for match in matches:
        result.append(match)
result = sorted(set(result))
print(';'.join(result))
