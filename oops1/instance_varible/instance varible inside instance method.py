class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        self.c=30
t=Test()
t.display()
print(t.__dict__)