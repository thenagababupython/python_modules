class Student:
    def SetName(self,name):
        self.name=name
    def getName(self,name):
        return  self.name

    def SetMarks(self,marks):
        self.marks=marks
    def GetMarks(self):
        return self.marks

n=int(input("enter number of students:"))
for i in range(n):
    s=Student()
    name=input("Enter Name:")
    s.SetName(name)
    marks=int(input("Enter Marks:"))
    s.SetMarks(marks)
    print("Hi",s.getName(marks))
    print("Your Marks:",s.GetMarks())
    print()
