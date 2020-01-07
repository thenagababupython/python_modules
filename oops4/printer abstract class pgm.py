from abc import *
class Printer(ABC):
    @abstractmethod
    def printit(self):pass

    @abstractmethod
    def disconnect(self):pass

class ESPON(Printer):
    def printit(self):
        print("Printing from ESPON printer..")
    def disconnect(self):
        print("Disconnect To ESPON printer..")

class HP(Printer):
    def printit(self):
        print("Printing from HP printer..")
    def disconnect(self):
        print("Disconnect To HP printer..")
dbname=input("enter your string:")
clasname=globals()[dbname]
x=clasname()
x.printit()
x.disconnect()

