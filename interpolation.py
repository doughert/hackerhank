import datetime

name = 'Fred'
age = 50
anniversary = datetime.date(1991, 10, 12)
print(f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.')