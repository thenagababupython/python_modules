class A:
    def m1(self):
        print("A class method")
class B(A):
    def m1(self):
        print("B class Method")
class C(B):
    def m1(self):
        print("C Class Method")
class  D(C):
    def m1(self):
        print("D class method")
class E(D):
    def m1(self):
        A.m1(self)
e=E()
e.m1()