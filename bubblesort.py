import random

list_to_sort = [random.randint(0, 100) for x in range(0, 10)]
print(list_to_sort)
for j in range(0, len(list_to_sort)):
    for i in range(0, len(list_to_sort) - j - 1):
        if list_to_sort[i] > list_to_sort[i + 1]:
            temp = list_to_sort[i]
            list_to_sort[i] = list_to_sort[i + 1]
            list_to_sort[i + 1] = temp

print(list_to_sort)