class p:
    def Property(self):
        print("Goald+Cash+Power+land")
    def marry(self):
        print("Appaalamma")
class C(p):
    def marry(self):
        super().marry()
        print("khatrina khif")
c=C()
c.Property()
c.marry()