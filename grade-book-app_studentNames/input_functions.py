#!/usr/bin/python3
def add_student(gradebook):
    student_id = int(input("Enter student ID: "))
    email = input("Enter student email: ")
    names = input("Enter student names: ")
    gradebook.add_student(student_id, email, names)

def add_course(gradebook):
    course_id = int(input("Enter course ID: "))
    name = input("Enter course name: ")
    trimester = input("Enter course trimester: ")
    credits = int(input("Enter course credits: "))
    gradebook.add_course(course_id, name, trimester, credits)

def register_student_for_course(gradebook):
    gradebook.display_students()
    student_id = int(input("Enter student ID to register for course: "))
    gradebook.display_courses()
    course_id = int(input("Enter course ID to register: "))
    gradebook.register_student_for_course(student_id, course_id)

def add_grade_to_student(gradebook):
    gradebook.display_students()
    student_id = int(input("Enter student ID to add grade: "))
    gradebook.display_courses()
    course_id = int(input("Enter course ID to add grade: "))
    grade = float(input("Enter grade: "))
    gradebook.add_grade_to_student(student_id, course_id, grade)

def display_students(gradebook):
    gradebook.display_students()

def display_courses(gradebook):
    gradebook.display_courses()

def calculate_gpa(gradebook):
    gradebook.display_students()
    student_id = int(input("Enter student ID to calculate GPA: "))
    gpa = gradebook.calculate_gpa(student_id)
    if gpa is not None:
        print(f"GPA for student {student_id} is {gpa:.2f}")
    else:
        print(f"Student with ID {student_id} not found.")

def delete_student(gradebook):
    student_id = int(input("Enter student ID to delete: "))
    if gradebook.delete_student(student_id):
        print(f"Student with ID {student_id} deleted.")
    else:
        print(f"Student with ID {student_id} not found.")

def delete_course(gradebook):
    course_id = int(input("Enter course ID to delete: "))
    if gradebook.delete_course(course_id):
        print(f"Course with ID {course_id} deleted.")
    else:
        print(f"Course with ID {course_id} not found.")

def calculate_ranking(gradebook):
    gradebook.calculate_ranking()

def search_by_grade(gradebook):
    gradebook.display_courses()
    course_id = int(input("Enter course ID to search by grade: "))
    grade = float(input("Enter grade to search: "))
    gradebook.search_by_grade(course_id, grade)

def generate_transcript(gradebook):
    gradebook.display_students()
    student_id = int(input("Enter student ID to generate transcript: "))
    gradebook.generate_transcript(student_id)
