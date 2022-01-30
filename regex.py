import re

Regex_Pattern = r'/hackerrank'	# Do not delete 'r'.

print(bool(re.match(Regex_Pattern,
               'https://www.hackerrank.com/challenges/matching-specific-string/problem')))