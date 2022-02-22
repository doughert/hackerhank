import re

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        command = input()
        match = re.match(r'([a-z]+) ?(\d+)? ?(\d+)?', command)
        if match.group(1) == 'insert':
            index = int(match.group(2))
            value = int(match.group(3))
            if index >= len(l):
                l.append(value)
            else:
                l = l[:index] + [value] + l[index:]
        elif match.group(1) == 'print':
            print(l)
        elif match.group(1) == 'remove':
            l.remove(int(match.group(2)))
        elif match.group(1) == 'append':
            l.append(int(match.group(2)))
        elif match.group(1) == 'sort':
            l.sort()
        elif match.group(1) == 'pop':
            l.pop()
        elif match.group(1) == 'reverse':
            l.reverse()