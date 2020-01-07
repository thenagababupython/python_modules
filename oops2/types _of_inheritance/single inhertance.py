class p:
    def m1(self):
        print("parent method")
class C(p):
    def m2(self):
        print("child method")
c=C()
c.m1()
c.m2()
