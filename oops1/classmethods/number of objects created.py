class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noofobjects(cls):
        print("the number objects created for test class",cls.count)
t1=Test()
t2=Test()
Test.noofobjects()
t3=Test()
t4=Test()
t5=Test()
Test.noofobjects()
