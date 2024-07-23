#!/usr/bin/python3
from student import Student
from course import Course

class Gradebook:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student_id, email, names):
        student = Student(student_id, email, names)
        self.students.append(student)
        return student

    def add_course(self, course_id, name, trimester, credits):
        course = Course(course_id, name, trimester, credits)
        self.courses.append(course)
        return course

    def register_student_for_course(self, student_id, course_id):
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        if student and course:
            student.register_for_course(course.course_id)
            print(f"Course {course.name} registered for student {student.names}.")
        else:
            print("Student or Course not found.")
    
    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def calculate_gpa(self, student_id):
        student = self.get_student(student_id)
        if student:
            return student.calculate_GPA()
        return None
    
    def delete_student(self, student_id):
        student = self.get_student(student_id)
        if student:
            self.students.remove(student)
            return True
        return False

    def get_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def delete_course(self, course_id):
        course = self.get_course(course_id)
        if course:
            self.courses.remove(course)
            return True
        return False

    def add_grade_to_student(self, student_id, course_id, grade):
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        if student and course:
            student.add_grade(course.course_id, grade)
            print(f"Grade {grade} added for course {course.name} for student {student.names}.")
            student.calculate_GPA()  # Update GPA after adding grade
        else:
            print("Student or Course not found.")

    def find_student_by_id(self, student_id):
        return next((student for student in self.students if student.student_id == student_id), None)

    def find_course_by_id(self, course_id):
        return next((course for course in self.courses if course.course_id == course_id), None)

    def display_students(self):
        for student in self.students:
            print(f"ID: {student.student_id}, Email: {student.email}, Name: {student.names}, GPA: {student.GPA:.2f}")

    def display_courses(self):
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}, Trimester: {course.trimester}, Credits: {course.credits}")

    def calculate_ranking(self):
        students_with_gpa = [(student, student.calculate_GPA()) for student in self.students]
        sorted_students = sorted(students_with_gpa, key=lambda x: x[1], reverse=True)
        for rank, (student, gpa) in enumerate(sorted_students, start=1):
            print(f"Rank {rank}: {student.names} with GPA {gpa:.2f}")

    def search_by_grade(self, course_id, grade):
        course = self.find_course_by_id(course_id)
        if course:
            for student in self.students:
                if course_id in student.courses_registered and student.courses_registered[course_id] == grade:
                    print(f"Student {student.names} has grade {grade} in course {course.name}")
        else:
            print("Course not found.")

    def generate_transcript(self, student_id):
        student = self.find_student_by_id(student_id)
        if student:
            print(f"Transcript for {student.names} (ID: {student.student_id}):")
            for course_id, grade in student.courses_registered.items():
                course = self.find_course_by_id(course_id)
                if course:
                    print(f"Course: {course.name}, Trimester: {course.trimester}, Credits: {course.credits}, Grade: {grade}")
            gpa = student.calculate_GPA()
            print(f"GPA: {gpa:.2f}")
        else:
            print("Student not found.")
