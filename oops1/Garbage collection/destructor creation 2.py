import time
class Test:
    def __init__(self):
       print("object initialization.....")
    def __del__(self):
        print("fulfilling the last wish performing cleanup activates")
t1=Test()
t2=t1
t3=t2
del t1
time.sleep(5)
print("object not at destroed after deleting t1")
del t2
time.sleep(5)
print("object not at destroyed even after deleting: t2")
print("i am atring to delete last reference varible")
del t3
