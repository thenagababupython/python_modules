import csv
with open("emp1.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("enter number of employess:"))
    for i in range(n):
        eno=input("enter employee number:")
        ename=input("enter employee name:")
        esal=input("enter employee salary:")
        eaddress=input("enter employee addreess:")
        w.writerow([eno,ename,esal,eaddress])
print("total data written to csv file successfully")