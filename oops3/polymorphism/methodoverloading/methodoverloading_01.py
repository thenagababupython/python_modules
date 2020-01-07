class Test:
    def m1(self):
        print("No arg method")
    def m1(self,a):
        print("one arg method")
    def m1(self,a,b):
        print("Two arg Method")
t=Test()
# t.m1()
# t.m1(10)
t.m1(10,20)