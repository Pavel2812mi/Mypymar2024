"""files"""


import os

file_path = "students.txt"

if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(
            "Sergei, group 2, math = 5, chemistry = 5, physics = 5\n"
            "Oleg, group 3, math = 5, chemistry = 5, physics = 5\n"
            "Anya, group 2, math = 3, chemistry = 3, physics = 4\n"
            "Ivan, group 1, math = 5, chemistry = 4, physics = 3\n"
            "Andrei, group 1, math = 5, chemistry = 5, physics = 3\n"
            "Nastya, group 3, math = 3, chemistry = 3, physics = 5\n"
        )

groups: dict[int, list[int]] = {1: [], 2: [], 3: []}
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    parts = line.split(", ")
    current_group = int(parts[1].split()[1])
    grades = [int(part.split("=")[1]) for part in parts if "=" in part]
    groups[current_group].extend(grades)

with open(file_path, "a", encoding="utf-8") as file:
    file.write(f"Number of students: {len(lines)}\n")
    for group, grades_list in groups.items():
        if grades_list:
            average_rating = sum(grades_list) / len(grades_list)
            file.write(
                f"Group {group} students number: {len(grades_list) // 3}\n"
                f"Group {group} average rating: {average_rating:.2f}\n"
            )

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
