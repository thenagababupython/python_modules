class Student:
    """this is student class with required data"""
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("Student Name :{}\n Rollno :{} \n marks: {} \n".format(self.name,self.rollno,self.marks))
s1=Student("nagababu",101,209)
s1.display()
s2=Student("babu",203,309)
s2.display()