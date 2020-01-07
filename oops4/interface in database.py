from abc import *
class Dbinterface(ABC):
    @abstractmethod
    def connect(self):pass

    @abstractmethod
    def disconnect(self):pass

class Oracle(Dbinterface):
    def connect(self):
        print("Connect To Oracle Database..")
    def disconnect(self):
        print("Disconnect To Oracle Database..")

class Sybase(Dbinterface):
    def connect(self):
        print("Connect To Sybase Database..")
    def disconnect(self):
        print("Disconnect To Syebase Database..")
dbname=input("enter your string:")
clasname=globals()[dbname]
x=clasname()
x.connect()
x.disconnect()

