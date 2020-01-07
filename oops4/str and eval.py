# import datetime
# today=datetime.datetime.now()
# s=str(today) #converting oject to str
# print(s)
# d=eval(s) #convert str to object
#
import datetime
today=datetime.datetime.now()
s=repr(today)
print(s)
d=eval(s)
print(d)