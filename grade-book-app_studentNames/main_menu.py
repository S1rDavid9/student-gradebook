#!/usr/bin/python3
from gradebook import Gradebook
from file_operations import save_students_to_file, load_students_from_file, save_courses_to_file, load_courses_from_file
from input_functions import add_student, add_course, register_student_for_course, add_grade_to_student, display_students, display_courses, calculate_gpa, delete_student, delete_course, calculate_ranking, search_by_grade, generate_transcript

# Initialize Gradebook
gradebook = Gradebook()

# File to store student and course data
student_filename = 'students.txt'
course_filename = 'courses.txt'

# Load existing courses
gradebook.courses = load_courses_from_file(course_filename)

# Load existing students
gradebook.students = load_students_from_file(student_filename)

# Main menu
def main_menu():
    print()
    print("--Welcome to the student grade-book--")
    while True:
        print()
        print("     Please select an option")

        print("\n1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Add Grade to Student")
        print("5. Display Students")
        print("6. Display Courses")
        print("7. Calculate GPA")
        print("8. Delete a student")
        print("9. Delete a course")
        print("10. Calculate Ranking")
        print("11. Search by Grade")
        print("12. Generate Transcript")
        print("13. Save and Exit")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(gradebook)
            print("---student added successfully!")
        elif choice == '2':
            add_course(gradebook)
            print("---course added successfully!")
        elif choice == '3':
            register_student_for_course(gradebook)
        elif choice == '4':
            add_grade_to_student(gradebook)
        elif choice == '5':
            display_students(gradebook)
        elif choice == '6':
            display_courses(gradebook)
        elif choice == '7':
            calculate_gpa(gradebook)
        elif choice == '8':
            delete_student(gradebook)
        elif choice == '9':
            delete_course(gradebook)
        elif choice == '10':
            calculate_ranking(gradebook)
        elif choice == '11':
            search_by_grade(gradebook)
        elif choice == '12':
            generate_transcript(gradebook)
        elif choice == '13':
            save_students_to_file(gradebook.students, student_filename)
            save_courses_to_file(gradebook.courses, course_filename)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
