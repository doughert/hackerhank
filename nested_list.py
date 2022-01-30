if __name__ == '__main__':
    
    records = [[input(), float(input())] for _ in range(int(input()))]
    grades = set()
    for record in records:
        grades.add(record[1])
    grades.remove(min(grades))
    second_lowest_grade = min(grades)
    students = []
    for record in records:
        if record[1] == second_lowest_grade:
            students.append(record[0])
    students = sorted(students)
    for student in students:
        print(student)
