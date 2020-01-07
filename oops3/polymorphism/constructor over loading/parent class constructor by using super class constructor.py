class  Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def display(self):
        print("Employee name",self.name)
        print("Employee Age",self.age)
        print("Employee Number",self.eno)
        print("Employee Salry",self.esal)
e=Employee("Nagababu",25,105,40000)
e.display()