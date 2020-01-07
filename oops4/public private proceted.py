class Test:
    x=10
    _y=20
    __z=30
    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)
c=Test()
c.m1()
print(c.x)
print(c._y)
# print(c._Test.__z)