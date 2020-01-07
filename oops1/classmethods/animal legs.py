class Animal:
    legs=4
    @classmethod
    def Walk(cls,name):
        print("{} walks with {} legs".format(name,cls.legs))
Animal.Walk("dog")
Animal.Walk("cow")
