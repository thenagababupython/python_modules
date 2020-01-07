# a4b3c2
# aaaabbbcc
n=input("enter some string:")
output=''
for x in n:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+previous*(int(x)-1)
print(output)
