class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=0 and b!=0 and c!=None:
            print("The sum of three Number:",a+b+c)
        elif a!=None and b!=None:
            print("The sum of Two numbers:",a+b)
        else:
            print("Please Provide 2 or 3 arguments")
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)

