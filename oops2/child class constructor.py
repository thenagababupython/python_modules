class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        return "Name={}\n Age={} \n Rollno ={} \n Marks={}".format(self.name,self.age,self.rollno,self.marks)
s=Student("Nagababu",12,101,98)
print(s)
