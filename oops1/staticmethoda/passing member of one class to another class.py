class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print("Employe  number is:",self.eno)
        print("Employe  name is:",self.ename)
        print("Employe  salary is:",self.esal)
class Test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()
e=Employee(100,'nagababu',10000)
Test.modify(e)