#!/usr/bin/python3
class Student:
    def __init__(self, student_id, email, names):
        self.student_id = student_id
        self.email = email
        self.names = names
        self.courses_registered = {}  # course_id: grade
        self.GPA = 0.0

    def calculate_GPA(self):
        total_points = 0
        total_courses = 0
        for grade in self.courses_registered.values():
            if grade is not None:
                total_points += grade
                total_courses += 1
        self.GPA = total_points / total_courses if total_courses > 0 else 0.0
        return self.GPA

    def register_for_course(self, course_id):
        if course_id not in self.courses_registered:
            self.courses_registered[course_id] = None  # Register for a course with no grade yet

    def add_grade(self, course_id, grade):
        if course_id in self.courses_registered:
            self.courses_registered[course_id] = grade  # Add or update grade for a course

    def to_string(self):
        course_str = ','.join(f'{course_id}:{grade}' for course_id, grade in self.courses_registered.items())
        return f'{self.student_id}|{self.email}|{self.names}|{self.GPA}|{course_str}'

    @classmethod
    def from_string(cls, data):
        try:
            parts = data.strip().split('|')
            if len(parts) < 4:
                raise ValueError("Insufficient parts in student data")
            student_id = int(parts[0])
            email = parts[1]
            names = parts[2]
            GPA = float(parts[3])
            courses_registered = {}
            if len(parts) > 4 and parts[4]:
                course_parts = parts[4].split(',')
                for course in course_parts:
                    course_id, grade = course.split(':')
                    courses_registered[int(course_id)] = float(grade)
            student = cls(student_id, email, names)
            student.GPA = GPA
            student.courses_registered = courses_registered
            return student
        except (IndexError, ValueError) as e:
            print(f"Error parsing student data: {data}. Error: {e}")
            return None
