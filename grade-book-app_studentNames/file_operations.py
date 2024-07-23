#!/usr/bin/python3
from student import Student
from course import Course

def save_students_to_file(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            if student is not None:
                file.write(student.to_string() + '\n')

def load_students_from_file(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                student = Student.from_string(line)
                if student is not None:
                    students.append(student)
    except FileNotFoundError:
        pass
    return students

def save_courses_to_file(courses, filename):
    with open(filename, 'w') as file:
        for course in courses:
            if course is not None:
                file.write(course.to_string() + '\n')

def load_courses_from_file(filename):
    courses = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                course = Course.from_string(line)
                if course is not None:
                    courses.append(course)
    except FileNotFoundError:
        pass
    return courses
