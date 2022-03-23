# https://www.hackerrank.com/challenges/ip-address-validation/problem

import re

n = int(input())
for _ in range(n):
    ip_test = input().strip()

    if bool(re.match(r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d).(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d).(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d).(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$', ip_test)):
        print('IPv4')
    elif bool(re.match(r'^[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}$', ip_test)):
        print('IPv6')
    else:
        print('Neither')
