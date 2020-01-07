class Outer:
    def __init__(self):
        print("the outer class object creation")
    class inner:
        def __init__(self):
            print("the inner class object creation")
        def m1(self):
            print("innerr class method")
o=Outer().inner()
o.m1()