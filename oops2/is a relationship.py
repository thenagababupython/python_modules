class P:
    a=10
    def __init__(self):
        self.b=20
        print("this is Parent Class Method")
    def m3(self):
        print("this is m3 method")
    @classmethod
    def m1(cls):
        print("this is Parent Class Method")
    @staticmethod
    def m2():
        print("This is static Method")
class C(P):
    pass
c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()