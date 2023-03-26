from enum import Enum


class AliveStatus(Enum):
    deceased = 0
    alive = 1


class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, alive):
        self.alive = alive


class Instructor(Person):
    def __init__(self, first_name, last_name, dob, alive, instructor_id):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = instructor_id


class Student(Person):
    def __init__(self, first_name, last_name, dob, alive, student_id):
        super().__init__(first_name, last_name, dob, alive)
        self.student_id = student_id


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob, alive, student_id):
        super().__init__(first_name, last_name, dob, alive, student_id)


class PreKStudent(Student):
    def __init__(self, first_name, last_name, dob, alive, student_id):
        super().__init__(first_name, last_name, dob, alive, student_id)


class MiddleSchoolStudent(Student):
    def __init__(self, first_name, last_name, dob, alive, student_id):
        super().__init__(first_name, last_name, dob, alive, student_id)


class CollegeStudent(Student):
    def __init__(self, first_name, last_name, dob, alive, student_id):
        super().__init__(first_name, last_name, dob, alive, student_id)


class Classroom:
    students = []
    instructors = []

    def __init__(self, students, instructors):
        self.students.append(students)
        self.instructors.append(instructors)

    def add_instructor(self, instructors):
        self.instructors.append(instructors)

    def remove_instructor(self, instuctors):
        self.instructors.remove(instuctors)

    def add_student(self, student):
        self.students.append(students)

    def remove_student(self, students):
        self.students.remove(students)

    def print_instructors(self, instructors):
        print(instructors)

    def print_students(self, students):
        print(students)
