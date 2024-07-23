"""files"""


import os

file_path = "../../students.txt"


def read_student_data(file_path_local):
    """Reads student data from a file and groups it into groups."""
    groups = {1: [], 2: [], 3: []}
    with open(file_path_local, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split(", ")
            current_group = int(parts[1].split()[1])
            grades = [int(part.split("=")[1]) for part in parts if "=" in part]
            groups[current_group].extend(grades)
    return groups


def calculate_and_write_statistics(file_path_local, groups):
    """Calculates the average score for each group
    and writes statistics to a file."""
    with open(file_path_local, "a", encoding="utf-8") as file:
        file.write(f"Number of students:"
                   f" {sum(len(grades) // 3 for grades in groups.values())}\n")
        for group, grades_list in groups.items():
            if grades_list:
                average_rating = sum(grades_list) / len(grades_list)
                file.write(
                    f"Group {group} students number: {len(grades_list) // 3}\n"
                    f"Group {group} average rating: {average_rating:.2f}\n"
                )


def main():
    """The main function that controls program execution."""
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
    groups = read_student_data(file_path)
    calculate_and_write_statistics(file_path, groups)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    main()
