rec={}
n=int((input("enter number of students:")))
i=1
while i<=n:
    name=input("enter student name:")
    marks=int(input("enter % of student marks:"))
    rec[name]=marks
    i=i+1
    print("student name   ","% of marks")
for x in rec:
    print("   ",x,"    ",rec[x])