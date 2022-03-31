# https://www.hackerrank.com/challenges/uk-and-us-2/problem

import re

sentences = ''
for _ in range(int(input())):
    sentences += input() + ' '
for _ in range(int(input())):
    word = input()
    word = re.sub(r'our','ou?r', word)
    print(len(re.findall(rf'\b{word}\b', sentences)))
