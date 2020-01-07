word=input("enter any word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
print(sorted(d))
for k,v in d.items():
    print("{} occured {}".format(k,v))