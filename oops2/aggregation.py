class Student:
    collegename="jntuh"
    def __init__(self,name):
        self.name=name
print(Student.collegename)
s=Student("Nagabbau")
print(s.name)