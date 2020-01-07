from abc import *
class CollegeAutoMation(ABC):
    @abstractmethod
    def m1(self):pass

    @abstractmethod
    def m2(self):pass

    @abstractmethod
    def m3(self):pass

class AbcCls(CollegeAutoMation):
    def m1(self):
        print("m1 method implementation")
    def m2(self):
        print("m2 method implementation")

class connerctclass(AbcCls):
    def m3(self):
        print("m3 method implementation")

c=connerctclass()
c.m1()
c.m2()
c.m3()