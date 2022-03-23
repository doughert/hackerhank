# https://www.hackerrank.com/challenges/matching-x-repetitions/problem

import re

regex_pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'

print(str(bool(re.search(regex_pattern, input()))).lower())
