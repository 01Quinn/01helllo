class Student:
    count = 0
    department = "computer science"

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = self.last_name @metropolia.fi
        self.count = []
        self.stuents = []
        Student.count += 1

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_gender(self):
        return self.gender

    def enrollment(self, course):
        self.count.append(course)
        print(f"course added {course}.")


    def set_age(self, age):
        self.age = age


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


student1 = Student("John", "Smith", 23, "male")
student2 = Student("Mary", "Smith", 24, "female")
student3 = Student("Sara", "Smith", 25, "female")
print(student1.get_full_name(), student2.get_full_name(), student3.get_full_name(), Student.department)

print(student1.age, student2.age, student3.age)

print(student1.gender, student2.gender, student3.gender)

print(Student.count)

class Course:
    def __init__(self, course_name, course_description):
        self.course_name = course_name
        self.course_description = course_description
        self.students = []

    def get_student(self):
        for student in self.students:
            print(student)

class Faculty:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)
        print(f"student {student.name} added.")

    def get_course(self):
        print(self.courses)
        for course in self.courses:
            print(course)
