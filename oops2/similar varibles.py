class P:
    a=10
    def __init__(self):
        self.b=20
class c(P):
    c=30
    def __init__(self):
        super().__init__()
        self.d=40
c1=c()
print(c1.a,c1.b,c1.c,c1.d)