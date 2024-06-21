"""Files"""


try:
    with open('D:\\students.txt', 'x', encoding='utf-8') as file:
        file.write("Sergei, group 2, math = 5, chemistry = 5, physics = 5\n")
        file.write("Oleg, group 3, math = 5, chemistry = 5, physics = 5\n")
        file.write("Anya, group 2, math = 3, chemistry = 3, physics = 4\n")
        file.write("Ivan, group 1, math = 5, chemistry = 4, physics = 3\n")
        file.write("Andrei, group 1, math = 5, chemistry = 5, physics = 3\n")
        file.write("Nastya, group 3, math = 3, chemistry = 3, physics = 5\n")

except FileExistsError:
    print("File 'students.txt' already exists.")


with open('D:\\students.txt', 'r', encoding='utf-8') as myfile:
    lines = myfile.readlines()

number_of_students = len(lines)
group_1_students_number = 0
group1_assessments = []
group1_average_rating = 0.0
group_2_students_number = 0
group2_assessments = []
group2_average_rating = 0.0
group_3_students_number = 0
group3_assessments = []
group3_average_rating = 0.0

for i, line in enumerate(lines):
    if "group 1" in line:
        group_1_students_number += 1
        parts = line.split(', ')
        for part in parts:
            if '=' in part:
                number = int(part.split('=')[1])
                group1_assessments.append(number)
                group1_average_rating = (sum(group1_assessments)
                                         / len(group1_assessments))

    if "group 2" in line:
        group_2_students_number += 1
        parts = line.split(', ')
        for part in parts:
            if '=' in part:
                number = int(part.split('=')[1])
                group2_assessments.append(number)
                group2_average_rating = (sum(group2_assessments)
                                         / len(group2_assessments))

    if "group 3" in line:
        group_3_students_number += 1
        parts = line.split(', ')
        for part in parts:
            if '=' in part:
                number = int(part.split('=')[1])
                group3_assessments.append(number)
                group3_average_rating = (sum(group3_assessments)
                                         / len(group3_assessments))

with open('D:\\students.txt', 'a', encoding='utf-8') as file:
    file.write(f"Number of students: {number_of_students}\n")
    file.write(f"Group 1 students number: {group_1_students_number}\n")
    file.write(f"Group 1 average rating: {group1_average_rating:.2f}\n")
    file.write(f"Group 2 students number: {group_2_students_number}\n")
    file.write(f"Group 2 average rating: {group2_average_rating:.2f}\n")
    file.write(f"Group 3 students number: {group_3_students_number}\n")
    file.write(f"Group 3 average rating: {group3_average_rating:.2f}")

with open('D:\\students.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
