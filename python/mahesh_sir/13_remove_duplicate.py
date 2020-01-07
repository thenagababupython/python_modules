s=input("enter your string:")
l=[]
for i in s:
    if i not in l:
        l.append(i)
print(l)