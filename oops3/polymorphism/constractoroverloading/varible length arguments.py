class Test:
    def __init__(self,*a):
        print("constructor with varible number of arguments")
t=Test()
t=Test(10)
t=Test(10,20)
t=Test(10,20,30)
t=Test(10,20,30,40)
t=Test(10,20,30,40,50)