from storage import save_data, load_data

# students = [
#   {"name": "bob", "level": 4},
#   {"name": "steve", "level": 4},

# ]

# save_data("students.json", students)

loaded_students = load_data("students.json")
print(loaded_students)
# student_name = input("Student name: ")
# score = int(input("Score: "))
# message = helpers.greet_student(student_name)

# print(helpers.format_score(student_name, score))
# print(message)

