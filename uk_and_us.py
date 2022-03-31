# https://www.hackerrank.com/challenges/uk-and-us/problem

import re

sentences = ''
for _ in range(int(input())):
    sentences += input() + ' '
for _ in range(int(input())):
    test = input()
    print(len(re.findall(rf'\b{test[:len(test)-2]}(se|ze)\b', sentences)))
