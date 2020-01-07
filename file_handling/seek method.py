data="ALL STUDENTS ARE STUPIDS"
f=open("abc.txt","w")
f.write(data)
with open("abc.txt","r+") as f:
    text=f.read()
    print(text)
    print("the current position of cursor is:",f.tell())
    f.seek(17)
    print("the current position of cursor is:",f.tell())
    f.write("GEMS!!!")
    f.seek(0)
    text=f.read()
    print("Data After modification")
    print(text)