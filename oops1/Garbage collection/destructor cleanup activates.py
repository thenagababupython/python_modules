import time
class Test:
    def __init__(self):
       print("object initialization.....")
    def __del__(self):
        print("fulfilling the last wish performing cleanup activates")
t1=Test()
t1=None
time.sleep(5)
print("End Of Application")