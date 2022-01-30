#!/bin/python3
import os


def time_conversion(s):
    am_pm = s[-2:]
    hour = s[:2]

    if am_pm == 'AM' and hour == '12':
        hour = '00'
    elif am_pm == 'PM' and hour != '12':
        hour = str(int(hour) + 12)

    return hour + s[2:8]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion(s)

    f.write(result + '\n')

    f.close()




