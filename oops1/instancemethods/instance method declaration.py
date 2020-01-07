class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("student name", self.name)
        print("student Marks", self.marks)

    def grade(self):
        if self.marks >= 60:
            print("first class")
        elif self.marks >= 50:
            print("second class")
        elif self.marks >= 35:
            print("third grade")
        else:
            print("Your Failed in exam")


n = int(input("enter number of students:"))
for i in range(n):
    name = input("Enter student Name:")
    marks = int(input("Enter your marks:"))
    s = Student(name, marks)
    s.display()
    s.grade()
    print()
