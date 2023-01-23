records = int(input())
students_and_grades_list = {}

for i in range(records):
    name, grade = input().split()
    if name not in students_and_grades_list.keys():
        students_and_grades_list[name] = []
    students_and_grades_list[name].append(float(grade))

for k, v in students_and_grades_list.items():
    avg = sum(v) / len(v)
    grades_str = ' '.join([f'{x:.2f}' for x in v])
    print(f"{k} -> {grades_str} (avg: {avg:.2f})", sep=' ')



# n = int(input())
# students_data = {}
#
# for _ in range(n):
#     student_name, grade = input().split(' ')
#     if student_name not in students_data:
#         students_data[student_name] = []
#
#     students_data[student_name].append(float(grade))
#
# for student, grades in students_data.items():
#     print(grades)
#     convert_grades_to_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
#     average_grade = sum(grades) / len(grades)
#     print(f'{student} -> {convert_grades_to_string} (avg: {average_grade:.2f})')
