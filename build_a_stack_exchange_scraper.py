# https://www.hackerrank.com/challenges/stack-exchange-scraper/problem

import re
import sys

lines = sys.stdin.read()
matches = re.findall(r'(?ms)<a href=\"/questions/(\d+)/.*?\" class=\"question-hyperlink\">(.*?)</a>.*?<span title=\".*?\" class=\"relativetime\">(.*?)</span>', lines)
for match in matches:
    print(';'.join(match))
