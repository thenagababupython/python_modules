class Test:
    def sum(self,*a):
        totoal=0
        for x in a:
            totoal=totoal+x
        print("The sum of:",totoal)
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum()