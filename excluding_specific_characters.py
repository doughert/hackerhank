import re

Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\r\n\t\f ][^AEIOU][^.,]$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
