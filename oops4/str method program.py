class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def __str__(self):
        return "student name:{} and rollno:{}".format(self.name,self.rollno)


s1=Student("Nagabbau",105)
s2=Student("babunaga",106)
print(s1)
print(s2)