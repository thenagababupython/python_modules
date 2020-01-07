class P:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("Instance Method")
    @classmethod
    def m2(cls):
        print("Class Method")
    @staticmethod
    def m3():
        print("ststic Method")
class C(P):
    a=888
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a)
        print(self.b)
        super().m1()
        super().m2()
        super().m3()
c=C()
