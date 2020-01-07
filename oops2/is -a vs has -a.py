class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("\tCarName :{} \n\t Model :{} \n\t color :{}".format(self.name,self.model,self.color))
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatdrink(self):
        print("Eat biryani and chill Beer")
class  Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def work(self):
        print("coding python and eating Barayani")
    def empinfo(self):
        print("Employeee Name:",self.name)
        print("Employeee Age:",self.age)
        print("Employeee number:",self.eno)
        print("Employee salary",self.esal)
        print("Employee car info")
        self.car.getinfo()
c=Car("Innnova","2.5v","Grey")
e=Employee('Durga',48,103,300000,c)
e.eatdrink()
e.work()
e.empinfo()
