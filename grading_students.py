#!/bin/python3

import os


def grading_students(grades):

    result = []

    for grade in grades:
        rounding_number = -1 * ((grade % 5) - 5)

        if grade < 38 or grade % 5 == 0 or rounding_number >= 3:
            result.append(grade)
        else:
            result.append(grade + rounding_number)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = grading_students(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
