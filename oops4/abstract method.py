from abc import *
class Vechile(ABC):
    @abstractmethod
    def noofwheels(self):
        pass
class Bus(Vechile):
    def noofwheels(self):
        return 7
class Auto(Vechile):
    def noofwheels(self):
        return 3
b=Bus()
print(b.noofwheels())

a=Auto()
print(a.noofwheels())
