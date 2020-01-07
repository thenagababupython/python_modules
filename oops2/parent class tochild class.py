class P:
    def m1(self):
        print("parent class method")
class c(P):
    def m2(self):
        print("child class method")
k=c()
k.m1()
k.m2()