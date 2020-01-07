class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatdrink(self):
        print("Eat biryani and Drink beer")
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print("coding Python very Easy")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee Number:",self.eno)
        print("Employee Salary:",self.esal)
e=Employee("Naga",25,101,200000)
e.eatdrink()
e.work()
e.empinfo()