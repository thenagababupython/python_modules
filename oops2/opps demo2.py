class car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("Car Name {} and Model {} and car Color {}".format(self.name,self.model,self.color))
class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def empinfo(self):
        print("Employee Name:",self.ename)
        print("Employee Eno:",self.eno)
        print("Employee Car:")
        self.car.getinfo()

c=car("Innova","2.5v","Red")
e=Employee("Durga",1000,c)
e.empinfo()