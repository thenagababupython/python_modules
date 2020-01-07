import os,sys
fname=input("enetr file name:")
if os.path.isfile(fname):
    print("file exists:",fname)
    f=open(fname,"r")
else:
    print("File Does not Exists:",fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
print("no of lines",lcount)
print("no of wors",wcount)
print("no of characters",ccount)