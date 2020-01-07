import os,sys
fname=input("Enter File Name:")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("the file does not exists:",fname)
    sys.exit(0)
print("the content of file is:")
data=f.read()
print(data)