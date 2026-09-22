# Build a small Student Management System using Python OOP.

# Requirements: Create a Student class with attributes such as name, email, student ID, course, and marks.
# Create multiple student objects and methods to display details, update marks, and calculate average marks.
#  Use a class variable to track the total number of students and a class method such as get_total_students().

# Expected concepts: Class, objects, __init__, instance methods, class variable, class method.
class Student:
    total_students = 0

    def __init__(self,name,email,stud_id,course,marks):
        self.name = name
        self.email = email
        self.stud_id = stud_id
        self.course = course
        self.marks = marks
        Student.total_students += 1

    def display_details(self):
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Student ID : ",self.stud_id)
        print("Course : ",self.course)
        print("Marks : ",self.marks)

    def update_marks(self,new_marks):
        self.marks = new_marks
        print("Marks Updated Successfully to : ",self.marks)

    def average_marks(self):
        avg = sum(self.marks) / len(self.marks)
        print("Average Marks : ",avg)

    @classmethod
    def get_total_students(cls):
        return cls.total_students

stud = Student("Gauri","gauri.indani@gmail.com","S101","Python",[85,65,23])
stud.display_details()
stud.average_marks()
print("Total Students : ",Student.get_total_students())