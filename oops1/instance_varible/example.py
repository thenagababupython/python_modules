class Student:
    """ Developed by Durga python"""
    def __init__(self):
        self.name='durga'
        self.age=25
        self.marks=80
    def display(self):
        print("Hello i am ",self.name)
        print("my age is ",self.age)
        print("My marks are: ",self.marks)
a=Student()
a.display()